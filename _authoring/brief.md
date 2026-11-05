# Brief: writing lessons for the DHS Geometry book

You are writing lessons for a geometry textbook: a Quarto book plus printable
HTML handouts ("guided notes") with teacher keys, for Frederick Douglass High
School in Columbia, Missouri. It is an alternative school. About 80% of the
students are English learners, many read far below grade level, and some have
had little school before. The teacher (Mr. Ross) teaches from the book and puts
the handouts on a smartboard and on paper. Reading is the barrier, not the
mathematics: simplify the sentences, never the math.

Tools folder: `TOOLS=/tmp/claude-0/-home-claude/1a39dfb0-44c1-5a62-8c73-190714273cb1/scratchpad/tools`

## Where you work

- Your git worktree and branch are in your assignment. Work ONLY there. Never
  touch `/home/claude/geometry` or another worktree. Do not push.
- Use absolute paths. Use the Write tool for new files and Edit for changes.

## Read first, in your worktree

1. `CLAUDE.md`: the project rules (writing style, notation, course design,
   printables). Follow it exactly.
2. The pilot lesson, the pattern to copy closely:
   `chapters/Unit_1/1.1_Points_Lines_Segments_and_Angles.qmd`,
   `guided_notes/src/1.1.html`, and three or four of `figures/Unit_1/1.1_*.tex`.
3. `figures/preamble.tex` (TikZ styles and macros), `guided_notes/README.md`
   (handout shorthands and blocks), `guided_notes/assets/guided-notes.css`.
4. `index.md` (course map) and `glossary.qmd`.
5. `$TOOLS/specs.md`: shared conventions at the top, then the spec for every
   lesson. Read the shared part, your lessons, and the lessons just before and
   after yours.

## What you make, for each lesson X.Y

- `chapters/Unit_X/<file>.qmd`, file name exactly as in the spec.
- `guided_notes/src/X.Y.html`. Header: `lesson: X.Y`, `title:` (the page
  title), `unit: X`, `unit_title:` (from `index.md`), `slug:` (the file name
  after `X.Y_`). Its `.guided-notes-link` on the page points to
  `/guided_notes/Unit_X/X.Y_<slug>.html`.
- `figures/Unit_X/X.Y_<what>.tex`, one per picture, built to
  `images/Unit_X/X.Y_<what>.svg` by `scripts/make-figures.sh X.Y_`.
- `glossary_add/X.Y.qmd`: glossary entries for the new terms your lesson uses,
  in the `glossary.qmd` format (`### term {#glossary-term-with-hyphens}`, a
  one- or two-sentence definition, an optional `> **Example:**` block, an
  optional `**See Also:**` line). Do not repeat a term already in
  `glossary.qmd`. Every `{{< glink ... >}}` on your page must name a term in
  `glossary.qmd` or in your own `glossary_add/` file. Another lesson written
  at the same time may add the same word; that is fine, it gets merged.

## Do not edit

`glossary.qmd`, `_quarto.yml`, `index.md`, any `chapters/Unit_X/index.qmd`,
`guided-notes.qmd`, `assessments/`, `scripts/`, `styles/`,
`figures/preamble.tex`, `guided_notes/assets/`, `CLAUDE.md`, or another
lesson's files. A TikZ helper you need goes inside your own figure `.tex`,
after `\input{../preamble}`. The builder rewrites `guided-notes.qmd` and
`assessments/index.html` every run: before you commit, run
`git checkout -- guided-notes.qmd assessments/index.html` and make sure
`git status` lists only your own files.

## Lesson page (copy the shape of 1.1)

- `# X.Y - Title {.unnumbered}`, then a concrete hook (a picture, a number,
  a short story) before any rule.
- `.objectives` with 3 or 4 "I can" lines; `.vocab` with a glink for each new
  term; the `.guided-notes-link`.
- `{{< warmup >}}`: 3 short items. One reviews an earlier lesson of this book
  (see the course map), one practices an algebra skill this lesson needs.
- `{{< learn >}}`: 3 to 5 sections `### X.Y.1 - Name`. Each has a short plain
  explanation, a labeled figure where it helps, worked examples
  (`**Example n:** Title`, with every step shown), and a You Try
  (`.you-try-m` followed by `.answer`, or `.you-try` with the question as its
  title and the solution inside). Use `.remember` for the rule or formula,
  `.gotcha` for a common mistake, `.think` for a question to talk about,
  `.real-world` for an application. Separate examples with `***`.
- `{{< practice >}}`: 20 to 30 problems in groups with bold headings, from
  routine to harder, with word problems. Then **Test practice**: 2 multiple
  choice items in long test wording. Then **Challenge**: 1 or 2. No answers
  on the page. A You Try or example never reuses a practice problem's numbers
  or story.
- Students do about 10 problems in 45 minutes. A lesson is one or two class
  blocks.

## Handout (`guided_notes/src/X.Y.html`)

Mirror the page the way 1.1 does: objectives box, Warm-Up, each section's key
ideas as fill-in blanks (`.keys` with `.b` blanks), every example as `.ex`
with blanks or work space, every You Try as `.ex.yours`, a Summary box with a
word bank (5 sentences, 1 to 3 extra words in the bank), `{{practice-head}}`,
every practice problem with room to work, then "Questions I still have".
Every blank and work area holds its answer in `{{a}}...{{/a}}`, so the key is
complete. Figures with `{{fig X.Y_name|alt text|width}}`. Real room to work:
`.work` with `.h08` to `.h2`, ruled lines for sentences, `{{grid}}` or
`{{grid-sm}}` where a student plots. Radicals: `<span class="sqrt">72</span>`,
fractions `{{f a/b}}`, exponents `<sup>2</sup>`, `&pi;`, `&deg;`, `&ang;`,
`&cong;`, `&#8741;` (parallel), `&perp;`, `&#9651;` (triangle), `&sim;`.
Aim for 5 to 8 printed pages; avoid half-empty pages.

## Figures

- One standalone `.tex` per picture, `\input{../preamble}`, built with
  `scripts/make-figures.sh X.Y_`. Use the preamble styles: `fig`, `line`,
  `ray`, `tick1/2/3`, `par1/2`, `\pic[ang]`, `\pic[rt]`, `\pt{A}{(x,y)}{pos}`,
  `\cgrid{xmin}{xmax}{ymin}{ymax}{label step}`, `answer`, `\ans{}`.
- Draw to scale: compute coordinates (TikZ `calc`, polar `(40:3)`, or
  numbers from python). A figure that is not to scale says "not drawn to
  scale" in the figure and is used on purpose.
- Labels must not touch lines or each other. Keep fonts readable at the
  width you show the figure (page widths 300 to 600px; handout 2 to 5.5in).
- Answers drawn on a figure (an image after a transformation, a construction,
  a shaded region, a plotted point) go inside `\ifkey ... \fi` in the key
  colour (`answer` style, `\ans{}` labels). The handout key then shows the
  `_KEY.svg` twin by itself. On the page, show the `_KEY.svg` version in a
  solution or answer callout when that helps.
- Practice figures are different from example figures.

## Writing (CLAUDE.md has the full rules)

Short sentences, one idea each. Common words. No idioms. No dash asides: no
em or en dashes, and no spaced hyphen asides in prose (headings keep
`X.Y.1 - Name`). Lead with the concrete. Steps that matter go in worked
examples, labeled figures, or blanks, not in paragraphs. "Work with a
partner", never "work by yourself". No age-of-the-Earth or age-of-the-universe
references. Money in prose is math: `$\$84{,}000$`. Real notation, said in
words the first time it appears in your lesson. Every problem that needs
rounding says how. Course design (CLAUDE.md): coordinate plane as the spine,
no two-column proofs, and the four ways to justify. Use them where they fit.
Introduce a problem type in plain words first, then show one worded the way a
test words it.

## Check before you commit (required)

1. Run `$TOOLS/preview.sh <your worktree> $TOOLS/../pv/<your branch> X.Y [X.Y ...]`.
   It builds your figures and handouts, prints the student copy and the key,
   and checks the page's math and image paths. Read EVERY PNG it writes
   (`X.Y_figs.png`, `X.Y_student.png`, `X.Y_key.png`) with the Read tool.
   Fix label collisions, figures too small or too big, a question split from
   its work space, half-empty pages, missing answers in the key. Run it again
   until it is clean and the math check says ok.
2. Compute every answer (use python for anything numeric): the key, the
   worked examples and the You Try answers must all be right and must agree
   with each other.
3. `cd <worktree> && quarto render chapters/Unit_X/<file>.qmd --to html` must
   finish with no errors. Then delete what it writes beside the file
   (`<file>.html` and the `<file>_files/` folder).
4. `grep -n "—\|–\| - " <your qmd and fragment>`: no dashes in prose
   (headings excepted).

## Commit

`git add` only your files, one commit on your branch:

```
Lessons X.Y to X.Z: <short titles>

<1 to 3 lines on what is in them>

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015VmZ8iCVJWi5TZn4oT8SPP
```

## Report back (short)

The commit hash; the files; glossary terms added; each handout's page count;
anything you assumed about a neighbouring lesson; anything the teacher should
decide.
