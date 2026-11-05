#!/usr/bin/env python3
"""Wire written lessons into the Geometry book (run from the repo root).

- merges glossary_add/*.qmd into glossary.qmd (dedupe by slug, earliest lesson
  wins, alphabetical by term) and removes glossary_add/
- rewrites the chapters list in _quarto.yml from the files that exist
- links every written lesson, Summary and Review in the index.md course map
"""
import glob, os, re, sys

UNIT_TITLES = {
    1: "Lines, Angles, and Equations",
    2: "The Pythagorean Theorem and the Coordinate Plane",
    3: "Transformations",
    4: "Congruence",
    5: "Similarity",
    6: "Right Triangle Trigonometry",
    7: "Circles",
    8: "Area, Surface Area, and Volume",
}


def lesson_num(path):
    m = re.match(r"(\d+)\.(\d+)_", os.path.basename(path))
    return (int(m.group(1)), int(m.group(2))) if m else None


# ---------------------------------------------------------------- glossary
ENTRY = re.compile(r"^### (.+?) \{#(glossary-[^}]+)\}\s*$", re.M)


def entries(text):
    """[(term, slug, body)] where body runs to the next entry or end."""
    out = []
    ms = list(ENTRY.finditer(text))
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        body = text[m.end():end].strip()
        body = re.sub(r"\n\*\*\*\s*$", "", body).strip()
        out.append((m.group(1).strip(), m.group(2).strip(), body))
    return out


def merge_glossary():
    base = open("glossary.qmd").read()
    head = base[:ENTRY.search(base).start()] if ENTRY.search(base) else "# Glossary {.unnumbered}\n\n"
    have = {slug: (term, body) for term, slug, body in entries(base)}
    added, dupes = [], []
    adds = sorted(glob.glob("glossary_add/*.qmd"),
                  key=lambda p: [int(x) for x in re.findall(r"\d+", os.path.basename(p))])
    for path in adds:
        for term, slug, body in entries(open(path).read()):
            if slug in have:
                dupes.append(f"{slug} ({os.path.basename(path)})")
                continue
            have[slug] = (term, body)
            added.append(slug)
    items = sorted(have.items(), key=lambda kv: kv[1][0].lower())
    text = head.rstrip() + "\n\n" + "\n\n***\n\n".join(
        f"### {term} {{#{slug}}}\n\n{body}" for slug, (term, body) in items) + "\n"
    open("glossary.qmd", "w").write(text)
    for path in adds:
        os.remove(path)
    if os.path.isdir("glossary_add") and not os.listdir("glossary_add"):
        os.rmdir("glossary_add")
    print(f"glossary: {len(added)} added, {len(dupes)} duplicates skipped, {len(items)} total")
    if dupes:
        print("  skipped:", ", ".join(dupes))
    return {slug for slug, _ in items}


# ---------------------------------------------------------------- _quarto.yml
def chapters_block():
    lines = ["  chapters:", "    - file: index.md", ""]
    for u in range(1, 9):
        d = f"chapters/Unit_{u}"
        if not os.path.exists(f"{d}/index.qmd"):
            continue
        lessons = sorted((p for p in glob.glob(f"{d}/*.qmd") if lesson_num(p)), key=lesson_num)
        lines.append(f'    - part: "Unit {u}: {UNIT_TITLES[u]}"')
        lines.append("      chapters:")
        lines.append(f"        - file: {d}/index.qmd")
        for p in lessons:
            lines.append(f"        - file: {p}")
        for extra in ("Summary", "Review"):
            if os.path.exists(f"{d}/{extra}.qmd"):
                lines.append(f"        - file: {d}/{extra}.qmd")
        lines.append("")
    lines += ["    - file: guided-notes.qmd", "    - file: glossary.qmd", ""]
    return "\n".join(lines)


def rewrite_quarto():
    s = open("_quarto.yml").read()
    i = s.index("  chapters:")
    s = s[:i] + chapters_block()
    open("_quarto.yml", "w").write(s)
    print("_quarto.yml: chapters rewritten")


# ---------------------------------------------------------------- index.md
def rewrite_course_map():
    s = open("index.md").read()
    out = []
    for line in s.split("\n"):
        m = re.match(r"^\| (?:\[)?(\d+)\.(\d+)(?:\]\([^)]*\))? \| (.*) \|$", line)
        if m:
            u, n = int(m.group(1)), int(m.group(2))
            files = glob.glob(f"chapters/Unit_{u}/{u}.{n}_*.qmd")
            label = f"[{u}.{n}]({files[0]})" if files else f"{u}.{n}"
            out.append(f"| {label} | {m.group(3)} |")
            continue
        out.append(line)
    s = "\n".join(out)
    # Summary and Review rows after each unit's last lesson
    s = re.sub(r"\n\| \[?(?:Summary|Review)\]?(?:\([^)]*\))? \|[^\n]*", "", s)
    def add_rows(text, u):
        rows = []
        for extra, desc in (("Summary", f"Unit {u} summary"), ("Review", f"Unit {u} review")):
            if os.path.exists(f"chapters/Unit_{u}/{extra}.qmd"):
                rows.append(f"| [{extra}](chapters/Unit_{u}/{extra}.qmd) | {desc} |")
        if not rows:
            return text
        last = [m for m in re.finditer(rf"^\| \[?{u}\.\d+.*$", text, re.M)][-1]
        return text[:last.end()] + "\n" + "\n".join(rows) + text[last.end():]
    for u in range(1, 9):
        s = add_rows(s, u)
    s = s.replace("\nEvery unit ends with a **Summary** and a **Review**.\n", "\n")
    open("index.md", "w").write(s.rstrip() + "\n")
    print("index.md: course map links rewritten")


# ---------------------------------------------------------------- checks
def check_glinks(slugs):
    bad = []
    for p in glob.glob("chapters/Unit_*/*.qmd"):
        for m in re.finditer(r'\{\{< glink (?:slug="([^"]+)"[^>]*|"([^"]+)"|(\S+)) >\}\}', open(p).read()):
            if m.group(1):   # slug= is given without the glossary- prefix (glink.lua)
                slug = "glossary-" + m.group(1)
            else:            # glink.lua: lower case, whitespace runs become "-"
                slug = "glossary-" + re.sub(r"\s+", "-", (m.group(2) or m.group(3)).lower())
            if slug not in slugs:
                bad.append(f"{os.path.basename(p)}: {slug}")
    print(f"glinks: {len(bad)} missing")
    for b in bad:
        print("  ", b)


if __name__ == "__main__":
    slugs = merge_glossary()
    rewrite_quarto()
    rewrite_course_map()
    check_glinks(slugs)
