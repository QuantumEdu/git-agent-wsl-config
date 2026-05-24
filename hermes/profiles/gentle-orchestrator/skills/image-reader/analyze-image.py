#!/usr/bin/env python3
"""
analyze-image.py — Analyze image structure before OCR
Outputs JSON with layout information to guide Tesseract PSM selection.
"""

import sys
import json
from pathlib import Path

def analyze_image(image_path: str) -> dict:
    try:
        from PIL import Image
    except ImportError:
        return {"error": "Pillow not installed. Run: pip install Pillow"}

    img = Image.open(image_path)
    w, h = img.size
    mode = img.mode

    # Convert to RGB for consistent analysis
    if mode != "RGB":
        img = img.convert("RGB")

    # Resize for analysis
    thumb_w = min(w, 200)
    thumb_h = int(h * (thumb_w / w))
    thumb = img.resize((thumb_w, thumb_h))

    # Background detection
    pixels = list(thumb.getdata())
    from collections import Counter
    colors = Counter(pixels)
    bg_color = colors.most_common(1)[0][0]
    bg_count = colors.most_common(1)[0][1]
    total_pixels = len(pixels)
    bg_ratio = bg_count / total_pixels

    # Content density
    content_ratio = 1.0 - bg_ratio

    # Detect text density per horizontal slice
    slices = 20
    text_density_profile = []
    for i in range(slices):
        y = int(h * (i / slices))
        row = [img.getpixel((x, y)) for x in range(0, w, max(1, w // 200))]
        non_bg = sum(1 for p in row if _color_distance(p, bg_color) > 40)
        text_density_profile.append({
            "position_pct": round(i / slices * 100),
            "density": round(non_bg / len(row), 2)
        })

    # Detect dominant non-background colors (potential UI elements)
    non_bg_colors = [(c, cnt) for c, cnt in colors.most_common(20) if _color_distance(c, bg_color) > 30]
    dominant_colors = [
        {"rgb": list(c), "hex": f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}", "pct": round(cnt/total_pixels*100, 1)}
        for c, cnt in non_bg_colors[:8]
    ]

    # Estimate text regions — lower threshold for anti-aliased text on light bg
    high_density_slices = sum(1 for s in text_density_profile if s["density"] > 0.10)
    text_coverage = high_density_slices / slices

    # Content type heuristic based on average density
    avg_density = sum(s["density"] for s in text_density_profile) / len(text_density_profile)
    if avg_density > 0.25:
        content_type = "document_or_screenshot"
    elif avg_density > 0.10:
        content_type = "diagram_or_mixed"
    else:
        content_type = "photo_or_sparse_text"

    # Recommended PSM
    if content_type == "document_or_screenshot":
        psm_recommendation = 6  # uniform block
    elif content_type == "diagram_or_mixed":
        psm_recommendation = 3  # auto
    else:
        psm_recommendation = 11  # sparse text

    return {
        "file": Path(image_path).name,
        "dimensions": {"width": w, "height": h, "aspect_ratio": round(w/h, 2)},
        "mode": mode,
        "content_type": content_type,
        "background": {
            "color_rgb": list(bg_color),
            "coverage_pct": round(bg_ratio * 100, 1)
        },
        "content_density": round(content_ratio, 2),
        "text_coverage_estimate": round(text_coverage, 2),
        "dominant_colors": dominant_colors,
        "text_density_profile": text_density_profile,
        "recommended_psm": psm_recommendation,
        "psm_options": {
            3: "Auto — fully automatic page segmentation",
            4: "Single column — variable text sizes",
            6: "Uniform block — best for screenshots and diagrams",
            11: "Sparse text — scattered annotations",
            12: "Sparse text with orientation detection"
        }
    }


def _color_distance(c1: tuple, c2: tuple) -> float:
    """Euclidean distance in RGB space."""
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: analyze-image.py <image_path>"}, indent=2))
        sys.exit(1)

    result = analyze_image(sys.argv[1])
    print(json.dumps(result, indent=2))
