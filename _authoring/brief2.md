# Brief: unit check, Summary, Review and Quiz for the DHS Geometry book

The lessons of your unit are written and merged. Your job has two parts:

1. **Check the unit's lessons** with fresh eyes (you did not write them).
2. **Write the unit's Summary, Review and Quiz.**

Read `$TOOLS/brief.md` first: everything there about the school, the
students, writing style, figures, handouts, checks and commits applies to you
too. Then read `CLAUDE.md` in your worktree (sections "Unit Pages and
Assessments" and "Guided Notes" matter most here), `$TOOLS/specs.md` (shared
conventions and your unit), your unit's intro `chapters/Unit_X/index.qmd`, and
every lesson page and handout fragment in your unit.

`TOOLS=/tmp/claude-0/-home-claude/1a39dfb0-44c1-5a62-8c73-190714273cb1/scratchpad/tools`

## Part 1: check the lessons

For every lesson in your unit, page (`chapters/Unit_X/X.Y_*.qmd`) and handout
(`guided_notes/src/X.Y.html`):

- Recompute every answer with python: worked examples, You Try answers, and
  every `{{a}}` answer in the handout key. Fix wrong ones.
- The page and the handout must restate the same examples and practice with
  the same numbers. Fix drift.
- Notation and formulas match the shared conventions in specs.md and the
  lessons before them in this unit (the same symbol and the same words for the
  same idea). Fix cross-lesson inconsistencies in your unit.
- Writing rules: no dash asides (no em or en dashes; no spaced hyphen asides
  in prose), short sentences, no idioms, "Work with a partner".
- Run `$TOOLS/preview.sh <worktree> $TOOLS/../pv/<branch> X.1 X.2 ...` for
  every lesson and read every PNG. Fix label collisions, figures that are
  wrong or not to scale, broken layout, missing key answers.
- Fix what is clearly wrong. Do not rewrite what is fine; do not add or cut
  lessons or change what a lesson covers. List every fix in your report.

## Part 2: write Summary, Review and Quiz

### Summary (`chapters/Unit_X/Summary.qmd` + `guided_notes/src/X.Summary.html`)

- Page: `# Unit X Summary {.unnumbered}`, one or two sentences, a
  `.guided-notes-link` to `/guided_notes/Unit_X/Unit_X_Summary.html`, then a
  `## X.Y - Lesson title` section per lesson: the rules, formulas, vocabulary
  and one small worked example each, in tables where that is clearer. Every
  tool the unit teaches, in the lessons' own words and notation. Nothing new.
  Reuse the lessons' SVG figures (`/images/Unit_X/X.Y_name.svg`); make a new
  figure only if a table needs a tiny picture.
- Handout header:
  ```
  lesson: Unit X
  title: Summary
  unit: X
  unit_title: <from index.md>
  slug: Summary
  file: Unit_X_Summary
  page: Summary
  label: Unit Summary
  ```
  A reference sheet students keep beside them: 2 to 3 printed pages, compact
  tables, no blanks, no `{{a}}` (so it has no key).

### Review (`chapters/Unit_X/Review.qmd` + `guided_notes/src/X.Review.html`)

- Page: `# Unit X Review {.unnumbered}`, a line saying it practices every
  skill before the quiz, the `.guided-notes-link` to
  `/guided_notes/Unit_X/Unit_X_Review.html`, `{{< learn >}}` with one short
  worked example per lesson (new numbers), then `{{< practice >}}`.
- Practice: one group per lesson, headed by the lesson's main "I can" goal in
  bold. Each group has 4 to 6 problems: the same kinds of question the quiz
  asks for that goal (2 to 3 times as many), new numbers. Then **Test
  practice**: 6 to 8 multiple-choice items in long test wording covering the
  whole unit. No answers on the page.
- Handout header: as the Summary but `title: Review`, `slug: Review`,
  `file: Unit_X_Review`, `page: Review`, `label: Unit Review`. Full room to
  work and a complete key (`{{a}}` everywhere). Starts with the worked examples
  as `.ex` with blanks, then `{{practice-head}}` and the practice.

### Quiz (`assessments/src/UnitX_Quiz.html`, no page)

- Header:
  ```
  lesson: Unit X
  title: Quiz
  unit: X
  unit_title: <from index.md>
  slug: Quiz
  file: UnitX_Quiz
  ```
- A section per lesson, `<h2>` with the lesson number and its main "I can"
  goal (e.g. `<h2><span class="num">2.4</span>I can find the distance between two points</h2>`).
  Two questions per lesson, at the level of the lesson's practice, new numbers
  (not copied from the lesson or the review). At least one question in the quiz
  per justification type the unit uses (show with coordinates, counterexample,
  shows vs suggests, error analysis) where the unit has it.
- Room to work on every question (`.work` with `.h1` to `.h2`), and the answer
  to every part in `{{a}}...{{/a}}` in that space, so the key lines up with the
  student copy page for page. Directions are short.
- No name/date header needed in the body: the builder adds it.

### Figures for these

Name them `X.S_<what>.tex` (summary), `X.R_<what>.tex` (review), `X.Q_<what>.tex`
(quiz) in `figures/Unit_X/`, build with `scripts/make-figures.sh X.R_` and so
on. Answers drawn on them go in `\ifkey`. Use `{{fig X.R_name|alt|width}}`.

## Check

- `$TOOLS/preview.sh <worktree> $TOOLS/../pv/<branch> X.Summary X.Review UnitX_Quiz`
  (and every lesson you changed). Read every PNG. The math check runs on
  Summary.qmd and Review.qmd.
- Compute every answer in the Review key and the Quiz key with python.
- `quarto render chapters/Unit_X/Summary.qmd --to html` and the same for
  `Review.qmd`: no errors; delete the output written beside them.
- Every `{{< glink >}}` you use names a term in `glossary.qmd`.

## Do not edit

`_quarto.yml`, `index.md`, `chapters/Unit_X/index.qmd`, `glossary.qmd`,
`scripts/`, `styles/`, `figures/preamble.tex`, `guided_notes/assets/`,
`CLAUDE.md`, another unit's files. Before committing:
`git checkout -- guided-notes.qmd assessments/index.html`.

## Commit and report

One commit on your branch: `Unit X: lesson fixes, Summary, Review, Quiz`, a
short body listing the lesson fixes, and the two trailer lines from brief.md.
Report: commit hash; every lesson fix (file and what was wrong); page counts
of the Summary, Review and Quiz (student and key); anything the teacher
should decide.
