#!/bin/bash
# Visual check for one or more lessons in a Geometry worktree.
#   preview.sh <worktree> <outdir> <stem> [<stem> ...]
# A stem is a fragment name: 2.4, 3.Summary, 3.Review, Unit3_Quiz.
# For each stem it:
#   - builds that lesson's figures (names starting with the stem) and printables
#   - writes <outdir>/<stem>_figs.png, a contact sheet of every figure (and _KEY twin)
#   - prints the student copy and the key to PDF with headless Chromium and
#     writes <outdir>/<stem>_student.png and <stem>_key.png, all pages side by side
#   - runs the page-math check (pandoc --mathml) on the matching .qmd
# Read the PNGs with the Read tool and look at every one.
set -uo pipefail
WT="$1"; OUT="$2"; shift 2
CH=/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell
mkdir -p "$OUT"
cd "$WT" || exit 1
for stem in "$@"; do
  echo "=== $stem"
  if [[ "$stem" =~ ^[0-9]+\.[0-9]+$ ]]; then
    scripts/make-figures.sh "${stem}_" | sed 's/^/  fig /' || { echo "FIGURE BUILD FAILED"; continue; }
  fi
  python3 scripts/build-guided-notes.py "$stem" | grep -v '^wrote' | sed 's/^/  /'
  # figure contact sheet from the SVGs (rendered by Chromium so it matches the browser)
  python3 - "$WT" "$OUT" "$stem" "$CH" <<'PY'
import glob, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw
wt, out, stem, ch = sys.argv[1:]
if not stem[0].isdigit() or "." not in stem:
    sys.exit(0)
unit = stem.split(".")[0]
svgs = sorted(glob.glob(f"{wt}/images/Unit_{unit}/{stem}_*.svg")) if stem.split(".")[1].isdigit() else []
if not svgs:
    sys.exit(0)
tmp = tempfile.mkdtemp()
html = os.path.join(tmp, "sheet.html")
with open(html, "w") as f:
    f.write("<html><body style='margin:8px;font:12px sans-serif;background:#fff'>")
    for s in svgs:
        f.write(f"<div style='display:inline-block;vertical-align:top;margin:6px;border:1px solid #ddd;padding:4px'>"
                f"<div style='color:#06c'>{os.path.basename(s)}</div><img src='file://{s}' style='max-width:620px'></div>")
    f.write("</body></html>")
png = os.path.join(out, f"{stem}_figs.png")
subprocess.run(["timeout", "90", ch, "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                "--window-size=1400,3000", f"--screenshot={png}", f"file://{html}"],
               capture_output=True)
im = Image.open(png).convert("RGB")
# trim the white bottom
px = im.load(); h = im.height
while h > 50 and all(px[x, h - 1] == (255, 255, 255) for x in range(0, im.width, 7)):
    h -= 1
im.crop((0, 0, im.width, min(im.height, h + 10))).save(png)
print("  figures sheet:", png)
PY
  for f in guided_notes/src/"$stem".html assessments/src/"$stem".html; do
    [[ -f "$f" ]] || continue
    file=$(grep -m1 '^file:' "$f" | sed 's/file: *//')
    lesson=$(grep -m1 '^lesson:' "$f" | sed 's/lesson: *//'); slug=$(grep -m1 '^slug:' "$f" | sed 's/slug: *//')
    unit=$(grep -m1 '^unit:' "$f" | sed 's/unit: *//')
    [[ -n "$file" ]] || file="${lesson}_${slug}"
    case "$f" in guided_notes/*) dir=guided_notes/Unit_$unit ;; *) dir=assessments/Unit_$unit ;; esac
    for k in "" _KEY; do
      html="$dir/$file$k.html"; [[ -f "$html" ]] || { echo "  missing $html"; continue; }
      pdf="$OUT/${stem}$k.pdf"
      timeout 90 "$CH" --no-sandbox --disable-gpu --no-pdf-header-footer --print-to-pdf="$pdf" "file://$PWD/$html" >/dev/null 2>&1
      n=$(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages/{print $2}')
      rm -f "$OUT"/pg_${stem}${k}-*.png
      pdftocairo -png -r 55 "$pdf" "$OUT/pg_${stem}${k}"
      name=$([[ -z "$k" ]] && echo student || echo key)
      python3 - "$OUT" "${stem}$k" "$OUT/${stem}_${name}.png" <<'PY'
import glob, sys
from PIL import Image
out, pre, dest = sys.argv[1:]
fs = sorted(glob.glob(f"{out}/pg_{pre}-*.png"), key=lambda f: int(f.rsplit("-", 1)[1][:-4]))
ims = [Image.open(f).convert("RGB") for f in fs]
# two rows when there are many pages
per = 4 if len(ims) > 4 else len(ims)
rows = [ims[i:i + per] for i in range(0, len(ims), per)]
W = max(sum(i.width for i in r) + 10 * len(r) for r in rows); H = sum(max(i.height for i in r) + 10 for r in rows)
sheet = Image.new("RGB", (W, H), (120, 120, 120)); y = 0
for r in rows:
    x = 0
    for i in r:
        sheet.paste(i, (x, y)); x += i.width + 10
    y += max(i.height for i in r) + 10
sheet.save(dest)
for f in fs:
    import os; os.remove(f)
PY
      echo "  $name: $n pages -> $OUT/${stem}_${name}.png"
    done
  done
  # page math check
  case "$stem" in
    *.Summary) qmd="chapters/Unit_${stem%%.*}/Summary.qmd" ;;
    *.Review)  qmd="chapters/Unit_${stem%%.*}/Review.qmd" ;;
    *) qmd=$(ls chapters/Unit_${stem%%.*}/${stem}_*.qmd 2>/dev/null | head -1) ;;
  esac
  if [[ -n "$qmd" && -f "$qmd" ]]; then
    warn=$(pandoc -f markdown -t html --mathml "$qmd" -o /dev/null 2>&1 | grep -A2 "Could not convert")
    [[ -z "$warn" ]] && echo "  page math: ok ($qmd)" || { echo "  PAGE MATH ERRORS in $qmd:"; echo "$warn" | sed 's/^/    /'; }
    for img in $(grep -o '/images/[^)]*\.svg' "$qmd"); do [[ -f ".$img" ]] || echo "  MISSING IMAGE on page: $img"; done
  fi
done
