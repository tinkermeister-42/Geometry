#!/usr/bin/env python3
"""Fail the deploy if a figure or a guided-notes handout is stale or missing.

- every figures/Unit_X/<name>.tex has images/Unit_X/<name>.svg (and
  <name>_KEY.svg when it uses \\ifkey), newer than the .tex and the shared
  figures/preamble.tex.  Run scripts/make-figures.sh to fix
- every printable (guided notes, summary, review, quiz) and key matches what
  its fragment builds today.
  Run scripts/build-guided-notes.py to fix
- every handout, and every image a handout shows, is in _book/

"Newer" uses the last commit time for a file that is committed and unchanged,
and the file's mtime otherwise.  A checkout or fresh clone rewrites mtimes in
no useful order, so mtimes alone report clean files as stale.
"""
import pathlib, re, subprocess, sys

root = pathlib.Path(__file__).resolve().parent.parent
bad = []


def git(*args):
    try:
        return subprocess.run(["git", "-C", str(root), *args],
                              capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return ""


dirty = set()
for line in git("status", "--porcelain", "-uall").splitlines():
    dirty.add(line[3:].split(" -> ")[-1])

committed = {}  # path -> time of the newest commit that touched it
when = None
for line in git("log", "--format=%x00%ct", "--name-only").splitlines():
    if line.startswith("\x00"):
        when = int(line[1:])
    elif line and line not in committed:
        committed[line] = when


def stamp(p):
    rel = p.relative_to(root).as_posix()
    if rel in committed and rel not in dirty:
        return committed[rel]
    return p.stat().st_mtime


preamble = root / "figures" / "preamble.tex"
for src in sorted(root.glob("figures/Unit_*/*.tex")):
    names = [src.stem]
    if "\\ifkey" in src.read_text():
        names.append(src.stem + "_KEY")
    newest = max(stamp(src), stamp(preamble))
    for name in names:
        svg = root / "images" / src.parent.name / (name + ".svg")
        if not svg.exists() or stamp(svg) < newest:
            bad.append(f"stale or missing {svg.relative_to(root)} (run scripts/make-figures.sh)")

notes = subprocess.run([sys.executable, str(root / "scripts" / "build-guided-notes.py"), "--check"],
                       capture_output=True, text=True)
if notes.returncode:
    bad.append((notes.stdout + notes.stderr).strip())

book = root / "_book"
if book.exists():
    for page in (sorted(root.glob("guided_notes/Unit_*/*.html")) +
                 sorted(root.glob("assessments/Unit_*/*.html")) + [root / "assessments" / "index.html"]):
        rel = page.relative_to(root)
        if not (book / rel).exists():
            bad.append(f"not in site: _book/{rel}")
        for img in re.findall(r'<img[^>]+src="([^"]+)"', page.read_text()):
            target = (page.parent / img).resolve()
            built = book / target.relative_to(root)
            if not built.exists():
                bad.append(f"not in site: _book/{target.relative_to(root)} (shown by {rel.name})")

if bad:
    print("check-site-assets:\n  " + "\n  ".join(bad))
    sys.exit(1)
print("check-site-assets: ok")
