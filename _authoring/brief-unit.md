# Brief: write one whole unit of the DHS Geometry book (lean version)

You write every lesson of one unit, then its Summary, Review and Quiz, in your
own git worktree, and commit once. Work in order, one lesson at a time. Keep
your own reading and checking lean: the teacher is paying for every token.

The book: Quarto textbook plus printable HTML handouts ("guided notes") with
teacher keys, for Frederick Douglass High School (Columbia, MO), an
alternative school. About 80% of students are English learners and many read
far below grade level. Simplify sentences, never the math.

## Read once, at the start (nothing else unless you need it)

1. `CLAUDE.md` (rules: writing style, notation, course design, printables).
2. `chapters/Unit_1/1.1_Points_Lines_Segments_and_Angles.qmd` and
   `guided_notes/src/1.1.html`: the pattern to copy. Read each once.
3. `figures/preamble.tex` and one figure, `figures/Unit_1/1.1_marks.tex`.
4. `guided_notes/README.md`, only the "Shorthands" and "Building blocks" parts.
5. `_authoring/specs.md`: the shared conventions at the top and your unit.
6. `_authoring/unit_intros/Unit_X_index.qmd` (your unit's intro). Move it to
   `chapters/Unit_X/index.qmd` (`mkdir -p chapters/Unit_X` and `git mv`).

Check a glossary term with `grep -n "^### " glossary.qmd`, not by reading it.

## Per lesson X.Y (file names exactly as in specs.md)

- Page `chapters/Unit_X/<file>.qmd`: `# X.Y - Title {.unnumbered}`; concrete
  hook; `.objectives` (3 or 4 "I can"); `.vocab` with `{{< glink term >}}`
  for new terms; `.guided-notes-link` to `/guided_notes/Unit_X/X.Y_<slug>.html`;
  `{{< warmup >}}` (3 items: one review, one algebra skill); `{{< learn >}}`
  with 3 to 5 `### X.Y.n - Name` sections of short explanation, labeled
  figures, worked examples (`**Example n:** Title`, every step), and a You Try
  (`.you-try-m` + `.answer`, or `.you-try` with the question as title); use
  `.remember`, `.gotcha`, `.think`, `.real-world` where they fit;
  `{{< practice >}}` with 20 to 30 grouped problems, then **Test practice**
  (2 multiple choice in long test wording) and **Challenge** (1 or 2). No
  answers on the page. Examples and You Trys never reuse practice numbers.
- Handout `guided_notes/src/X.Y.html` (header: lesson, title, unit,
  unit_title, slug = file name after `X.Y_`): mirrors the page like 1.1.html
  does; fill-in `.keys`; `.ex` for examples; `.ex.yours` for You Trys; a
  Summary box with a word bank; `{{practice-head}}`; every practice problem
  with room to work; every blank and work area answered in `{{a}}...{{/a}}`.
  5 to 8 printed pages.
- Figures `figures/Unit_X/X.Y_<what>.tex` (standalone, `\input{../preamble}`),
  drawn to scale, labels clear of lines. Answers drawn on a figure go in
  `\ifkey ... \fi` in the key colour (`answer`, `\ans{}`); the handout key
  shows the `_KEY` twin automatically. Grid figures use `\cgrid`.
- Glossary: new terms go in `glossary_add/X.Y.qmd`, same format as
  `glossary.qmd` (`### term {#glossary-term-with-hyphens}`, short definition,
  optional `> **Example:**`, optional `**See Also:**`). Never edit
  `glossary.qmd`. Every glink must name a term in one of the two.

Writing: short sentences, common words, no idioms, no dash asides (no em or
en dashes, no spaced hyphen asides; headings keep `X.Y.n - Name`), lead with
the concrete, steps in examples and blanks not paragraphs, "Work with a
partner", no age-of-the-Earth references, money as `$\$84{,}000$`, rounding
stated in every problem that needs it. Varied names from many cultures. Use
the course design in CLAUDE.md: coordinate plane as the spine, no two-column
proofs, the four ways to justify.

## Check each lesson, lean

1. Compute every answer with one python script (examples, You Trys, every
   `{{a}}`). Page and handout numbers must agree.
2. `bash _authoring/preview.sh <worktree> <scratch>/pv/<branch> X.Y` where
   `<scratch>` is `/tmp/claude-0/-home-claude/1a39dfb0-44c1-5a62-8c73-190714273cb1/scratchpad`.
   It builds figures and handouts and checks page math and image paths. Read
   only `X.Y_figs.png` and `X.Y_key.png` (the student copy is the key without
   the red). Fix collisions, bad layout, missing answers; re-run only if you
   changed something visible.
3. Do not run quarto; the teacher's build runs it once for the whole book.

## After the lessons: Summary, Review, Quiz

- `chapters/Unit_X/Summary.qmd` (`# Unit X Summary {.unnumbered}`, the
  `.guided-notes-link` to `/guided_notes/Unit_X/Unit_X_Summary.html`, a
  `## X.Y - Title` section per lesson with its rules, formulas, vocabulary and
  one small example, tables where clearer, nothing new, reusing lesson SVGs)
  and `guided_notes/src/X.Summary.html` (header: `lesson: Unit X`,
  `title: Summary`, `unit`, `unit_title`, `slug: Summary`,
  `file: Unit_X_Summary`, `page: Summary`, `label: Unit Summary`): a 2 to 3
  page reference sheet, no blanks, no `{{a}}`.
- `chapters/Unit_X/Review.qmd` (`# Unit X Review {.unnumbered}`, link to
  `/guided_notes/Unit_X/Unit_X_Review.html`, `{{< learn >}}` with one short
  worked example per lesson, `{{< practice >}}` with a group per lesson headed
  by its main "I can" goal, 4 to 6 problems each, then 6 to 8 test-worded
  multiple choice) and `guided_notes/src/X.Review.html` (as the Summary header
  with `title: Review`, `slug: Review`, `file: Unit_X_Review`, `page: Review`,
  `label: Unit Review`), complete key.
- `assessments/src/UnitX_Quiz.html` (header: `lesson: Unit X`, `title: Quiz`,
  `unit`, `unit_title`, `slug: Quiz`, `file: UnitX_Quiz`): a section per
  lesson, `<h2><span class="num">X.Y</span>I can ...</h2>`, two questions
  each, new numbers, room to work, every answer in `{{a}}`.
- Figures for these: `X.S_`, `X.R_`, `X.Q_` prefixes in `figures/Unit_X/`.
- Check: python for every key answer;
  `bash _authoring/preview.sh <worktree> <scratch>/pv/<branch> X.Summary X.Review UnitX_Quiz`,
  reading only the key PNGs (the Summary has no key, read its student PNG).

## Do not edit

`glossary.qmd`, `_quarto.yml`, `index.md`, `scripts/`, `styles/`,
`figures/preamble.tex`, `guided_notes/assets/`, `CLAUDE.md`, `_authoring/`
(except moving your unit intro out), other units. Before committing:
`git checkout -- guided-notes.qmd assessments/index.html`.

## Commit and report

One commit on your branch: `Unit X: lessons X.1 to X.N, Summary, Review, Quiz`,
a one-line body, then

```
Co-Authored-By: Claude <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_015VmZ8iCVJWi5TZn4oT8SPP
```

Report in under 15 lines: commit hash, files, handout page counts, anything
the teacher should decide.
