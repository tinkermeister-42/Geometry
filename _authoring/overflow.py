"""Find printables whose content spills past the printed page width.
Usage: python3 overflow.py <repo> [glob ...]"""
import glob, sys, os
from playwright.sync_api import sync_playwright
repo = sys.argv[1]
pats = sys.argv[2:] or ["guided_notes/Unit_*/*.html", "assessments/Unit_*/*.html"]
files = sorted(f for p in pats for f in glob.glob(os.path.join(repo, p)))
JS = """() => {
  const lim = document.body.getBoundingClientRect().right + 2;
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const r = el.getBoundingClientRect();
    if (r.width > 0 && r.right > lim) {
      // report only the outermost overflowing element
      let p = el.parentElement, outer = true;
      while (p && p !== document.body) { if (p.getBoundingClientRect().right > lim) { outer = false; break; } p = p.parentElement; }
      if (outer) out.push([el.tagName.toLowerCase() + (el.className ? '.' + String(el.className).replace(/ /g,'.') : ''),
                           Math.round(r.right - lim), (el.innerText || el.getAttribute('src') || '').replace(/\\s+/g,' ').slice(0, 70)]);
    }
  }
  return out;
}"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 720, "height": 1000})   # 7.5 in printable width at 96 dpi
    pg.emulate_media(media="print")
    bad = 0
    for f in files:
        pg.goto("file://" + os.path.abspath(f))
        res = pg.evaluate(JS)
        if res:
            bad += 1
            print(os.path.relpath(f, repo), len(res))
            for tag, px, txt in res[:4]:
                print(f"   +{px}px {tag}: {txt}")
    print(f"{bad} of {len(files)} files overflow")
    b.close()
