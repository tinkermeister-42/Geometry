#!/bin/bash
# Render SVG figures to one PNG for a look:  _authoring/snap.sh out.png a.svg [b.svg ...]
# Each figure is drawn at 1.6x its natural size with its file name above it.
out="$1"; shift
html="$(mktemp --suffix=.html)"
{ echo "<html><body style='margin:6px;background:#fff;font:12px sans-serif'>"
  for f in "$@"; do
    w=$(grep -o 'width="[0-9.]*' "$f" | head -1 | cut -d'"' -f2)
    echo "<div style='display:inline-block;vertical-align:top;margin:6px;border:1px solid #ddd'><div style='color:#06c'>$(basename "$f")</div><img src='file://$(realpath "$f")' style='width:$(python3 -c "print(round(float('${w:-200}')*1.6))")px'></div>"
  done; echo "</body></html>"; } > "$html"
/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell \
  --no-sandbox --disable-gpu --hide-scrollbars --window-size=1400,2400 --screenshot="$out" "file://$html" >/dev/null 2>&1
python3 - "$out" <<'PY'
import sys
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGB"); px = im.load(); h = im.height
while h > 40 and all(px[x, h - 1] == (255, 255, 255) for x in range(0, im.width, 9)): h -= 1
im.crop((0, 0, im.width, h + 6)).save(sys.argv[1])
PY
rm -f "$html"
