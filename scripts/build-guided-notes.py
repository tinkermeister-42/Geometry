#!/usr/bin/env python3
"""Build the printable handouts: guided notes, unit summaries and reviews, quizzes.

Each printable lives as a body fragment with a small metadata header:

  guided_notes/src/<lesson>.html  ->  guided_notes/Unit_<n>/<lesson>_<Slug>.html
  guided_notes/src/<n>.Summary.html, <n>.Review.html  (unit summary and review)
  assessments/src/Unit<n>_Quiz.html  ->  assessments/Unit_<n>/Unit<n>_Quiz.html

Header keys: lesson, title, unit, unit_title, slug.  Optional: file (the
output name, default <lesson>_<slug>), page (the lesson page the backlink
goes to, default the same as file), label (the line under the title,
default "Guided Notes", or "Quiz" for an assessment).  Quizzes get no
backlink and are not listed on guided-notes.qmd.

Answers live in the same fragment, wrapped in {{a}}...{{/a}}.  The student
handout drops them; the teacher key renders them in red.  A key is written
only for lessons whose fragment actually contains answers.

    python3 scripts/build-guided-notes.py            # build everything
    python3 scripts/build-guided-notes.py 3.4 3.5    # build just these
    python3 scripts/build-guided-notes.py --keys-only
    python3 scripts/build-guided-notes.py --check    # exit 1 if any built file is stale

Figures come from the same TikZ sources as the lesson pages:
{{fig 1.1_name|alt text}} or {{fig 1.1_name|alt text|2.4in}} is the SVG at
images/Unit_1/1.1_name.svg (made by scripts/make-figures.sh).  On a key, a
figure with a _KEY.svg twin (its .tex uses \\ifkey) shows that twin instead.

The listing page guided-notes.qmd and the teacher bookmark
assessments/index.html are written from the fragments, so neither needs
editing by hand.  Nothing links to the bookmark or to any _KEY file.
"""
import glob
import os
import re
import sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
# (kind, fragment folder, output folder, path from an output page to the shared assets)
SOURCES = [
    ("notes", os.path.join(ROOT, "guided_notes", "src"), os.path.join(ROOT, "guided_notes"), "../assets/"),
    ("quiz", os.path.join(ROOT, "assessments", "src"), os.path.join(ROOT, "assessments"),
     "../../guided_notes/assets/"),
]
SRC = SOURCES[0][1]

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{label} {lesson} - {title}{title_suffix}</title>
<link rel="stylesheet" href="{assets}guided-notes.css">
</head>
<body>
<section class="sheet">

  <div class="masthead">
    {backlink}<h1>{lesson} &nbsp;{title}</h1>
    <div class="sub">{label} - Unit {unit}: {unit_title} - DHS Geometry</div>
    {idline}
  </div>

{body}
</section>
</body>
</html>
"""

# Lightweight shorthands so the fragments stay readable.  Expanded here.
SHORTHAND = {  # {assets} is filled in per output folder
    "{{nl}}":       '<img class="nl" src="{assets}nl.svg" alt="number line from -10 to 10">',
    "{{nl-blank}}": '<img class="nl" src="{assets}nl-blank.svg" alt="blank number line">',
    "{{nl-0}}":     '<img class="nl" src="{assets}nl-zero.svg" alt="number line with only zero labeled">',
    "{{nl-11}}":    '<img class="nl" src="{assets}nl-blank-11.svg" alt="blank number line">',
    "{{grid}}":     '<img class="grid" src="{assets}grid.svg" alt="coordinate grid">',
    "{{grid-sm}}":  '<img class="grid sm" src="{assets}grid.svg" alt="coordinate grid">',
    "{{grid-lg}}":  '<img class="grid lg" src="{assets}grid.svg" alt="coordinate grid">',
    "{{grid-blank}}": '<img class="grid" src="{assets}grid-blank.svg" alt="blank coordinate grid">',
    "{{grid-q1}}":  '<img class="grid" src="{assets}grid-q1.svg" alt="first quadrant grid">',
    "{{break}}":    '<div class="pagebreak"></div>',
}

HEADER_RE = re.compile(r"\A<!--(.*?)-->\s*", re.S)
# {{a}}...{{/a}} marks answer content: dropped from the student handout,
# shown in red on the teacher key.
ANS_RE = re.compile(r"\{\{a\}\}(.*?)\{\{/a\}\}", re.S)
# an answer holding block-level markup needs a block wrapper, not a <span>
BLOCK_RE = re.compile(r"<(table|div|p|ul|ol|h[1-6])\b", re.I)

IDLINE = ('<div class="idline"><span>Name</span>'
          '<span class="small">Date</span><span class="small">Period</span></div>')
KEYLINE = '<div class="keybadge">Teacher Key: answers in red</div>'


def _drop_answers(body):
    # An answer sitting alone on its line takes the whole line with it, so the
    # student handout is byte-identical to one built from a fragment carrying no
    # answers at all.  Each answer collapses to a sentinel first: a line left
    # holding nothing but sentinels goes, anything else just loses them.
    sent = "\x00"
    lines = []
    for line in ANS_RE.sub(sent, body).split("\n"):
        if sent in line and not line.replace(sent, "").strip():
            continue
        lines.append(line.replace(sent, ""))
    return "\n".join(lines)


def _show_answers(body):
    def repl(m):
        inner = m.group(1)
        tag = "div" if BLOCK_RE.search(inner) else "span"
        return '<%s class="ans-key">%s</%s>' % (tag, inner, tag)
    return ANS_RE.sub(repl, body)
# {{f 3/4}} -> a stacked fraction.  The parts may contain markup, so the
# dividing slash is the first one that is not part of a "</" or "/>" tag.
FRAC_RE = re.compile(r"\{\{f (.+?)\}\}", re.S)

# Geometry notation.  Point names are italic capitals; the mark above them is
# drawn with borders in guided-notes.css so it prints without backgrounds.
#   {{seg AB}} segment   {{ray AB}} ray   {{line AB}} line   {{arc AB}} arc
#   {{ang ABC}} angle ABC    {{mang ABC}} the measure of angle ABC
GEO_RE = re.compile(r"\{\{(seg|ray|line|arc|ang|mang) ([^}]+?)\}\}")


def _geo(match):
    kind, name = match.group(1), match.group(2).strip()
    if kind == "ang":
        return "&ang;<var>%s</var>" % name
    if kind == "mang":
        return "<i>m</i>&ang;<var>%s</var>" % name
    return '<span class="%s"><var>%s</var></span>' % (kind, name)


FIG_RE = re.compile(r"\{\{fig ([^|}]+)\|([^|}]*)(?:\|([^}]+))?\}\}")


def _figure(match, key):
    name, alt, width = (match.group(1).strip(), match.group(2).strip(),
                        (match.group(3) or "").strip())
    unit = name.split(".", 1)[0]
    if not unit.isdigit():
        raise SystemExit("{{fig %s}}: name must start with its lesson number" % name)
    if key and os.path.exists(os.path.join(ROOT, "images", "Unit_%s" % unit,
                                           name + "_KEY.svg")):
        name += "_KEY"
    if not os.path.exists(os.path.join(ROOT, "images", "Unit_%s" % unit, name + ".svg")):
        raise SystemExit("{{fig %s}}: images/Unit_%s/%s.svg is missing "
                         "(run scripts/make-figures.sh)" % (name, unit, name))
    style = ' style="width:%s"' % width if width else ""
    return ('<img class="fig" src="../../images/Unit_%s/%s.svg" alt="%s"%s>'
            % (unit, name, alt, style))


def _fraction(match):
    """Split {{f a/b}} at its dividing slash.

    Slashes inside a tag (</var>, />) or inside a <sup> (a fractional exponent
    like x^{5/4}) are not the fraction bar, so they are skipped.
    """
    body = match.group(1)
    sup, i, n = 0, 0, len(body)
    while i < n:
        if body.startswith("<sup", i):
            sup += 1
        elif body.startswith("</sup>", i):
            sup -= 1
        if body[i] == "<":                     # step over the whole tag
            close = body.find(">", i)
            i = close + 1 if close >= 0 else i + 1
            continue
        if body[i] == "/" and sup == 0:
            return ('<span class="f"><b>%s</b><b>%s</b></span>'
                    % (body[:i].strip(), body[i + 1:].strip()))
        i += 1
    raise SystemExit("no dividing slash in {{f %s}}" % body)


def parse(path):
    raw = open(path).read()
    m = HEADER_RE.match(raw)
    if not m:
        raise SystemExit(f"{path}: missing metadata header comment")
    meta = {}
    for line in m.group(1).strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    for key in ("lesson", "title", "unit", "unit_title", "slug"):
        if key not in meta:
            raise SystemExit(f"{path}: metadata is missing '{key}'")
    kind = source_of(path)[0]
    meta.setdefault("file", "%s_%s" % (meta["lesson"], meta["slug"]))
    meta.setdefault("page", meta["file"])
    meta.setdefault("label", "Quiz" if kind == "quiz" else "Guided Notes")
    meta["kind"] = kind
    return meta, raw[m.end():]


def source_of(path):
    folder = os.path.dirname(os.path.abspath(path))
    for src in SOURCES:
        if os.path.abspath(src[1]) == folder:
            return src
    raise SystemExit(f"{path}: not in a fragment folder")


def build(path, key=False, check=False):
    """Render one fragment.  key=True produces the teacher answer key.
    check=True writes nothing and returns None when the file on disk is stale."""
    meta, body = parse(path)
    kind, _, out_root, assets = source_of(path)
    body = _show_answers(body) if key else _drop_answers(body)
    for token, html in SHORTHAND.items():
        body = body.replace(token, html.replace("{assets}", assets))
    body = FIG_RE.sub(lambda m: _figure(m, key), body)
    body = GEO_RE.sub(_geo, body)
    body = FRAC_RE.sub(_fraction, body)
    # a practice section always starts on a fresh page, with its own name line
    body = body.replace("{{practice-head}}",
                        '<div class="pagebreak"></div>\n'
                        '  <div class="parthead"><b>%s %s - Practice</b>%s</div>'
                        % (meta["lesson"], meta["title"],
                           "" if key else '<span class="nm">Name</span>'))
    backlink = ("" if kind == "quiz" else
                '<a class="backlink" href="../../chapters/Unit_%s/%s.html">&larr; back to the lesson</a>\n    '
                % (meta["unit"], meta["page"]))
    page = SHELL.format(body=body.rstrip() + "\n",
                        title_suffix=" (Teacher Key)" if key else "",
                        idline=KEYLINE if key else IDLINE,
                        assets=assets, backlink=backlink,
                        **{k: v for k, v in meta.items() if k != "kind"})
    unit_dir = os.path.join(out_root, "Unit_%s" % meta["unit"])
    os.makedirs(unit_dir, exist_ok=True)
    dest = os.path.join(unit_dir, "%s%s.html" % (meta["file"], "_KEY" if key else ""))
    if check:
        if not os.path.exists(dest) or open(dest).read() != page:
            return None
        return os.path.relpath(dest, ROOT)
    with open(dest, "w") as f:
        f.write(page)
    return os.path.relpath(dest, ROOT)


def has_answers(path):
    return bool(ANS_RE.search(open(path).read()))


LISTING_HEAD = """# Printable Guided Notes {.unnumbered}

Every lesson has a **guided notes** handout. It has the objectives, the key ideas
with blanks to fill in, and every example and practice problem with room to work.

Open one and use your browser's **Print** command. They are laid out for
letter-size paper.

***
"""


def order(meta):
    """Lessons in number order, then the unit Summary, then the Review."""
    m = re.match(r"^(\d+)\.(\d+)$", meta["lesson"])
    if m:
        return (int(meta["unit"]), 0, int(m.group(2)))
    return (int(meta["unit"]), {"Summary": 1, "Review": 2}.get(meta["title"], 3), 0)


def all_fragments():
    for _, folder, _, _ in SOURCES:
        for path in glob.glob(os.path.join(folder, "*.html")):
            yield path


def write_if_changed(dest, text):
    if os.path.exists(dest) and open(dest).read() == text:
        return False
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as f:
        f.write(text)
    return True


def write_listing():
    """guided-notes.qmd: every handout, grouped by unit, in lesson order."""
    units = {}
    for path in all_fragments():
        meta, _ = parse(path)
        if meta["kind"] == "notes":
            units.setdefault(int(meta["unit"]), []).append(meta)
    out = [LISTING_HEAD]
    for unit in sorted(units):
        lessons = sorted(units[unit], key=order)
        out.append("\n## Unit %d - %s\n" % (unit, lessons[0]["unit_title"]))
        for m in lessons:
            name = ("%s - %s" % (m["lesson"], m["title"]) if order(m)[1] == 0
                    else "Unit %s %s" % (m["unit"], m["title"]))
            out.append("  - [%s](/guided_notes/Unit_%s/%s.html){target=\"_blank\"}"
                       % (name, m["unit"], m["file"]))
    return write_if_changed(os.path.join(ROOT, "guided-notes.qmd"), "\n".join(out) + "\n")


BOOKMARK = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>DHS Geometry - teacher bookmark</title>
<style>
body {{ font-family: Georgia, serif; max-width: 52rem; margin: 2rem auto; padding: 0 1rem; color: #111; }}
h1 {{ font-size: 1.4rem; }} h2 {{ font-size: 1.1rem; margin-top: 1.6rem; border-bottom: 1px solid #ccc; }}
table {{ border-collapse: collapse; width: 100%; }} td {{ padding: .2rem .5rem; border-bottom: 1px solid #eee; }}
td.k a {{ color: #c0192b; }}
</style></head><body>
<h1>DHS Geometry: printables and keys</h1>
<p>Unlisted. Nothing in the book links here or to any key.</p>
{body}
</body></html>
"""


def write_bookmark():
    """assessments/index.html: every printable with its key, for the teacher."""
    units = {}
    for path in all_fragments():
        meta, _ = parse(path)
        units.setdefault(int(meta["unit"]), []).append((path, meta))
    out = []
    for unit in sorted(units):
        rows = sorted(units[unit], key=lambda pm: (pm[1]["kind"] == "quiz", order(pm[1])))
        out.append("<h2>Unit %d: %s</h2>\n<table>" % (unit, rows[0][1]["unit_title"]))
        for path, m in rows:
            folder = "guided_notes" if m["kind"] == "notes" else "assessments"
            href = "../%s/Unit_%s/%s" % (folder, m["unit"], m["file"])
            key = ('<a href="%s_KEY.html">key</a>' % href) if has_answers(path) else ""
            out.append('<tr><td><a href="%s.html">%s %s</a></td><td class="k">%s</td></tr>'
                       % (href, m["lesson"], m["title"], key))
        out.append("</table>")
    return write_if_changed(os.path.join(ROOT, "assessments", "index.html"),
                            BOOKMARK.format(body="\n".join(out)))


def sort_key(path):
    meta, _ = parse(path)
    return (meta["kind"] == "quiz",) + order(meta)


if __name__ == "__main__":
    args = sys.argv[1:]
    keys_only = "--keys-only" in args
    check = "--check" in args
    wanted = set(a for a in args if not a.startswith("--"))
    made, keys, no_key, stale = [], [], [], []
    for path in sorted(all_fragments(), key=sort_key):
        stem = os.path.splitext(os.path.basename(path))[0]
        if wanted and stem not in wanted:
            continue
        jobs = [] if keys_only else [False]
        if has_answers(path):
            jobs.append(True)
        else:
            no_key.append(stem)
        for key in jobs:
            done = build(path, key=key, check=check)
            if done is None:
                stale.append("%s%s" % (stem, " key" if key else ""))
            else:
                (keys if key else made).append(done)
    if check:
        if stale:
            print("stale printables (run scripts/build-guided-notes.py): " + " ".join(stale))
            sys.exit(1)
        print("printables: %d handout(s), %d key(s) up to date" % (len(made), len(keys)))
        sys.exit(0)
    for m in made + keys:
        print("built", m)
    if write_listing():
        print("wrote guided-notes.qmd")
    if write_bookmark():
        print("wrote assessments/index.html")
    print("%d handout(s), %d teacher key(s)" % (len(made), len(keys)))
    if no_key:
        print("no answers yet (no key written): %s" % " ".join(sorted(no_key)))
