# -*- coding: utf-8 -*-
"""Subject 01 — Engineering Mathematics (13 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

# ---------------------------------------------------------------- 1. Overview
S.append({
 "id": "overview", "title": "Overview & Weightage",
 "html": """
<div class="kv">
  <span class="chip">Marks <b>13 / 100</b></span>
  <span class="chip">Typical Qs <b>8–10</b></span>
  <span class="chip">Sections <b>4</b></span>
  <span class="chip">Scoring <b>Very high yield</b></span>
</div>
<p>Engineering Mathematics is the <b>single most dependable block of marks</b> in GATE CS. It is finite in scope,
formula-driven, and repeated almost verbatim across years. If you are starting late, this is where the
<b>highest marks-per-hour-of-study</b> sits — ahead of any core subject.</p>

<h3>What it contains</h3>
<table>
<tr><th>Section</th><th>Typical marks</th><th>Difficulty</th><th>Priority</th></tr>
<tr><td>Discrete Mathematics</td><td>6–9</td><td>Medium</td><td>★★★★★</td></tr>
<tr><td>Probability &amp; Statistics</td><td>3–5</td><td>Easy–Medium</td><td>★★★★★</td></tr>
<tr><td>Linear Algebra</td><td>3–4</td><td>Easy</td><td>★★★★☆</td></tr>
<tr><td>Calculus</td><td>1–3</td><td>Easy</td><td>★★★☆☆</td></tr>
</table>

<div class="box tip"><div class="lbl">How to study this for GATE 2027</div>
<ol>
<li><b>Discrete Maths first</b> — it overlaps with Algorithms and TOC, so it pays twice.</li>
<li><b>Probability next</b> — 3–5 marks that are near-free if you learn 6 formulas.</li>
<li><b>Linear Algebra third</b> — small, closed syllabus, almost guaranteed questions.</li>
<li><b>Calculus last</b> — 1–3 marks, mostly limits, maxima–minima and definite integrals.</li>
<li><b>Practise past questions.</b> GATE repeats the <i>pattern</i> even when it changes the numbers.</li>
</ol>
</div>

<div class="box trap"><div class="lbl">Negative marking reality</div>
MCQs carry −1/3 (1-mark) and −2/3 (2-mark). <b>NAT questions have NO negative marking.</b>
In maths, if you can bound an answer numerically, guess NATs freely — but never blind-guess MCQs.
</div>
"""
})

# ------------------------------------------------- 2. Propositional logic
S.append({
 "id": "logic", "title": "Discrete Maths — Logic", "children": [
  CH("prop", "Propositional Logic", """
<p>A <b>proposition</b> is a statement that is definitely T or F. Connectives build compound propositions.</p>
<table>
<tr><th>Name</th><th>Symbol</th><th>True when…</th></tr>
<tr><td>Negation</td><td>¬p</td><td>p is false</td></tr>
<tr><td>Conjunction</td><td>p ∧ q</td><td>both true</td></tr>
<tr><td>Disjunction</td><td>p ∨ q</td><td>at least one true</td></tr>
<tr><td>Implication</td><td>p → q</td><td>false <b>only</b> when p=T, q=F</td></tr>
<tr><td>Biconditional</td><td>p ↔ q</td><td>same truth value</td></tr>
<tr><td>XOR</td><td>p ⊕ q</td><td>exactly one true</td></tr>
</table>

<div class="box formula"><div class="lbl">Must-memorise identities</div>
<ul>
<li><b>Implication as OR:</b> p → q ≡ ¬p ∨ q</li>
<li><b>Contrapositive:</b> p → q ≡ ¬q → ¬p &nbsp;(equivalent ✔)</li>
<li><b>Converse</b> q → p and <b>Inverse</b> ¬p → ¬q &nbsp;(NOT equivalent ✘)</li>
<li><b>De Morgan:</b> ¬(p ∧ q) ≡ ¬p ∨ ¬q &nbsp;·&nbsp; ¬(p ∨ q) ≡ ¬p ∧ ¬q</li>
<li><b>Absorption:</b> p ∧ (p ∨ q) ≡ p &nbsp;·&nbsp; p ∨ (p ∧ q) ≡ p</li>
<li><b>Distributive:</b> p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)</li>
<li><b>Exportation:</b> (p ∧ q) → r ≡ p → (q → r)</li>
</ul>
</div>

<h4>Classification of formulas</h4>
<ul>
<li><b>Tautology</b> — true for every assignment (e.g. p ∨ ¬p)</li>
<li><b>Contradiction</b> — false for every assignment (e.g. p ∧ ¬p)</li>
<li><b>Contingency</b> — neither</li>
<li><b>Satisfiable</b> — true for at least one assignment (every tautology is satisfiable)</li>
</ul>

<div class="box formula"><div class="lbl">Normal forms</div>
<b>CNF</b> = AND of OR-clauses (each clause = literals OR-ed). <b>DNF</b> = OR of AND-terms.<br>
Every formula has an equivalent CNF and DNF. <b>Full CNF/DNF</b> uses every variable in every clause —
the full DNF gives exactly the rows where the formula is TRUE, full CNF the rows where it is FALSE.
</div>

<details><summary>Worked example — is (p → q) ∧ (q → r) → (p → r) a tautology?</summary>
<div class="dc">
<p>Try to make it FALSE: need (p→q)∧(q→r) true and (p→r) false.</p>
<p>(p→r) false ⇒ p = T, r = F.<br>
(q→r) true with r=F ⇒ q must be F.<br>
(p→q) true with p=T, q=F ⇒ <b>contradiction</b>.</p>
<p>No assignment makes it false ⇒ it is a <b>tautology</b> (this is Hypothetical Syllogism / transitivity).</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
"p only if q" = p → q. "p if q" = q → p. "p unless q" = ¬q → p ≡ p ∨ q.
Misreading these three costs 1–2 marks almost every year.
</div>
"""),
  CH("fol", "First-Order Logic (Quantifiers)", """
<p>Adds predicates, variables and quantifiers over a domain (usually non-empty).</p>
<ul>
<li><b>Universal</b> ∀x P(x) — true if P holds for every element.</li>
<li><b>Existential</b> ∃x P(x) — true if P holds for at least one element.</li>
</ul>

<div class="box formula"><div class="lbl">Negation of quantifiers (De Morgan for quantifiers)</div>
¬∀x P(x) ≡ ∃x ¬P(x) &nbsp;&nbsp;·&nbsp;&nbsp; ¬∃x P(x) ≡ ∀x ¬P(x)
</div>

<h4>Nested quantifier rules</h4>
<table>
<tr><th>Formula</th><th>Meaning</th><th>Note</th></tr>
<tr><td>∀x ∀y P</td><td>all pairs</td><td>≡ ∀y ∀x P</td></tr>
<tr><td>∃x ∃y P</td><td>some pair</td><td>≡ ∃y ∃x P</td></tr>
<tr><td>∀x ∃y P</td><td>for each x some y (y may depend on x)</td><td rowspan="2"><b>Order matters</b> — these two are NOT equivalent</td></tr>
<tr><td>∃y ∀x P</td><td>one y works for all x (stronger)</td></tr>
</table>
<p><b>Implication chain:</b> ∃y ∀x P ⇒ ∀x ∃y P. The reverse does <b>not</b> hold.</p>

<details><summary>Worked example — negate ∀x ∃y (x + y = 0) over integers</summary>
<div class="dc">
<p>¬[∀x ∃y (x+y=0)] ≡ ∃x ¬[∃y (x+y=0)] ≡ ∃x ∀y (x+y ≠ 0).</p>
<p>Translation: "there is an integer x such that for every integer y, x+y ≠ 0." (False in reality, but that is the negation.)</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
A formula with a <b>free variable</b> has no truth value until the variable is bound or assigned.
Also: ∀x (P(x) → Q(x)) is <b>vacuously true</b> if nothing satisfies P — a favourite trick question.
</div>
""")]})

# --------------------------------------------- 3. Sets, relations, functions
S.append({
 "id": "sets", "title": "Discrete Maths — Sets, Relations, Functions", "children": [
  CH("sets2", "Sets & Counting", """
<div class="box formula"><div class="lbl">Set identities</div>
|A ∪ B| = |A| + |B| − |A ∩ B|<br>
|A ∪ B ∪ C| = Σ|A| − Σ|A∩B| + |A∩B∩C|<br>
Power set: |P(A)| = 2<sup>|A|</sup> &nbsp;·&nbsp; Subsets of size k: C(n,k)<br>
If |A| = m, |B| = n → <b>functions</b> A→B: n<sup>m</sup> &nbsp;·&nbsp; <b>relations</b> A→B: 2<sup>mn</sup>
</div>
<p><b>Cartesian product</b> A×B = {(a,b) : a∈A, b∈B}, with |A×B| = |A|·|B|.</p>
"""),
  CH("rel", "Relations", """
<p>A relation R on A is a subset of A×A. The four key properties:</p>
<table>
<tr><th>Property</th><th>Condition</th></tr>
<tr><td>Reflexive</td><td>∀a: (a,a) ∈ R</td></tr>
<tr><td>Symmetric</td><td>(a,b) ∈ R ⇒ (b,a) ∈ R</td></tr>
<tr><td>Transitive</td><td>(a,b),(b,c) ∈ R ⇒ (a,c) ∈ R</td></tr>
<tr><td>Antisymmetric</td><td>(a,b),(b,a) ∈ R ⇒ a = b</td></tr>
</table>

<div class="box formula"><div class="lbl">Equivalence relation</div>
<b>Reflexive + Symmetric + Transitive.</b> Partitions A into disjoint equivalence classes.
Number of equivalence relations on n elements = <b>Bell number B<sub>n</sub></b>
(1, 2, 5, 15, 52, …).
</div>

<div class="box formula"><div class="lbl">Partial order</div>
<b>Reflexive + Antisymmetric + Transitive.</b> Written (A, ≼).
A <b>total order</b> additionally compares every pair.
Number of partial orders on n elements is large and not a simple formula — GATE usually
gives the relation and asks you to <i>check</i>, not count.
</div>

<h4>Hasse diagram — how to draw it fast</h4>
<ol>
<li>Drop all self-loops (reflexive edges).</li>
<li>Drop all edges implied by transitivity.</li>
<li>Draw larger elements above smaller ones.</li>
<li>Connect with straight lines, no arrowheads.</li>
</ol>

<div class="box formula"><div class="lbl">Lattice</div>
A poset where <b>every pair</b> has a least upper bound (join, ∨) and greatest lower bound (meet, ∧).
<ul>
<li><b>Total order ⇒ always a lattice.</b></li>
<li>The "diamond" and "chain" posets are lattices; the "N-shaped" poset is <b>not</b>.</li>
<li>A <b>bounded</b> lattice has a unique least element 0 and greatest element 1.</li>
</ul>
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
<b>Symmetric and antisymmetric are not opposites.</b> A relation can be both (then it is a diagonal/identity-type
relation) or neither. Only "asymmetric" (never both directions) excludes symmetric.
Also: a relation that is <b>reflexive and transitive and symmetric</b> is an equivalence relation — a relation
that is reflexive, transitive and antisymmetric is a partial order. Do not mix them up.
</div>
"""),
  CH("fn", "Functions", """
<table>
<tr><th>Type</th><th>Condition</th><th>Exists A→B when…</th></tr>
<tr><td>Injective (one-one)</td><td>f(a)=f(b) ⇒ a=b</td><td>|A| ≤ |B|</td></tr>
<tr><td>Surjective (onto)</td><td>every b∈B is hit</td><td>|A| ≥ |B|</td></tr>
<tr><td>Bijective</td><td>both</td><td>|A| = |B|</td></tr>
</table>
<p>For finite sets of equal size, injective ⇔ surjective ⇔ bijective.</p>
<div class="box formula"><div class="lbl">Count of functions</div>
Total functions A→B: n<sup>m</sup> · Injective: <sup>n</sup>P<sub>m</sub> · Onto (surjective):
n! · S(m,n) where S is a Stirling number of the second kind.
</div>
""")]})

# -------------------------------------------- 4. Algebraic structures
S.append({
 "id": "algebra", "title": "Discrete Maths — Groups & Monoids", "children": [
  CH("grp", "Algebraic Structures", """
<table>
<tr><th>Structure</th><th>Requirements</th></tr>
<tr><td>Semigroup</td><td>Closure + Associativity</td></tr>
<tr><td>Monoid</td><td>Semigroup + Identity element</td></tr>
<tr><td>Group</td><td>Monoid + Inverse for every element</td></tr>
<tr><td>Abelian group</td><td>Group + Commutativity</td></tr>
</table>
<p><b>Group = (G, ∘)</b> satisfying: closure, associativity, identity <i>e</i>, and inverse for every element.</p>

<div class="box formula"><div class="lbl">Group theory essentials</div>
<ul>
<li><b>Order of a group</b> |G| = number of elements.</li>
<li><b>Order of an element</b> a = smallest k&gt;0 with a<sup>k</sup> = e. It always <b>divides</b> |G| (Lagrange).</li>
<li><b>Cyclic group</b> — generated by one element: G = ⟨a⟩. Every cyclic group is Abelian.</li>
<li>Every group of <b>prime order</b> is cyclic (hence Abelian).</li>
<li><b>Z<sub>n</sub></b> under addition mod n is cyclic of order n, generated by 1.</li>
<li>(Z<sub>n</sub>, ×) is a group <b>only if n is prime</b> (otherwise non-coprime elements have no inverse).</li>
</ul>
</div>

<details><summary>Worked example — smallest group that is non-Abelian</summary>
<div class="dc">
<p>Order 6. |G| = 6 groups: Z<sub>6</sub> (cyclic, Abelian) and <b>S<sub>3</sub></b>, the symmetric group of
permutations of 3 elements, which is <b>non-Abelian</b>.</p>
<p>So the <b>smallest non-Abelian group has order 6</b> (note: order 4 groups Z<sub>4</sub> and
Z<sub>2</sub>×Z<sub>2</sub> are both Abelian; order 6 is where non-Abelian first appears).</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Order of every element divides |G|, but the converse is false — a divisor of |G| need not be the order of
any element (e.g. in Z<sub>2</sub>×Z<sub>2</sub> of order 4, no element has order 4).
Also: <b>number of generators of a cyclic group of order n = φ(n)</b> (Euler's totient).
</div>
""")]})

# --------------------------------------------------- 5. Combinatorics
S.append({
 "id": "comb", "title": "Discrete Maths — Combinatorics & Recurrences", "children": [
  CH("count", "Counting Techniques", """
<div class="box formula"><div class="lbl">Core counting formulas</div>
<ul>
<li>Permutations: <sup>n</sup>P<sub>r</sub> = n!/(n−r)! &nbsp;·&nbsp; Combinations: <sup>n</sup>C<sub>r</sub> = n!/(r!(n−r)!)</li>
<li>Circular arrangements of n distinct objects: <b>(n−1)!</b></li>
<li><b>Pigeonhole:</b> n items in m boxes ⇒ some box has ⌈n/m⌉ items.</li>
<li><b>Inclusion–Exclusion:</b> |A∪B∪C| = ΣA − ΣA∩B + A∩B∩C</li>
<li>Derangements (no item in its own place): D<sub>n</sub> = n!·Σ<sub>k=0..n</sub> (−1)<sup>k</sup>/k!</li>
<li><b>Stars and bars:</b> x<sub>1</sub>+…+x<sub>k</sub> = n with x<sub>i</sub> ≥ 0 has <b>C(n+k−1, k−1)</b> solutions.</li>
<li><b>Catalan number</b> C<sub>n</sub> = C(2n,n)/(n+1) — counts balanced parentheses, BSTs, Dyck paths.</li>
</ul>
</div>
"""),
  CH("rec", "Recurrence Relations", """
<h3>Linear homogeneous recurrence</h3>
<p>a<sub>n</sub> = c<sub>1</sub>a<sub>n−1</sub> + c<sub>2</sub>a<sub>n−2</sub> + … → write the <b>characteristic equation</b>
r<sup>k</sup> − c<sub>1</sub>r<sup>k−1</sup> − … − c<sub>k</sub> = 0.</p>
<ul>
<li>Distinct real roots r<sub>1</sub>, r<sub>2</sub>: a<sub>n</sub> = A·r<sub>1</sub><sup>n</sup> + B·r<sub>2</sub><sup>n</sup></li>
<li>Repeated root r (multiplicity m): multiply by n<sup>j</sup> terms — A·r<sup>n</sup> + B·n·r<sup>n</sup> + …</li>
<li>Use initial conditions to solve for A, B.</li>
</ul>

<h3>Master Theorem (for divide &amp; conquer)</h3>
<div class="box formula"><div class="lbl">T(n) = aT(n/b) + f(n), with f(n) = Θ(n<sup>d</sup>)</div>
<ul>
<li>If d &lt; log<sub>b</sub>a &nbsp;→&nbsp; T(n) = <b>Θ(n<sup>log<sub>b</sub>a</sup>)</b></li>
<li>If d = log<sub>b</sub>a &nbsp;→&nbsp; T(n) = <b>Θ(n<sup>d</sup> log n)</b></li>
<li>If d &gt; log<sub>b</sub>a &nbsp;→&nbsp; T(n) = <b>Θ(n<sup>d</sup>)</b></li>
</ul>
</div>

<details><summary>Worked example — T(n) = 2T(n/2) + n</summary>
<div class="dc">
<p>a = 2, b = 2, d = 1. log<sub>2</sub>2 = 1 = d ⇒ <b>case 2</b> ⇒ T(n) = Θ(n log n). (Merge sort.)</p>
<p>Compare T(n) = 2T(n/2) + n<sup>2</sup>: d = 2 &gt; log<sub>2</sub>2 = 1 ⇒ case 3 ⇒ Θ(n<sup>2</sup>).</p>
</div></details>

<h4>Generating functions</h4>
<p>The generating function of ⟨a<sub>n</sub>⟩ is G(x) = Σ a<sub>n</sub>x<sup>n</sup>.</p>
<div class="box formula"><div class="lbl">Useful closed forms</div>
1/(1−x) = 1 + x + x² + … &nbsp;·&nbsp; 1/(1−x)² = Σ(n+1)x<sup>n</sup> &nbsp;·&nbsp;
1/(1−ax) = Σa<sup>n</sup>x<sup>n</sup> &nbsp;·&nbsp; e<sup>x</sup> = Σx<sup>n</sup>/n!
</div>
""")]})

# --------------------------------------------------- 6. Graph theory
S.append({
 "id": "graph", "title": "Discrete Maths — Graph Theory", "children": [
  CH("gbase", "Graph Basics & Connectivity", """
<div class="box formula"><div class="lbl">Handshaking lemma</div>
Σ<sub>v∈V</sub> deg(v) = <b>2|E|</b> &nbsp;⇒&nbsp; the number of odd-degree vertices is always <b>even</b>.
</div>
<table>
<tr><th>Term</th><th>Meaning</th></tr>
<tr><td>Simple graph</td><td>no self-loops, no multi-edges; max edges = C(n,2)</td></tr>
<tr><td>Complete graph K<sub>n</sub></td><td>every pair joined; n(n−1)/2 edges</td></tr>
<tr><td>Bipartite</td><td>vertices split into 2 sets, edges only across; <b>no odd cycle</b></td></tr>
<tr><td>Tree</td><td>connected + acyclic; exactly n−1 edges</td></tr>
<tr><td>Spanning tree</td><td>tree on all n vertices; K<sub>n</sub> has <b>n<sup>n−2</sup></b> of them (Cayley)</td></tr>
<tr><td>Cut vertex / bridge</td><td>removal disconnects the graph</td></tr>
</table>
<div class="box formula"><div class="lbl">Planarity</div>
Euler's formula for a connected planar graph: <b>V − E + F = 2</b>.<br>
Necessary condition: E ≤ 3V − 6 (and E ≤ 2V − 4 if bipartite).<br>
<b>K<sub>5</sub> and K<sub>3,3</sub> are non-planar</b> (Kuratowski's theorem).
</div>
<div class="box formula"><div class="lbl">Euler vs Hamiltonian</div>
<b>Euler path</b> uses every <i>edge</i> exactly once — exists iff 0 or 2 vertices have odd degree.<br>
<b>Euler circuit</b> — exists iff <b>all</b> vertices have even degree.<br>
<b>Hamiltonian</b> path/cycle uses every <i>vertex</i> once — no simple necessary-and-sufficient condition (NP-hard to test).
</div>
<div class="box formula"><div class="lbl">Colouring &amp; matching</div>
<b>Chromatic number χ(G)</b>: minimum colours for a proper colouring.<br>
χ = 2 ⇔ bipartite · χ(K<sub>n</sub>) = n · any planar graph has χ ≤ 4 (Four Colour Theorem).<br>
<b>Hall's Marriage Theorem:</b> a perfect matching in a bipartite graph exists iff for every subset S of one side,
|N(S)| ≥ |S|.
</div>
<details><summary>Worked example — is K<sub>4</sub> planar? How many regions?</summary>
<div class="dc">
<p>K<sub>4</sub>: V = 4, E = 6. Check E ≤ 3V−6 = 6 ✓ (tight).</p>
<p>Euler: F = 2 − V + E = 2 − 4 + 6 = <b>4 regions</b> (3 internal + 1 outer). K<sub>4</sub> <b>is</b> planar.</p>
</div></details>
<div class="box trap"><div class="lbl">GATE trap</div>
"Exactly two vertices of odd degree" ⇒ Euler <i>path</i> exists (not a circuit). Students lose this
half-mark constantly. Also a disconnected graph can never have an Euler circuit regardless of degrees.
</div>
""")]})

# --------------------------------------------------- 7. Linear algebra
S.append({
 "id": "linalg", "title": "Linear Algebra", "children": [
  CH("la", "Matrices, Rank & Systems", """
<div class="box formula"><div class="lbl">Rank–nullity theorem</div>
<b>rank(A) + nullity(A) = n</b> &nbsp; (n = number of columns). Nullity = dimension of the null space.
</div>
<table>
<tr><th>Concept</th><th>Key fact</th></tr>
<tr><td>Rank</td><td>number of non-zero rows in row-echelon form; also the largest non-zero minor order</td></tr>
<tr><td>Trace</td><td>sum of diagonal = <b>sum of eigenvalues</b></td></tr>
<tr><td>Determinant</td><td>= <b>product of eigenvalues</b></td></tr>
<tr><td>Symmetric</td><td>A<sup>T</sup> = A — all eigenvalues real</td></tr>
<tr><td>Skew-symmetric</td><td>A<sup>T</sup> = −A — eigenvalues are 0 or purely imaginary</td></tr>
<tr><td>Idempotent</td><td>A² = A — eigenvalues are only 0 or 1</td></tr>
<tr><td>Nilpotent</td><td>A<sup>k</sup> = 0 — all eigenvalues are 0</td></tr>
<tr><td>Orthogonal</td><td>A<sup>T</sup>A = I — determinant ±1</td></tr>
</table>
<div class="box formula"><div class="lbl">Consistency of Ax = b</div>
Form the augmented matrix [A | b] and reduce.<br>
<ul>
<li>rank(A) ≠ rank([A|b]) &nbsp;→&nbsp; <b>no solution</b> (inconsistent)</li>
<li>rank(A) = rank([A|b]) = n (number of unknowns) &nbsp;→&nbsp; <b>unique solution</b></li>
<li>rank(A) = rank([A|b]) &lt; n &nbsp;→&nbsp; <b>infinitely many solutions</b></li>
</ul>
</div>
"""),
  CH("eig", "Eigenvalues & Eigenvectors", """
<p>Ax = λx with x ≠ 0. Find λ from the <b>characteristic equation det(A − λI) = 0</b>.</p>
<div class="box formula"><div class="lbl">Rules that save time in the exam</div>
<ul>
<li>Σλ<sub>i</sub> = trace(A) &nbsp;·&nbsp; Πλ<sub>i</sub> = det(A)</li>
<li>Eigenvalues of A<sup>k</sup> = λ<sup>k</sup>; of A<sup>−1</sup> = 1/λ; of (A + cI) = λ + c</li>
<li>A is <b>singular ⇔ 0 is an eigenvalue</b></li>
<li>Triangular / diagonal matrices: eigenvalues <b>are</b> the diagonal entries</li>
<li>Symmetric real matrix ⇒ eigenvalues real and eigenvectors orthogonal</li>
<li><b>Cayley–Hamilton:</b> A satisfies its own characteristic polynomial</li>
</ul>
</div>
<details><summary>Worked example — eigenvalues of [[2,1],[1,2]]</summary>
<div class="dc">
<p>trace = 4, det = 4 − 1 = 3. Solve λ² − 4λ + 3 = 0 ⇒ (λ−1)(λ−3) = 0 ⇒ <b>λ = 1, 3</b>.</p>
<p>Check: sum 4 = trace ✔, product 3 = det ✔. Eigenvector for λ=3: (1,1)<sup>T</sup>; for λ=1: (1,−1)<sup>T</sup>.</p>
</div></details>
<div class="box tip"><div class="lbl">Speed trick</div>
For a 2×2 matrix never expand the determinant — use λ² − (trace)λ + (det) = 0.
For 3×3, use trace/det plus one eigenvalue you can spot from the diagonal.
</div>
""")]})

# --------------------------------------------------- 8. Calculus
S.append({
 "id": "calc", "title": "Calculus", "children": [
  CH("cal", "Limits, Maxima–Minima, Integration", """
<div class="box formula"><div class="lbl">Standard limits</div>
lim<sub>x→0</sub> (sin x)/x = 1 &nbsp;·&nbsp; lim<sub>x→0</sub> (e<sup>x</sup>−1)/x = 1 &nbsp;·&nbsp;
lim<sub>x→0</sub> (1+x)<sup>1/x</sup> = e &nbsp;·&nbsp; lim<sub>x→0</sub> ln(1+x)/x = 1<br>
lim<sub>x→∞</sub> (1 + a/x)<sup>x</sup> = e<sup>a</sup> &nbsp;·&nbsp;
lim<sub>x→0</sub> (1−cos x)/x² = 1/2
</div>
<p><b>L'Hôpital's rule:</b> for 0/0 or ∞/∞, lim f/g = lim f′/g′ — apply repeatedly while the form persists.</p>

<h3>Maxima &amp; minima</h3>
<ol>
<li>Find f′(x) = 0 → <b>critical points</b>.</li>
<li><b>Second derivative test:</b> f″(x) &lt; 0 → local max; f″(x) &gt; 0 → local min.</li>
<li>For a <b>global</b> extremum on [a,b], also check the endpoints a and b.</li>
</ol>

<h3>Mean value theorems</h3>
<table>
<tr><th>Theorem</th><th>Statement</th></tr>
<tr><td>Rolle's</td><td>f(a)=f(b), f continuous on [a,b] and differentiable on (a,b) ⇒ ∃c with f′(c)=0</td></tr>
<tr><td>Lagrange's (MVT)</td><td>∃c ∈ (a,b) with f′(c) = [f(b) − f(a)]/(b − a)</td></tr>
<tr><td>Cauchy's</td><td>∃c with f′(c)/g′(c) = [f(b)−f(a)]/[g(b)−g(a)]</td></tr>
</table>

<div class="box formula"><div class="lbl">Integrals worth memorising</div>
∫<sub>0</sub><sup>1</sup> x<sup>n</sup> dx = 1/(n+1) · ∫<sub>0</sub><sup>∞</sup> e<sup>−x</sup> dx = 1 ·
∫<sub>0</sub><sup>∞</sup> x<sup>n−1</sup>e<sup>−x</sup>dx = Γ(n) = (n−1)!<br>
∫<sub>−∞</sub><sup>∞</sup> e<sup>−x²</sup>dx = √π · ∫<sub>0</sub><sup>∞</sup> dx/(1+x²) = π/2
</div>
<div class="box formula"><div class="lbl">Taylor / Maclaurin series</div>
e<sup>x</sup> = Σ x<sup>n</sup>/n! &nbsp;·&nbsp; sin x = x − x³/3! + x⁵/5! − … &nbsp;·&nbsp; cos x = 1 − x²/2! + x⁴/4! − …<br>
ln(1+x) = x − x²/2 + x³/3 − … (|x|&lt;1) &nbsp;·&nbsp; 1/(1−x) = 1 + x + x² + …
</div>
""")]})

# --------------------------------------------------- 9. Probability
S.append({
 "id": "prob", "title": "Probability & Statistics", "children": [
  CH("pb", "Probability Fundamentals", """
<div class="box formula"><div class="lbl">Core rules</div>
P(A∪B) = P(A) + P(B) − P(A∩B) · P(A<sup>c</sup>) = 1 − P(A) · P(A∩B) = P(A)·P(B) if independent<br>
<b>Conditional:</b> P(A|B) = P(A∩B)/P(B)<br>
<b>Bayes:</b> P(A<sub>i</sub>|B) = P(B|A<sub>i</sub>)·P(A<sub>i</sub>) / Σ<sub>j</sub> P(B|A<sub>j</sub>)·P(A<sub>j</sub>)<br>
<b>Total probability:</b> P(B) = Σ P(B|A<sub>j</sub>)·P(A<sub>j</sub>)
</div>
<p><b>Independence</b> is <i>not</i> the same as mutual exclusivity. Mutually exclusive events with non-zero
probability are <b>never</b> independent.</p>

<details><summary>Worked example — the classic Bayes test</summary>
<div class="dc">
<p>A disease affects 1% of people. A test is 99% sensitive and 99% specific. Given a positive test, what is P(disease)?</p>
<p>P(D)=0.01, P(+|D)=0.99, P(+|¬D)=0.01.<br>
P(+) = 0.99·0.01 + 0.01·0.99 = 0.0198.<br>
P(D|+) = 0.0099/0.0198 = <b>0.5 (50%)</b>. Base rates dominate — a GATE favourite.</p>
</div></details>
"""),
  CH("dist", "Random Variables & Distributions", """
<div class="box formula"><div class="lbl">Expectation &amp; variance</div>
E[X] = Σ x·P(x) &nbsp;(discrete) or ∫ x·f(x)dx (continuous)<br>
Var(X) = E[X²] − (E[X])² &nbsp;·&nbsp; Var(aX + b) = a²·Var(X)<br>
E[X + Y] = E[X] + E[Y] <b>always</b> &nbsp;·&nbsp; Var(X+Y) = Var(X)+Var(Y) <b>only if independent</b><br>
E[XY] = E[X]·E[Y] if independent
</div>
<table>
<tr><th>Distribution</th><th>Parameters</th><th>Mean</th><th>Variance</th></tr>
<tr><td>Binomial B(n,p)</td><td>n trials, prob p</td><td>np</td><td>np(1−p)</td></tr>
<tr><td>Poisson(λ)</td><td>rate λ</td><td>λ</td><td>λ</td></tr>
<tr><td>Uniform(a,b)</td><td>interval</td><td>(a+b)/2</td><td>(b−a)²/12</td></tr>
<tr><td>Exponential(λ)</td><td>rate λ</td><td>1/λ</td><td>1/λ²</td></tr>
<tr><td>Normal(μ,σ²)</td><td>mean μ, var σ²</td><td>μ</td><td>σ²</td></tr>
</table>
<p><b>Binomial→Poisson:</b> when n is large and p small with np = λ fixed, B(n,p) → Poisson(λ).</p>
<p><b>Memoryless property</b> holds only for the exponential (continuous) and geometric (discrete) distributions.</p>
<div class="box formula"><div class="lbl">Inequalities</div>
<b>Markov:</b> P(X ≥ a) ≤ E[X]/a &nbsp;(X ≥ 0, a &gt; 0)<br>
<b>Chebyshev:</b> P(|X − μ| ≥ kσ) ≤ 1/k² — no distribution assumption needed
</div>
""")]})

# --------------------------------------------------- 10. Formula sheet
S.append({
 "id": "formulas", "title": "One-Page Formula Sheet (Revise Before Exam)",
 "html": """
<table>
<tr><th>Area</th><th>Formula</th></tr>
<tr><td>Implication</td><td>p→q ≡ ¬p∨q ≡ ¬q→¬p</td></tr>
<tr><td>De Morgan (logic)</td><td>¬(p∧q) ≡ ¬p∨¬q</td></tr>
<tr><td>Quantifier negation</td><td>¬∀x P ≡ ∃x ¬P</td></tr>
<tr><td>Set union</td><td>|A∪B| = |A|+|B|−|A∩B|</td></tr>
<tr><td>Power set</td><td>|P(A)| = 2<sup>|A|</sup></td></tr>
<tr><td>Equivalence relations on n elements</td><td>Bell number B<sub>n</sub>: 1,2,5,15,52,203</td></tr>
<tr><td>Cyclic group generators</td><td>φ(n)</td></tr>
<tr><td>Pigeonhole</td><td>n items, m boxes ⇒ some box has ⌈n/m⌉</td></tr>
<tr><td>Stars and bars</td><td>C(n+k−1, k−1)</td></tr>
<tr><td>Derangements</td><td>D<sub>n</sub> = n!·Σ(−1)<sup>k</sup>/k!</td></tr>
<tr><td>Catalan</td><td>C<sub>n</sub> = C(2n,n)/(n+1)</td></tr>
<tr><td>Master theorem</td><td>T(n)=aT(n/b)+Θ(n<sup>d</sup>): compare d with log<sub>b</sub>a</td></tr>
<tr><td>Handshaking</td><td>Σdeg = 2|E|</td></tr>
<tr><td>Euler (planar)</td><td>V − E + F = 2</td></tr>
<tr><td>Planar bound</td><td>E ≤ 3V − 6</td></tr>
<tr><td>Cayley</td><td>spanning trees of K<sub>n</sub> = n<sup>n−2</sup></td></tr>
<tr><td>Rank–nullity</td><td>rank + nullity = n</td></tr>
<tr><td>Trace/det ↔ eigenvalues</td><td>Σλ = trace · Πλ = det</td></tr>
<tr><td>2×2 eigenvalues</td><td>λ² − (trace)λ + det = 0</td></tr>
<tr><td>Var</td><td>E[X²] − (E[X])²</td></tr>
<tr><td>Chebyshev</td><td>P(|X−μ| ≥ kσ) ≤ 1/k²</td></tr>
</table>
<div class="box tip"><div class="lbl">Exam-day plan for Eng Maths</div>
Attempt <b>Discrete Maths + Probability</b> questions first (highest accuracy), then Linear Algebra,
then Calculus. For NAT questions, if you can bound the value, always attempt — no negative marking.
</div>
"""
})

S.append({
 "id": "strategy", "title": "Exam Strategy",
 "html": """
<div class="box tip"><div class="lbl">Attempt order (highest accuracy first)</div>
<ol>
<li><b>Probability &amp; Statistics</b> — short, formula-driven, high accuracy.</li>
<li><b>Discrete Maths</b> — logic, relations, counting, graphs. Reliable marks.</li>
<li><b>Linear Algebra</b> — usually 1–2 near-guaranteed questions.</li>
<li><b>Calculus</b> — attempt last; only 1–3 marks and calculation-heavy.</li>
</ol>
</div>

<h3>Time budget</h3>
<table>
<tr><th>Task</th><th>Time</th><th>Note</th></tr>
<tr><td>Engineering Maths block</td><td>~15–18 min</td><td>For 8–10 questions</td></tr>
<tr><td>Per 1-mark question</td><td>≤ 1.5 min</td><td>If stuck, mark and move on</td></tr>
<tr><td>Per 2-mark question</td><td>≤ 3 min</td><td>2-mark NATs are worth the effort</td></tr>
</table>

<h3>Common time sinks — avoid these</h3>
<ul>
<li><b>Long determinant expansion.</b> Use λ² − (trace)λ + det for 2×2. Never expand 4×4 by minors.</li>
<li><b>Brute-force truth tables</b> for 4+ variables. Use equivalences and the "try to make it false" method.</li>
<li><b>Re-deriving eigenvalues</b> when the matrix is triangular — read them off the diagonal.</li>
<li><b>Integrating by parts</b> when a standard form (Γ function, e<sup>−x²</sup>) applies.</li>
</ul>

<h3>Answering strategy by question type</h3>
<table>
<tr><th>Type</th><th>Strategy</th></tr>
<tr><td>MCQ (1 or 2 mark)</td><td>−1/3 and −2/3 penalty. Only guess if you can eliminate at least two options.</td></tr>
<tr><td>MSQ</td><td><b>No negative marking.</b> Evaluate every option independently and select all that hold.</td></tr>
<tr><td>NAT</td><td><b>No negative marking.</b> Always enter your best value — even an estimate can be right.</td></tr>
</table>

<div class="box trap"><div class="lbl">The three mistakes that cost the most marks</div>
<ol>
<li><b>Misreading "only if" / "if" / "unless".</b> p only if q = p→q. p if q = q→p. p unless q = p∨q.</li>
<li><b>Confusing converse with contrapositive.</b> Only the contrapositive is equivalent to the original.</li>
<li><b>Rushing NAT rounding.</b> GATE NAT answers usually need 1–2 decimal places — read the instruction.</li>
</ol>
</div>

<div class="box tip"><div class="lbl">Minimum viable target</div>
Engineering Mathematics is 13 marks. Even with partial preparation, a realistic target is
<b>8–10 marks</b> (6–7 correct answers). That alone is 8–10% of the paper from a small, finite syllabus —
which is exactly why it should be prepared <b>before</b> the larger core subjects.
</div>
"""
})

QUIZ = [
 {"q":"Which is logically equivalent to p → q?","opts":["q → p","¬p → ¬q","¬q → ¬p","p ∧ ¬q"],"a":2,
  "ex":"Contrapositive: p→q ≡ ¬q→¬p. The converse (q→p) and inverse (¬p→¬q) are NOT equivalent."},
 {"q":"The negation of ∀x ∃y P(x,y) is:","opts":["∃x ∀y ¬P(x,y)","∀x ∃y ¬P(x,y)","∃x ∃y ¬P(x,y)","∀x ∀y ¬P(x,y)"],"a":0,
  "ex":"Negation flips each quantifier and moves inward: ¬∀x∃y P = ∃x¬∃y P = ∃x∀y¬P."},
 {"q":"Number of equivalence relations on a 3-element set is:","opts":["3","5","6","9"],"a":1,
  "ex":"Bell number B3 = 5. They correspond to the partitions of {1,2,3}."},
 {"q":"The smallest non-Abelian group has order:","opts":["4","6","8","12"],"a":1,
  "ex":"Order 6: S3 (symmetric group on 3 elements). Orders 1–5 are all cyclic/Abelian."},
 {"q":"K5 is:","opts":["Planar","Bipartite","Non-planar","A tree"],"a":2,
  "ex":"K5 violates E ≤ 3V−6 (10 > 9), so it is non-planar by Kuratowski's theorem."},
 {"q":"A connected graph has an Euler circuit iff:","opts":["exactly two vertices have odd degree","all vertices have even degree","it is bipartite","it has no bridges"],"a":1,
  "ex":"All even degrees ⇒ Euler circuit. Exactly two odd ⇒ Euler path (not circuit)."},
 {"q":"Number of spanning trees of K4 is:","opts":["4","8","16","64"],"a":2,
  "ex":"Cayley: n^(n−2) = 4^2 = 16."},
 {"q":"For a 2×2 matrix with trace 5 and determinant 6, the eigenvalues are:","opts":["1 and 5","2 and 3","−2 and −3","6 and 1"],"a":1,
  "ex":"λ² − 5λ + 6 = 0 ⇒ (λ−2)(λ−3)=0 ⇒ λ = 2, 3. Sum=5 ✓, product=6 ✓."},
 {"q":"If A is a 3×5 matrix with rank 3, the nullity is:","opts":["0","2","3","5"],"a":1,
  "ex":"rank + nullity = number of columns = 5, so nullity = 2."},
 {"q":"The system Ax = b has infinitely many solutions when:","opts":["rank(A) ≠ rank([A|b])","rank(A) = rank([A|b]) = n","rank(A) = rank([A|b]) < n","det(A) ≠ 0"],"a":2,
  "ex":"Consistent (equal ranks) but free variables exist (rank < number of unknowns) ⇒ infinitely many."},
 {"q":"For a Poisson distribution with mean 3, the variance is:","opts":["√3","3","9","1/3"],"a":1,
  "ex":"Poisson(λ): mean = variance = λ = 3."},
 {"q":"Var(2X + 5) where Var(X) = 3 equals:","opts":["6","11","12","17"],"a":2,
  "ex":"Var(aX+b) = a²Var(X) = 4 × 3 = 12. The constant 5 adds nothing to variance."},
 {"q":"The memoryless property holds for:","opts":["Binomial","Normal","Exponential","Uniform"],"a":2,
  "ex":"Only the exponential (continuous) and geometric (discrete) are memoryless."},
 {"q":"lim(x→0) (sin 3x)/x equals:","opts":["0","1","3","1/3"],"a":2,
  "ex":"(sin 3x)/x = 3·(sin 3x)/(3x) → 3·1 = 3."},
 {"q":"Value of ∫₀^∞ e^(−x) dx is:","opts":["0","1","e","∞"],"a":1,
  "ex":"∫₀^∞ e^(−x)dx = [−e^(−x)]₀^∞ = 0 − (−1) = 1."},
 {"q":"If f(a) = f(b) and f is continuous on [a,b] and differentiable on (a,b), Rolle's theorem guarantees:","opts":["f′(a)=0","∃c with f′(c)=0","f is constant","f″(c)=0"],"a":1,
  "ex":"Rolle's theorem: there exists at least one c in (a,b) with f′(c) = 0."},
 {"q":"Mutually exclusive events with non-zero probability are:","opts":["always independent","never independent","sometimes independent","always dependent"],"a":1,
  "ex":"If P(A∩B)=0 and both are non-zero, P(A)·P(B)>0 ≠ 0, so they can never be independent."},
 {"q":"Number of ways to arrange 5 people around a circular table is:","opts":["120","24","60","12"],"a":1,
  "ex":"Circular arrangements of n distinct objects = (n−1)! = 4! = 24."},
 {"q":"For T(n) = 4T(n/2) + n, the time complexity is:","opts":["Θ(n)","Θ(n log n)","Θ(n²)","Θ(n³)"],"a":2,
  "ex":"a=4, b=2, d=1. log₂4 = 2 > 1 ⇒ case 1 ⇒ Θ(n^log_b a) = Θ(n²)."},
 {"q":"The number of odd-degree vertices in any graph is:","opts":["always odd","always even","can be anything","always zero"],"a":1,
  "ex":"Handshaking lemma: Σdeg = 2|E|. Odd-degree vertices must come in pairs, so their count is even."}
]

SUBJECT = {
 "code": "S01", "title": "Engineering Mathematics",
 "subtitle": "GATE CS 2027 · 13 marks · Discrete Maths, Linear Algebra, Calculus, Probability",
 "weight_note": "GATE CS 2027 · Engineering Mathematics section (13 marks)",
 "sections": S, "quiz": QUIZ,
}
