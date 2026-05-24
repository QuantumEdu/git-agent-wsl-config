#!/usr/bin/env bash
# setup-tesseract.sh — Portable Tesseract OCR setup for Hermes image-reader skill
# Downloads and extracts tesseract + dependencies to /tmp/tesseract_hermes/
# No sudo required. Cached across runs.

set -euo pipefail

CACHE_DIR="/tmp/tesseract_hermes"
LIB_DIR="$CACHE_DIR/libs"
BIN_DIR="$CACHE_DIR/bin"
TESSDATA_DIR="$CACHE_DIR/tessdata"
WORK_DIR="/tmp/tesseract_setup_$$"

# If cached and working, skip
if [ -x "$BIN_DIR/tesseract" ] && [ -f "$TESSDATA_DIR/eng.traineddata" ]; then
	echo "✓ Tesseract ya está configurado en $CACHE_DIR"
	exit 0
fi

echo "🔧 Configurando Tesseract OCR portable..."

# Clean any partial setup
rm -rf "$CACHE_DIR" "$WORK_DIR"
mkdir -p "$CACHE_DIR" "$LIB_DIR" "$BIN_DIR" "$TESSDATA_DIR" "$WORK_DIR"

cd "$WORK_DIR"

# Download packages
echo "  📥 Descargando paquetes..."
for pkg in tesseract-ocr libtesseract5 libleptonica6 libarchive13t64 libgif7 tesseract-ocr-eng; do
	apt download "$pkg" 2>/dev/null || {
		echo "  ⚠️  No se pudo descargar $pkg"
		continue
	}
done

# Extract all debs
echo "  📦 Extrayendo paquetes..."
for deb in *.deb; do
	[ -f "$deb" ] || continue
	dpkg-deb -x "$deb" "$WORK_DIR/extracted" 2>/dev/null || true
done

# Copy tesseract binary
if [ -f "$WORK_DIR/extracted/usr/bin/tesseract" ]; then
	cp "$WORK_DIR/extracted/usr/bin/tesseract" "$BIN_DIR/"
	chmod +x "$BIN_DIR/tesseract"
	echo "  ✓ tesseract binary installed"
else
	echo "  ❌ No se encontró el binario de tesseract"
	exit 1
fi

# Copy libraries
echo "  📚 Recolectando librerías..."
find "$WORK_DIR/extracted" -name "*.so*" -exec cp {} "$LIB_DIR/" \; 2>/dev/null || true

# Copy tessdata
if [ -d "$WORK_DIR/extracted/usr/share/tesseract-ocr/5/tessdata" ]; then
	cp "$WORK_DIR/extracted/usr/share/tesseract-ocr/5/tessdata/"*.traineddata "$TESSDATA_DIR/" 2>/dev/null || true
	echo "  ✓ tessdata installed"
fi

# Ensure english is present
if [ ! -f "$TESSDATA_DIR/eng.traineddata" ]; then
	echo "  📥 Descargando eng.traineddata..."
	curl -sL "https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata" -o "$TESSDATA_DIR/eng.traineddata" || {
		echo "  ❌ No se pudo descargar eng.traineddata"
		exit 1
	}
fi

# Cleanup
rm -rf "$WORK_DIR"

# Verify
echo "  🔍 Verificando instalación..."
export LD_LIBRARY_PATH="$LIB_DIR:$LD_LIBRARY_PATH"
export TESSDATA_PREFIX="$TESSDATA_DIR"

if "$BIN_DIR/tesseract" --version >/dev/null 2>&1; then
	VERSION=$("$BIN_DIR/tesseract" --version 2>&1 | head -1)
	echo "✅ Tesseract configurado exitosamente: $VERSION"
	echo "   Ruta: $BIN_DIR/tesseract"
	echo "   Librerías: $LIB_DIR"
	echo "   Tessdata: $TESSDATA_DIR"
else
	echo "❌ Falló la verificación"
	exit 1
fi
