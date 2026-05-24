---
name: image-reader
description: "Extract and analyze text from images (PNG, JPG, GIF, WebP) using OCR. Use when the user needs to read text from screenshots, diagrams, photos, or any image containing text."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ocr, image, text-extraction, vision, screenshot, diagram]
    related_skills: []
---

# Image Reader: OCR Text Extraction from Images

## Overview

This skill enables you (Hermes) to extract text from images using Tesseract OCR. You will set up the OCR engine if needed, run it on the target image, and return structured, human-readable output along with a visual analysis of the image layout.

## When to Use

Use this skill when:

- The user provides an image file (.png, .jpg, .jpeg, .gif, .webp) and asks "qué dice acá", "leé esta imagen", "analizá esta captura", etc.
- A diagram, screenshot, or photo contains text that needs to be extracted
- The user wants to understand the structure and content of a visual document
- You need to extract data from a chart, table, or form in image format

Do NOT use:

- For purely photographic images with no text (describe them instead)
- When the user explicitly wants you to use browser vision tools for web pages

## Prerequisites

The skill sets up Tesseract OCR automatically. It uses a portable approach:

1. Downloads Tesseract and its dependencies (leptonica, libarchive, libgif) via apt
2. Extracts them to a local directory (`/tmp/tesseract_hermes/`)
3. Downloads English language data (`eng.traineddata`)
4. Runs OCR with `LD_LIBRARY_PATH` pointing to the extracted libraries

No system-wide installation or sudo is required once the portable setup is cached.

## Workflow

### Phase 1: Setup (if first use)

Run the setup script bundled with this skill:

```bash
bash {skill_dir}/setup-tesseract.sh
```

This script:

1. Checks if `/tmp/tesseract_hermes/` already exists (skip if cached)
2. Downloads tesseract-ocr, libtesseract, libleptonica, libarchive, libgif debs
3. Extracts them to `/tmp/tesseract_hermes/`
4. Downloads `eng.traineddata` if not present
5. Creates a flat library directory for LD_LIBRARY_PATH

Output: exits 0 on success, exits 1 with error message on failure.

### Phase 2: Analyze Image Structure

Before OCR, analyze the image to understand its layout:

```bash
python3 {skill_dir}/analyze-image.py <image_path>
```

This outputs:

- Image dimensions and format
- Dominant colors (helps understand if it's a diagram, screenshot, photo)
- Text density per horizontal slice (identifies text-heavy vs image regions)
- Background color detection
- Estimated number of text regions

Use this information to decide PSM mode:

- PSM 6: Uniform block of text (default — good for screenshots and diagrams)
- PSM 3: Fully automatic page segmentation (for mixed content)
- PSM 4: Single column of text of variable sizes
- PSM 11: Sparse text (for images with scattered text)
- PSM 12: Sparse text with OSD (orientation and script detection)

### Phase 3: Run OCR

Execute Tesseract with the appropriate PSM mode:

```bash
export LD_LIBRARY_PATH=/tmp/tesseract_hermes/libs:$LD_LIBRARY_PATH
export TESSDATA_PREFIX=/tmp/tesseract_hermes/tessdata
/tmp/tesseract_hermes/bin/tesseract <image_path> /tmp/hermes_ocr_output -l eng --psm <psm_mode>
```

Available languages (install more as needed):

- `eng` — English (always installed)
- `spa` — Spanish (install with: download `spa.traineddata` to `$TESSDATA_PREFIX`)
- `eng+spa` — Combined English + Spanish (recommended for bilingual content)

After OCR, read the output:

```bash
cat /tmp/hermes_ocr_output.txt
```

### Phase 4: Structure and Present Results

#### Step 1: Raw OCR output

Present the raw text extracted, preserving line breaks where they indicate structure.

#### Step 2: Layout Reconstruction

Based on the text positions and the image analysis from Phase 2, reconstruct the document structure:

- Identify titles and headers (all-caps, short lines, centered text)
- Group related text into logical sections
- Identify bullet points and numbered lists
- Detect table-like structures (aligned columns)
- Mark code blocks or monospaced text

#### Step 3: Visual Description

Describe what the image looks like:

- Type of content: diagram, screenshot, document, photo, chart
- Color scheme and background
- Number of distinct visual regions
- Notable visual elements (arrows, boxes, icons, photos)

#### Step 4: Structured Markdown Output

Output in this format:

```markdown
## 📷 Análisis de Imagen: <filename>

**Tipo**: <diagrama | captura | documento | foto | gráfico>
**Dimensiones**: <width>×<height> px
**Densidad de texto**: <alta | media | baja>
**Idioma detectado**: <español | inglés | bilingüe>

### 🏗️ Estructura Visual

[Descripción de la disposición: columnas, cajas, flujo]

### 📝 Contenido Extraído

[Texto estructurado con secciones, listas, tablas]

### 🔍 Observaciones

- [Nota sobre formato, legibilidad, elementos no textuales]
- [Sugerencias si algo no se extrajo bien]
```

## Tips for Better Results

- **Preprocessing**: For low-contrast images, increase contrast first:
  ```bash
  python3 -c "from PIL import Image, ImageEnhance; img=Image.open('file.png'); ImageEnhance.Contrast(img).enhance(2.0).save('enhanced.png')"
  ```
- **Bilingual content**: Install Spanish language data for mixed ES/EN text:
  ```bash
  cd $TESSDATA_PREFIX && curl -sLO https://github.com/tesseract-ocr/tessdata/raw/main/spa.traineddata
  ```
- **Large images**: Resize to max 4000px on longest side for faster processing:
  ```bash
  python3 -c "from PIL import Image; img=Image.open('file.png'); w,h=img.size; s=4000/max(w,h); img.resize((int(w*s),int(h*s))).save('resized.png')"
  ```
- **Noisy images**: Apply grayscale + threshold:
  ```bash
  python3 -c "from PIL import Image; img=Image.open('file.png').convert('L'); img.point(lambda x: 255 if x>128 else 0).save('bw.png')"
  ```
- **Table extraction**: If the image contains tables, try PSM 6 first, then mention that table structure was preserved as best-effort aligned text.

## Troubleshooting

| Problem                                | Solution                                                                                                   |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| "error while loading shared libraries" | Re-run setup script: `bash {skill_dir}/setup-tesseract.sh`                                                 |
| OCR returns garbage                    | Try different PSM mode (`--psm 3` or `--psm 4`)                                                            |
| Spanish text not detected              | Install Spanish language data (see Tips)                                                                   |
| Image too large / timeout              | Resize to max 4000px (see Tips)                                                                            |
| No text found (blank output)           | Image may be purely visual — describe it instead                                                           |
| Permission denied                      | Ensure `/tmp/tesseract_hermes/bin/tesseract` is executable: `chmod +x /tmp/tesseract_hermes/bin/tesseract` |

## Reference: PSM Modes

| PSM | Description                            | Best for                              |
| --- | -------------------------------------- | ------------------------------------- |
| 0   | Orientation and script detection only  | Unknown image orientation             |
| 1   | Auto page segmentation with OSD        | Mixed content documents               |
| 3   | Fully auto page segmentation (default) | General documents                     |
| 4   | Single column of variable sizes        | Plain text pages                      |
| 6   | Uniform block of text                  | Screenshots, diagrams with text boxes |
| 7   | Single text line                       | Barcodes, labels                      |
| 8   | Single word                            | Signs, logos                          |
| 9   | Single word in circle                  | Badges, icons                         |
| 10  | Single character                       | Individual letters                    |
| 11  | Sparse text                            | Scattered annotations                 |
| 12  | Sparse text with OSD                   | Unknown sparse text                   |
| 13  | Raw line                               | Pipe output to another tool           |
