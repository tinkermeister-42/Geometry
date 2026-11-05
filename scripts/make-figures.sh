#!/bin/bash
# Render the figures: figures/Unit_X/<name>.tex -> images/Unit_X/<name>.svg
#   scripts/make-figures.sh            all figures
#   scripts/make-figures.sh 1.3        only figures whose name starts with 1.3
# The lesson page and the guided notes both use the SVG, so one .tex is the
# only copy of a picture.  A figure that uses \ifkey also gets <name>_KEY.svg,
# built with the answers drawn in.
set -euo pipefail
cd "$(dirname "$0")/.."
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
shopt -s nullglob
for tex in figures/Unit_*/*.tex; do
  name="$(basename "$tex" .tex)"
  if [[ $# -gt 0 ]]; then
    hit=false; for p in "$@"; do [[ "$name" == "$p"* ]] && hit=true; done
    $hit || continue
  fi
  unit="$(basename "$(dirname "$tex")")"
  mkdir -p "images/$unit"
  jobs=("$name")
  grep -q '\\ifkey' "$tex" && jobs+=("${name}_KEY")
  for job in "${jobs[@]}"; do
    if [[ "$job" == *_KEY ]]; then src="\def\iskey{}\input{$name}"; else src="$name.tex"; fi
    ( cd "$(dirname "$tex")" && pdflatex -interaction=nonstopmode -halt-on-error \
        -output-directory="$tmp" -jobname="$job" "$src" >/dev/null ) \
      || { grep -A3 '^!' "$tmp/$job.log"; exit 1; }
    pdftocairo -svg "$tmp/$job.pdf" "images/$unit/$job.svg"
    echo "images/$unit/$job.svg"
  done
done
