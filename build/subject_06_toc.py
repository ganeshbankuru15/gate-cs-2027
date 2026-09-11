# -*- coding: utf-8 -*-
"""Subject 06 — Theory of Computation (8 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

# ---------------------------------------------------------------- 1. Overview
S.append({
 "id": "toc-overview", "title": "Overview & Weightage",
 "html": """
<div class="kv">
  <span class="chip">Marks <b>8 / 100</b></span>
  <span class="chip">Typical Qs <b>3–5</b></span>
  <span class="chip">Sections <b>7</b></span>
  <span class="chip">Scoring <b>Concept-heavy, high yield</b></span>
</div>
<p>Theory of Computation rewards <b>precise, rule-based reasoning</b> and punishes vague
intuition. Roughly two-thirds of the marks go to <b>regular languages</b> (FSAs, regex,
pumping lemma, closure) and <b>context-free languages</b> (grammars, PDA, pumping).
The remaining third is <b>Turing machines and undecidability</b> — mostly conceptual.</p>

<h3>What to attack first</h3>
<table>
<tr><th>Area</th><th>Typical marks</th><th>Style</th><th>Priority</th></tr>
<tr><td>Finite automata + regex</td><td>3–4</td><td>Numerical/construct</td><td>★★★★★</td></tr>
<tr><td>Closure + pumping lemma</td><td>1–2</td><td>True/false + proof</td><td>★★★★★</td></tr>
<tr><td>CFG + PDA</td><td>1–2</td><td>Construct + reasoning</td><td>★★★★★</td></tr>
<tr><td>TM + undecidability</td><td>1–2</td><td>Conceptual</td><td>★★★★☆</td></tr>
</table>

<div class="box tip"><div class="lbl">How to study TOC for GATE 2027</div>
<ol>
<li><b>Master closure properties first</b> — they underpin 80% of the true/false questions and interact with Algorithms/Compiler Design.</li>
<li><b>Practise pumping-lemma proofs</b> on a^n b^n, equal counts, palindromes, a^n b^n c^n — the pattern is identical every year.</li>
<li><b>Memorise the decidability table</b> (which problems are decidable/undecidable) — it is near-free marks.</li>
<li><b>Do not chase exotic variants.</b> GATE asks standard FSAs, ε-NFA, PDA, single-tape TMs.</li>
</ol>
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
Marks here come from <b>exactness</b>. "All regular languages are context-free" is TRUE, but
"all context-free languages are regular" is FALSE. Answer what the question literally asks —
many traps depend on reversing the implication or adding a single word like "every"/"some".
</div>
"""
})

# ------------------------------------------------- 2. Finite Automata
S.append({
 "id": "finite", "title": "Finite Automata & Regular Languages", "children": [
  CH("dfa", "DFA, NFA & Equivalence", """
<p>A <b>finite automaton</b> is a 5-tuple (Q, Σ, δ, q0, F): a finite set of states, input alphabet,
transition function, start state, and accepting (final) states. It accepts a language iff every
accepting computation ends in F.</p>

<table>
<tr><th>Feature</th><th>DFA</th><th>NFA</th></tr>
<tr><td>Move on a symbol</td><td>exactly one state</td><td>0, 1 or many states</td></tr>
<tr><td>ε-transitions</td><td>not allowed</td><td>allowed</td></tr>
<tr><td>Implementation</td><td>direct hardware</td><td>requires backtracking/subset</td></tr>
<tr><td>States to convert</td><td>—</td><td>up to 2<sup>n</sup> states as a DFA</td></tr>
<tr><td>Language power</td><td colspan="2"><b>identical</b> — every NFA has an equivalent DFA</td></tr>
</table>

<div class="box formula"><div class="lbl">Subset construction (NFA → DFA)</div>
Each DFA state is a <b>set of NFA states</b>: start = ε-closure(q0). On symbol a, move =
ε-closure(∪ of all NFA states reachable from the current set on a). A DFA state is <b>accepting</b>
if it contains any NFA accepting state. Worst case 2<sup>n</sup> DFA states, but it proves
<b>DFA = NFA = ε-NFA</b> in power (all = regular languages).
</div>

<details><summary>Worked example — ε-NFA → DFA via subset construction</summary>
<div class="dc">
<p>ε-NFA with states {1,2}, start 1, F={2} (state 1 not accepting), transitions:
δ(1,ε)={2}, δ(2,a)={2}, δ(2,b)={1}.</p>
<p>Start state A = ε-closure(1) = {1,2} (1 goes to 2 by ε). Contains F ⇒ <b>A is accepting</b>.</p>
<p>From A on a: all states reachable = δ(2,a)={2}, plus no ε further ⇒ {2} = B (accepting, contains 2).<br>
From A on b: δ(2,b)={1}, ε-closure(1)={1,2} ⇒ back to A.</p>
<p>From B on a: δ(2,a)={2} ⇒ B. From B on b: δ(2,b)={1} ⇒ A.</p>
<p>Result: DFA with start A, accepting {A,B}, δ(A,a)=B, δ(A,b)=A, δ(B,a)=B, δ(B,b)=A —
a 2-state DFA equivalent to the given ε-NFA.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
The subset construction can require <b>exponentially more</b> states (2<sup>n</sup>) — for example an n-state NFA
for the language of strings whose k<sup>th</sup>-from-last symbol is 1 needs a 2<sup>n</sup>-state DFA.
DFA and NFA have <i>equal power</i> but <i>different size</i> — a guaranteed one-word trap.
</div>
"""),
  CH("dfamin", "DFA Minimisation & Myhill–Nerode", """
<p>Every regular language has a <b>unique minimal DFA</b> (up to renaming states). Minimise by
merging <b>indistinguishable</b> states — two states are distinguishable if a string takes exactly one
of them to an accepting state.</p>

<h4>Table-filling algorithm</h4>
<ol>
<li>Mark every pair (p, q) where p ∈ F, q ∉ F as <b>distinguishable</b>.</li>
<li>For each unmarked pair, if δ(p,a), δ(q,a) are distinguishable for some a, mark (p,q) distinguishable.</li>
<li>Repeat until nothing changes; the remaining unmarked pairs are merged.</li>
</ol>

<details><summary>Worked example — minimise the DFA with states {A,B,C,D}, F={C}, transitions: δ(A,a)=B, δ(A,b)=C, δ(B,a)=D, δ(B,b)=D, δ(C,a)=C, δ(C,b)=C, δ(D,a)=D, δ(D,b)=D</summary>
<div class="dc">
<p>Distinguishable pairs first: C vs {A,B,D} (C accepting, others not).</p>
<p>(A,B): A-on-a=B, B-on-a=D (unmarked); A-on-b=C, B-on-b=D. C distinguishable from D ⇒ mark (A,B).</p>
<p>(A,D): A-on-a=B (B vs D — B not yet distinguishable from D); A-on-b=C ⇒ C vs D distinguishable, so δ(A,b)=C and δ(D,b)=D are distinguishable ⇒ mark (A,D).</p>
<p>(B,D): B-on-a=D, D-on-a=D; B-on-b=D, D-on-b=D ⇏ distinguishable ⇒ (B,D) stay <b>unmarked</b>.</p>
<p>So only B, D merge. Minimal DFA has 3 states: {A}, {B,D}, {C}.</p>
</div></details>

<div class="box formula"><div class="lbl">Myhill–Nerode theorem</div>
A language L is regular iff the number of <b>equivalence classes of its right-invariant
indistinguishability relation</b> is finite; that count equals the number of states in the minimal DFA.
Two strings x, y are equivalent iff for every suffix z, xz ∈ L ⇔ yz ∈ L.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
You can prove a language is <b>regular</b> by constructing a DFA/NFA/regex (existence is enough —
you need not find the smallest one). You can prove it is <b>non-regular</b> only by the pumping lemma
or Myhill–Nerode. Do not "prove non-regular" by saying a DFA "would be complicated" — that is not a proof.
</div>
""")]})

# ------------------------------------------------- 3. Regular Expressions
S.append({
 "id": "regex", "title": "Regular Expressions & Their Languages", "children": [
  CH("regexrep", "Regex ⇔ Finite Automata", """
<p>Every regular expression stands for a regular language, and vice versa. The three operations are
<b>union (|)</b>, <b>concatenation (.)</b> and <b>Kleene star (*)</b>. Order of precedence for reading:
star &gt; concatenation &gt; union.</p>

<div class="box formula"><div class="lbl">Notation cheat-sheet</div>
a<sup>+</sup> = a·a<sup>*</sup> (one or more) &nbsp;·&nbsp; a<sup>n</sup> = a repeated n times (n ≥ 0)<br>
(a|b) = either a or b &nbsp;·&nbsp; ε = empty string &nbsp;·&nbsp; ∅ = empty language<br>
(a*)* = a* &nbsp;·&nbsp; a<sup>+</sup> ≡ a·a<sup>*</sup> (not a new operator, just shorthand)<br>
If r<sub>1</sub>, r<sub>2</sub> are regular, then r<sub>1</sub>|r<sub>2</sub>, r<sub>1</sub>r<sub>2</sub>, r<sub>1</sub><sup>*</sup> are regular.
</div>

<p>To build a <b>NFA from a regex</b>: every symbol and ε becomes a small automaton, and union/star/concatenation
are glued with ε-transitions (Thompson's construction). To go the other way, use the state-elimination method.</p>

<details><summary>Worked example — language of (0|1)*010</summary>
<div class="dc">
<p>(0|1)* generates any binary string; *010 appends the ending "010".</p>
<p>So L = <b>all binary strings ending in 010</b>. Strings "010", "1010", "00010" are in L; "110" is not.</p>
<p>A 4-state DFA accepting exactly L: start s0; track the last 3 bits; only the state reached after reading
0→1→0 is accepting. This is the classic "ends-in-010" minimal DFA.</p>
</div></details>

<div class="box formula"><div class="lbl">Regular-language algebraic identities</div>
(r|∅) = r &nbsp;·&nbsp; (r·ε) = r &nbsp;·&nbsp; ∅<sup>*</sup> = ε &nbsp;·&nbsp; ε<sup>*</sup> = ε<br>
r(s|t) = rs|rt (left distributivity only) &nbsp;·&nbsp; (r<sup>*</sup>)<sup>*</sup> = r<sup>*</sup> &nbsp;·&nbsp; (r<sup>*</sup>s<sup>*</sup>)<sup>*</sup> = (r|s)<sup>*</sup>
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
<b>NOT all "regular-looking" patterns are regular expressions.</b> Backreferences, nesting/balanced
parentheses, and counting (exactly equal numbers of a and b) are NOT regular. If a description requires
an infinite counter or arbitrary nesting, it is beyond regular regardless of how it is phrased.
</div>
""")]})

# ------------------------------------------------- 4. Closure & Pumping (Regular)
S.append({
 "id": "regprop", "title": "Closure Properties & Pumping Lemma (Regular)", "children": [
  CH("closure", "Closure Properties of Regular Languages", """
<p>Regular languages are closed under almost <b>every</b> operation you are likely to be asked about —
union, intersection, and complement added together make them a <b>Boolean algebra</b> of languages.</p>

<table>
<tr><th>Operation</th><th>Regular closed?</th><th>Why / idea</th></tr>
<tr><td>Union A ∪ B</td><td><b>Yes</b></td><td>DFA product / a fresh start with |</td></tr>
<tr><td>Intersection A ∩ B</td><td><b>Yes</b></td><td>Product automaton (pair of states)</td></tr>
<tr><td>Complement ¬A</td><td><b>Yes</b></td><td>Swap accepting/non-accepting states of a DFA</td></tr>
<tr><td>Concatenation AB</td><td><b>Yes</b></td><td>ε-link, or NFA</td></tr>
<tr><td>Kleene star A*</td><td><b>Yes</b></td><td>NFA</td></tr>
<tr><td>Reversal A<sup>R</sup></td><td><b>Yes</b></td><td>Reverse arrows, swap start/final</td></tr>
<tr><td>Homomorphism h(A)</td><td><b>Yes</b></td><td>Replace each symbol</td></tr>
<tr><td>Inverse homomorphism h<sup>−1</sup>(A)</td><td><b>Yes</b></td><td>Simulate on DFA</td></tr>
<tr><td>Quotient (right/left)</td><td><b>Yes</b></td><td>Pumping-length bound on states</td></tr>
</table>

<div class="box trap"><div class="lbl">GATE trap</div>
Because regular languages are closed under complement <b>and</b> intersection, the two classic
{"not closed"} answers — intersection and complement — are <b>wrong for regular</b>. Both are handled
by the product construction. Contrast with CFLs (below), where intersection and complement genuinely fail.
</div>
"""),
  CH("pumping", "Pumping Lemma & Proving Non-Regularity", """
<div class="box formula"><div class="lbl">Pumping lemma for regular languages</div>
If L is regular, there exists a constant p (the <b>pumping length</b>) such that every string
w ∈ L with |w| ≥ p can be written w = xyz where:<br>
<ol>
<li>|xy| ≤ p (and |y| ≥ 1),</li>
<li>xy<sup>k</sup>z ∈ L for <b>all</b> k ≥ 0.</li>
</ol>
Intuition: a p-state DFA revisits a state as it reads p symbols, so the loop y can be repeated or removed.
</div>

<h4>Standard proof recipe (contrapositive)</h4>
<ol>
<li>Assume L is regular; let p be its pumping length.</li>
<li>Pick a specific w ∈ L with |w| ≥ p (choose it so the argument runs through).</li>
<li>Because |xy| ≤ p and |xy| ≤ p gives you a constraint on y, show xy<sup>k</sup>z ∉ L for some k.</li>
<li>Conclude L is <b>not</b> regular. (You control w; the variables x, y, z are arbitrary — your case must hold for every possible split.)</li>
</ol>

<details><summary>Worked example — L = {aⁿbⁿ : n ≥ 0} is not regular</summary>
<div class="dc">
<p>Assume regular with pumping length p. Choose w = a<sup>p</sup>b<sup>p</sup>, |w| = 2p ≥ p.</p>
<p>Since |xy| ≤ p and all of a<sup>p</sup>b<sup>p</sup> begins with a's, the substring y consists <b>only of a's</b>:
y = a<sup>m</sup> with 1 ≤ m ≤ p.</p>
<p>Pump k = 0 (remove y): xy<sup>0</sup>z = a<sup>p−m</sup>b<sup>p</sup>. Now there are p−m a's but p b's — not equal ⇒ ∉ L.</p>
<p>This contradicts the pumping lemma ⇒ <b>L is not regular.</b> (Same reasoning kills {ww}, equal-0/equal-1 counts, and {w : |w| = 2ⁿ}.)</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
The pumping lemma is a <b>necessary, not sufficient, condition</b> for regularity. A language can
satisfy the lemma yet still be non-regular (e.g. far-from-regular languages can pump vacuously).
So you may <b>use it to prove non-regularity</b>, never to prove regularity. Also: when chosen,
you may not choose w whose length is < p — the lemma only guarantees a split for strings that are long enough.
</div>
""")]})

# ------------------------------------------------- 5. Context-Free Grammars
S.append({
 "id": "cfg", "title": "Context-Free Grammars", "children": [
  CH("cfgbasic", "CFG, Derivation & Ambiguity", """
<p>A <b>context-free grammar</b> is a 4-tuple (V, T, P, S): variables, terminals, productions, start
symbol. Each production is A → α with a single variable on the left — that single-variable restriction
is exactly what gives the context-free languages their power (beyond regular).</p>

<div class="box formula"><div class="lbl">Grammar for balanced parentheses</div>
S → (S) | SS | ε &nbsp; generates every string of balanced parentheses.<br>
Equivalently S → ε | ( S ) S. The classic <b>ambiguous</b> arithmetic grammar is E → E+E | E×E | (E) | id.
</div>

<h4>Ambiguity</h4>
<p>A grammar is <b>ambiguous</b> if some string in its language has ≥ 2 distinct <b>leftmost derivations</b>
(equivalently ≥ 2 different parse trees). A language is <b>inherently ambiguous</b> if <i>every</i> grammar
for it is ambiguous — the classic example is {a<sup>i</sup>b<sup>j</sup>c<sup>k</sup> : i = j or j = k}.</p>

<details><summary>Worked example — is E → E+E | id ambiguous?</summary>
<div class="dc">
<p>String id+id+id has two different leftmost derivations:</p>
<p>E ⇒ E+E ⇒ id+E ⇒ id+E+E ⇒ id+id+E ⇒ id+id+id<br>
E ⇒ E+E ⇒ E+E+E ⇒ id+id+E ⇒ id+id+id</p>
<p>Same string, two parse trees ⇒ <b>ambiguous</b>. Fix by introducing precedence levels:
E → E+T | T; T → T×F | F; F → (E) | id. That grammar is unambiguous and respects × before +.</p>
</div></details>

<div class="box tip"><div class="lbl">Quick parse-ambiguity shortcut</div>
To decide if a grammar is ambiguous, do NOT enumerate all strings — try the <b>shortest string</b> that can
be reached two ways. For arithmetic, id+id+id and id×id+id are the typical witnesses. For balanced brackets,
the double-nested forms ()(), (()), ()() () are the usual witnesses.
</div>
"""),
  CH("cfgform", "Normal Forms & Simplification", """
<h4>Remove useless &amp; nullable symbols</h4>
<ol>
<li>Delete variables that cannot generate <i>any</i> terminal string (non-productive).</li>
<li>Delete variables unreachable from S.</li>
<li>If A → ε, add all productions with A erased; remove A → ε (unless S → ε).</li>
<li>Remove unit productions A → B by copying B's right-hand sides into A.</li>
</ol>

<div class="box formula"><div class="lbl">Chomsky Normal Form (CNF)</div>
Every CFL (without ε) has a grammar where every production is A → BC or A → a
(two variables, or one terminal). Converting: add new variables for terminals, and replace A → BCD with
A → BC′, C′ → CD … (binary branching). Also, a parse tree in CNF has <b>exactly 2n − 1 internal nodes</b>
(and n leaves) for a string of length n — used in CFL pumping arguments.

<h4>Greibach Normal Form (GNF)</h4>
Every production is A → aB<sub>1</sub>…B<sub>k</sub> (a single terminal first). Any CFL has a GNF grammar
used when building a PDA with a single-pop strategy.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
Removing ε-productions and unit productions <b>changes</b> the grammar, but if the language originally
contained ε, the CNF grammar will produce everything except possibly ε. Do not claim the CNF grammar
generates ε when it can't — a CNF grammar represents L − {ε}. Also "A → ε" removal must not kill strings
that used A as a "skip".
</div>
""")]})

# ------------------------------------------------- 6. Pushdown Automata
S.append({
 "id": "pda", "title": "Pushdown Automata & CFLs", "children": [
  CH("pdamachine", "PDA & its Equivalence with CFG", """
<p>A <b>pushdown automaton</b> (PDA) is an NFA with a <b>stack</b>. Power is identical to CFGs:
<b>CFG ⇔ PDA</b>. The stack gives it unbounded (but restricted) memory, which is why PDAs handle
aⁿbⁿ (needs a counter) but not aⁿbⁿcⁿ (needs two counters / simultaneously tracking both).</p>

<table>
<tr><th>Feature</th><th>NFA/DFA</th><th>PDA</th></tr>
<tr><td>Memory</td><td>none (just state)</td><td>one stack</td></tr>
<tr><td>Languages</td><td>regular</td><td>context-free</td></tr>
<tr><td>Non-determinism</td><td>can be removed (subset)</td><td><b>cannot always be removed</b> (NPDAs > DPDAs)</td></tr>
<tr><td>Membership check</td><td>O(n)</td><td>O(n³) (CYK)</td></tr>
</table>

<p><b>Deterministic PDAs (DPDAs)</b> are a proper subclass — they see a real (though far less important
in GATE) distinction: DPDA languages are closed under complement, and DPDAs accept exactly the
<i>LR(k)</i> languages (the parser-friendly ones). Some CFLs (e.g. even-length palindromes ww<sup>R</sup>)
need non-determinism to guess the middle.</p>

<details><summary>Worked example — PDA for {aⁿbⁿ : n ≥ 1}</summary>
<div class="dc">
<p>Idea: push one X per 'a', then pop one X per 'b'; accept when stack is empty exactly at end.</p>
<p>Transitions (reading left to right, Z0 = bottom marker):<br>
δ(q0, a, Z0) = (q0, XZ0) — first a pushes a guard then X.<br>
δ(q0, a, X) = (q0, XX) — push X per a.<br>
δ(q0, b, X) = (q1, ε) — first b moves to popping state.<br>
δ(q1, b, X) = (q1, ε) — pop X per b.<br>
δ(q1, ε, Z0) = (qf, ε) — accept only when stack returns to Z0 with no input left.</p>
<p>Because each 'a' pushes exactly one X and each 'b' pops exactly one X, acceptance happens iff the counts
are equal and the input is exactly a* b* ⇒ language is aⁿbⁿ. Non-determinism is not even needed here.</p>
</div></details>

<div class="box tip"><div class="lbl">Building PDAs fast</div>
Ask "what must be remembered?" If a single counter suffices, use the stack like a counter (push on one symbol,
pop on the other). If you must guess a split or a middle point, use <b>non-determinism</b> and switch state at
the guess. If two independent counters are needed (aⁿbⁿcⁿ), no PDA exists.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
A PDA accepting by <b>final state</b> and one accepting by <b>empty stack</b> are equivalent in power —
but a single PDA may not accept by both conventions for the same language. Also, emptiness of a CFL is
<b>decidable</b> (contrast with TMs), and there is an O(n³) CYK membership algorithm for CFL strings.
</div>
""")]})

# ------------------------------------------------- 7. Context-Free Languages
S.append({
 "id": "cfl", "title": "Context-Free Languages: Closure & Pumping", "children": [
  CH("cflclosure", "Closure Properties of CFLs", """
<table>
<tr><th>Operation</th><th>CFL closed?</th><th>Reason / counter-example</th></tr>
<tr><td>Union</td><td><b>Yes</b></td><td>fresh start S → S₁ | S₂</td></tr>
<tr><td>Concatenation</td><td><b>Yes</b></td><td>S → S₁ S₂</td></tr>
<tr><td>Kleene star</td><td><b>Yes</b></td><td>S → S₁ S | ε</td></tr>
<tr><td>Reversal</td><td><b>Yes</b></td><td>reverse every production's RHS</td></tr>
<tr><td>Homomorphism</td><td><b>Yes</b></td><td>replace terminals</td></tr>
<tr><td>Intersection with a regular language</td><td><b>Yes</b></td><td>PDA × DFA product construction</td></tr>
<tr><td><b>Intersection (CFL ∩ CFL)</b></td><td><b>No</b></td><td>aⁿbⁿcⁿ = {aⁿbⁿc* } ∩ {a*bⁿcⁿ}</td></tr>
<tr><td><b>Complement</b></td><td><b>No</b></td><td>would imply closed under intersection via De Morgan</td></tr>
</table>

<div class="box trap"><div class="lbl">GATE trap</div>
CFLs are closed under union but <b>not</b> intersection or complement — the exact opposite emphasis from
regular languages. The standard counter-example: L₁ = {aⁿbⁿc<sup>m</sup>}, L₂ = {a<sup>m</sup>bⁿcⁿ} are each
context-free, but their intersection {aⁿbⁿcⁿ} is <b>not</b> context-free. This single fact is asked almost every year.
</div>
"""),
  CH("cflpump", "Pumping Lemma for CFLs", """
<div class="box formula"><div class="lbl">Pumping lemma for context-free languages</div>
If L is a CFL, ∃p such that every w ∈ L with |w| ≥ p can be split w = uvxyz where:<br>
<ol>
<li>|vxy| ≤ p and |vy| ≥ 1 (the pumped pair),</li>
<li>uv<sup>k</sup>xy<sup>k</sup>z ∈ L for <b>all</b> k ≥ 0.</li>
</ol>
Intuition: in a CNF parse tree with &gt; 2<sup>p</sup> leaves, some non-terminal repeats on a path, giving two
pumpable subtrees v and y.
</div>

<details><summary>Worked example — L = {aⁿbⁿcⁿ : n ≥ 0} is not context-free</summary>
<div class="dc">
<p>Assume CFL, pumping length p, choose w = a<sup>p</sup>b<sup>p</sup>c<sup>p</sup> (length 3p ≥ p).</p>
<p>Because |vxy| ≤ p, the sub-string vxy spans at most <b>two</b> of the three blocks of letters. That is the key:
it cannot contain a, b AND c together.</p>
<p>Now uv<sup>2</sup>xy<sup>2</sup>z adds copies of v and y. But these copies only touch a and b (or b and c, or a and the
end), so after pumping the string has unequal numbers of a, b, c ⇒ ∉ L.</p>
<p>Contradiction ⇒ <b>aⁿbⁿcⁿ is not context-free.</b> (It is context-sensitive.)</p>
</div></details>

<h4>Decision problems for CFLs</h4>
<p>Membership (given a string, is it generated) — <b>decidable</b>, O(n³) via CYK.<br>
Emptiness (does it generate any string) — <b>decidable</b>.<br>
Finiteness — <b>decidable</b>.<br>
Equivalence of two CFGs — <b>undecidable</b>. Ambiguity of a CFG — <b>undecidable</b>.</p>

<div class="box trap"><div class="lbl">GATE trap</div>
For the CFL pumping lemma choose w so that <b>vxy spans at most two symbol-blocks</b> — that is the whole trick
for aⁿbⁿcⁿ-type languages. Beginners waste p on the wrong length or pick w that lets vxy contain all three letters.
Also note "is {aⁿbⁿcⁿ} regular?" is trivially NO — it is not even context-free.
</div>
""")]})

# ------------------------------------------------- 8. Turing Machines
S.append({
 "id": "turing", "title": "Turing Machines & Recursively Enumerable Languages", "children": [
  CH("tmbasic", "Turing Machine Model", """
<p>A <b>Turing machine</b> is a DFA with an infinite tape and the ability to <b>read and write</b> on it and
<b>move</b> left/right. Acceptance is by entering a final state; the machine can also halt (and therefore loop forever).</p>

<div class="box formula"><div class="lbl">Church–Turing thesis</div>
Everything computationally possible (algorithmically computable by any reasonable model) is computable by a
Turing machine. All reasonable models — TM, RAM, λ-calculus, Turing-equivalent formalisms — are equivalent in
computational power.
</div>

<table>
<tr><th>Variant</th><th>Equivalence to standard TM</th></tr>
<tr><td>Multi-tape TM</td><td>Equivalent (simulated with a work tape encoding all tapes)</td></tr>
<tr><td>Non-deterministic TM</td><td>Equivalent (systematic simulation / BFS on computation tree)</td></tr>
<tr><td>Two-way infinite tape</td><td>Equivalent</td></tr>
<tr><td>Multidimensional / random-access TM</td><td>Equivalent</td></tr>
<tr><td>Universal TM</td><td>A TM that takes ⟨M, w⟩ and simulates M on w — a program you can run</td></tr>
</table>

<div class="box trap"><div class="lbl">GATE trap</div>
Non-deterministic TMs are <b>equivalent</b> to deterministic ones (unlike PDAs)! This exponential-simulation
gap is only about <i>speed</i>, not accept power — a guaranteed one-liner fact. TM variants do NOT extend the
set of accepted languages.
</div>
"""),
  CH("tmlangs", "Language Classes & Simple Problems", """
<h4>Decidable (recursive)</h4>
<p>A language is <b>decidable</b> (recursive) if some TM always <b>halts</b> with the right answer (accept/reject).
Its complement is also decidable. Membership, emptiness and equivalence for <b>regular languages</b>, and
membership/emptiness for <b>CFLs</b>, are all decidable because small dedicated automata/parsers decide them.</p>

<h4>Semi-decidable (recursively enumerable)</h4>
<p>A language is <b>recursively enumerable (RE)</b> if some TM accepts every string in L (it may loop on strings
not in L). A TM can accept a string in L but can loop forever on a non-L string; "can a decider exist" is the sharp line.</p>

<div class="box formula"><div class="lbl">Key vocabulary to memorise</div>
<b>Recursive</b> = TM always halts and decides. <b>RE</b> = TM accepts members (may loop on others).<br>
<b>co-RE</b> = complement is RE. <b>Recursive ⇔ recursive ∩ co-recursively-enumerable</b>
(i.e. L and its complement both RE ⇔ L decidable).<br>
A language that is RE but not recursive (e.g. the Halting problem) has a <b>non-RE complement</b>.
</div>

<details><summary>Worked example — is the language of encodings of strings with an even number of 0s decidable?</summary>
<div class="dc">
<p>Yes. This is a regular language — build a 2-state DFA (parity of 0s). Every regular language is decidable</b>,
so there is a TM that halts.</p>
<p>Implication chain to keep straight: Regular ⊆ Context-Free ⊆ Decidable ⊆ Recursively-Enumerable ⊆ All languages
(the complement of RE). Every regular and every CFL membership test terminates.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
<b>A decidable language is RE, but an RE language need not be decidable.</b> If a language and its complement
are both RE, the language is <i>decidable</i>; if L is RE but its complement is NOT RE, L is undecidable and
not recursive (this is exactly the Halting problem). Getting this subset chain direction wrong is the #1 TOC trap.
</div>
""")]})

# ------------------------------------------------- 9. Decidability & Undecidability
S.append({
 "id": "undec", "title": "Undecidability, Rice's Theorem & Reductions", "children": [
  CH("atileasyd", "Which Problems Are Decidable?", """
<table>
<tr><th>Problem</th><th>Domain</th><th>Status</th></tr>
<tr><td>Membership w ∈ L(M)</td><td>DFA / regular</td><td><b>Decidable</b></td></tr>
<tr><td>Emptiness of L(M)</td><td>DFA / regular</td><td><b>Decidable</b></td></tr>
<tr><td>Equivalence of two automata</td><td>DFA / regular</td><td><b>Decidable</b></td></tr>
<tr><td>Membership of a string in a CFG</td><td>CFL</td><td><b>Decidable</b> (CYK, O(n³))</td></tr>
<tr><td>Emptiness of a CFL</td><td>CFL</td><td><b>Decidable</b></td></tr>
<tr><td>Equivalence of two CFGs</td><td>CFL</td><td><b>Undecidable</b></td></tr>
<tr><td>Ambiguity of a CFG</td><td>CFL</td><td><b>Undecidable</b></td></tr>
<tr><td>Membership A_TM = {⟨M,w⟩ : M accepts w}</td><td>TM</td><td><b>Undecidable</b> (and RE, not recursive)</td></tr>
<tr><td>Halting problem HALT_TM</td><td>TM</td><td><b>Undecidable</b> (and RE, not recursive)</td></tr>
<tr><td>Does TM accept the empty language? E_TM</td><td>TM</td><td><b>Undecidable</b></td></tr>
<tr><td>Equivalence/regularity of a TM's language</td><td>TM</td><td><b>Undecidable</b> (Rice)</td></tr>
</table>

<div class="box trap"><div class="lbl">GATE trap</div>
The switch between decidable and undecidable happens exactly at the boundary from automata/simple PDAs to general
TMs. "Emptiness of a DFA" and "emptiness of a PDA/CFG" are decidable; "does this <b>TM</b> accept anything?" (E_TM)
is undecidable. Do not transfer a decidable result from finite automata to arbitrary TMs.
</div>
"""),
  CH("rice", "Rice's Theorem", """
<div class="box formula"><div class="lbl">Rice's theorem</div>
Any <b>non-trivial property of the language</b> recognised by a Turing machine is <b>undecidable</b>.
"Non-trivial" = some TM has it and some TM doesn't. (The property must depend only on the <i>language</i>,
not on the machine.)<br>
Consequences — all <b>undecidable</b>: does a TM accept a given string? the empty language? a regular language?
a finite language? two strings? Conversely, properties of the <i>machine</i> itself (e.g. "does this TM have 5
states?") are <b>not</b> language properties — they may be decidable.
</div>

<div class="box tip"><div class="lbl">Applying Rice in 5 seconds</div>
Ask: (1) is the property a property of the <b>language</b>? (2) do <b>some</b> TMs satisfy it and <b>some</b> not?
If both yes ⇒ <b>undecidable</b>. If it talks about the machine's internal details (number of states, start state
name, whether it has a specific transition) ⇒ Rice does <b>not</b> apply.
</div>

<details><summary>Worked example — is "does TM M accept exactly the language a*?" decidable?</summary>
<div class="dc">
<p>Property of the language accepted by M (it depends only on L(M) = a*). It is non-trivial: one TM accepting
a* exists (a single-loop machine), and another TM accepting something else exists. So by Rice's theorem this is
<b>undecidable</b>. Same conclusion for "accepts a regular language", "accepts a finite language", "accepts a string
of length 2", etc.
</p></div></details>
"""),
  CH("reductions", "Reductions & Proving Undecidability", """
<p>If language A reduces to B (A ≤ B), then a decider for B would give a decider for A. Contrapositive:
if A is <b>known undecidable and A ≤ B, then B is undecidable</b>. The standard source problem is the Halting
problem; you show a new problem is undecidable by building a reduction <b>from</b> a known undecidable problem
<b>to</b> it.</p>

<div class="box formula"><div class="lbl">Halting problem</div>
HALT_TM = {⟨M, w⟩ : TM M halts on input w} is <b>undecidable</b>. The canonical diagonal argument: assume a decider H
exists; build D that runs H on ⟨D, D⟩; whichever D does, it contradicts what H "predicted". The membership
problem A_TM = {⟨M,w⟩ : M accepts w} is likewise undecidable, and both are RE but not recursive.
</div>

<details><summary>Worked example — reducing HALT to the "accepts empty language" problem</summary>
<div class="dc">
<p>To show E_TM = {⟨M⟩ : L(M) = ∅} is undecidable, assume decider E for E_TM. From any ⟨M,w⟩ build a machine
M′ that ignores its own input, runs M on w, and accepts if M accepts w; M′ accepts e.g. "1" iff M accepts w,
otherwise accepts nothing.</p>
<p>Then E(M′) returns YES ⇔ L(M′) = ∅ ⇔ M rejects/loops on w. But deciding "does M halt/accept w" is the Halting
problem, which we know is undecidable ⇒ contradiction ⇒ E_TM is undecidable. Reductions work <i>from</i> a known
hard problem <i>to</i> the target.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
The direction of the reduction matters. To prove B undecidable you reduce a <b>known-undecidable A to B</b>
(A ≤ B). Reducing an easy problem to B proves nothing. Also, a reduction from a decidable problem gives no
conclusion about B; and you may only conclude <b>undecidability</b>, not "non-RE", from a plain Rice-style argument
(Rice shows non-decidability; Rice's <i>extended</i> version handles RE/non-RE with monotonicity).
</div>
""")]})

# ------------------------------------------------- 10. Chomsky Hierarchy
S.append({
 "id": "chomsky", "title": "Chomsky Hierarchy of Languages", "html": """
<table>
<tr><th>Type</th><th>Grammar</th><th>Recogniser</th><th>Example language</th></tr>
<tr><td>Type 3</td><td>Regular (right/left-linear)</td><td>DFA/NFA</td><td>0*1(0|1)* — ending in 1</td></tr>
<tr><td>Type 2</td><td>Context-free (A → α)</td><td>PDA</td><td>aⁿbⁿ — equal counts</td></tr>
<tr><td>Type 1</td><td>Context-sensitive (αAβ → αγβ)</td><td>Linear-bounded automaton</td><td>aⁿbⁿcⁿ, a²ⁿ</td></tr>
<tr><td>Type 0</td><td>Unrestricted / phrase-structure</td><td>Turing machine</td><td>Halting problem complements</td></tr>
</table>
<p>The hierarchy is <b>strictly nested</b>: Regular ⊂ Context-Free ⊂ Context-Sensitive ⊂ Recursively Enumerable ⊂ all
languages. Every regular language is context-free; every context-free language is context-sensitive; every
context-sensitive language is decidable; every decidable is RE.</p>

<div class="box formula"><div class="lbl">Membership note by level</div>
Regular: O(n) scanning. Context-free: O(n³) CYK. Context-sensitive: membership is <b>decidable</b> but may be
exponential. Type-0 (unrestricted): membership is <b>undecidable in general</b>.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
The nesting direction is the trap: aⁿbⁿcⁿ is Type-1 (context-sensitive), <b>not</b> Type-2. And every
regular-language recogniser (DFA/NFA) sits strictly inside the PDA recogniser class, not the reverse.
{{a, b} with equal counts of a and b with order preserved} is Type-2.
</div>
"""
})

# ------------------------------------------------- 11. Formula sheet
S.append({
 "id": "formulas", "title": "One-Page Formula Sheet (Revise Before Exam)", "html": """
<table>
<tr><th>Fact</th><th>Statement</th></tr>
<tr><td>DFA = NFA = ε-NFA</td><td>equal accept power; subset construction, up to 2<sup>n</sup> DFA states</td></tr>
<tr><td>Regular closed under</td><td>∪ , ∩ , complement , · , * , reversal , h , h<sup>−1</sup></td></tr>
<tr><td>Regular equals</td><td>Regex ⇔ DFA/NFA (exactly the regular languages)</td></tr>
<tr><td>Pumping lemma (regular)</td><td>w = xyz , |xy| ≤ p , |y| ≥ 1 , xy<sup>k</sup>z ∈ L ∀k</td></tr>
<tr><td>CFL closed under</td><td>∪ , · , * , reversal , homomorphism , ∩ regular</td></tr>
<tr><td>CFL NOT closed under</td><td>∩ , complement</td></tr>
<tr><td>CFG ⇔ PDA</td><td>equivalent; even-length palindromes need NPDA (NPDA ⊋ DPDA)</td></tr>
<tr><td>CNF parse tree</td><td>2n − 1 internal nodes for length-n string</td></tr>
<tr><td>Pumping lemma (CFL)</td><td>w = uvxyz , |vxy| ≤ p , |vy| ≥ 1 , uv<sup>k</sup>xy<sup>k</sup>z ∈ L ∀k</td></tr>
<tr><td>aⁿbⁿ</td><td>type-2 (CFL). aⁿbⁿcⁿ → type-1. ww → type-1. ww<sup>R</sup> → type-2.</td></tr>
<tr><td>TM variants</td><td>all equivalent (multi-tape, NTM, 2-way, universal)</td></tr>
<tr><td>Decidable problems</td><td>membership/emptiness/equivalence for regular; CFL membership &amp; emptiness</td></tr>
<tr><td>Undecidable</td><td>CFG equivalence &amp; ambiguity; A_TM ; HALT ; E_TM ; any Rice property</td></tr>
<tr><td>Rice's theorem</td><td>non-trivial property of L(M) is undecidable</td></tr>
<tr><td>Halting problem</td><td>RE but not recursive; complement is not RE</td></tr>
<tr><td>Hierarchy</td><td>Regular ⊂ CFL ⊂ CSL ⊂ RE ⊂ all</td></tr>
<tr><td>L decidable ⇔</td><td>L RE and L<sup>c</sup> RE</td></tr>
</table>
<div class="box tip"><div class="lbl">Final-hour drill</div>
Re-derive aⁿbⁿ (PDA) and aⁿbⁿcⁿ (pumping) once each, re-read the decidability table, and confirm you know which
direction each implication in the hierarchy runs (Regular ⊂ CFL ⊂ …). Those three drills cover the majority of the
marks in under 20 minutes.
</div>
"""
})

# ------------------------------------------------- 12. Exam strategy
S.append({
 "id": "strategy", "title": "Exam Strategy for Theory of Computation", "html": """
<div class="box"><div class="lbl">How to attempt TOC in the exam</div>
<ol>
<li><b>Do the true/false and closure questions first</b> — they are the fastest accuracy. Read each statement
carefully for reversal words: "all regular are CF" (true) vs "all CF are regular" (false).</li>
<li><b>Construction questions second</b> (build a DFA/PDA/regex or minimise). If a construction gets messy,
you likely took a wrong model — re-check whether the language is actually regular/CF.</li>
<li><b>Pumping-lemma proofs third</b>. Always pick w that lets you pin down y (ends: "because |xy| ≤ p, y is all
a's" style). Choose the witness w so the argument closes cleanly.</li>
<li><b>Undecidability last (if time allows)</b>. Rice's theorem + the recogniser classes answer 90% of these —
know {regular, CFL, decidable, RE} membership for a handful of canonical problems and apply it rather than
reasoning from scratch.</li>
</ol>
</div>
<div class="box trap"><div class="lbl">Time sinks to avoid</div>
Do NOT spend minutes trying to disprove a Rice-property question with a construction — Rice says it is undecidable
immediately. Do NOT re-minimise by hand when you can table-fill. For pumping-lemma proofs, do NOT write a generic
paragraph; pin down exactly where y lives. If a closure question is about ∩ or complement of CFLs, the classic
aⁿbⁿcⁿ counter-example usually settles it — memorise it.
</div>
<div class="box tip"><div class="lbl">What to skip under pressure</div>
If you are short on time, skip long construction or pumping proofs in favour of the quick membership/closure
true-false items, which give the best time-to-marks ratio. A blank construction is 0; a correct closure-class
answer is a reliable +1 or +2.
</div>
"""
})

QUIZ = [
 {"q":"Which of the following is NOT a regular language?","opts":["0*1(0|1)*","word ending in \"010\"","{0ⁿ1ⁿ : n ≥ 0}","(0|1)(0|1)*"],"a":2,
  "ex":"{0ⁿ1ⁿ} needs a counter for n, impossible for a finite automaton. The other three are regular (star/union/regex constructions)."},
 {"q":"Every NFA with n states can be converted to an equivalent DFA with at most:","opts":["n states","n² states","2ⁿ states","n! states"],"a":2,
  "ex":"Subset construction maps each DFA state to a set of NFA states, so at most 2ⁿ (usually fewer)."},
 {"q":"Regular languages are closed under:","opts":["intersection but not complement","complement but not intersection","union, intersection and complement","neither union nor complement"],"a":2,
  "ex":"Product automaton handles intersection; swapping accepting states handles complement; union via a fresh NFA start. All three are regular."},
 {"q":"The empty set language is regular. Its Kleene star ∅* equals:","opts":["∅","ε (the language {ε})","the set of all strings","{0}"],"a":1,
  "ex":"∅* = ε by definition of the Kleene star on the empty set — a key algebraic identity."},
 {"q":"Which language is context-free but NOT regular?","opts":["{0ⁿ1ⁿ}","{0ⁿ1ⁿ2ⁿ}","{ww}","{w : number of 0s is even}"],"a":0,
  "ex":"{0ⁿ1ⁿ} is generated by S → 0S1 | ε; it needs a counter so it is not regular. The other three fail at type-2 or are regular."},
 {"q":"A PDA and a CFG are related how?","opts":["PDAs accept strictly more languages","CFGs generate strictly more languages","they accept exactly the same (context-free) languages","they are unrelated"],"a":2,
  "ex":"CFG ⇔ PDA — every context-free language has a PDA and vice versa."},
 {"q":"{aⁿbⁿcⁿ : n ≥ 1} is:","opts":["regular","context-free","context-sensitive (not CF)","recursively enumerable only"],"a":2,
  "ex":"It needs two independent counts, beyond any PDA; it is context-sensitive (type-1)."},
 {"q":"Which statement is TRUE?","opts":["Every context-free language is regular","Every regular language is context-free","No context-free language is regular","Context-free ⊂ regular"],"a":1,
  "ex":"Regular ⊆ Context-free (each DFA can be written as a CFG); the inclusion is strict, so the other options invert or deny nesting."},
 {"q":"The pumping lemma for regular languages states there exists p such that for all w with |w| ≥ p:","opts":["w = xyz with |xy| ≤ p, |y| ≥ 1, xyᵏz ∈ L for all k","w = xyz with |yz| ≤ p","w is always accepted","w = uvxyz with |vy| ≥ 1"],"a":0,
  "ex":"The regular-pumping split is xyz with |xy| ≤ p, |y| ≥ 1 and xyᵏz ∈ L. The uvxyz form belongs to CFL pumping."},
 {"q":"Which closure property is FALSE for context-free languages?","opts":["union","concatenation","intersection","Kleene star"],"a":2,
  "ex":"CFLs are closed under union, concatenation and star, but NOT under intersection or complement."},
 {"q":"The language {w w : w ∈ {0,1}*} is:","opts":["regular","context-free","context-sensitive (not CF)","decidable and context-free"],"a":2,
  "ex":"{ww} requires matching a stored copy against the tail with no marker — beyond CFG/PDA power; it is context-sensitive."},
 {"q":"A non-deterministic Turing machine, compared to a deterministic one, accepts:","opts":["strictly more languages","strictly fewer languages","exactly the same languages","only regular languages"],"a":2,
  "ex":"Nondeterministic and deterministic TMs are equivalent in accepted-language power (though a deterministic simulation can be exponentially slower)."},
 {"q":"Which is TRUE about the Halting problem?","opts":["it is decidable and recursive","it is undecidable and RE but not recursive","it is undecidable and not RE","its complement is RE"],"a":1,
  "ex":"HALT is RE (a TM can simulate and report halting) but undecidable; its complement is not RE."},
 {"q":"The membership problem A_TM = {⟨M,w⟩ : M accepts w} is:","opts":["decidable","undecidable and not RE","undecidable but RE","decidable only for finite w"],"a":2,
  "ex":"A_TM is RE (simulate M on w) but undecidable — the canonical diagonalization argument."},
 {"q":"Rice's theorem says:","opts":["every property of TMs is decidable","every non-trivial property of the language accepted by a TM is undecidable","every TM halts","regular languages are undecidable"],"a":1,
  "ex":"Rice: any non-trivial property that depends only on the language L(M) is undecidable. Machine-internal properties are outside its scope."},
 {"q":"Which problem is DECIDABLE?","opts":["ambiguity of a context-free grammar","equivalence of two CFGs","does a TM accept the empty string? (E_TM)","emptiness of a context-free language"],"a":3,
  "ex":"Emptiness of a CFL is decidable (via reachability of productive symbols). CFG ambiguity, CFG equivalence and E_TM are all undecidable."},
 {"q":"Which is the correct subset relationship?","opts":["CFL ⊆ Regular","Regular ⊆ CFL","CSL ⊆ CFL","RE ⊆ Decidable"],"a":1,
  "ex":"Regular ⊂ CFL ⊂ CSL ⊂ Decidable ⊂ RE. The inclusion CFL ⊆ Regular is backwards, and the hierarchy is strictly nested upward."},
 {"q":"To construct the minimal DFA, a machine must:","opts":["merge indistinguishable (equivalent) states","add states for ε-transitions","duplicate accepting states","remove the start state"],"a":0,
  "ex":"Minimisation merges states that are indistinguishable; the result is the unique minimal DFA."},
 {"q":"Two states p (accepting) and q (non-accepting) of a DFA are:","opts":["always equivalent","always distinguishable","equivalent only if p=q","merged directly"],"a":1,
  "ex":"The empty string distinguishes them: ε takes p to accepting but q to non-accepting, so they cannot be merged during minimisation."},
 {"q":"Which problem is UNDECIDABLE?","opts":["membership in a DFA","emptiness of a context-free language","whether a given context-free grammar is ambiguous","membership of a string in a regular language"],"a":2,
  "ex":"Ambiguity of a CFG is undecidable. The other three (DFA membership, CFL emptiness, regular membership) are all decidable."}
]

SUBJECT = {
 "code": "S06", "title": "Theory of Computation",
 "subtitle": "GATE CS 2027 · 8 marks · Finite automata, regex, CFG/PDA, pumping lemma, Turing machines, undecidability",
 "weight_note": "GATE CS 2027 · Theory of Computation section (8 marks)",
 "sections": S, "quiz": QUIZ,
}