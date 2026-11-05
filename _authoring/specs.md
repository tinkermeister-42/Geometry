# DHS Geometry: lesson specs

Use the exact file name given. The title in the page heading is the file name
with spaces (and the commas a title needs). Sections listed are the minimum;
split or add a section if the material needs it. "Spine" items use the
coordinate plane on purpose (CLAUDE.md, Course Design).

## Shared conventions (every lesson)

- **Notation.** Segment $\overline{AB}$, length $AB$, ray $\overrightarrow{AB}$, line $\overleftrightarrow{AB}$,
  angle $\angle ABC$, measure $m\angle ABC = 40^\circ$, congruent $\cong$ (introduced in 1.2),
  similar $\sim$ (5.2), parallel $\parallel$, perpendicular $\perp$ (1.4), triangle $\triangle ABC$,
  arc $\overset{\frown}{AB}$ (7.1). Images after a transformation: $A'$ ("A prime"), then $A''$.
  Mapping rules: $(x, y) \rightarrow (x + 3, y - 2)$.
- **Formulas, as the book writes them.**
  Slope $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ (taught in Algebra 1, 4.2).
  Distance $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
  Midpoint $M = \left(\dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2}\right)$.
  Pythagorean theorem $a^2 + b^2 = c^2$, $c$ the hypotenuse.
  Polygon angle sum $(n - 2) \cdot 180^\circ$.
  Trig: $\sin A = \dfrac{\text{opposite}}{\text{hypotenuse}}$, $\cos A = \dfrac{\text{adjacent}}{\text{hypotenuse}}$, $\tan A = \dfrac{\text{opposite}}{\text{adjacent}}$, inverse $\sin^{-1}$.
  Circle $C = 2\pi r$, $A = \pi r^2$, $(x - h)^2 + (y - k)^2 = r^2$.
- **Rounding and pi.** Every problem that needs rounding says how ("Round to the nearest tenth").
  Circle answers: give the exact answer in terms of $\pi$ and a decimal from the $\pi$ key, unless
  the problem says otherwise. Trig: calculator in degree mode (say so in 6.2).
- **Units.** Mostly feet, inches, yards, miles; some meters and centimeters. Area in square units,
  volume in cubic units, always labeled.
- **Algebra in every lesson.** Where a figure gives a length or angle as an expression ($2x + 7$),
  students write and solve the equation. Keep negatives, fractions and multi-step work.
- **The four ways to justify** (no two-column proofs): computation with coordinates, counterexample,
  what a figure shows vs. suggests (only marks and given facts count), error analysis
  ("Amira says ... Find her mistake."). Every lesson uses at least one, in an example or practice.
- **Names** in word problems: varied, from many cultures (Amira, Diego, Mohammed, Esperanza, Thu,
  Kofi, Olena, Jamal, Hnin, Samir, Lucía, Daniel, Fatima, Moses, Ana, Ahmad).

## Unit 1: Lines, Angles, and Equations (1.1 is written)

### 1.2 Segment and Angle Addition, `1.2_Segment_and_Angle_Addition`
- 1.2.1 Length on a number line and with a ruler: $AB = |a - b|$; length is never negative.
- 1.2.2 Segment addition: if $B$ is between $A$ and $C$ (collinear), $AB + BC = AC$. Solve for $x$
  ($AB = 2x + 3$, $BC = x - 1$, $AC = 17$; find $x$ and every length). Real: three towns on a straight
  highway, mile markers.
- 1.2.3 Congruent segments and midpoints: introduce $\cong$ (same size and shape) vs $=$ (numbers):
  $\overline{AB} \cong \overline{CD}$ means $AB = CD$. Midpoint splits a segment into two congruent
  parts; segment bisector. Equations from $AM = MB$. (The midpoint *formula* is 2.5; here only the idea.)
- 1.2.4 Angle addition and angle bisectors: if $D$ is in the interior of $\angle ABC$,
  $m\angle ABD + m\angle DBC = m\angle ABC$. Bisector makes two congruent angles. Solve for $x$.
  Reading a protractor (inner and outer scales) from a drawn protractor figure.
- Shows vs suggests: a point that looks like a midpoint without tick marks.

### 1.3 Complementary, Supplementary, and Vertical Angles, `1.3_Complementary_Supplementary_and_Vertical_Angles`
- 1.3.1 Complementary (sum $90^\circ$) and supplementary (sum $180^\circ$); they do not have to touch.
  Find the complement and supplement of an angle; of $x^\circ$ ($90 - x$, $180 - x$).
- 1.3.2 Adjacent angles, linear pairs (always supplementary).
- 1.3.3 Vertical angles are equal. Show WHY with numbers then with $x$: each vertical angle makes a
  linear pair with the same angle, so both equal $180 - x$. No two-column proof.
- 1.3.4 Solving for $x$: two angles complementary ($3x + 5$ and $2x$); vertical angles set equal
  ($4x - 10 = 2x + 30$); a linear pair; a system of two angles (crossing lines with three expressions).
  Real: scissors, an X-shaped sawhorse, crossing roads on a map, a ramp meeting the ground.
- Error analysis: a student adds vertical angles to 180.

### 1.4 Parallel Lines and Transversals, `1.4_Parallel_Lines_and_Transversals`
- 1.4.1 Parallel ($\parallel$, never meet, same plane), perpendicular ($\perp$, right angles), skew
  (in space, a box figure). Arrow marks for parallel lines.
- 1.4.2 A transversal makes 8 angles: corresponding, alternate interior, alternate exterior,
  same-side (consecutive) interior. Name pairs in a numbered figure.
- 1.4.3 When the lines are parallel: corresponding, alternate interior and alternate exterior are
  equal; same-side interior are supplementary. Given one angle, find all eight. Solve for $x$.
- 1.4.4 Are the lines parallel? Use angle measures to decide (converse). Shows vs suggests: two lines
  that LOOK parallel with angles $88^\circ$ and $92^\circ$ marked. Counterexample: equal-looking
  corresponding angles without the parallel marks.
- Real: parking lot stripes, railroad tracks, a street grid crossed by a diagonal avenue, stair rails.

### 1.5 Angles in Triangles and Polygons, `1.5_Angles_in_Triangles_and_Polygons`
- 1.5.1 Triangle angle sum $180^\circ$. Show why: tear off the corners (figure), and with a line
  through one vertex parallel to the opposite side (alternate interior angles from 1.4).
- 1.5.2 Classify triangles by sides (scalene, isosceles, equilateral) and angles (acute, right,
  obtuse, equiangular). Solve for $x$ with angles $(2x)^\circ$, $(3x + 10)^\circ$, $(x - 4)^\circ$.
- 1.5.3 Exterior angle = sum of the two remote interior angles. Solve for $x$.
- 1.5.4 Polygons: name by sides (to 10 and n-gon), convex/concave, regular. Interior sum
  $(n - 2) \cdot 180^\circ$ (divide into triangles from one vertex). One angle of a regular polygon.
  Exterior angles of any convex polygon add to $360^\circ$ (walking around the shape).
  Find $n$ from an angle measure.
- Real: stop sign (octagon), honeycomb hexagons, floor tiles, a soccer ball, a gazebo.

## Unit 2: The Pythagorean Theorem and the Coordinate Plane

### 2.1 Square Roots and Simplifying Radicals, `2.1_Square_Roots_and_Simplifying_Radicals`
- 2.1.1 Perfect squares to $15^2$; square root as the side of a square with that area (figure).
  $\sqrt{49} = 7$; principal (positive) root in geometry.
- 2.1.2 Estimate between whole numbers ($\sqrt{50}$ is between 7 and 8, closer to 7); calculator
  decimals rounded to the nearest tenth.
- 2.1.3 Simplify with perfect-square factors: $\sqrt{72} = \sqrt{36}\sqrt{2} = 6\sqrt{2}$. Use prime
  factorization pairs (Algebra 1, 1.2) as a second method.
- 2.1.4 Multiply ($\sqrt{3}\cdot\sqrt{12} = 6$, $2\sqrt{3}\cdot 5\sqrt{6}$), add like radicals
  ($3\sqrt{2} + 5\sqrt{2}$, $\sqrt{8} + \sqrt{18}$), rationalize a simple denominator
  ($\frac{6}{\sqrt{2}} = 3\sqrt{2}$), needed in 6.1.
- Real: side of a square garden with area 50 square feet; a square rug.
- Error analysis: $\sqrt{9 + 16} \neq 3 + 4$.

### 2.2 The Pythagorean Theorem and Its Converse, `2.2_The_Pythagorean_Theorem_and_Its_Converse`
- 2.2.1 Parts of a right triangle: legs, hypotenuse (opposite the right angle, longest side).
- 2.2.2 The theorem with squares on the sides (figure with grid squares counted for 3-4-5); show why
  with the rearrangement picture (four copies of the triangle in a big square, two ways to fill it).
- 2.2.3 Find the hypotenuse; find a leg; leave exact as a simplified radical (2.1) and as a decimal.
  Solve when sides are expressions (legs $x$ and $x + 7$, hypotenuse 13).
- 2.2.4 Pythagorean triples (3-4-5, 5-12-13, 8-15-17, 7-24-25) and their multiples.
- 2.2.5 Converse: is it a right triangle? Compare $c^2$ with $a^2 + b^2$: equal right, less acute,
  greater obtuse. Can these three lengths make a triangle at all (triangle inequality: the two short
  sides must add to more than the long one).
- Shows vs suggests: a triangle that looks right but $5, 6, 8$ is obtuse.

### 2.3 The Pythagorean Theorem in the Real World, `2.3_The_Pythagorean_Theorem_in_the_Real_World`
- Always: draw and label the right triangle first, then solve, then answer in a sentence with units.
- 2.3.1 Squaring a corner: builders mark 3 ft and 4 ft and check for 5 ft (6-8-10, 9-12-15 for large
  slabs); check a rectangle by its diagonal. Is a 10 ft by 24 ft deck square if the diagonal is 26 ft 2 in?
- 2.3.2 Ladders: a 20 ft ladder with its base 5 ft from the wall; the 4-to-1 safety rule (base 1 ft out
  for every 4 ft up).
- 2.3.3 Screens: a 55-inch TV is measured on the diagonal; find width/height given one; phone screens.
- 2.3.4 Shortcuts and distances: walking across a rectangular park vs around it; a ball field
  (90 ft bases, home to second base); a ramp's length from rise and run; a wire from a pole top.
- 2.3.5 Two steps: the longest pole that fits in a box (diagonal of the floor, then the box diagonal).
- Test-worded items: two long EOC-style word problems in the practice.

### 2.4 Distance on the Coordinate Plane, `2.4_Distance_on_the_Coordinate_Plane`
- 2.4.1 Horizontal and vertical distance: same $y$ means subtract the $x$'s (absolute value). Count on a grid.
- 2.4.2 Slanted distance: draw the right triangle (legs are the horizontal and vertical changes), use
  the Pythagorean theorem. Several worked on a grid.
- 2.4.3 The distance formula as the same steps in symbols. Exact (simplified radical) and decimal.
- 2.4.4 Use it: which point is closer; is a triangle isosceles (two equal sides); find a missing
  coordinate given a distance ($(1, k)$ is 5 from $(4, 2)$, two answers).
- Real: a town map on a grid (each unit 1 mile), drone flight straight line vs streets (taxicab) as a
  "which is shorter" comparison.

### 2.5 Midpoint, `2.5_Midpoint`
- 2.5.1 Midpoint on a number line: the average of the two numbers (halfway between $-3$ and $9$).
- 2.5.2 The midpoint formula: average the $x$'s, average the $y$'s. Figure on a grid showing the
  half-way point of the horizontal and vertical changes.
- 2.5.3 Find an endpoint from a midpoint and the other endpoint (two ways: "same step again", and
  solve $\frac{x_1 + x}{2} = 3$).
- 2.5.4 Use it: meet halfway between two homes on a map grid; the center of a circle from the ends of a
  diameter; check that a point is the midpoint (distance both ways equal AND collinear).
- Error analysis: subtracting instead of adding in the formula.

### 2.6 Slope, Parallel Lines, and Perpendicular Lines, `2.6_Slope_Parallel_Lines_and_Perpendicular_Lines`
- 2.6.1 Review slope from two points and from $y = mx + b$ (Algebra 1, 4.2 and 4.3). Horizontal 0,
  vertical undefined.
- 2.6.2 Parallel lines have the same slope (and are not the same line). Show why with matching
  rise-over-run staircases.
- 2.6.3 Perpendicular lines: slopes are opposite reciprocals, product $-1$. Show why by rotating a
  rise-run right triangle $90^\circ$ on a grid. Horizontal and vertical lines are perpendicular.
- 2.6.4 Decide parallel, perpendicular, or neither from equations (rewrite $2x + 3y = 6$ first) or
  from two pairs of points.
- 2.6.5 Write the equation of the line through a point parallel or perpendicular to a given line
  (slope-intercept; point-slope as an option). Real: a new road parallel/perpendicular to Main St on
  a city grid.

### 2.7 Dividing a Segment in a Ratio, `2.7_Dividing_a_Segment_in_a_Ratio`
- 2.7.1 On a number line: the point $\frac{1}{3}$ of the way from 2 to 14. Ratio $a:b$ means the
  point is $\frac{a}{a+b}$ of the way.
- 2.7.2 On the plane: find the run and rise from $A$ to $B$, take that fraction of each, add to $A$
  (figure: the big staircase cut into equal small steps). Formula
  $P = \left(x_1 + k(x_2 - x_1),\ y_1 + k(y_2 - y_1)\right)$ with $k = \frac{a}{a+b}$.
- 2.7.3 Order matters: "from $A$ to $B$" vs "from $B$ to $A$" (same segment, different point).
- 2.7.4 Real: a rest stop $\frac{2}{5}$ of the way along a straight trail on a map; a bridge support
  dividing a span 3:1; check with distance that the parts are in the ratio.

### 2.8 Perimeter and Area on the Coordinate Plane, `2.8_Perimeter_and_Area_on_the_Coordinate_Plane`
- 2.8.1 Perimeter of a polygon from its vertices (distance formula for each side), exact and rounded.
- 2.8.2 Area with horizontal/vertical sides: rectangles, right triangles, trapezoids by counting and
  subtracting coordinates.
- 2.8.3 Area of a slanted triangle or quadrilateral by the box method (enclose in a rectangle,
  subtract the corner right triangles).
- 2.8.4 Area of a slanted rectangle or square from side lengths (distance formula), check against
  the box method.
- Real: a fenced garden on a property map (fence = perimeter, mulch = area), a parking lot plan.

### 2.9 Checking Shapes with Coordinates, `2.9_Checking_Shapes_with_Coordinates`
- The lesson that introduces "computation as proof". Every example ends with a written sentence:
  "Because ..., $ABCD$ is a ...".
- 2.9.1 Right triangle? Two ways: perpendicular slopes, or the Pythagorean converse with distances.
- 2.9.2 Isosceles or equilateral triangle? Compare distances.
- 2.9.3 Quadrilaterals: parallelogram (both pairs of opposite sides parallel, by slope), rectangle
  (parallelogram + a right angle), rhombus (four equal sides), square (both). Short decision table.
  (Full properties come in 4.4; here only the definitions needed to check.)
- 2.9.4 Looks vs is: a shape that looks like a square on the grid but is a rhombus (equal sides, slopes
  not perpendicular); one that looks like a rectangle but has slightly different slopes. Counterexample:
  "four equal sides makes a square" is false.
- Error analysis: a student claims "it's a rectangle because opposite sides are equal" and stops; what
  is missing.
- Find the fourth vertex of a parallelogram given three.

## Unit 3: Transformations

### 3.1 Translations, `3.1_Translations`
- 3.1.1 Transformation, preimage, image ($A \rightarrow A'$). A translation slides every point the
  same distance in the same direction.
- 3.1.2 Rules: $(x, y) \rightarrow (x + a, y + b)$; describe in words ("4 left and 3 up"); find the
  rule from a point and its image.
- 3.1.3 Graph the image of a triangle and a quadrilateral (grid figures; key shows the image in red).
- 3.1.4 What stays the same: check with the distance formula that side lengths match, and with slope
  that sides stay parallel to their images (spine). A translation is a rigid motion.
- Real: moving a desk on a floor plan, a video game character, a chess knight move as a translation.

### 3.2 Reflections, `3.2_Reflections`
- 3.2.1 Reflect over the $x$-axis $(x, -y)$ and $y$-axis $(-x, y)$; find the rules from examples.
- 3.2.2 Over $y = x$: $(y, x)$; over $y = -x$: $(-y, -x)$; over $x = a$ and $y = b$ by counting.
- 3.2.3 The line of reflection is the perpendicular bisector of $\overline{AA'}$: check with midpoint
  (on the line) and slope (perpendicular). Find the line of reflection from a point and its image.
- 3.2.4 Orientation reverses (letters read backward; clockwise order of labels flips).
- Real: mirror writing (AMBULANCE), a lake reflection; Challenge: shortest path to a river and back
  (reflect one point).

### 3.3 Rotations, `3.3_Rotations`
- 3.3.1 Rotation: center, angle, direction. Counterclockwise is positive; clockwise $-90^\circ$ =
  $270^\circ$ counterclockwise.
- 3.3.2 About the origin: $90^\circ$ $(x, y) \rightarrow (-y, x)$, $180^\circ$ $(-x, -y)$,
  $270^\circ$ $(y, -x)$. Discover with a tracing-paper style figure; check with slope (radius to $A$
  and to $A'$ are perpendicular for $90^\circ$) and distance (same distance from the center).
- 3.3.3 Graph the image of a figure (key in red).
- 3.3.4 Find the rotation that maps one figure to another.
- Real: clock hands (from 1.1), a Ferris wheel seat, a wheel, a fan.

### 3.4 Dilations, `3.4_Dilations`
- 3.4.1 A dilation with center and scale factor $k$: enlargement ($k > 1$), reduction ($0 < k < 1$).
  Center at the origin: $(x, y) \rightarrow (kx, ky)$.
- 3.4.2 Lengths multiply by $k$ (check with the distance formula); angles stay the same; a side and its
  image are parallel (same slope). Not a rigid motion.
- 3.4.3 Find the scale factor from a figure and its image ($k = \frac{\text{image length}}{\text{original length}}$).
- 3.4.4 Center not at the origin: subtract the center, multiply, add the center back (one worked example
  and one practice; figure with rays from the center).
- Real: enlarging a photo, a projector, a map scale, a model car.

### 3.5 Sequences of Transformations and Symmetry, `3.5_Sequences_of_Transformations_and_Symmetry`
- 3.5.1 Do one transformation, then another ($A \rightarrow A' \rightarrow A''$). Combined rule.
- 3.5.2 Order matters: a counterexample (reflect then translate vs translate then reflect).
- 3.5.3 Describe a sequence that maps one figure onto another (more than one right answer).
- 3.5.4 Rigid motions (translation, reflection, rotation) keep length and angle; a dilation keeps only
  angle. Sort transformations.
- 3.5.5 Line symmetry and rotational symmetry (order $n$, smallest angle $\frac{360^\circ}{n}$) of
  letters, flags, logos, a hubcap, a snowflake, regular polygons (link to 1.5).

## Unit 4: Congruence

### 4.1 Congruent Figures and Rigid Motions, `4.1_Congruent_Figures_and_Rigid_Motions`
- 4.1.1 Congruent figures: one can be moved onto the other by rigid motions (Unit 3). Same size and shape.
- 4.1.2 Corresponding parts; congruence statements $\triangle ABC \cong \triangle DEF$: order tells
  which vertices match. Write the matching parts; fix a wrong statement (error analysis).
- 4.1.3 Corresponding parts of congruent figures are congruent: use it to find missing sides and angles,
  with algebra ($AB = 3x - 2$, $DE = x + 10$).
- 4.1.4 Decide on a grid: find the rigid motion, or show side lengths differ (distance formula).
- Real: mass-produced parts, floor tiles, the two halves of a folding table.

### 4.2 Triangle Congruence, `4.2_Triangle_Congruence` (heading: "4.2 - Triangle Congruence: SSS, SAS, ASA, AAS, and HL")
- 4.2.1 Why triangles: a triangle frame is rigid, a square frame wobbles (figure); three sides fix a
  triangle. SSS.
- 4.2.2 SAS (angle between the sides), ASA (side between the angles), AAS, HL (right triangles only).
- 4.2.3 What is NOT enough: SSA (two different triangles, figure) and AAA (same shape, different size).
  Counterexamples, drawn to scale.
- 4.2.4 Which shortcut? Use only the marks and given facts (shows vs suggests); a shared side counts
  for both triangles; vertical angles from 1.3; parallel lines give alternate interior angles (1.4).
  Write the congruence statement in the right order. "Not enough information" is an answer.
- 4.2.5 Solve for $x$ in congruent triangles.
- Real: roof trusses, bridge trusses, bike frames, shelf brackets.

### 4.3 Isosceles and Equilateral Triangles, `4.3_Isosceles_and_Equilateral_Triangles`
- 4.3.1 Parts: legs, base, vertex angle, base angles.
- 4.3.2 Base angles are equal; the converse. Show why by folding (reflection over the line through the
  vertex and the midpoint of the base, from Unit 3).
- 4.3.3 Equilateral means equiangular, each $60^\circ$.
- 4.3.4 Solve for $x$ and angles (vertex $40^\circ$; base angles $(3x + 5)^\circ$; sides $2x + 1$ and $x + 8$).
  Multi-step figures with two isosceles triangles sharing a side.
- 4.3.5 Spine: the line from the vertex to the midpoint of the base is perpendicular to the base (check
  with slopes on a grid).
- Real: A-frame, roof gable, yield sign, a tent.

### 4.4 Quadrilaterals and Their Properties, `4.4_Quadrilaterals_and_Their_Properties`
- 4.4.1 The family: quadrilateral, trapezoid, isosceles trapezoid, kite, parallelogram, rectangle,
  rhombus, square. A family-tree diagram. Angle sum $360^\circ$ (from 1.5).
- 4.4.2 Parallelograms: opposite sides equal, opposite angles equal, consecutive angles supplementary,
  diagonals bisect each other (check: the diagonals have the same midpoint, spine). Solve for $x$.
- 4.4.3 Rectangles (diagonals equal), rhombuses (diagonals perpendicular, bisect the angles), squares
  (all). Solve for $x$.
- 4.4.4 Trapezoids (isosceles: base angles equal, diagonals equal; midsegment = average of the bases)
  and kites (one pair of equal opposite angles, perpendicular diagonals).
- 4.4.5 Always, sometimes, never ("a rectangle is a rhombus"); counterexamples.
- Real: builders check a frame is rectangular by measuring both diagonals; a parallelogram lift / scissor
  lift; a kite.

### 4.5 Constructions, `4.5_Constructions`
- Compass and straightedge only. Each construction: numbered steps with small step figures, then a
  "why it works" sentence using congruent triangles (SSS from 4.2) or equal radii.
- 4.5.1 Copy a segment; copy an angle.
- 4.5.2 Perpendicular bisector of a segment (midpoint construction).
- 4.5.3 Bisect an angle.
- 4.5.4 Perpendicular from a point to a line; a line parallel to a given line through a point (copy a
  corresponding angle).
- 4.5.5 Equilateral triangle; regular hexagon inscribed in a circle (radius steps around 6 times).
- Handout: give real blank space for each construction (2 to 2.5 in); the key shows the finished
  construction in red (key twin figures). Practice is mostly "construct ..." on given starting figures.
- Spine/check: after constructing a perpendicular bisector on a grid, check with slope and midpoint.

## Unit 5: Similarity

### 5.1 Ratios and Proportions, `5.1_Ratios_and_Proportions`
- 5.1.1 Ratio as $a:b$, $\frac{a}{b}$, "a to b"; simplify; ratios with units converted first
  (2 ft to 8 in).
- 5.1.2 Proportion; cross products, with the reason (multiply both sides by both denominators).
  Solve $\frac{x}{12} = \frac{5}{8}$, $\frac{3}{x + 2} = \frac{4}{x}$, $\frac{x - 1}{4} = \frac{9}{x - 1}$
  (two answers).
- 5.1.3 Scale drawings and maps: scale $1 \text{ in} : 20 \text{ ft}$; find real length or drawing length.
- 5.1.4 Ratios in a figure: angles in the ratio $2:3:4$ in a triangle; a segment divided $3:5$ with
  total length.
- Real: recipe scaling, a floor plan, a map, mixing concrete 1:2:3.

### 5.2 Similar Figures and Scale Factor, `5.2_Similar_Figures_and_Scale_Factor`
- 5.2.1 Similar ($\sim$): same shape, maybe different size. A dilation plus rigid motions (Unit 3).
  Corresponding angles equal, corresponding sides proportional.
- 5.2.2 Similarity statements and matching parts; scale factor (say which direction).
- 5.2.3 Decide whether two polygons are similar (check every ratio and angle); counterexample: two
  rectangles with equal angles that are not similar.
- 5.2.4 Find missing sides with a proportion; solve for $x$.
- 5.2.5 Perimeters scale by $k$; areas by $k^2$ (count grid squares in a figure doubled). (Volume $k^3$
  waits for 8.6.)
- Real: photo sizes (4 by 6 to 8 by 12 vs 8 by 10), a model car $1:24$, a phone screen and a TV.

### 5.3 Similar Triangles, `5.3_Similar_Triangles`
- 5.3.1 AA similarity (third angle comes free, from 1.5).
- 5.3.2 SSS similarity and SAS similarity (ratios equal; included angle).
- 5.3.3 Which test, or not similar; write the statement in order.
- 5.3.4 Overlapping (nested) triangles: draw them separately, then set up the proportion. Solve for $x$
  with expressions ($x + 4$ over $x$).
- 5.3.5 Spine: on a grid, check similarity with distances (ratios) or slopes (parallel sides give
  equal angles).
- Real: a ramp and its supports, a camera's image (pinhole camera figure).

### 5.4 Triangle Proportionality, `5.4_Triangle_Proportionality`
- 5.4.1 A line parallel to one side divides the other two sides proportionally (from similar nested
  triangles, 5.3). Solve for $x$.
- 5.4.2 Converse: proportional pieces mean the line is parallel; decide.
- 5.4.3 Midsegment: joins two midpoints, parallel to the third side, half as long. Spine: check with
  midpoint and slope formulas on a grid.
- 5.4.4 Three or more parallel lines cut two transversals proportionally (property lines on a street
  map figure).
- Real: lots on a street between parallel cross streets, ladder rungs, shelf supports.

### 5.5 Indirect Measurement, `5.5_Indirect_Measurement`
- Measure what you cannot reach with similar triangles. Every problem: sketch, label, proportion, answer
  with units.
- 5.5.1 Shadows: a person and a tree at the same time of day make similar triangles.
- 5.5.2 Mirrors: the angles at the mirror are equal; person and building make similar triangles.
- 5.5.3 Across a river or a pond: the nested-triangle method with stakes.
- 5.5.4 Mixed real problems in test wording (EOC style, long), including one where the student must
  decide which lengths match.
- Class activity idea in a .note: measure the flagpole's height with shadows or a mirror.

## Unit 6: Right Triangle Trigonometry

### 6.1 Special Right Triangles, `6.1_Special_Right_Triangles`
- 6.1.1 $45^\circ$-$45^\circ$-$90^\circ$: half a square; use the Pythagorean theorem to show the
  hypotenuse is $\text{leg}\cdot\sqrt{2}$. From a leg; from the hypotenuse (rationalize, 2.1).
- 6.1.2 $30^\circ$-$60^\circ$-$90^\circ$: half an equilateral triangle (4.3); short leg $x$, hypotenuse
  $2x$, long leg $x\sqrt{3}$. From any one side, find the other two.
- 6.1.3 Find exact answers; then decimals. Which side is opposite which angle.
- 6.1.4 Real: diagonal of a square tile or a baseball diamond, a $30^\circ$ ramp, an equilateral
  truss height, a hexagon nut.
- Error analysis: putting $\sqrt{3}$ on the hypotenuse.

### 6.2 The Trigonometric Ratios, `6.2_The_Trigonometric_Ratios`
- 6.2.1 Name the sides from an angle: opposite, adjacent, hypotenuse (they change with the angle).
- 6.2.2 Why ratios work: right triangles with the same acute angle are similar (AA, 5.3), so their
  side ratios are equal. A figure with three nested right triangles and a measured table.
- 6.2.3 Sine, cosine, tangent (SOH CAH TOA). Write the ratios from side lengths, as fractions and
  decimals.
- 6.2.4 Calculator: degree mode; $\sin 35^\circ$ to four decimals; check $\tan 45^\circ = 1$.
- 6.2.5 Spine: tangent is slope. A line through the origin making angle $\theta$ with the $x$-axis has
  slope $\tan\theta$ (figure on a grid); a road grade of 8% is a slope of 0.08.
- Use only sin, cos, tan (no reciprocal ratios).

### 6.3 Solving for a Side, `6.3_Solving_for_a_Side`
- 6.3.1 Choose the ratio: which side do I know, which do I want, relative to the given angle.
- 6.3.2 Unknown on top: $x = 12\sin 40^\circ$.
- 6.3.3 Unknown on the bottom: $\cos 25^\circ = \frac{8}{x}$, so $x = \frac{8}{\cos 25^\circ}$
  (two-step, the common error).
- 6.3.4 Find all missing sides of a triangle (trig, then the Pythagorean theorem to check).
- Real: how high a 24 ft ladder reaches at $75^\circ$; a kite string; a slide; a guy wire.
- Round to the nearest tenth; state the rounding in every problem.

### 6.4 Solving for an Angle, `6.4_Solving_for_an_Angle`
- 6.4.1 Inverse ratios: $\sin^{-1}$, $\cos^{-1}$, $\tan^{-1}$ "undo" (calculator keys). The
  $^{-1}$ is not an exponent.
- 6.4.2 Find an angle from two sides; choose the ratio.
- 6.4.3 Solve a right triangle completely (all sides and angles) with the Pythagorean theorem, trig and
  the angle sum; check by a second method.
- 6.4.4 Real: roof pitch ($6/12$ pitch means rise 6 per run 12, angle $\tan^{-1}(0.5) \approx 26.6^\circ$),
  the 1:12 wheelchair ramp angle, a road grade to degrees, the sun's angle from a shadow, stairs (rise 7 in,
  run 11 in).

### 6.5 Sine and Cosine of Complementary Angles, `6.5_Sine_and_Cosine_of_Complementary_Angles`
- 6.5.1 In a right triangle the acute angles are complementary (1.3, 1.5).
- 6.5.2 The opposite side for one angle is the adjacent side for the other, so
  $\sin A = \cos(90^\circ - A)$. Check with a table of calculator values.
- 6.5.3 Use it: if $\sin 28^\circ \approx 0.469$, find $\cos 62^\circ$; write $\cos 15^\circ$ as a sine.
- 6.5.4 Solve: $\sin(2x + 10)^\circ = \cos(3x)^\circ$ gives $2x + 10 + 3x = 90$; $\sin(x + 20)^\circ = \cos(2x - 5)^\circ$.
- 6.5.5 Also: $\tan A = \frac{\sin A}{\cos A}$ (from the side ratios) and $\tan A \cdot \tan(90^\circ - A) = 1$.
- Test-worded items (this topic is often a multiple-choice question).

### 6.6 Angles of Elevation and Depression, `6.6_Angles_of_Elevation_and_Depression`
- 6.6.1 Measured from the horizontal: elevation looking up, depression looking down. Error to avoid:
  measuring from the vertical.
- 6.6.2 The angle of elevation from A to B equals the angle of depression from B to A (alternate
  interior angles, 1.4). Figure with the two horizontals.
- 6.6.3 Height problems; distance problems; add the observer's eye height.
- 6.6.4 Two-angle problems (moving closer, two observers) as Challenge.
- Real: a lighthouse and a boat, an airplane landing, a drone, a cell tower, a clinometer activity
  (.note: make a clinometer from a protractor and string).

### 6.7 Modeling with Right Triangles, `6.7_Modeling_with_Right_Triangles`
- Multi-step real problems; choose the tool: Pythagorean theorem, special triangles, or trig. Each
  worked example shows: sketch, label, choose, solve, check, sentence answer.
- 6.7.1 Ramps: the 1:12 rule; how long a ramp for a 30 in rise; its angle; does a 15 ft ramp rising 18 in
  meet the rule.
- 6.7.2 Roofs: rafter length from pitch and span, with overhang.
- 6.7.3 Distances you cannot measure: across a river, a tree's height from a measured angle.
- 6.7.4 Navigation and maps: walking 3 miles north then 4 east, bearing angle; a plane's climb.
- 6.7.5 Solar panels tilted to an angle; a wheelchair-accessible doorway; a guy wire with a required
  angle.
- Practice: mostly multi-step word problems, several in long test wording.

## Unit 7: Circles

### 7.1 Circumference and Arc Length, `7.1_Circumference_and_Arc_Length`
- 7.1.1 Parts: center, radius, diameter, chord, arc (minor, major, semicircle), central angle. Name a
  circle by its center ($\odot P$ or "circle $P$").
- 7.1.2 $\pi$ as circumference divided by diameter (table of measured round objects).
  $C = \pi d = 2\pi r$; find $r$ from $C$.
- 7.1.3 Arc measure (degrees, equals the central angle) vs arc length (a distance). Arc length
  $= \frac{\text{central angle}}{360^\circ} \cdot 2\pi r$.
- 7.1.4 Solve for $x$ with arcs adding up ($360^\circ$ around), find the radius from an arc length.
- Real: a bike wheel (distance per turn, turns per mile), a running track's curved ends, a pizza crust
  edge, a clock's minute hand tip.

### 7.2 Area of Circles and Sectors, `7.2_Area_of_Circles_and_Sectors`
- 7.2.1 $A = \pi r^2$. Show why: cut the circle into thin wedges and rearrange into a near-parallelogram
  ($\frac{1}{2}C$ by $r$), figure.
- 7.2.2 Sector area $= \frac{\text{central angle}}{360^\circ} \cdot \pi r^2$. Find the angle or radius from
  a sector area.
- 7.2.3 Composite and shaded regions: a ring (annulus), a square with a circle cut out, a semicircle on
  a rectangle (window).
- 7.2.4 Real: a pizza slice per dollar (which is the better deal), a sprinkler's watered region, a round
  tabletop's paint, a cow on a rope at a barn corner (Challenge, three-quarter circle).

### 7.3 Radians, `7.3_Radians`
- 7.3.1 A radian: the central angle whose arc is one radius long (figure: radius laid along the arc).
  A full turn is $2\pi$ radians, about 6.28.
- 7.3.2 Convert: $180^\circ = \pi$ radians. Degrees to radians and back; common angles
  ($30^\circ, 45^\circ, 60^\circ, 90^\circ, 180^\circ, 360^\circ$) as exact multiples of $\pi$.
- 7.3.3 Arc length $s = r\theta$ and sector area $A = \frac{1}{2}r^2\theta$ ($\theta$ in radians);
  compare with the degree formulas from 7.1 and 7.2.
- 7.3.4 Real: how far a point on a wheel travels in 3 radians, a windshield wiper's swept area.
- Error analysis: using degrees in $s = r\theta$.

### 7.4 Inscribed Angles and Tangents, `7.4_Inscribed_Angles_and_Tangents`
- 7.4.1 Inscribed angle (vertex on the circle) is half its intercepted arc. Two inscribed angles on the
  same arc are equal.
- 7.4.2 An angle inscribed in a semicircle is a right angle. Spine: check on a grid with slopes
  (circle centered at the origin, radius 5, points like $(3, 4)$).
- 7.4.3 A quadrilateral inscribed in a circle has opposite angles supplementary. Solve for $x$.
- 7.4.4 Tangent lines: a tangent is perpendicular to the radius at the point of tangency (check with
  slopes on a grid); two tangents from one outside point are equal. Solve with the Pythagorean theorem
  and with algebra.
- Real: a camera at the edge of a circular stage (all seats on one arc see the stage at the same angle),
  a belt around two pulleys, a road tangent to a circular track.

### 7.5 The Equation of a Circle, `7.5_The_Equation_of_a_Circle`
- 7.5.1 Every point on a circle is the same distance $r$ from the center: write the distance formula and
  square it to get $(x - h)^2 + (y - k)^2 = r^2$ (spine, from 2.4).
- 7.5.2 Read the center and radius (signs!); graph.
- 7.5.3 Write the equation from center and radius; from center and a point on the circle; from the ends
  of a diameter (midpoint 2.5 + distance 2.4).
- 7.5.4 Expanded form to standard form by completing the square (Algebra 1, 6.5):
  $x^2 + y^2 - 6x + 4y - 12 = 0$.
- 7.5.5 Is a point on, inside, or outside the circle? Real: a cell tower's coverage on a town grid
  (does it reach the school at $(7, 3)$), a sprinkler on a yard plan, an earthquake epicenter radius.

## Unit 8: Area, Surface Area, and Volume

### 8.1 Area of Polygons and Composite Figures, `8.1_Area_of_Polygons_and_Composite_Figures`
- 8.1.1 Rectangles, parallelograms ($bh$, height perpendicular to the base, cut-and-move figure),
  triangles ($\frac{1}{2}bh$), trapezoids ($\frac{1}{2}(b_1 + b_2)h$).
- 8.1.2 Regular polygons: apothem, $A = \frac{1}{2}aP$ (cut into triangles); a hexagon with side 6
  (apothem from 30-60-90, 6.1).
- 8.1.3 Composite figures: add and subtract; L-shaped rooms; with a semicircle (7.2).
- 8.1.4 Solve for a missing dimension from the area (algebra: trapezoid with $b_1 = x$, $b_2 = x + 4$).
- Real: flooring for a room in square feet and cost, painting a wall minus a window and door, sod for an
  irregular yard, a stop-sign sheet of metal.

### 8.2 Cross Sections and Solids of Revolution, `8.2_Cross_Sections_and_Solids_of_Revolution`
- 8.2.1 Solids: prism, pyramid, cylinder, cone, sphere; faces, edges, vertices; Euler's pattern
  $F + V - E = 2$ checked in a table.
- 8.2.2 Cross sections: slice a cube (square, rectangle, triangle, even a hexagon), a cylinder (circle,
  rectangle), a cone (circle, triangle), a pyramid, a sphere (circles). Figures with the cutting plane.
- 8.2.3 Solids of revolution: spin a rectangle (cylinder), a right triangle (cone), a semicircle
  (sphere); which shape makes this solid.
- 8.2.4 Real: slicing bread, cheese, an orange; a pottery wheel; a lathe.
- Figures here are 3D (TikZ with oblique or isometric projection, dashed hidden edges). Keep them
  clean and consistent.

### 8.3 Surface Area and Nets, `8.3_Surface_Area_and_Nets`
- 8.3.1 Nets of a cube, rectangular prism, triangular prism, pyramid, cylinder (figures; match nets to
  solids, and one that does NOT fold into a cube).
- 8.3.2 Surface area of prisms: add the faces; lateral area.
- 8.3.3 Cylinders: $2\pi r^2 + 2\pi rh$ (the label unrolls into a rectangle).
- 8.3.4 Pyramids and cones: slant height (Pythagorean theorem, 2.2), $\pi r^2 + \pi r \ell$.
  Spheres: $4\pi r^2$ (state it; a short why with the orange-peel idea in a .note).
- Real: wrapping paper for a box, paint for a water tank, a soup-can label, a tent's fabric.

### 8.4 Volume of Prisms and Cylinders, `8.4_Volume_of_Prisms_and_Cylinders`
- 8.4.1 Volume as unit cubes; $V = Bh$ for any prism ($B$ is the base area).
- 8.4.2 Cylinders $V = \pi r^2 h$.
- 8.4.3 Cavalieri's principle: a slanted (oblique) stack of coins or paper has the same volume (figure).
- 8.4.4 Unit conversions with volume: 27 cubic feet in a cubic yard; 1 cubic foot holds about 7.48 gallons.
- 8.4.5 Real: concrete for a slab in cubic yards (a 12 ft by 20 ft patio 4 in thick), water in a round
  pool or an aquarium, how many cans fill a box, a raised garden bed's soil.
- Solve for a missing dimension (height of a tank from its volume).

### 8.5 Volume of Pyramids, Cones, and Spheres, `8.5_Volume_of_Pyramids_Cones_and_Spheres`
- 8.5.1 Pyramids and cones: $\frac{1}{3}Bh$ (three cones fill a cylinder, figure; a .note pouring activity).
- 8.5.2 Use the slant height to find the height first (Pythagorean theorem).
- 8.5.3 Spheres $V = \frac{4}{3}\pi r^3$; hemispheres.
- 8.5.4 Composite solids: a silo (cylinder + hemisphere), an ice cream cone with a scoop, a pencil.
- 8.5.5 Real: a pile of sand or salt (cone), a grain silo, a ball's air volume, a funnel.

### 8.6 Density and Modeling, `8.6_Density_and_Modeling`
- 8.6.1 Density $= \frac{\text{mass}}{\text{volume}}$; weight from volume (concrete about 150 lb per cubic
  foot, water about 62.4 lb per cubic foot); will it float (compare with water).
- 8.6.2 Population density (people per square mile) from a map area; compare two cities or counties.
- 8.6.3 Scaling: if lengths scale by $k$, area scales by $k^2$ and volume by $k^3$ (from 5.2). A model
  and the real thing; why giant animals have thick legs (.note).
- 8.6.4 Modeling and design: how many 80 lb concrete bags for a slab (one bag makes about 0.6 cubic
  feet); which can design uses less metal for the same volume; how many trips a truck makes.
- Practice: multi-step, test-worded problems that combine area, volume, density and unit conversion.
