#!/bin/bash
# Build the figures and the guided notes for some or all lessons.
#   ./build.sh            everything
#   ./build.sh 1.1 2.4    only those lessons (figure names and handouts that start with them)
set -euo pipefail
cd "$(dirname "$0")"
scripts/make-figures.sh "$@"
if [[ $# -gt 0 ]]; then
  # handout fragments are named by lesson number: guided_notes/src/1.1.html
  python3 scripts/build-guided-notes.py "$@"
else
  python3 scripts/build-guided-notes.py
fi
