#!/usr/bin/env python3
"""Find figure labels that touch a line, a dot, or another label.

    python3 _authoring/collisions.py [glob ...]      (default: images/Unit_*/*.svg)

Each SVG is opened in headless Chromium (Playwright). Text in a pdftocairo SVG
is a run of <use href="#glyph..."> elements; glyphs that sit side by side on
one baseline are grouped into a label. A label collides when:
  - a dark stroked path (a side, an axis, an arc, a ray) passes through it,
  - a dark filled shape (a point, an arrowhead) overlaps it, or
  - it overlaps another label.
Light strokes (grid lines) and light or white fills (shading, label backings)
are ignored. Prints one line per figure with collisions, with each label's
position as a percentage of the figure (x from the left, y from the top).
Exit status 1 when anything collides.
"""
import glob, os, sys
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHELL = "/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"

JS = r"""() => {
  const svg = document.querySelector('svg');
  const W = svg.getBoundingClientRect().width, H = svg.getBoundingClientRect().height;
  const lum = (c) => {
    if (!c || c === 'none') return null;
    const m = c.match(/rgb\(([\d.]+)%?,\s*([\d.]+)%?,\s*([\d.]+)%?\)/);
    if (!m) return c === 'white' || c === '#fff' || c === '#ffffff' ? 1 : 0;
    const k = c.includes('%') ? 100 : 255;
    return (0.3 * m[1] + 0.59 * m[2] + 0.11 * m[3]) / k;
  };
  // labels: pdftocairo writes each text run as a <g> of glyph <use>s. A label
  // can be two runs (a letter and its primes), so runs are only said to clash
  // when their glyphs overlap a lot, not when they touch.
  const isGlyph = (u) => (u.getAttribute('xlink:href') || u.getAttribute('href') || '').startsWith('#glyph');
  const runs = new Map();
  for (const u of document.querySelectorAll('use')) {
    if (!isGlyph(u)) continue;
    const r = u.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) continue;
    if (!runs.has(u.parentNode)) runs.set(u.parentNode, []);
    runs.get(u.parentNode).push(r);
  }
  const labels = [...runs.values()].map(rs => ({g: rs,
    l: Math.min(...rs.map(r => r.left)), r: Math.max(...rs.map(r => r.right)),
    t: Math.min(...rs.map(r => r.top)), b: Math.max(...rs.map(r => r.bottom))}));
  const inset = 0.7;
  // a dark line closer than 0.8px to a glyph's box counts as touching it
  const near = 0.8;
  const inside = (L, x, y) => L.g.some(r => x > r.left - near && x < r.right + near && y > r.top - near && y < r.bottom + near);
  const hits = labels.map(() => new Set());
  // drawn paths (not glyph outlines in <defs>)
  for (const p of document.querySelectorAll('path')) {
    if (p.closest('defs') || p.closest('clipPath')) continue;
    const cs = getComputedStyle(p);
    const st = cs.stroke !== 'none' ? lum(cs.stroke) : null;
    const fl = cs.fill !== 'none' ? lum(cs.fill) : null;
    const sw = parseFloat(cs.strokeWidth || '0');
    if (st !== null && st < 0.6 && sw > 0.25) {
      const len = p.getTotalLength(), M = p.getScreenCTM();
      if (!M || !len) continue;
      const n = Math.min(4000, Math.ceil(len / 0.6));
      const cnt = labels.map(() => 0);
      for (let k = 0; k <= n; k++) {
        const q = p.getPointAtLength(len * k / n);
        const x = M.a * q.x + M.c * q.y + M.e, y = M.b * q.x + M.d * q.y + M.f;
        labels.forEach((L, i) => { if (inside(L, x, y)) cnt[i]++; });
      }
      cnt.forEach((c, i) => { if (c >= 2) hits[i].add('line'); });
    } else if (fl !== null && fl < 0.6) {
      const r = p.getBoundingClientRect();
      if (r.width > 14 || r.height > 14) continue;      // big dark fills are rare; skip
      labels.forEach((L, i) => {
        if (L.g.some(q => Math.min(q.right - inset, r.right) - Math.max(q.left + inset, r.left) > 0.6 &&
                          Math.min(q.bottom - inset, r.bottom) - Math.max(q.top + inset, r.top) > 0.6)) hits[i].add('dot');
      });
    }
  }
  for (let i = 0; i < labels.length; i++) for (let j = i + 1; j < labels.length; j++) {
    // glyph boxes shrunk 15% a side: rotated text has fat boxes that meet at
    // the corners without the letters touching
    const sh = (r) => ({l: r.left + .15 * r.width, r: r.right - .15 * r.width, t: r.top + .15 * r.height, b: r.bottom - .15 * r.height, w: r.width, h: r.height});
    if (labels[i].g.map(sh).some(a => labels[j].g.map(sh).some(b => {
          const ox = Math.min(a.r, b.r) - Math.max(a.l, b.l);
          const oy = Math.min(a.b, b.b) - Math.max(a.t, b.t);
          return ox > 0.3 && oy > 0.3 && ox * oy > 0.1 * Math.min(a.w * a.h, b.w * b.h);
        }))) { hits[i].add('label'); hits[j].add('label'); }
  }
  return labels.map((L, i) => [Math.round(100 * (L.l + L.r) / 2 / W), Math.round(100 * (L.t + L.b) / 2 / H), [...hits[i]].join('+')])
               .filter(x => x[2]);
}"""

def main(pats):
    files = sorted(f for p in (pats or ["images/Unit_*/*.svg"]) for f in glob.glob(os.path.join(ROOT, p)))
    bad = 0
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=SHELL, args=["--no-sandbox"])
        page = b.new_page(viewport={"width": 1200, "height": 1200})
        for f in files:
            page.goto("file://" + f)
            res = page.evaluate(JS)
            if res:
                bad += 1
                print(os.path.relpath(f, ROOT) + ": " + "; ".join(f"({x}%,{y}%) {w}" for x, y, w in res))
        b.close()
    print(f"{bad} of {len(files)} figures have collisions", file=sys.stderr)
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
