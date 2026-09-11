# -*- coding: utf-8 -*-
"""Subject 07 — Compiler Design (6 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

# ---------------------------------------------------------------- 1. Overview
S.append({
 "id": "overview", "title": "Overview & Weightage",
 "html": """
<div class="kv">
  <span class="chip">Marks <b>6 / 100</b></span>
  <span class="chip">Typical Qs <b>3–4</b></span>
  <span class="chip">Sections <b>7</b></span>
  <span class="chip">Scoring <b>Medium–high yield</b></span>
</div>
<p>Compiler Design is compact and <b>algorithmic</b>: most questions reduce to computing FIRST/FOLLOW,
building an LL(1)/LR table, following a data-flow analysis, or tracing a translation scheme. The
syllabus is closed and the tricks repeat every year.</p>
<table>
<tr><th>Topic</th><th>Typical marks</th><th>Difficulty</th><th>Priority</th></tr>
<tr><td>Lexical analysis</td><td>1</td><td>Easy</td><td>★★★★☆</td></tr>
<tr><td>Parsing (top-down, LL(1))</td><td>1.5</td><td>Easy–Medium</td><td>★★★★★</td></tr>
<tr><td>Parsing (bottom-up, LR family, operator precedence)</td><td>1.5</td><td>Medium–Hard</td><td>★★★★★</td></tr>
<tr><td>Syntax-directed translation</td><td>0.5</td><td>Medium</td><td>★★★☆☆</td></tr>
<tr><td>Runtime environments</td><td>0.5</td><td>Easy</td><td>★★★☆☆</td></tr>
<tr><td>Intermediate code + optimisation + data-flow</td><td>1</td><td>Medium–Hard</td><td>★★★★☆</td></tr>
</table>

<div class="box tip"><div class="lbl">Where to spend your hour</div>
Master FIRST/FOLLOW and the LL(1) condition first — they are the single most repeated
two-mark block and gatekeep the LR family. Then memorise the <b>SLR ⊂ LALR ⊂ LR(1)</b> hierarchy
and the classic conflict grammars, because conflict-analysis questions appear almost every year.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
This is a small subject — do <b>not</b> over-invest. Two data-flow questions (liveness + constant
propagation) and one LL(1)/FIRST-FOLLOW question approximate the full mark. Slip past optimisation
and you waste your best 1–2 marks.
</div>
"""
})

# ---------------------------------------------------------------- 2. Lexical
S.append({
 "id": "lexical", "title": "Lexical Analysis", "children": [
  CH("scanner", "Role of the Scanner", """
<p>The <b>lexical analyzer</b> turns the character stream into a stream of <b>tokens</b>
<span class="chip">(lexeme, token-name, attributes)</span> and discards whitespace and comments.</p>
<table>
<tr><th>Token class</th><th>Examples</th></tr>
<tr><td>Keyword</td><td>if, else, while, return</td></tr>
<tr><td>Identifier</td><td>count, x, compute</td></tr>
<tr><td>Operator</td><td>+, * , −, =, &lt;=</td></tr>
<tr><td>Punctuation</td><td>( , ) , ; , { , }</td></tr>
<tr><td>Literal / constant</td><td>42, 3.14, 'a', "hi"</td></tr>
</table>
<p>The scanner is a <b>DFA</b> built from a regular expression. It reports <b>lexical errors</b>
(illegal characters, unterminated strings, invalid numbers).</p>

<div class="box formula"><div class="lbl">Lexical analysis essentials</div>
<ul>
<li>A token = (name, attribute); a <b>pattern</b> = a regular expression describing lexemes.</li>
<li><b>Lexeme</b> = the actual string matched; <b>token</b> = the abstract category.</li>
<li>The scanner implements <b>longest-match</b> and <b>keyword-first</b> (reserved word) rules.</li>
<li>Uses <b>DFA minimisation</b> to reduce states of the recognizer.</li>
</ul>
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
Lexical errors are caught at <b>compilation time</b> (not runtime). Syntax errors are caught by the
parser; semantic errors (type mismatches, undeclared variables) by the semantic analyzer. Students
routinely confuse which phase detects which error class.
</div>
"""),
  CH("regex", "Regular Expressions → DFA", """
<p>Every <b>regular expression</b> corresponds to a DFA/NFA; together they generate exactly the
<b>regular languages</b>. Reserved-word and identifier recognition is done with regexes.</p>
<div class="box formula"><div class="lbl">Regex operators (highest to lowest precedence)</div>
<code>*</code> (Kleene star: zero+), then <b>concatenation</b>, then <code>|</code> (union/alternation).<br>
a* = {ε, a, aa, …} &nbsp;·&nbsp; (a|b) = {a, b} &nbsp;·&nbsp; [a-z] = any letter.<br>
To recognise a keyword "if" that is a substring of "ifx": use the <b>longest-match</b> + keyword-resolution rule.
</div>
<div class="box formula"><div class="lbl">Eliminate left-factoring ambiguity in token rules</div>
Reserved words must be checked <b>before</b> identifier patterns in a DFA, else every identifier
starting with a keyword is mis-tokenised.
</div>
""")]})

# ----------------------------------------------------- 3. Top-down parsing
S.append({
 "id": "topparse", "title": "Parsing — Top-Down (FIRST, FOLLOW, LL(1))", "children": [
  CH("firstfollow", "FIRST & FOLLOW Sets", """
<p>Top-down (predictive, LL(1)) parsing needs, for every choice <code>A → α</code>, to pick the
right production by looking at one input symbol. <b>FIRST</b> and <b>FOLLOW</b> make this precise.</p>

<div class="box formula"><div class="lbl">FIRST(α) — set of first terminals derivable</div>
<ul>
<li>If X is a terminal: FIRST(X) = {X}.</li>
<li>If X → ε: then ε ∈ FIRST(X).</li>
<li>If X → Y<sub>1</sub>…Y<sub>k</sub>: put FIRST(Y<sub>1</sub>) − {ε} in FIRST(X); if Y<sub>1</sub> is
nullable continue to Y<sub>2</sub>; if all are nullable (or k=0), add ε.</li>
<li>For a string α = Y<sub>1</sub>…Y<sub>k</sub>: FIRST(α) = FIRST(Y<sub>1</sub>) − {ε}, plus
FIRST(Y<sub>2</sub>)… while each previous symbol is nullable.</li>
</ul>
</div>

<div class="box formula"><div class="lbl">FOLLOW(A) — set of terminals that may follow A</div>
<ul>
<li>FOLLOW(start-symbol) always contains <b>$</b>.</li>
<li>For A → αBβ: put <b>FIRST(β) − {ε}</b> in FOLLOW(B).</li>
<li>For A → αB (β empty) or αBβ where β is nullable: put <b>FOLLOW(A)</b> in FOLLOW(B).</li>
</ul>
</div>

<div class="box formula"><div class="lbl">LL(1) condition — grammar is LL(1) iff</div>
For every pair of productions A → α | β with FIRST(α), FIRST(β) both non-empty, they must be
<b>disjoint</b>, and if ε ∈ FIRST(α) then <b>FIRST(β) ∩ FOLLOW(A) = ∅</b>.<br>
Left recursion and left factoring are applied to make grammars LL(1)-suitable (after this an ambiguous
grammar is <i>still</i> not LL(1)).
</div>

<details><summary>Worked example — compute FIRST and FOLLOW for E → T E′; E′ → +T E′ | ε; T → F T′; T′ → *F T′ | ε; F → (E) | id</summary>
<div class="dc">
<p><b>Step 1 — FIRST, bottom-up:</b></p>
<table>
<tr><th>Symbol</th><th>FIRST</th><th>Reason</th></tr>
<tr><td>F</td><td>{( , id}</td><td>F → (E) | id</td></tr>
<tr><td>T′</td><td>{*, ε}</td><td>T′ → *F T′ | ε</td></tr>
<tr><td>T</td><td>{( , id}</td><td>= FIRST(F) as T → F T′</td></tr>
<tr><td>E′</td><td>{+, ε}</td><td>E′ → +T E′ | ε</td></tr>
<tr><td>E</td><td>{( , id}</td><td>= FIRST(T) as E → T E′</td></tr>
</table>
<p><b>Step 2 — FOLLOW, top-down, one pass per change:</b></p>
<table>
<tr><th>Symbol</th><th>FOLLOW</th><th>Why</th></tr>
<tr><td>E</td><td>{$, )}</td><td>start ⇒ $; F → (E) ⇒ )</td></tr>
<tr><td>E′</td><td>{$, )}</td><td>= FOLLOW(E) via E → T E′</td></tr>
<tr><td>T</td><td>{+, $, )}</td><td>E → T E′ ⇒ FIRST(E′)−{ε} = {+} ∪ FOLLOW(E′) = {$,)}</td></tr>
<tr><td>T′</td><td>{+, $, )}</td><td>= FOLLOW(T) via T → F T′</td></tr>
<tr><td>F</td><td>{*, +, $, )}</td><td>T → F T′ ⇒ FIRST(T′)−{ε} = {*} ∪ FOLLOW(T′) = {+,$,)}</td></tr>
</table>
<p>This grammar is <b>non-left-recursive</b> and will pass the LL(1) disjointness test.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
FOLLOW never contains <b>ε</b> — ε belongs only in FIRST. And FIRST is computed bottom-up;
FOLLOW top-down (from the start symbol). The most common error: forgetting to add FOLLOW(A) into
FOLLOW(B) when the production is <code>A → α B</code> (β is empty), or when β is nullable.
</div>
"""),
  CH("ll1", "LL(1) Predictive Parsing Table", """
<p>Build a table row per nonterminal, column per terminal (plus $). For each production
<code>A → α</code>: for every <code>a ∈ FIRST(α)</code> put the production in <code>M[A, a]</code>;
if <code>ε ∈ FIRST(α)</code>, put it in <code>M[A, b]</code> for every <code>b ∈ FOLLOW(A)</code>
(and at <code>$</code> if $ ∈ FOLLOW(A)).</p>

<details><summary>Worked example — construct the LL(1) table for E → TE′ ; E′ → +TE′ | ε ; T → FT′ ; T′ → *FT′ | ε ; F → (E) | id</summary>
<div class="dc">
<p>Use the FIRST/FOLLOW sets from the previous example. Fill each cell by the rule above:</p>
<table>
<tr><th>Nonterminal</th><th>id</th><th>+</th><th>*</th><th>(</th><th>)</th><th>$</th></tr>
<tr><td>E</td><td>E→TE′</td><td></td><td></td><td>E→TE′</td><td></td><td></td></tr>
<tr><td>E′</td><td></td><td>E′→+TE′</td><td></td><td></td><td>E′→ε</td><td>E′→ε</td></tr>
<tr><td>T</td><td>T→FT′</td><td></td><td></td><td>T→FT′</td><td></td><td></td></tr>
<tr><td>T′</td><td></td><td>T′→ε</td><td>T′→*FT′</td><td></td><td>T′→ε</td><td>T′→ε</td></tr>
<tr><td>F</td><td>F→id</td><td></td><td></td><td>F→(E)</td><td></td><td></td></tr>
</table>
<p>E′ gets ε under ) and $ because ) , $ ∈ FOLLOW(E′); T′ gets ε under +, ), $ because
FOLLOW(T′) = {+, $, )}. No cell has two productions ⇒ the grammar is <b>LL(1)</b> and a
non-recursive, table-driven, one-token-lookahead parser exists.</p>
</div></details>

<div class="box formula"><div class="lbl">Why a grammar with both left AND right recursion fails</div>
A grammar with a production like <code>A → A α | β A</code> — or any <b>ambiguity</b> — will produce a
cell with two entries in the LL(1) table ⇒ <b>not LL(1)</b>. Top-down parsing requires unique choices.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
"Eliminating left recursion" or "left-factoring" does <b>not</b> make an ambiguous grammar LL(1):
ambiguity is a property of the language's grammar, not of the form. If two entries collide after
left-factoring, the grammar is genuinely ambiguous — no transformation fixes LL(1)-ness.
</div>
""")]})

# ----------------------------------------------------- 4. Bottom-up parsing
S.append({
 "id": "bottomparse", "title": "Parsing — Bottom-Up (LR family, Operator Precedence)", "children": [
  CH("lr0", "LR(0) Items & the SLR Table", """
<p>Bottom-up parsing is a <b>shift-reduce</b> parser that repeatedly shifts input symbols onto a stack
and reduces a handle to a nonterminal. Building <b>canonical LR(0) item sets</b> partitions grammar
pseudo-items <code>A → α·β</code> into states; transitions make the automaton, whose GOTO/ACTION table
is the SLR parser.</p>

<div class="box formula"><div class="lbl">LR parsing facts</div>
<ul>
<li><b>Handle</b> = a substring that is a right-hand side and whose reduction leads to the start symbol (a right-sentential-form prefix).</li>
<li>States are sets of LR(0) items; <b>closure</b> adds items for dotted nonterminals; <b>GOTO</b> moves the dot after a symbol.</li>
<li><b>SLR(1)</b>: reduce only when the next input ∈ FOLLOW(A) — the lookahead mass is computed from FOLLOW.</li>
<li>Hierarchy of grammar families: <b>LL(0/1) ⊂ SLR(1) ⊂ LALR(1) ⊂ LR(1)</b> (each class strictly contains the previous).</li>
</ul>
</div>

<details><summary>Worked example — canonical LR(0) automaton for E′ → E; E → E+n | n</summary>
<div class="dc">
<p><b>State I<sub>0</sub></b> = closure({E′→·E}) = {E′→·E, E→·E+n, E→·n}.</p>
<p>Transitions from I<sub>0</sub>: on <b>E</b> → I<sub>1</sub>, on <b>n</b> → I<sub>2</sub>.</p>
<p><b>I<sub>1</sub></b> = {E′→E·, E→E·+n} — a <b>reduce-or-shift</b> candidate state. On <b>+</b> → I<sub>3</sub>.</p>
<p><b>I<sub>2</sub></b> = {E→n·} — reduce (handle n, reduce E→n).</p>
<p><b>I<sub>3</sub></b> = {E→E+·n}. On <b>n</b> → I<sub>4</sub>.</p>
<p><b>I<sub>4</sub></b> = {E→E+n·} — reduce (E→E+n).</p>
<p><b>ACTION table:</b> I<sub>1</sub> on $ → accept (E′→E); I<sub>1</sub> on + → shift to I<sub>3</sub>
(both actions never collide here ⇒ an <b>SLR</b> parser exists for this grammar).</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap (SLR vs LALR conflict)</div>
The grammar <code>S → L = R | R; L → * R | id; R → L</code> is <b>unambiguous</b> yet has a
shift-reduce conflict under SLR (state where <code>R → L·</code> and <code>L → ·= R</code>: reducing
<i>R→L</i> is wrong before an <code>=</code>, but the SLR lookahead FOLLOW(R) contains <code>=</code>).
It <b>is</b> LALR(1)/LR(1). Sequence: NOT LL(1) ⊄ LALR ⊃ SLR is a standard assertion.
</div>
"""),
  CH("lalr", "LALR(1) & Conflict Resolution", """
<p><b>LALR(1)</b> merges LR(1) states that share the same LR(0) kernel, keeping only the
<b>lookaheads</b> for reductions. It produces <b>fewer states</b> than LR(1) yet can still recognise
the same class of <b>LALR grammars</b>. It is the parser used in yacc/Bison.</p>
<div class="box formula"><div class="lbl">Parser families compared</div>
<table>
<tr><th>Parser</th><th>Grammar class / lookahead</th><th>States</th></tr>
<tr><td>LL(1)</td><td>top-down, 1 token, no left recursion</td><td>table M[A, terminal]</td></tr>
<tr><td>SLR(1)</td><td>LR(0) items, FOLLOW lookahead</td><td>canonical LR(0) states</td></tr>
<tr><td>LALR(1)</td><td>merged LR(1) lookaheads</td><td>≈ LR(0) state count</td></tr>
<tr><td>LR(1)</td><td>full lookahead in each item</td><td>most states</td></tr>
</table>
</div>
<p><b>Conflict resolution rules</b> (given a shift/reduce clash): default to <b>shift</b>;
associativity/precedence declared by the grammar disambiguates. prefer shift over reduce; for
reduce/reduce, apply the earlier-listed production.</p>

<div class="box trap"><div class="lbl">GATE trap</div>
Merging LR(1) states into LALR can introduce <b>reduce-reduce conflicts</b> that did not exist in the
original LR(1) automaton, but it never introduces a <b>shift-reduce</b> conflict. Keep this asymmetry —
it is a classic assertion question.
</div>
"""),
  CH("opprec", "Operator-Precedence Parsing", """
<p><b>Operator-precedence parsing</b> is a lightweight shift-reduce method for operator-rich grammars
(no ε, no two adjacent nonterminals). The table gives a relation between trailing/leading terminals:
<code>id</code> terminals are compared with <code>&lt;·</code>, <code>·&gt;</code> or <code>=·</code>.</p>
<div class="box formula"><div class="lbl">Precedence relations (left-assoc: shift→reduce)</div>
<table>
<tr><th>Operator pair</th><th>Relation</th><th>Meaning</th></tr>
<tr><td>a = b</td><td>a =· b</td><td>equal precedence, e.g. balanced parens</td></tr>
<tr><td>a &lt;· b</td><td>shift</td><td>a has lower precedence / right-assoc grouping</td></tr>
<tr><td>a ·&gt; b</td><td>reduce</td><td>a has higher precedence / left-assoc chain</td></tr>
</table>
</div>

<details><summary>Worked example — parse id * id + id with precedence ( * &gt; + , both left-assoc )</summary>
<div class="dc">
<p>Precedence matrix (only relevant pairs):</p>
<table><tr><th></th><th>id</th><th>+</th><th>*</th><th>$</th></tr>
<tr><td>id</td><td></td><td>·&gt;</td><td>·&gt;</td><td>·&gt;</td></tr>
<tr><td>+</td><td>&lt;·</td><td>·&gt;</td><td>&lt;·</td><td>·&gt;</td></tr>
<tr><td>*</td><td>&lt;·</td><td>·&gt;</td><td>·&gt;</td><td>·&gt;</td></tr>
<tr><td>$</td><td>&lt;·</td><td>&lt;·</td><td>&lt;·</td><td></td></tr></table>
<p>Trace (compare top-of-stack terminal with next input):</p>
<ol>
<li>$ | id * id + id $ → $ &lt;· id ⇒ <b>shift id</b>.</li>
<li>$ id | * id + id $ → id ·&gt; * ⇒ <b>reduce F→id</b> → $ F.</li>
<li>$ F | * id + id $ → $ &lt;· * ⇒ <b>shift *</b>.</li>
<li>$ F * | id + id $ → * &lt;· id ⇒ <b>shift id</b>.</li>
<li>$ F * id | + id $ → id ·&gt; + ⇒ <b>reduce F→id</b> → $ F * F.</li>
<li>$ F * F | + id $ → * ·&gt; + ⇒ <b>reduce T→T*F</b> (handle F*F) → $ T.</li>
<li>$ T | + id $ → $ &lt;· + ⇒ shift +.</li>
<li>$ T + | id $ → + &lt;· id ⇒ shift id.</li>
<li>$ T + id | $ → id ·&gt; $ ⇒ reduce F→id → $ T + F → reduce T→T+F → $ T.</li>
<li>$ T | $ → accept (string is a valid expression). ✔</li>
</ol>
<p>Note the <b>handle</b> (the maximal span between two &lt;· and ·&gt; relations) is reduced from
right to left, which is why <b>*</b> binds tighter than <b>+</b>.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Operator-precedence parsing is grammar-restricted (no ε-productions, no two adjacent nonterminals) and
cannot handle a unary minus or a right-hand operator of equal precedence without explicit relations.
It is the cheapest correct approach for expression grammars, but it is <b>not</b> the general method.
</div>
""")]})

# ------------------------------------------------------- 5. SDT
S.append({
 "id": "sdt", "title": "Syntax-Directed Translation", "children": [
  CH("sdtschemes", "SDD, SDT & Semantic Actions", """
<p>A <b>syntax-directed definition (SDD)</b> attaches <b>semantic attributes</b> to grammar symbols and
<b>semantic rules</b> to productions. A <b>syntax-directed translation scheme (SDT)</b> embeds the
actions in the production body as program fragments.</p>
<div class="box formula"><div class="lbl">Attribute kinds</div>
<ul>
<li><b>Synthesized</b> attributes — value computed from <b>children</b> at a node. Computed in an
<b>S-attributed</b> definition using a <b>bottom-up</b> (post-order) pass.</li>
<li><b>Inherited</b> attributes — value passed <b>from parent / left siblings</b>. Needed for
<b>L-attributed</b> definitions, computed top-down (pre-order), only when SDT actions are placed
<b>before</b> the children they depend on.</li>
</ul>
</div>
<table>
<tr><th>Definition type</th><th>Attribute mixing</th><th>Evaluation order</th></tr>
<tr><td>S-attributed</td><td>only synthesized</td><td>bottom-up only</td></tr>
<tr><td>L-attributed</td><td>synthesized + inherited (dependencies only left-to-right)</td><td>top-down / depth-first (LL)</td></tr>
</table>
<div class="box trap"><div class="lbl">GATE trap</div>
S-attributed definitions are evaluated <b>bottom-up</b> (they can, but need not, be evaluated during an
LR parse). L-attributed definitions are evaluated <b>top-down / depth-first</b>. An inherited attribute
is how the left part of a parent production feeds a child — a clean example is a declaration that
pushes the <b>type</b> into each identifier's <b>in.type</b>.
</div>
"""),
  CH("sdtimpl", "Translation Schemes in Practice", """
<p>Typical SDT applications: building an <b>AST</b>, generating 3-address code, type checking, and
<i>inheritance</i> of a surrounding type/register/offset.</p>

<details><summary>Worked example — SDT that types a declaration: D → T L ;  L → L , id | id</summary>
<div class="dc">
<p>Give each token's <b>type</b> as a synthesized attribute of T, then copy it into each identifier
using an inherited attribute <code>in</code>:</p>
<p><code>D → T L&nbsp;&nbsp;&nbsp;&nbsp;{ L.in = T.type }</code><br>
<code>T → int&nbsp;&nbsp;&nbsp;&nbsp;{ T.type = integer }</code><br>
<code>T → real&nbsp;&nbsp;&nbsp;{ T.type = real }</code><br>
<code>L → L<sub>1</sub> , id&nbsp;&nbsp;&nbsp;{ L<sub>1</sub>.in = L.in; addtype(id.entry, L.in) }</code><br>
<code>L → id&nbsp;&nbsp;&nbsp;&nbsp;{ addtype(id.entry, L.in) }</code></p>
<p>Evaluation: <b>T.type</b> is synthesized and computed first (bottom-up). The <b>in</b> attribute is
inherited (passed top-down, left-to-right) so every <code>id</code> gets the declaration's type. This is
an <b>L-attributed</b> definition — valid in an LL(1) parse.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
An <b>S-attributed</b> definition can be parsed &amp; evaluated in one bottom-up pass (no extra tree).
An <b>L-attributed</b> definition is evaluated in conjunction with a <b>top-down / depth-first</b> parse.
Many questions give a small SDD and ask you whether it is S- or L-attributed — check whether any
attribute of the left-hand side flows back into a right-hand-side child.
</div>
""")]})

# ------------------------------------------------------- 6. Runtime
S.append({
 "id": "runtime", "title": "Runtime Environments", "children": [
  CH("activation", "Activation Records & Stack Allocation", """
<p>Procedure calls create an <b>activation record</b> on a run-time <b>stack</b>; the sequence of
live activations at any moment is the <b>activation tree</b>. For <b>non-recursive</b> procedures, an
activation records per call needs no dynamic memory; recursion requires stack (or heap) allocation.</p>
<div class="box formula"><div class="lbl">A typical activation record (top → bottom)</div>
<code>return-value</code> ↓ <code>actual parameters</code> ↓ <code>control link (saved FP)</code> ↓
<code>return address / saved return PC</code> ↓ <code>saved registers</code> ↓ <code>local data</code>
↓ <code>temporaries</code>.<br>
The record is anchored by the <b>frame pointer FP</b>; locals are at
<b>negative offsets</b> from FP, parameters at positive offsets.
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
<b>Recursion and variable-size needs both activate records (stack) for calls.</b> A nested procedure's
<b>display / static link</b> finds enclosing-scope locals at compile time. Scoped symbol tables and dynamic
scope are tested via the <b>closest binding</b> rule — an inner declaration shadows an outer one.
</div>
"""),
  CH("heap", "Heap Allocation & Garbage Collection", """
<p><b>Heap</b> allocates data whose lifetime outlives the activation that created it (e.g. objects,
closures). A <b>run-time stack</b> cannot reclaim an object referenced by another live object.</p>
<table>
<tr><th>Scheme</th><th>Mechanism</th><th>Notes</th></tr>
<tr><td>Reference counting</td><td>count per object; free at 0</td><td>cannot collect cycles</td></tr>
<tr><td>Mark-sweep</td><td>mark reachable, sweep rest</td><td>stops world, no compaction</td></tr>
<tr><td>Copying / semi-space</td><td>copy live objects to other half</td><td>compacts, frees fragmentation</td></tr>
<tr><td>Generational</td><td>young/old generations</td><td>young objects die fast</td></tr>
</table>
<div class="box formula"><div class="lbl">Storage classes</div>
<b>Static</b> (constant address, whole program) vs <b>stack</b> (per activation) vs <b>heap</b>
(lifetime managed at runtime). A <b>disjoint, separately managed heap</b> can also be used for
non-stack, non-heap data when a language uses both.
</div>
""")]})

# ------------------------------------------------------- 7. Intermediate code
S.append({
 "id": "icode", "title": "Intermediate Code Generation", "children": [
  CH("ir", "Three-Address Code (TAC) & Quadruples", """
<p>Intermediate representations sit between the parse tree and target machine code. <b>Three-address
code</b> is a linear sequence where each instruction has at most one operator and references at most
three operands <code>x = y op z</code>.</p>
<div class="box formula"><div class="lbl">Four IR forms (all equivalent expressiveness)</div>
<ul>
<li><b>Quadruple:</b> <code>( op, arg1, arg2, result )</code> — e.g. <code>( +, a, b, t1 )</code>.</li>
<li><b>Triple:</b> <code>( op, arg1, arg2 )</code> — no result field; operands may be pointers to entries.</li>
<li><b>Indirect triple:</b> triples + a table indirection.</li>
<li><b>SSA / graph forms</b> used in modern compilers; <b>P-code</b> = stack-machine virtual code.</li>
</ul>
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
A <b>quadruple</b> stores results explicitly, so a value computed once can be reused (good for CSE /
register allocation). A <b>triple</b> must be re-evaluated or its position stored — optimisation that
reorders or duplicates statements is harder for triples than for quadruples. This is a favourite
"which representation is best for …" question.
</div>
"""),
  CH("icodeimpl", "Generating TAC from Expressions", """
<p>Evaluate an expression into TAC with fresh temporaries <code>t1, t2, …</code>. Each operator becomes
one instruction; the standard postfix (right-most derivation) order matches a bottom-up parse.</p>

<details><summary>Worked example — TAC for a := b * –c + b * –c</summary>
<div class="dc">
<p>Recognise the common subexpression <code>b * –c</code>:</p>
<pre><code>t1 = –c
t2 = b * t1
t3 = –c          # duplicate of t1
t4 = b * t3
t5 = t2 + t4
a  = t5</code></pre>
<p>The <b>duplicated</b> computation (t3 = –c, t4 = b*t3) is wasteful; after constant/application
analysis or CSE, <code>t2</code> can be reused: <code>a = t2 + t2</code> then <code>a = 2*t2</code>
local optimisation). We classified the two uses — the CSE pass removes the redundant block.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Every freshly generated temporary counts as a distinct value. Register allocation maps a
<b>liveness range</b> to one register; on a machine with only <b>N</b> registers, more than N live
temporaries forces a <b>spill</b> to memory. Counting live temporaries in a straight-line sequence is a
standard 1-mark calculation in interleaving of IR + liveness.
</div>
""")]})

# ---------------------------------------------------- 8. Optimisation & data-flow
S.append({
 "id": "opt", "title": "Local Optimisation & Data-Flow Analysis", "children": [
  CH("localopt", "Local Optimisations on a Basic Block", """
<p>A <b>basic block</b> is a maximal straight-line code sequence entered only at the top and exited only
at the bottom. <b>Local</b> optimisation operates within one block; <b>global (data-flow)</b> across blocks.</p>
<div class="box formula"><div class="lbl">Fast local optimisations (each preserves semantics)</div>
<ul>
<li><b><b>Constant folding</b>:</b> <code>x = 2*3</code> → <code>x = 6</code>.</li>
<li><b>Copy propagation:</b> replace later uses of the RHS of <code>x = y</code> with <code>y</code>.</li>
<li><b>Dead code elimination:</b> drop statements whose result is never used (after copy propagation).</li>
<li><b>Algebraic identity:</b> <code>x + 0 = x, x*1 = x, x - x = 0</code>.</li>
<li><b>Common subexpression elimination (CSE)</b> within the block.</li>
</ul>
</div>

<details><summary>Worked example — optimise a basic block using DAG</summary>
<div class="dc">
<pre><code>t1 = a + b
t2 = t1 + c
t3 = a + b        # same operands as t1
t4 = t3 + c        # same shape as t2
x  = t4</code></pre>
<p>A <b>DAG</b> (directed acyclic graph) for the block shares the node for <code>a+b</code> (used for both
t1 and t3) and for <code>+c</code> (t2 and t4). The optimised block:</p>
<pre><code>t1 = a + b
t2 = t1 + c
x  = t2</code></pre>
<p>t3, t4 are removed by CSE because the DAG shows identical computation; x reuses t2. This is a single-pass
local optimisation on one basic block requiring no inter-block (global) analysis.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
<b>Dead code</b> is a statement whose result is never used (its value never reaches a use) — it is not
the same as a statement after an <i>unreachable</i> label. Optimisation must <b>preserve semantics</b>;
aliasing and side effects (function calls, memory writes) can block otherwise-legal optimisations.
</div>
"""),
  CH("constprop", "Constant Propagation (forward data-flow)", """
<p><b>Constant propagation</b> replaces a variable with its known constant when the value is provably
constant on every path reaching that statement. It is a <b>forward</b> data-flow problem: information
flows from predecessors to each block.</p>
<div class="box formula"><div class="lbl">Forward transfer + meet (intersection = "all-paths")</div>
IN<sub>B</sub> = ∩ OUT<sub>P</sub> over all predecessors P of B  (meet = intersection).<br>
OUT<sub>B</sub> = Gen<sub>B</sub> ∪ (IN<sub>B</sub> − <b>Kill<sub>B</sub></b>);<br>
Kill<sub>B</sub> removes a variable that B redefines; a new constant for it is added to Gen<sub>B</sub>.
</div>

<details><summary>Worked example — propagate constants across a small flow graph</summary>
<div class="dc">
<pre><code>B1: c = 1          B2: c = 2
    d = c + 1           e = c + 1
    |        \          |
    |         → B4: d = d + 1
    →  B3: c = 1        x = d
        e = c + 1
</code></pre>
<p>IN is the <b>intersection</b> of the OUT of all predecessors. After B1, c=1; after B2, c=2. At B4,
IN(B4) = {c=&perp; (top)} because B1 and B2 disagree on c ⇒ c is <b>not constant</b> on entry to B4.</p>
<p>Every path reaching B4 redefines <code>d</code> then reads it, so <code>d</code> is a constant on every
path; <code>e</code> is constant in each branch. After propagation and dead-code removal, most
arithmetic is trivial — the answer the question wants is which variables are provably constant, so
this is a pure meet-analysis exercise.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Constant propagation is <b>forward</b> with an <b>intersection (all-paths)</b> meet: a constant must be
the same on <b>every</b> branch reaching the point. If any predecessor does not have the constant, the
result is <b>not constant</b>. Backward tests (like liveness) use union — flip the direction and you
get the wrong answer every time.
</div>
"""),
  CH("liveness", "Liveness Analysis (backward data-flow)", """
<p><b>Liveness</b> asks which variables hold a value that may yet be used. A variable is <b>live</b> at a
point if there is a path to a use of its current value without an intervening redefinition. It is a
<b>backward</b> analysis (information flows from successors).</p>
<div class="box formula"><div class="lbl">Backward transfer equations</div>
OUT<sub>B</sub> = ∪ IN<sub>S</sub> over successors S of B  (meet = union).<br>
IN<sub>B</sub> = Gen<sub>B</sub> ∪ (OUT<sub>B</sub> − <b>Kill<sub>B</sub></b>),<br>
where Gen<sub>B</sub> = variables used before redefinition in B (bottom-up), Kill<sub>B</sub> = variables
redefined in B. Live ranges feed <b>register allocation</b>.
</div>

<details><summary>Worked example — compute live-out at each block</summary>
<div class="dc">
<pre><code>B1: a = b + c      B2: x = a * b      B3: c = x + y
    d = a * b            if x &lt; 5 goto B4      print c
    goto B4             goto B5                goto B6
                     B4: a = d + x      B5: b = x + c
                         goto B5             goto B6
                                         B6: print b
</code></pre>
<p>Work <b>backward</b>, union over successors:</p>
<p>liveout(B6) = ∅ (print b reads it, so it is used at the end of B6, not live out).<br>
liveout(B5) = {b} ∪ liveout(B6) = {b}.<br>
liveout(B4) = {b} ∪ liveout(B5) = {b}.<br>
liveout(B3) = {b} ∪ liveout(B6) = {b}.<br>
liveout(B2) = {a, b} ∪ liveout(B4) ∪ liveout(B5) = {a, b}.<br>
liveout(B1) = {a, b, c} ∪ liveout(B4) = {a, b, c}.</p>
<p>At each point, unresolved equations are re-evaluated until fixpoint (a set is monotonically
increasing — this is the standard iterative algorithm). Non-maximal answers → keep iterating.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Liveness is <b>backward</b> + <b>union</b>; constant propagation is <b>forward</b> + <b>intersection</b>.
One quick check: a variable is "used" meaning its register still points to a value, whereas scope of a
declaration is compile-time. Liveness never "kills" a use made by a later block's <b>read</b> — only a
redefinition kills a value.
</div>
"""),
  CH("cse", "Common Subexpression Elimination", """
<p><b>CSE</b> removes a repeated computation whose operands are guaranteed unchanged
(<b>available expressions</b> data-flow problem — forward, intersection meet). It is the global-safety
basis for the local DAG optimisation above.</p>
<div class="box formula"><div class="lbl">Available expressions</div>
OUT<sub>B</sub> = Gen<sub>B</sub> ∪ (IN<sub>B</sub> − <b>Kill<sub>B</sub></b>), IN<sub>B</sub> =
∩ OUT<sub>P</sub> over predecessors.<br>
Expression <code>x op y</code> is <b>available</b> at a point if evaluated on every path and neither
x nor y was redefined since. When available on all paths, replace the second evaluation with a temporary.
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
CSE is valid only if the expression is available on <b>every</b> path (intersection meet) and none of
its operands changed. If one path lacks the computation, the transformation is <b>unsafe</b> (changes
behaviour). Redefinition of any operand kills the expression — a subtle "is this CSE legal?" trap.
</div>
""")]})

# -------------------------------------------------- 9. Formula sheet
S.append({
 "id": "formulas", "title": "One-Page Formula Sheet (Revise Before Exam)",
 "html": """
<table>
<tr><th>Area</th><th>Formula / fact</th></tr>
<tr><td>FIRST</td><td>FIRST(X) = {X} for terminal; ε if X→ε; FIRST(Y₁)(−ε) then nullable-drift right; ε if all nullable</td></tr>
<tr><td>FOLLOW</td><td>FOLLOW(start) ∋ $; A→αBβ ⇒ ∪ FIRST(β)−ε; β nullable/empty ⇒ ∪ FOLLOW(A)</td></tr>
<tr><td>FOLLOW note</td><td>FOLLOW never contains ε</td></tr>
<tr><td>FIRST order</td><td>FIRST computed bottom-up, FOLLOW top-down</td></tr>
<tr><td>LL(1) condition</td><td>disjoint FIRST(α), FIRST(β); and FIRST(α) ∩ FOLLOW(A) = ∅ when ε ∈ FIRST(α)</td></tr>
<tr><td>A → Aα|β  ⇒  A → βA′ ; A′ → αA′ | ε</td></tr>
<tr><td>Left factoring</td><td>A → αβ₁|αβ₂  ⇒  A → αA′ ; A′ → β₁|β₂</td></tr>
<tr><td>Grammar hierarchy</td><td>LL(1) ⊊ SLR(1) ⊊ LALR(1) ⊊ LR(1)</td></tr>
<tr><td>LALR merge</td><td>merging cannot create SR conflict; may create RR conflict</td></tr>
<tr><td>SLR conflict</td><td>S→L=R|R; L→*R|id; R→L is unambiguous but not SLR(1)</td></tr>
<tr><td>Conflict rule</td><td>shift over reduce; associativity/precedence breaks ties</td></tr>
<tr><td>Operator precedence</td><td>shift on &lt;·, reduce on ·&gt;, =· for equal/grouping</td></tr>
<tr><td>SDT types</td><td>S-attributed = synthesized only ⇒ bottom-up; L-attributed = +inherited ⇒ top-down/DFS</td></tr>
<tr><td>Activation record</td><td>ret-val, params, control link, ret-addr, saved regs, locals, temps — stack</td></tr>
<tr><td>Liveness (backward)</td><td>IN = Gen ∪ (OUT − Kill); OUT = ∪ IN(successors)</td></tr>
<tr><td>Const propagation (forward)</td><td>IN = ∩ OUT(preds); OUT = Gen ∪ (IN − Kill)</td></tr>
<tr><td>Available expr (forward)</td><td>OUT = Gen ∪ (IN − Kill); IN = ∩ OUT(preds) — all-paths ⇒ CSE legal</td></tr>
<tr><td>Optimisations</td><td>constant folding, copy prop, dead-code elim, algebraic identity, CSE, DAG</td></tr>
<tr><td>IR forms</td><td>quadruple, triple, indirect triple, P-code/SSA</td></tr>
</table>
<div class="box tip"><div class="lbl">Ten-second exam scan</div>
If a question says "which parser class", remember the four-class hierarchy and the LALR merge
asymmetry. If it says data-flow, first ask <b>direction</b> (forward/backward) and <b>meet</b>
(intersection/union); that alone usually settles the answer.
</div>
"""
})

# -------------------------------------------------- 10. Exam strategy
S.append({
 "id": "strategy", "title": "Exam Strategy",
 "html": """
<div class="box tip"><div class="lbl">Attack order (6 marks)</div>
<ol>
<li><b>FIRST/FOLLOW + LL(1) table</b> first — near-free if you practise once; <b>1–2 marks</b>.</li>
<li><b>Bottom-up / LR family</b> second — often a single well-worn conflict or state-count question.</li>
<li><b>Data-flow (liveness / const-prop / CSE)</b> third — mechanical, high accuracy.</li>
<li><b>Lexical, runtime, IR, SDT</b> last — short, recall-heavy marks.</li>
</ol>
</div>

<div class="box trap"><div class="lbl">Common time sinks to avoid</div>
<ul>
<li><b>Building a full LR(1) automaton</b> by hand for a multi-nonterminal grammar — GATE rarely needs
more than the canonical LR(0) states of a 2–4 production grammar. If the grammar is clearly LALR
(large), answer qualitatively.</li>
<li><b>Re-deriving FOLLOW from scratch</b> — mark nullable symbols first, then do a single
fixpoint pass; never iterate more than once.</li>
<li><b>Operator-precedence traces</b> — lock the "shift on &lt;·, reduce on ·&gt;" rule and only compare
consecutive terminal pairs, not long handles.</li>
<li><b>Semantic-attribute theo questions</b> — distinguish compiled-time (type check, symbol table) from
run-time (activation, heap). If a sentence mixes them, it is wrong.</li>
</ul>
</div>

<div class="box"><div class="lbl">What to skip under time pressure</div>
<p>Skip any question requiring a 4+ state automaton build or a long grammar's conflict enumeration unless
you already have 4 marks banked. Prefer <b>qualitative</b> classification (LL(1)? No — left recursion;
SLR? No — the classic S→L=R conflict; LALR/LR(1)? Yes) — that mode answers 60% of parsing MCQs in under
a minute.</p>
</div>
"""
})

QUIZ = [
 {"q":"Which phase of the compiler produces the token stream?","opts":["Parsing","Lexical analysis","Code generation","Semantic analysis"],"a":1,
  "ex":"The lexical analyzer (scanner) reads the character stream and emits tokens; the parser consumes them."},
 {"q":"An ambiguous context-free grammar is always:","opts":["LL(1)","Not LL(1)","LALR(1)","unambiguous"],"a":1,
  "ex":"Ambiguity means some sentence has two parse trees, so the LL(1) table gets two entries in one cell — ambiguous grammars can never be LL(1)."},
 {"q":"FOLLOW(A), the set of terminals that can follow A, never contains:","opts":["the end-marker $","a terminal from the input alphabet","the symbol ε","the start symbol"],"a":2,
  "ex":"ε belongs only in FIRST of nullable symbols; FOLLOW holds only real terminals (and $), never ε."},
 {"q":"Which of these is a valid action of the classic operator-precedence method?","opts":["handle both ε-productions and adjacent nonterminals","require a grammar with no ε-productions and no two adjacent nonterminals","parse using state lookaheads of LR(1)","handle unary minus automatically"],"a":1,
  "ex":"Operator-precedence parsing assumes no ε-productions and no right-hand side with two adjacent nonterminals, restricting it to expression-like grammars."},
 {"q":"For a top-down (LL) parser, the grammar A → A α | β must first have:","opts":["left factoring applied","left recursion eliminated","the FOLLOW set computed for terminals","the grammar converted to CNF"],"a":1,
  "ex":"Left recursion makes a top-down parser loop forever in the recursion; it is eliminated (A → βA′; A′ → αA′|ε) before building an LL parser."},
 {"q":"The grammar hierarchy among the following is:","opts":["SLR ⊊ LALR ⊊ LR(1)","LR(1) ⊊ LALR ⊊ SLR","LALR ⊊ SLR ⊊ LR(1)","SLR = LALR = LR(1)"],"a":0,
  "ex":"Every SLR grammar is LALR(1) and every LALR grammar is LR(1), so SLR ⊊ LALR ⊊ LR(1) — each strictly wider than the one before it."},
 {"q":"Merging LR(1) states into an LALR(1) automaton may introduce a:","opts":["shift-reduce conflict only","reduce-reduce conflict, but never a new shift-reduce conflict","both new shift-reduce and reduce-reduce conflicts","neither type of conflict"],"a":1,
  "ex":"State merging can break two reductions apart that were disjoint, creating a reduce-reduce conflict, but the merge never changes shift/reduce decisions, so no new shift-reduce conflict appears."},
 {"q":"Which grammar is unambiguous but NOT SLR(1), yet is LALR(1)?","opts":["E → E + n | n","S → L = R | R; L → * R | id; R → L","S → A A; A → a A | b","E → ( E ) | id"],"a":1,
  "ex":"S → L = R | R, L → *R | id, R → L gives a shift-reduce conflict under SLR because FOLLOW(R) includes '=' but the correct choice needs full lookahead; it is LALR(1)."},
 {"q":"A syntax-directed definition that uses only synthesized attributes is evaluated:","opts":["top-down only","bottom-up only","in any order","only at run time"],"a":1,
  "ex":"An S-attributed definition computes each node's attributes from its children, so a single bottom-up (post-order) pass suffices."},
 {"q":"An L-attributed definition additionally uses inherited attributes and needs:","opts":["a bottom-up pass only","a top-down / depth-first evaluation","a second full parse","a separate symbol table"],"a":1,
  "ex":"Inherited attributes flow from parent/left siblings, so L-attributed definitions are evaluated in a top-down, depth-first manner (compatible with LL parsing)."},
 {"q":"The intermediate representation best suited for global optimisation such as CSE is:","opts":["triple","quadruple","P-code only","postfix notation"],"a":1,
  "ex":"Quadruples store the result explicitly, so a computed value can be reused across the block/CFG; triples make such reuse awkward because a result has no name."},
 {"q":"For a procedure call, the run-time storage for its activation record is allocated:","opts":["in the heap exclusively","on the run-time stack","in static memory","in a separate code segment"],"a":1,
  "ex":"Activation records for ordinary procedure calls are allocated on the run-time stack; heaps/static storage are used only for specific lifetime needs."},
 {"q":"A variable redefined inside a block B after its last use makes it:","opts":["live out of B","dead on entry to B","register-spilled","undefined"],"a":1,
  "ex":"If the variable's value is overwritten before any later use, no use of the original value follows, so it is not live out of B."},
 {"q":"In liveness analysis, the meet (combine) operation over successor sets is:","opts":["intersection","union","empty set","bitwise AND"],"a":1,
  "ex":"Liveness is backward with a union meet: a variable is live at a block if it is live in at least one successor."},
 {"q":"Constant propagation is computed as a:","opts":["backward analysis with union","forward analysis with intersection","backward analysis with intersection","random-order analysis"],"a":1,
  "ex":"It is forward (info from predecessors) and uses intersection, because a value is constant at a point only if it is constant on every path reaching it."},
 {"q":"The quadratic quadruple sequence t1=−c; t2=b*t1; t3=−c; t4=b*t3; t5=t2+t4; a=t5 can be improved by:","opts":["copy propagation only","common subexpression elimination (CSE)","constant folding only","nothing"],"a":1,
  "ex":"t3=−c and t4=b*t3 duplicate t1, t2; a DAG/available-expression pass recognises b*(−c) is computed twice, so CSE removes t3,t4 (a=t2+t2)."},
 {"q":"Which optimisation is invalid if an operand may be redefined along a path?","opts":["replacing a multi-path repeated expression (CSE)","constant folding of literals","dead-code elimination of unused stores","algebraic x+0=x"],"a":0,
  "ex":"CSE replaces an expression only if it is available on every path with operands unchanged; if an operand is redefined on some path the replacement is unsafe."},
 {"q":"A basic block is best described as:","opts":["any set of consecutive statements","maximal straight-line code entered only at top, exited only at bottom","a single function","code with no branches out"],"a":1,
  "ex":"By definition a basic block is straight-line with a single entry point and a single exit point (no branches into or out of the middle)."},
 {"q":"Which data-flow fact belongs to an SSA-style or dataflow family and is backward?","opts":["available expressions","constant propagation","liveness of variables","reaching definitions"],"a":2,
  "ex":"Liveness is backward, all-paths-of-successor union: it asks whether a value may yet be used. Available expressions and reaching defs/const-prop are forward."},
 {"q":"The canonical LR(0) automaton for E′ → E, E → E+n | n has how many states?","opts":["3","4","5","6"],"a":1,
  "ex":"I₀={E′→·E,E→·E+n,E→·n}, I₁={E′→E·,E→E·+n}, I₂={E→n·}, I₃={E→E+·n}, I₄={E→E+n·} — five states total."}
]

SUBJECT = {
 "code": "S07", "title": "Compiler Design",
 "subtitle": "GATE CS 2027 · 6 marks · Lexical analysis, parsing (LL/LR), SDT, runtime environments, IR, optimisation & data-flow",
 "weight_note": "GATE CS 2027 · Compiler Design section (6 marks)",
 "sections": S, "quiz": QUIZ,
}