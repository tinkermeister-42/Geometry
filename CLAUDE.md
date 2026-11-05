# DHS Geometry: Project Context

The Geometry textbook for Frederick Douglass High School, written for spring
2027. The teacher teaches from it; students do not work in another platform
alongside it. Khan Academy's High school geometry was used only as a coverage
checklist when the course map was drawn. The course map (8 units, 47 lessons)
is the table in `index.md`.

Built from the DHS Statistics book (`tinkermeister-42/Statistics`): same
theme, callouts, glossary and headings extensions, the same unit shape
(lessons, Summary, Review, quiz), and TikZ figures. One change from
Statistics: **printables are HTML, never PDF.** The classroom smartboard has
no PDF reader. Handouts use the Algebra 1 book's guided-notes builder
(`tinkermeister-42/Algebra1`).

## Build & Deploy
- **Figures:** `scripts/make-figures.sh [1.1 ...]` turns
  `figures/Unit_X/<name>.tex` into `images/Unit_X/<name>.svg` (pdflatex,
  pdftocairo). Shared macros are in `figures/preamble.tex`
- **Printables:** `python3 scripts/build-guided-notes.py [1.1 1.Review Unit1_Quiz ...]`
  builds `guided_notes/Unit_X/<lesson>_<Slug>.html` and `_KEY.html` from
  `guided_notes/src/<lesson>.html`, quizzes from `assessments/src/`, and
  rewrites the listing page `guided-notes.qmd` and the teacher bookmark.
  Never edit the built files, the listing or the bookmark by hand
- **Both at once:** `./build.sh [1.1 ...]`. Commit the SVGs and built HTML
- **Render:** `quarto render --to html` (run it twice on a fresh clone: the
  glossary post-render writes `glossary.json` after the copy step)
- **Deploy:** `./deploy.sh` renders, runs `scripts/check-site-assets.py`
  (fails on a stale or missing SVG, a handout that does not match its
  fragment, or a handout image missing from `_book`), and force-pushes `_book`
  to `gh-pages` (personal site: `tinkermeister-42.github.io/Geometry`)
- **Mirror to the work site is manual.** The teacher reviews the personal
  site, then runs "Mirror site to Work Account" from the Actions tab
  (`.github/workflows/sync-to-work.yml`). It needs the repo secrets
  `WORK_TOKEN`, `WORK_OWNER` and `WORK_REPO`, and the work repo must exist
- A shallow clone fetches only `main`, so `deploy.sh` dies with "invalid
  reference: origin/gh-pages". Fix with
  `git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*' && git fetch --depth 1 origin gh-pages`
- A container needs quarto >= 1.7 (tarball from the quarto-cli releases into
  `/opt/quarto`; `add_repo` for `quarto-dev/quarto-cli` opens the download),
  pdflatex, `pdftocairo` (poppler), pandoc, and a clean tree
- **Fresh clone mtimes:** checkout writes files in no useful order, so the
  asset check can call committed SVGs stale. They are not:
  `git ls-files 'images/*.svg' | xargs touch`

## Structure
```
chapters/Unit_1…8/     # Lessons: #.#_Topic.qmd, index.qmd, Summary.qmd, Review.qmd
figures/Unit_1…8/      # TikZ sources -> images/Unit_X/*.svg (page and handout)
guided_notes/src/      # Handout fragments, one per lesson (what you edit)
guided_notes/Unit_X/   # Built handouts and keys (generated, committed)
guided_notes/assets/   # Handout stylesheet, shared grids and number lines
scripts/               # Builders, asset check, glossary build, JS helpers
styles/                # CSS (from the Algebra 1 book)
_extensions/           # glossary, headings
glossary.qmd           # Source -> glossary.json on render
```

## Lesson Page Pattern
Title, a concrete hook, `.objectives`, `.vocab`, a `.guided-notes-link` to
the handout, `{{< warmup >}}`, `{{< learn >}}` with numbered `### #.#.# -`
sections, then `{{< practice >}}` restating the handout's practice. Callouts
are the Algebra 1 set (`.remember`, `.you-try`, `.you-try-m` + `.answer`,
`.think`, `.gotcha`, `.note`, `.real-world`).

- **Lesson, handout and figures are one change.** The handout restates the
  page's examples and practice. Edit the `.qmd`, the fragment and any figure
  together, then `./build.sh <lesson>`
- **One figure source.** A picture is drawn once, in `figures/`, and both the
  page (`![](/images/Unit_X/<name>.svg)`) and the handout
  (`{{fig <name>|alt text}}`) show that SVG. Name figures `<lesson>_<what>`
- **Key figures:** answers drawn on a figure go inside `\ifkey ... \fi` in
  the key colour (`\ans{}`, `answer` style). The figure builder then makes a
  `_KEY.svg` twin and the handout key shows it automatically
- **Keys are unlisted.** `<name>_KEY.html` sits beside the handout and nothing
  links to it. The URL is predictable on purpose so it can be shared with
  colleagues. Practice answers are not printed on the page, so a You Try or
  worked example never reuses a practice problem's numbers or scenario
- **A key answers the paper in the space provided.** Answers go inline with
  `{{a}}...{{/a}}` in the fragment, in the blank or work area they answer
- **A new lesson wires itself in:** add it to `_quarto.yml`, link its row in
  the `index.md` course map, and link its line in the unit intro (unwritten
  lessons stay as plain bold text so the site has no dead links)
- Worksheet directions say "Work with a partner", never "work by yourself"
- **Money in prose is math:** write `$\$84{,}000$`. A bare `$84,000` pairs
  with the next dollar sign and MathJax renders the text between as math

## Guided Notes
- Fragment header: `lesson`, `title`, `unit`, `unit_title`, `slug`. The slug
  matches the lesson `.qmd` file name after the number
- Shorthands (full list in `guided_notes/README.md`): `{{fig name|alt}}`,
  `{{seg AB}}`, `{{ray AB}}`, `{{line AB}}`, `{{arc AB}}`, `{{ang ABC}}`,
  `{{mang ABC}}`, `{{f a/b}}`, `{{grid}}`, `{{nl}}`, `{{break}}`,
  `{{practice-head}}`
- Self-contained: no JavaScript, no CDN. Math is HTML/CSS. Figures are
  `<img>` so they print with background graphics off
- Building blocks: `.keys`, `.ex` (`.q` + `.work`), `.ex.yours` (a student
  turn), `.box.tint`, `.box.warn`, `.b` blanks, `table.vocab`, `table.steps`,
  `table.fill`, `.cols2`, `.figrow`, work heights `.h05` to `.h25`

## Geometry Notation
Real notation, explained the first few times it appears, each symbol with a
glossary entry. Check page math with
`pandoc -f markdown -t html --mathml <file>.qmd -o /dev/null`: a "Could not
convert TeX math" warning is a typo MathJax will show raw.

| Idea | Page (MathJax) | Handout |
|---|---|---|
| segment | `$\overline{AB}$` | `{{seg AB}}` |
| ray | `$\overrightarrow{AB}$` | `{{ray AB}}` |
| line | `$\overleftrightarrow{AB}$` | `{{line AB}}` |
| length of a segment | `$AB$` | `<var>AB</var>` |
| arc, its measure | `$\overset{\frown}{AB}$`, `$m\overset{\frown}{AB}$` | `{{arc AB}}`, `<i>m</i>{{arc AB}}` |
| angle, its measure | `$\angle ABC$`, `$m\angle ABC$` | `{{ang ABC}}`, `{{mang ABC}}` |
| congruent, parallel, perpendicular | `$\cong$`, `$\parallel$`, `$\perp$` | `&cong;`, `&#8741;`, `&perp;` |

Figures mark equal parts with `tick1`/`tick2`/`tick3`, parallel lines with
`par1`/`par2`, angles with `\pic[ang]`, right angles with `\pic[rt]`.

## Course Design

**The coordinate plane is the spine.** Unit 2 builds the algebra tools
(Pythagorean theorem, distance, midpoint, slope), and every later unit uses
them: transformations on a grid, congruence checked with distance, similarity
with slope, trigonometry with tangent as slope. When a lesson can show an idea
both as a figure and on a grid, it does.

**No two-column proofs.** The teacher's view: the usual emphasis on formal
proof does not suit these students and is a poor introduction to proof. What
proof is for, telling what *looks* true from what *must* be true, is taught
other ways:

- **Computation as proof:** "show it with coordinates." Two equal slopes
  prove two lines are parallel. Starts in 2.9 and recurs
- **Counterexamples:** show a claim is not always true (SSA, a rhombus that
  is not a square)
- **Shows vs. suggests:** what the marks on a figure guarantee, against what
  the picture only appears to show. Figures are drawn to scale by default;
  a figure that is not says so, and those are used on purpose
- **Error analysis:** find and fix the mistake in sample work

**Real problems.** Trigonometry and the Pythagorean theorem carry the most
applications: squaring a corner with 3-4-5, ladders, ramps (1:12), roof
pitch, screens, angles of elevation. Volume uses concrete, water and paint.

## Unit Pages and Assessments
- **Unit intro:** `chapters/Unit_X/index.qmd`, a short welcome, "What you'll
  learn", and a topic list. Each topic line ends with a backslash (a hard
  line break). Trailing double spaces get stripped by editors
- **Summary page** (`Summary.qmd`) between the last lesson and the review:
  every tool the unit teaches, in the lessons' own words and notation; nothing
  new. Its printable is `guided_notes/src/<n>.Summary.html` (header
  `lesson: Unit <n>`, `title: Summary`, `slug: Summary`,
  `file: Unit_<n>_Summary`, `page: Summary`, `label: Unit Summary`)
- **Review page** (`Review.qmd`) mirrors the quiz goal for goal, at 2-3x the
  problems, then ends with test-style multiple choice. Printable:
  `guided_notes/src/<n>.Review.html` (`file: Unit_<n>_Review`,
  `page: Review`, `label: Unit Review`)
- **Quiz:** one per unit, the Statistics shape: a section per lesson headed
  by its "I can" goal, two questions per lesson. Fragment
  `assessments/src/Unit<n>_Quiz.html` (`lesson: Unit <n>`, `title: Quiz`,
  `slug: Quiz`, `file: Unit<n>_Quiz`) builds to
  `/assessments/Unit_<n>/Unit<n>_Quiz.html` and `_KEY.html`, unlisted
- **Teacher bookmark:** `/assessments/index.html` lists every printable with
  its key. The builder writes it; nothing links to it

## Branches

**Commit straight to `main`.** The teacher works alone, and his review step is
seeing the pages or printables before they go live, not a branch. Feature
branches are team ceremony here, and this session's credentials cannot delete
them (`git push origin --delete` returns HTTP 403), so they pile up.

- **Work on `main`.** Commit finished work to `main` and push it in the same
  turn. Squash work-in-progress commits locally before pushing, so `main`
  keeps a history of what was added, one commit per piece of work
- **Show before publishing.** Committing to `main` before he has looked is
  fine; deploying is not
- **Deploy only from `main`.** Run `./deploy.sh` on a clean `main`
- **Check at the start of every session:** `scripts/stale-branches.sh`. It
  lists every branch besides `main` and `gh-pages`, says whether its work is
  on `main`, and prints one delete command for the safe ones

Why: he assumes his changes are on `main` and can go weeks without noticing
they are not. In October 2026 the Statistics repo had five branches of
finished work sitting unmerged for up to two weeks.

## Writing Style

**Who is reading this.** About 80% of the students are not native English
speakers. Many read well below grade level, and some have never been to school
before and are placed in a class because of their age. Reading is the barrier,
not the mathematics. Every sentence a student has to decode twice is a sentence
that costs them the math.

Write for that reader:

- **Short sentences.** One idea each. Split a sentence before adding a clause
- **Common words.** Prefer "use" to "utilize", "shows" to "demonstrates",
  "same" to "equivalent" outside the glossary term itself
- **No colloquialisms or figurative idioms**, where the literal words do not
  give the meaning: "earns its keep", "comes in handy", "takes forever",
  "falls apart", "gets in the way", "what your gut tells you". Plain phrasal
  verbs ("show up", "figure out") are fine
- **No dash asides.** AI writes "the total goes up - removing a fee is like
  being handed the money" constantly; this teacher almost never does. The fix is
  not a different dash character, it is a different sentence. Split it in two,
  use a comma, or put a short aside in parentheses. Labels in a list take a
  colon ("**Ray**: starts at a point and goes on forever"). Section headings
  keep the spaced hyphen they already use
- **Lead with the concrete.** A number, a picture, or a story first; the
  general rule after
- **Do not let prose carry the math.** If a step matters, it belongs in a
  worked example, a labelled figure, or a fill-in blank, not buried in a
  paragraph

**The mathematics does not get easier.** Simplify the sentence, never the
problem: keep the multi-step work, the negatives, the word problems, the
rigour. The goal is that reading stops hiding what a student actually knows.

Because test items are wordy, the book should also build that reading up
rather than avoid it: introduce a type of problem in plain language first, then
show the same problem worded the way a test words it.

## Curriculum Judgment

**Do not propose cutting a lesson.** The teacher has taught geometry,
statistics, Algebra 2 and Algebra 1, and did mathematics professionally for
twenty years before that. Scope decisions are his. What a lesson is for is not
always visible in its text. Report what the measurements say and let him
decide.
