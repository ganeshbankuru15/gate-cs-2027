# -*- coding: utf-8 -*-
"""Subject 02 — Digital Logic (7 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

S.append({
 "id": "overview", "title": "Overview & Weightage",
 "html": """
<div class="kv">
  <span class="chip">Marks <b>7 / 100</b></span>
  <span class="chip">Typical Qs <b>3–5</b></span>
  <span class="chip">Style <b>Both MCQ &amp; NAT</b></span>
  <span class="chip">Scoring <b>High yield</b></span>
</div>
<p>Digital Logic is one of the <b>most reliable scoring blocks</b> in GATE CS. The syllabus is compact,
formula-driven and almost entirely closed — K-map minimisation, flip-flop timing and 2's-complement
arithmetic show up <b>every single year</b>. Best of all, its trace runs through Computer Organisation
(adders, FSM, hazard/delay ideas), so studying here pays twice.</p>

<h3>What it contains</h3>
<table>
<tr><th>Topic</th><th>Typical marks</th><th>Difficulty</th><th>Priority</th></tr>
<tr><td>Number conversion &amp; 2's-complement arithmetic</td><td>1–2</td><td>Easy</td><td>★★★★★</td></tr>
<tr><td>Boolean algebra &amp; K-map / Quine–McCluskey</td><td>2</td><td>Easy–Medium</td><td>★★★★★</td></tr>
<tr><td>Combinational: MUX, decoder, adder, code converter</td><td>1–2</td><td>Medium</td><td>★★★★★</td></tr>
<tr><td>Sequential: flip-flops, counters, shift registers</td><td>1–2</td><td>Medium</td><td>★★★★☆</td></tr>
<tr><td>FSM design</td><td>0–1</td><td>Medium</td><td>★★★★☆</td></tr>
<tr><td>CMOS &amp; timing (setup/hold, delay, hazards)</td><td>1</td><td>Medium–Hard</td><td>★★★☆☆</td></tr>
</table>

<div class="box tip"><div class="lbl">Order of attack for GATE 2027</div>
<ol>
<li><b>Number systems first</b> — 5 minutes of rules, near-guaranteed marks.</li>
<li><b>K-map next</b> — fastest, most mechanical marks in the paper.</li>
<li><b>Combinational circuits</b> — MUX/decoder "realise the function" questions are heavily repeated.</li>
<li><b>Sequential + FSM</b> — count, recognise states, draw state tables.</li>
<li><b>Timing last</b> — only if you have time; it is the densest, hardest part.</li>
</ol>
</div>

<div class="box trap"><div class="lbl">Negative marking reality</div>
MCQs carry −1/3 (1-mark) and −2/3 (2-mark). NAT questions carry <b>no negative marking</b> — for any
numerical answer you can bound (e.g. a K-map result, an adder output, a counter modulus), guess NATs
freely. Never blind-guess MCQs on Digital Logic because wrong traps are planted every year.
</div>
"""
})
# -------------------------------------------------- 2. Number representation
S.append({
 "id": "numrepr", "title": "Number Representation & Arithmetic", "children": [
  CH("bases", "Number Systems & Conversion", """
<p>Positional notation: a digit at position <i>k</i> from the radix point contributes
digit × base<sup>k</sup>. Common bases: binary (2), octal (8), decimal (10), hexadecimal (16).</p>
<table>
<tr><th>Conversion</th><th>Method</th></tr>
<tr><td>Decimal → binary</td><td>repeated division by 2, remainder gives LSB first; read bottom-up</td></tr>
<tr><td>Fraction .N → binary</td><td>repeated multiplication by 2, take integer parts in order</td></tr>
<tr><td>Binary → octal/hex</td><td>group 3 (octal) or 4 (hex) bits from the radix point; pad with 0s</td></tr>
<tr><td>Octal/hex → binary</td><td>each digit → its 3/4-bit group directly</td></tr>
<tr><td>Any → decimal</td><td>Horner / expand by repeated multiply-add</td></tr>
</table>
<p><b>Octal digit</b> = 3 bits; <b>hex digit</b> = 4 bits. Base-<i>b</i> has b symbols (0…b−1).</p>

<div class="box formula"><div class="lbl">Range of values in n bits (unsigned)</div>
Min = 0, Max = 2<sup>n</sup> − 1. A k-bit signed integer has range −2<sup>k−1</sup> …
+2<sup>k−1</sup> − 1 (2's complement). Number of distinct values = 2<sup>n</sup>.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
A fractional binary like 0.1 (decimal 0.5) is exact, but <b>0.1 decimal is not exactly representable</b>
in binary (it is a repeating bit pattern). Also: when converting binary→hex, always pad with <b>leading</b>
zeroes on the left side of the integer part, but on the <b>right</b> side of a fraction.
</div>
"""),
  CH("signed", "Signed Numbers & 2's Complement", """
<p>Three signed representations for <i>n</i>-bit integers (MSB = sign bit):</p>
<table>
<tr><th>Scheme</th><th>Range</th><th>Zero</th><th>−5 (8-bit)</th></tr>
<tr><td>Sign-magnitude</td><td>−(2<sup>n−1</sup>−1) … +(2<sup>n−1</sup>−1)</td><td>+0 and −0</td><td>1000 0101</td></tr>
<tr><td>1's complement</td><td>−(2<sup>n−1</sup>−1) … +(2<sup>n−1</sup>−1)</td><td>+0 and −0</td><td>1111 1010</td></tr>
<tr><td>2's complement</td><td>−2<sup>n−1</sup> … +2<sup>n−1</sup>−1</td><td>single 0</td><td>1111 1011</td></tr>
</table>

<div class="box formula"><div class="lbl">2's complement rules — memorise these</div>
<ul>
<li><b>Negate:</b> invert all bits, then add 1 (flip + add 1).</li>
<li><b>Shortcut:</b> copy from the LSB, copying all trailing 0s and the first 1, then invert the rest.</li>
<li>−x in <i>n</i> bits ≡ 2<sup>n</sup> − x (mod 2<sup>n</sup>).</li>
<li><b>Subtraction = addition of the 2's complement:</b> a − b = a + (2's complement of b).</li>
<li>Range: −2<sup>n−1</sup> … +2<sup>n−1</sup>−1 (asymmetric — no +2<sup>n−1</sup>).</li>
</ul>
</div>

<h4>Overflow detection</h4>
<p>Overflow occurs only when adding two numbers of the <b>same sign</b> gives a result of the opposite sign,
or when the carry into the MSB ≠ carry out of the MSB. Adding a +ve and a −ve can never overflow.</p>

<details><summary>Worked example — subtract 12 from 8 in 8-bit 2's complement</summary>
<div class="dc">
<p>8 − 12. 12 = 0000 1100 → complement: 1111 0011 + 1 = <b>1111 0100</b> (−12).</p>
<p>Add 8 (0000 1000): 0000 1000 + 1111 0100 = 1111 1100 with carry-out 1 (discarded).</p>
<p>1111 1100 = −4 (since 0000 0100 = 4, inverted+1 ⇒ −4). Answer <b>−4</b>. ✔ (Carry-out ≠ overflow.)</p>
</div></details>

<div class="box tip"><div class="lbl">Fast negation</div>
To negate in 2's complement, do "copy from right up to and including the first 1, flip everything left".
For 0010 1100 → copy "100" → flip left part to 1101 00 → <b>1101 0100</b>. Never invert-then-add-two-mistakes.
</div>
"""),
  CH("arith", "Arithmetic Circuits", """
<p>Arithmetic lives at the boundary of combinational logic.</p>
<div class="box formula"><div class="lbl">Half adder / Full adder truth — core facts</div>
<b>Half adder:</b> Sum = A ⊕ B, Carry = A·B.<br>
<b>Full adder</b> (3 inputs A, B, C<sub>in</sub>): Sum = A ⊕ B ⊕ C<sub>in</sub>; Carry-out = AB + C<sub>in</sub>(A ⊕ B).<br>
<b>n-bit ripple carry adder:</b> n full adders in series; worst-case delay <b>∝ n</b>.<br>
<b>Propagation delay of one FA ≈ 2 gate delays.</b>
</div>
<p>A <b>subtractor</b> = add 2's complement of B plus carry-in 1 (the "add inverted B, force carry-in" trick).
A <b>carry-lookahead adder</b> computes generate G<sub>i</sub> = A<sub>i</sub>B<sub>i</sub> and propagate
P<sub>i</sub> = A<sub>i</sub> ⊕ B<sub>i</sub>, then C<sub>i+1</sub> = G<sub>i</sub> + P<sub>i</sub>C<sub>i</sub> —
carry delay is constant (log-depth), independent of n.</p>

<div class="box trap"><div class="lbl">GATE trap</div>
A ripple-carry adder's worst-case delay is <b>O(n) gate delays</b>, not O(log n) — students import the O(log n)
CLA answer wrongly. Also remember the overflow rule: for sign-magnitude and 1's-complement, the <b>end-around
carry</b> must be wrapped back into the LSB, which makes them slower than 2's complement in hardware.
</div>
""")]})
# --------------------------------------------------- 4. Logic gates & CMOS
S.append({
 "id": "gates", "title": "Logic Gates & Static CMOS", "children": [
  CH("gatebase", "Universal Gates & Theorems", """
<table>
<tr><th>Gate</th><th>Expression</th><th>Output</th></tr>
<tr><td>AND</td><td>A·B</td><td>1 iff both 1</td></tr>
<tr><td>OR</td><td>A+B</td><td>1 iff ≥1 input 1</td></tr>
<tr><td>NOT</td><td>A′</td><td>invert</td></tr>
<tr><td>NAND</td><td>(A·B)′</td><td>0 iff both 1</td></tr>
<tr><td>NOR</td><td>(A+B)′</td><td>1 iff both 0</td></tr>
<tr><td>XOR</td><td>A ⊕ B</td><td>1 iff inputs differ</td></tr>
<tr><td>XNOR</td><td>(A ⊕ B)′</td><td>1 iff inputs same</td></tr>
</table>
<p><b>NAND and NOR are universal</b> — any Boolean function can be built using only NAND gates (or only NOR
gates). This is the single most repeated gate question.</p>
<div class="box formula"><div class="lbl">Universal-gate constructions</div>
<b>NOT from NAND:</b> tie inputs together → (A·A)′ = A′.<br>
<b>AND from NAND:</b> NAND then NOT: ((A·B)′)′ = A·B.<br>
<b>OR from NAND:</b> (A′·B′)′ = A + B (i.e. NAND of complements).<br>
<b>XOR from NAND:</b> A·B′ + A′·B using 4 NANDs. <b>XOR from NOR</b> needs 5 NORs.
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
<b>XOR and XNOR are NOT universal alone</b> (they cannot realise AND of a variable with both values in
general without constants). A single 2-input XOR cannot implement NOT A unless the other input is tied to 1
— that is a "with constants" trick, not universality. Also, NAND is universal; NOR is universal; but XOR
alone is not.
</div>
"""),
  CH("cmos", "Static CMOS Circuits", """
<p>Static CMOS uses two complementary networks between V<sub>DD</sub> and ground.</p>
<div class="box formula"><div class="lbl">CMOS structure — memorise the rule</div>
<ul>
<li><b>Pull-up network (PUN):</b> PMOS transistors to V<sub>DD</sub>. P-type conducts when input = 0.</li>
<li><b>Pull-down network (PDN):</b> NMOS transistors to ground. N-type conducts when input = 1.</li>
<li>For a logic function F: PUN implements <b>F′</b> in PMOS, PDN implements <b>F</b> in NMOS.</li>
<li>PMOS in <b>parallel</b> (OR) → series NMOS complement; PMOS in <b>series</b> (AND) → parallel NMOS (Duality).</li>
</ul>
<p>Static CMOS has <b>zero static power</b> (no current in steady state) and <b>full logic swing</b>.</p>
</div>
<table>
<tr><th>Gate</th><th>NMOS (pull-down)</th><th>PMOS (pull-up)</th><th>How many transistors</th></tr>
<tr><td>Inverter</td><td>1</td><td>1</td><td>2</td></tr>
<tr><td>NAND</td><td>2 in series</td><td>2 in parallel</td><td>4</td></tr>
<tr><td>NOR</td><td>2 in parallel</td><td>2 in series</td><td>4</td></tr>
<tr><td>AND / OR</td><td colspan="2">NAND/NOR + inverter</td><td>6</td></tr>
</table>
<details><summary>Worked example — why a CMos NAND is 2-series NMOS + 2-parallel PMOS</summary>
<div class="dc">
<p>F = (A·B)′. Output must be 0 ONLY when both A=B=1 (NAND: N(1,1)=0).</p>
<p>Pull-down must conduct ONLY then → two NMOS in <b>series</b> (both on).</p>
<p>Pull-up must conduct otherwise → two PMOS in <b>parallel</b> (either complements on).</p>
<p>Duality is automatic: series↔parallel, N↔P, F↔F′. Cost = 4 transistors, the minimum for a 2-input NAND.</p>
</div></details>
<div class="box trap"><div class="lbl">GATE trap</div>
The <b>pull-up is the complement</b>. Students wrongly draw the PMOS network as the same topology as the
NMOS network. For NAND F=(AB)′, pull-up is PMOS in PARALLEL. Always verify with the F=0 column of the truth
table, never assume topology follows the function symbol.
</div>
""")]})
# -------------------------------------------- 5. Combinational circuits
S.append({
 "id": "comb", "title": "Combinational Circuits: MUX, Decoder, Code Converters", "children": [
  CH("muxdec", "Multiplexers & Decoders", """
<p>A <b>multiplexer</b> selects one of many data inputs using select (control) lines. An n-select MUX has
<b>2<sup>n</sup> data inputs</b>. A <b>decoder</b> has n inputs and <b>2<sup>n</sup> outputs</b>, exactly one
active per input code.</p>
<div class="box formula"><div class="lbl">Key identities</div>
<ul>
<li>2<sup>n</sup>:1 MUX needs n select lines; n:2<sup>n</sup> decoder has 2<sup>n</sup> distinct outputs.</li>
<li>Any Boolean function of n variables can be realised directly with a 2<sup>n</sup>:1 MUX (constant data
inputs 0/1/their complements).</li>
<li>Any function of n variables can be realised with an (n−1)-select MUX by feeding the last variable (or
its complement / 0 / 1) into data inputs — this is <b>Shannon/expansion</b> and halves the MUX size.</li>
<li>A decoder + OR gates implements any SOP function (OR the decoder outputs of the 1-minterms); for active-low
decoders, use NAND. For POS, use the 0-minterms.</li>
<li>An <b>active-high</b> 2-to-4 decoder: each output O<sub>i</sub> = minterm m<sub>i</sub>.</li>
</ul>
</div>
<details><summary>Worked example — F(A,B,C)=Σm(1,3,5,7) with a 4:1 MUX (2 selects)</summary>
<div class="dc">
<p>Use A,B as selects (data D0..D3 correspond to AB=00,01,10,11). Expand each minterm in terms of C:</p>
<p>m1 (001): AB=00, output must = C (since F=1 only when C=1) → D0 = C.<br>
m3 (011): AB=01, needs C·(1) → D1 = C. Actually both endpoints C-terms → D1 = C.<br>
m5 (101): AB=10 needs C → D2 = C.<br>
m7 (111): AB=11 needs C → D3 = C.</p>
<p>So <b>all four data lines = C</b>. This is F = C·(A′B′+A′B+AB′+AB) = C·1 = C. Check: Σm(1,3,5,7) are exactly the odd minterms (all have LSB = 1) → F = C. ✔</p>
</div></details>
<div class="box trap"><div class="lbl">GATE trap</div>
Multiplexer and decoder are <b>opposite functions</b> — MUX goes 2<sup>n</sup>→1, decoder goes n→2<sup>n</sup>.
Students swap the input/output counts. Also, a decoder realised with NAND (active-low) ORs minterms via a
NAND gate and inverts the function view — read the active level before writing the answer.
</div>
"""),
  CH("codeconv", "Code Converters", """
<p>Code converters translate one code to another (pure logic, no memory).</p>
<div class="box formula"><div class="lbl">Binary ↔ Gray — the two formulas</div>
<b>Binary → Gray:</b> G<sub>k</sub> = B<sub>k</sub> ⊕ B<sub>k+1</sub> (MSB unchanged).<br>
<b>Gray → Binary:</b> B<sub>k</sub> = B<sub>k+1</sub> ⊕ G<sub>k</sub> (accumulate XOR from the MSB).<br>
Two consecutive Gray codes differ in exactly <b>one bit</b> — the property K-maps exploit for adjacency.
</div>
<p>Common conversions: binary↔gray, binary↔BCD, BCD↔excess-3, BCD→7-segment (for display), and ASCII↔BCD.
A <b>BCD code</b> uses 4 bits but is <b>not</b> 0–15: it only encodes 0–9; 1010–1111 are invalid and treated
as don't-cares. <b>Excess-3</b> code = (BCD + 3), is self-complementing (9's complement by bit-flipping).</p>

<details><summary>Worked example — convert binary 1011 to Gray code</summary>
<div class="dc">
<p>B = 1 0 1 1. G<sub>3</sub> = B<sub>3</sub> = 1. G<sub>2</sub> = B<sub>3</sub>⊕B<sub>2</sub> = 1⊕0 = 1. G<sub>1</sub> = B<sub>2</sub>⊕B<sub>1</sub> = 0⊕1 = 1. G<sub>0</sub> = B<sub>1</sub>⊕B<sub>0</sub> = 1⊕1 = 0.</p>
<p>Gray = <b>1110</b>. Sanity: B=1011 (decimal 11).  Check Gray of 10 is 1111, of 11 is 1110 ✓ (adjacent, differ one bit).
</div></details>
<div class="box trap"><div class="lbl">GATE trap</div>
The two Gray formulas are <b>not the same direction</b>. Binary→Gray XORs the bit with its <i>left</i>
neighbour; Gray→Binary XORs running from the left, using <i>each already-decoded</i> resulting bit. Reversing
them gives wrong codes. Memorise: "binary-grey: copy top, XOR with left; grey-binary: copy top, XOR down".
</div>
"""),
  CH("adders2", "Adders, Subtractors & Magnitude Comparators", """
<table>
<tr><th>Circuit</th><th>Inputs</th><th>Outputs</th><th>Cost / delay</th></tr>
<tr><td>Half adder</td><td>A, B</td><td>S=A⊕B, C=AB</td><td>1 XOR + 1 AND</td></tr>
<tr><td>Full adder</td><td>A, B, Cin</td><td>S=A⊕B⊕Cin, Cout=AB+Cin(A⊕B)</td><td>2 XOR + 2 AND + 1 OR (≈4 gates)</td></tr>
<tr><td>Ripple adder (n-bit)</td><td>n bits</td><td>sum + carry</td><td>delay ∝ n (n·t<sub>FA</sub>)</td></tr>
<tr><td>Carry-lookahead</td><td>n bits</td><td>sum + carry</td><td>delay O(log n)</td></tr>
<tr><td>Subtractor</td><td>n bits</td><td>diff = a + (2's comp of b)</td><td>adder + select/invert + Cin=1</td></tr>
</table>
<p>A <b>full subtractor</b> has inputs A, B, Borrow-in; outputs Difference = A ⊕ B ⊕ B<sub>in</sub> and
Borrow-out = A′B + B<sub>in</sub>(A′ ⊕ B) — identical in structure to a full adder but with an inversion.</p>
<p>A <b>magnitude comparator</b> for two n-bit numbers produces 3 outputs (A&gt;B, A=B, A&lt;B). An XOR on each
bit-pair detects equality; comparisons chain from the MSB. n-bit comparator can be built from an n-bit adder
or (A−B) with borrow/sign detection.</p>
<div class="box trap"><div class="lbl">GATE trap</div>
A subtractor with an adder ALONE cannot borrow — you must also <b>invert B and force carry-in = 1</b>. A
comparator is NOT just an adder; it needs borrow/sign logic. And a half adder cannot take a carry-in, so it
can never build an add chain by itself — every stage after the LSB must be a full adder.
</div>
""")]})
# ----------------------------------------------- 6. Latches & flip-flops
S.append({
 "id": "ff", "title": "Latches & Flip-Flops", "children": [
  CH("latch", "Latches vs Flip-Flops", """
<p>A <b>latch</b> is level-sensitive (transparent while enabled); a <b>flip-flop</b> is edge-triggered
(samples only on the clock edge). Note: GATE uses them interchangeably in places, but the distinction
(level vs edge) is examinable.</p>
<table>
<tr><th>Device</th><th>Enable</th><th>Transparent?</th></tr>
<tr><td>SR / D latch</td><td>level</td><td>yes while CLK high (or low)</td></tr>
<tr><td>D / JK / T flip-flop</td><td>edge</td><td>only at rising/falling edge</td></tr>
<tr><td>Master–slave FF</td><td>edge</td><td>no (acts edge-triggered, no transparency)</td></tr>
</table>
<div class="box formula"><div class="lbl">Characteristic equations (write these from memory)</div>
<b>SR:</b> Q<sup>+</sup> = S + R′·Q &nbsp;(S·R = 0 forbidden / undefined)<br>
<b>D:</b> Q<sup>+</sup> = D<br>
<b>JK:</b> Q<sup>+</sup> = J·Q′ + K′·Q<br>
<b>T:</b> Q<sup>+</sup> = T ⊕ Q = T·Q′ + T′·Q<br>
<b>JK→D:</b> set J=D, K=D′ &nbsp;·&nbsp; <b>JK→T:</b> J=K=T &nbsp;·&nbsp; <b>D→T:</b> D = T⊕Q
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
<b>SR latch has the invalid state S=R=1</b> (both outputs fight; behaviour undefined / prohibited). This is
why the JK FF was invented (J=K=1 → toggle instead of invalid). Master–slave overcomes <b>transparency/1-capture</b>
of a level latch — a direct question on why master–slave exists. Never say SR can accept S=R=1.
</div>
"""),
  CH("fpe", "Excitation Tables & Characteristic Table Use", """
<p><b>Excitation table</b>: given current state → next state and clock, what input do we apply. Essential
for counter and FSM design.</p>
<table>
<tr><th>FF</th><th>0→0</th><th>0→1</th><th>1→0</th><th>1→1</th></tr>
<tr><td>SR</td><td>S=0,R=X</td><td>S=1,R=0</td><td>S=0,R=1</td><td>S=X,R=0</td></tr>
<tr><td>JK</td><td>J=0,K=X</td><td>J=1,K=X</td><td>J=X,K=1</td><td>J=X,K=0</td></tr>
<tr><td>D</td><td>D=0</td><td>D=1</td><td>D=0</td><td>D=1</td></tr>
<tr><td>T</td><td>T=0</td><td>T=1</td><td>T=1</td><td>T=0</td></tr>
</table>
<p>To design a counter: write the state sequence, build the excitation table for each FF, derive K-maps for
each excitation input (they become functions of current state), and wire the logic between FF outputs and
their inputs.</p>
<div class="box tip"><div class="lbl">Tip</div>
For D-FF the excitation is trivial (D = next state), so counters and shift registers become easy. For JK/T
always write the excitation column before mapping — guessing plain gate connections wastes minutes.
</div>
""")]})
# -------------------------------------- 7. Counters & shift registers
S.append({
 "id": "counters", "title": "Counters & Shift Registers", "children": [
  CH("counter2", "Counters", """
<table>
<tr><th>Type</th><th>Clock</th><th>Delay / skew</th><th>Wide</th></tr>
<tr><td>Asynchronous / ripple</td><td>each FF clocked by previous stage's output</td><td>propagates (slow, n·t)<br>ripple delay adds up</td><td>simple, no global clock tree</td></tr>
<tr><td>Synchronous</td><td>all FFs share one clock</td><td>constant, equal; needs decoder logic from current state</td><td>used in high-speed design</td></tr>
</table>
<div class="box formula"><div class="lbl">Counter facts</div>
<ul>
<li>n FFs → modulo 2<sup>n</sup> (max) counter, count 0…2<sup>n</sup>−1.</li>
<li><b>Modulo-M counter</b> needs <b>⌈log<sub>2</sub> M⌉</b> flip-flops.</li>
<li><b>Up</b> vs <b>down</b> counter: with a T-FF, toggle each cycle (binary-count); direction changes the Q or Q′ used.</li>
<li>A ripple counter's max frequency is limited by the <b>cumulative FF delay</b> (n·t<sub>pd</sub>); synchronous counters are faster.</li>
<li><b>Ring counter:</b> n FFs, exactly one 1 circulating → modulo n, wastes states (2<sup>n</sup>−n unused).</li>
<li><b>Johnson / twisted-ring:</b> complement of last FF fed back → counts 2n — doubled length from same hardware.</li>
</ul>
</div>
<details><summary>Worked example — flip-flops needed for a mod-10 counter</summary>
<div class="dc">
<p>Need to count 0…9 (10 states). Smallest n with 2<sup>n</sup> ≥ 10 is n = 4 (2³=8 &lt;10, 2⁴=16 ≥10).</p>
<p>So a mod-10 BCD counter needs <b>4 flip-flops</b>, with combinational logic to reset/rescue counts 10–15.</p>
</div></details>
<div class="box trap"><div class="lbl">GATE trap</div>
Ripple counters are <b>slowest</b> (delay accumulates through n FFs) yet students pick them as fastest. Also,
a mod-M counter uses ⌈log<sub>2</sub> M⌉ FFs — not M FFs (that's M <i>states</i>, not FFs, unless it's a ring
counter). And unused states must be handled (start-up reset) else the counter may "hang".
</div>
"""),
  CH("shiftreg", "Shift Registers", """
<p>A shift register is a chain of D flip-flops that moves data one position per clock.</p>
<table>
<tr><th>Type</th><th>Input</th><th>Output</th><th>Use</th></tr>
<tr><td>SISO</td><td>1 bit serial</td><td>1 bit serial</td><td>delay line</td></tr>
<tr><td>SIPO</td><td>1 bit serial</td><td>all bits parallel</td><td>serial→parallel converter</td></tr>
<tr><td>PISO</td><td>parallel load</td><td>serial out</td><td>parallel→serial (e.g. UART tx)</td></tr>
<tr><td>PIPO</td><td>parallel</td><td>parallel</td><td>storage register</td></tr>
</table>
<p>A <b>bi-directional</b> shift register can shift left or right (a set of MUXes choose direction of the next
input = left neighbour, right neighbour, or parallel load). A shift register with feedback becomes a counter:
feedback from the last output to the first gives a <b>ring</b> (Q<sub>1</sub> feeds back directly) or a
<b>Johnson</b> (Q<sub>n</sub>′ feeds back).</p>
<div class="box trap"><div class="lbl">GATE trap</div>
Loading a shift register serially takes <b>n clocks</b>, but a PIPO load is <b>1 clock</b>. A SIPO in→parallel out also takes n clocks to fill. Students often answer "1 clock" for serial load. Also, a shift register is still a sequential circuit — it has no combinational feedback but stores state.
</div>
""")]})
# -------------------------------------------------------------- 8. FSM design
S.append({
 "id": "fsm", "title": "Finite State Machines", "children": [
  CH("fsmbasics", "FSM Fundamentals & Design Procedure", """
<p>A <b>FSM</b> (sequential machine) is defined by states, inputs, a transition function and (for Mealy) an
output on the transition or (for Moore) on the state. Design procedure:</p>
<ol>
<li><b>State diagram</b> → <b>state table</b> (current state, input, next state, output).</li>
<li><b>State assignment</b>: assign binary codes to states (minimum ⌈log<sub>2</sub> #states⌉ bits).</li>
<li><b>Derive flip-flop excitation</b> for each state bit (using the excitation tables).</li>
<li><b>K-map</b> the next-state and output logic; draw the circuit.</li>
</ol>
<div class="box formula"><div class="lbl">Mealy vs Moore</div>
<table>
<tr><th></th><th>Mealy</th><th>Moore</th></tr>
<tr><td>Output depends on</td><td>state <b>and</b> input</td><td>state <b>only</b></td></tr>
<tr><td>Output timing</td><td>may change during a clock (combinational)</td><td>stable across the whole clock</td></tr>
<tr><td>States needed</td><td>≤ (usually fewer)</td><td>≥ (often more)</td></tr>
<tr><td>Output glitches</td><td>possible (input changes)</td><td>glitch-free</td></tr>
</table>
</div>
<p>Any FSM's function can be represented by either a Mealy or a Moore machine; they are equivalent in
behaviour. FSM also ↔ regular language (deterministic vs non-deterministic holds — a DFA equivalent exists
for every NFA via subset construction).</p>
<div class="box trap"><div class="lbl">GATE trap</div>
<b>Moore output is associated with the state; it does not depend on the current input.</b> Students misread a
state-transition diagram and compute the Moore output as if Mealy. Also specifying a Moore machine requires
an output per state (not per transition), so Moore machines with many outputs are large. Both machines are
equivalent in <i>input–output language</i>, so don't claim Moore has fewer states (it rarely does).
</div>
"""),
  CH("fsmseq", "Sequence Detector & Counting FSM", """
<p>Classic GATE pattern: <b>sequence detector</b> — recognise a bit pattern like "101". Build states for the
prefix matched so far; when the pattern is complete raise an output.</p>
<details><summary>Worked example — Moore sequence detector for "101", overlapping allowed</summary>
<div class="dc">
<p>States: S0 (none matched), S1 (matched "1"), S2 (matched "10"), S3 (matched "101" → output 1).</p>
<p>Transitions (input bit):<br>
S0 --1--> S1 ; S0 --0--> S0<br>
S1 --0--> S2 ; S1 --1--> S1 (overlap: a 1 after a 1 is still a fresh "1")<br>
S2 --1--> S3(out=1) ; S2 --0--> S0<br>
S3 --0--> S2 ; S3 --1--> S1 (overlapping: after detecting 101, the last bit 1 starts a new pattern)<br>
The <b>overlap handling</b> is where marks are won — rechecking shared prefixes after a full match.</p>
</div></details>
<div class="box tip"><div class="lbl">Tip</div>
For overlap designs, always draw the partial-match "next" transition from the accepting state back to the
longest proper match (here a trailing 1 → S1). Skipping this costs 1–2 marks on a 2-mark FSM question.
</div>
""")]})
# -------------------------------------------------- 9. Timing & hazards
S.append({
 "id": "timing", "title": "Propagation Delay, Setup/Hold & Hazards", "children": [
  CH("timing2", "Delay, Setup & Hold Time", """
<div class="box formula"><div class="lbl">The two timing constraints — memorise both</div>
Let t<sub>clk-q</sub> = clock-to-output delay of a FF, t<sub>comb</sub> = combinational delay to the next FF's
input, t<sub>setup</sub> = setup time, t<sub>hold</sub> = hold time.<br>
<b>Setup (max period):</b> T<sub>clk</sub> ≥ t<sub>clk-q</sub> + t<sub>comb</sub> + t<sub>setup</sub>
&nbsp;→&nbsp; max frequency f<sub>max</sub> = 1 / (t<sub>clk-q</sub> + t<sub>comb</sub> + t<sub>setup</sub>).<br>
<b>Hold (min path):</b> t<sub>clk-q</sub> + t<sub>comb,min</sub> ≥ t<sub>hold</sub> (data must not change too
soon after the edge).<br>
<b>Critical path</b> = the <i>longest</i> combinational + FF delay between two FFs — it sets the clock period.
</div>
<table>
<tr><th>Parameter</th><th>Definition</th><th>Violated when</th></tr>
<tr><td>Propagation delay t<sub>pd</sub></td><td>input→output change of a gate</td><td>— (fix by faster gates / shorter path)</td></tr>
<tr><td>Setup time</td><td>data must be valid <i>before</i> the clock edge</td><td>period too short</td></tr>
<tr><td>Hold time</td><td>data must stay valid <i>after</i> the clock edge</td><td>short combinational path (clock skew)</td></tr>
<tr><td>Critical path delay</td><td>max t<sub>clk-q</sub>+t<sub>comb</sub>+t<sub>setup</sub></td><td>sets f<sub>max</sub></td></tr>
</table>
<details><summary>Worked example — max clock frequency for given delays</summary>
<div class="dc">
<p>t<sub>clk-q</sub> = 4 ns, t<sub>comb</sub> = 10 ns, t<sub>setup</sub> = 2 ns, t<sub>hold</sub> = 3 ns.</p>
<p>Setup: T ≥ 4 + 10 + 2 = 16 ns → f<sub>max</sub> = 1/16 ns = <b>62.5 MHz</b>.</p>
<p>Hold check: t<sub>clk-q</sub> + t<sub>comb,min</sub> ≥ 3. If t<sub>comb,min</sub> ≥ 0, 4+0=4 ≥ 3 ✓ (no hold violation).</p>
<p>Hold time does <b>not</b> limit the (max) frequency here; only setup does.</p>
</div></details>
<div class="box trap"><div class="lbl">GATE trap</div>
<b>Hold time limits the shortest path, setup limits the longest.</b> A short combinational path (or clock skew
causing the destination FF to clock early) causes a <b>hold violation</b>, which adding delay fixes — adding
delay does <i>not</i> fix a setup violation. Also, propagation delay and critical path are not the same thing:
critical path is the worst-case across the whole register-to-register path.
</div>
"""),
  CH("hazard", "Static & Dynamic Hazards", """
<p>A <b>hazard</b> is a transient (glitch) on an output when only one input changes, caused by unequal gate
delays on reconvergent paths.</p>
<table>
<tr><th>Type</th><th>Cause</th><th>Fix</th></tr>
<tr><td>Static-1</td><td>two paths carry complementary signals to an OR; one turns off before other turns on</td><td>add redundant consensus term (AB′ + BC‒style)</td></tr>
<tr><td>Static-0</td><td>complementary AND reconvergence</td><td>add redundant sum term</td></tr>
<tr><td>Dynamic</td><td>output changes 0→1 or 1→0 but glitches to the old value mid-way</td><td>equalise path delays</td></tr>
<tr><td>Data hazard</td><td>pipelined functional hazard between dependent instructions</td><td>forwarding / stall</td></tr>
</table>
<div class="box formula"><div class="lbl">Hazard detection rule</div>
A function has a static <b>1-hazard</b> between two <i>adjacent</i> minterms (differ in one variable) if they
are covered by <b>different K-map groups</b> — joining them with the consensus/implicant removes the glitch.
Static-0 hazards are symmetric on the POS side.
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
Hazards are a <b>combinational</b> glitch phenomenon; a "data hazard" in pipelining is a related but <b>different</b>
term (RAW/WAR/WAW forwarding). Don't mix them. A hazard is NOT a timing error that changes the "steady" truth
table — the final output is correct; only the transient glitches. Adding the consensus term removes the race
without changing the function.
</div>
""")]})
# ----------------------------------------------------------- 10. Formula sheet
S.append({
 "id": "formulas", "title": "One-Page Formula Sheet",
 "html": """
<table>
<tr><th>Area</th><th>Formula / fact</th></tr>
<tr><td>Unsigned range</td><td>n bits → 0 … 2<sup>n</sup>−1</td></tr>
<tr><td>2's complement range</td><td>−2<sup>n−1</sup> … +2<sup>n−1</sup>−1</td></tr>
<tr><td>Negation (2's)</td><td>flip all bits + 1; or copy up to first 1 then flip</td></tr>
<tr><td>Subtraction</td><td>a − b = a + (2's complement of b), discard carry-out</td></tr>
<tr><td>Half adder</td><td>S = A⊕B, C = AB</td></tr>
<tr><td>Full adder</td><td>S = A⊕B⊕Cin, Cout = AB + Cin(A⊕B)</td></tr>
<tr><td>Ripple vs CLA</td><td>delay O(n) vs O(log n)</td></tr>
<tr><td>De Morgan</td><td>(A+B)′ = A′B′ · (AB)′ = A′+B′</td></tr>
<tr><td>Absorption / Consensus</td><td>A+AB = A · AB+A′C+BC = AB+A′C</td></tr>
<tr><td>Universal gates</td><td>NAND and NOR; XOR/XNOR are NOT universal</td></tr>
<tr><td>K-map group</td><td>2<sup>k</sup> cells drops k variables; wrap-around allowed</td></tr>
<tr><td>MUX / decoder</td><td>n-select MUX → 2<sup>n</sup> data in; n in → 2<sup>n</sup> decoder out</td></tr>
<tr><td>Binary ↔ Gray</td><td>G<sub>k</sub> = B<sub>k</sub>⊕B<sub>k+1</sub>; B<sub>k</sub> = B<sub>k+1</sub>⊕G<sub>k</sub></td></tr>
<tr><td>Excess-3</td><td>= BCD + 3, self-complementing</td></tr>
<tr><td>SR / D / JK / T</td><td>Q+ = S+R′Q · Q+=D · Q+=JQ′+K′Q · Q+=T⊕Q</td></tr>
<tr><td>JK→D / JK→T / D→T</td><td>J=D,K=D′ · J=K=T · D = T⊕Q</td></tr>
<tr><td>Modulo counter</td><td>mod-M needs ⌈log<sub>2</sub> M⌉ flip-flops</td></tr>
<tr><td>Ring / Johnson</td><td>n FFs → mod n / mod 2n</td></tr>
<tr><td>Setup</td><td>T ≥ t<sub>clk-q</sub> + t<sub>comb</sub> + t<sub>setup</sub> → f_max</td></tr>
<tr><td>Hold</td><td>t<sub>clk-q</sub> + t<sub>comb,min</sub> ≥ t<sub>hold</sub></td></tr>
<tr><td>Static hazard</td><td>adjacent minterms in different groups → 1-hazard; add consensus</td></tr>
</table>
<div class="box tip"><div class="lbl">Revise-from-formula-sheet drill</div>
Each morning, write the five FF characteristic equations, the Gray formulas and the setup/hold inequality
from memory — 5 minutes, done before any practice set. These three are the highest-recurrence facts in GATE CS
Digital Logic.
</div>
""",
})
# ------------------------------------------------------------------- 11. Strategy
S.append({
 "id": "strategy", "title": "Exam Strategy",
 "html": """
<p>Digital Logic is worth <b>7 marks</b> and is one of the fastest, safest blocks. Work it early in the paper —
the rules are mechanical and you rarely run out of time on them.</p>
<table>
<tr><th>Question type</th><th>Time budget</th><th>Tactic</th></tr>
<tr><td>2's complement / number conversion</td><td>90 s</td><td>Answer first; verify with the bound (max value) in your head.</td></tr>
<tr><td>K-map minimisation</td><td>3–4 min</td><td>Draw, group power-of-2 cells, count literals. Don't forget wrap-around.</td></tr>
<tr><td>MUX / decoder realisation</td><td>3 min</td><td>Shannon-expand; for n-var with (n−1)-select use the last var as data.</td></tr>
<tr><td>Counter / FF arithmetic</td><td>2–3 min</td><td>Write the state seq + excitation column before wiring.</td></tr>
<tr><td>Setup/hold &amp; max frequency</td><td>2 min</td><td>Sum the worst path, invert. Setup limits max, hold limits min.</td></tr>
<tr><td>Hazard / CMOS questions</td><td>1–2 min</td><td>Recall the rule (complement pull-up; consensus fix) and move on.</td></tr>
</table>
<div class="box">What to skip under time pressure
<ul>
<li><b>Skip</b> long FSM state-table designs (Multi-step) if short on time — they are worth 2 marks but need
5+ minutes. Do number conversion, K-map and gate universality first.</li>
<li><b>Skip</b> dynamic-hazard path-equalisation questions unless given explicit delays — they are rare and slow.</li>
<li><b>Never skip</b> a K-map or 2's-complement question; they are the highest accuracy-per-minute in the block.</li>
</ul>
</div>
<div class="box trap"><div class="lbl">Final-tick checklist</div>
Watch for: signed overflow (same-sign adds), SR=S=R=1, pack padding side for hex, MUX vs decoder direction,
setup (long path) vs hold (short path), and Moore output = state-only. These five traps cover the bulk of
wrong answers in Digital Logic papers.
</div>
"""
})
QUIZ = [
 {"q":"The 8-bit binary representation of decimal 53 is:","opts":["110101","11011","101101","111001"],"a":0,
  "ex":"53 = 32 + 16 + 4 + 1 = 110101₂. Option B is 27 (11011), C is 45 (101101), D is 57 (111001)."},
 {"q":"The range of a 6-bit signed number in 2's complement is:","opts":["0 to 63","−32 to +31","−31 to +32","−64 to +63"],"a":1,
  "ex":"n-bit 2's complement covers −2^(n−1) to +2^(n−1)−1 = −32 to +31. The asymmetry (no +32) is the giveaway."},
 {"q":"The 8-bit 2's complement representation of −9 is:","opts":["11110110","11110111","11111001","00001011"],"a":1,
  "ex":"+9 = 00001001. Invert → 11110110, add 1 → 11110111. Option A is the 1's complement of 9 (missing +1)."},
 {"q":"Which single gate type is NOT sufficient by itself to implement any Boolean function?","opts":["NOR","NAND","XOR","NAND and NOR"],"a":2,
  "ex":"NOR and NAND are universal. A 2-input XOR alone cannot realise a general function (it can only flip parity); it is not universal."},
 {"q":"The Boolean expression AB + AB′ simplifies to:","opts":["A","B","AB","1"],"a":0,
  "ex":"Factor A: A(B + B′) = A·1 = A. This is the algebraic form of combining two adjacent K-map cells."},
 {"q":"By De Morgan's theorem, (A·B)′ equals:","opts":["A′·B′","A′ + B′","A + B","(A+B)′"],"a":1,
  "ex":"(A·B)′ = A′ + B′ — complement each variable and swap AND for OR. Option A is the complement of the sum, not the product."},
 {"q":"A minimal SOP for F(A,B,C) = Σm(0,1,3,7) is:","opts":["A′B′ + BC","ABC + A′B′C","B + C","A + B"],"a":0,
  "ex":"Group 000,001 → A′B′; group 011,111 → BC. Both minterm sets covered: F = A′B′ + BC."},
 {"q":"A multiplexer with n select lines has how many data inputs?","opts":["n","2ⁿ","n·2","n²"],"a":1,
  "ex":"An n-select MUX selects among 2ⁿ data lines (n selects address 2ⁿ positions). A decoder is the reverse direction."},
 {"q":"A binary-to-2ⁿ output decoder with n inputs produces exactly:","opts":["n outputs","n² outputs","2ⁿ outputs","2n outputs"],"a":2,
  "ex":"n input bits encode 2ⁿ distinct codes, each activating exactly one of the 2ⁿ output lines."},
 {"q":"The Sum output of a half adder is:","opts":["A·B","A ⊕ B","A + B","(A+B)′"],"a":1,
  "ex":"Half-adder sum = A⊕B (carry = A·B). It is 1 when exactly one input is 1."},
{"q":"A Johnson (twisted-ring) counter built from n flip-flops has a modulus of:","opts":["n","2n","2ⁿ","n/2"],"a":1,
  "ex":"Feeding back the complement of the last stage yields a 2n-state count (half the 2ⁿ states), doubling a plain ring's length."},
 {"q":"A ring counter made of 4 flip-flops counts through how many distinct states?","opts":["4","8","16","2"],"a":0,
  "ex":"A ring counter has exactly one 1 circulating → n states for n FFs. 2ⁿ−n states are left unused."},
 {"q":"How many flip-flops are required to build a mod-12 counter?","opts":["3","4","5","12"],"a":1,
  "ex":"Smallest n with 2ⁿ ≥ 12 is n = 4 (2³=8 < 12 ≤ 16=2⁴). You need 4 FFs plus logic to skip states 12–15."},
 {"q":"The characteristic equation of a D flip-flop is:","opts":["Q⁺ = Q","Q⁺ = D","Q⁺ = D′","Q⁺ = T⊕Q"],"a":1,
  "ex":"A D flip-flop simply copies its input: next state = D. That is why D-FF counters need the least feedback logic."},
 {"q":"For a JK flip-flop with J = 1 and K = 1 on a clock edge, the state:","opts":["sets to 1","resets to 0","toggles","is unchanged"],"a":2,
  "ex":"J=K=1 gives Q⁺ = JQ′ + K′Q = Q′ — the output toggles. This is the state SR would not allow."},
 {"q":"With t_clk-q = 3 ns, t_comb = 12 ns and t_setup = 2 ns, the maximum clock frequency is closest to:","opts":["66.7 MHz","58.8 MHz","50 MHz","83.3 MHz"],"a":1,
  "ex":"T ≥ 3 + 12 + 2 = 17 ns, so f_max = 1/(17 ns) ≈ 58.8 MHz. Only the setup (longest-path) sum matters here."},
 {"q":"Which statement about flip-flop timing is TRUE?","opts":["Hold time limits the longest path","Setup time limits the longest path, hold time the shortest","Both setup and hold limit the longest path","Hold time is independent of path length"],"a":1,
  "ex":"Setup constrains the max period (longest register-to-register path); hold constrains the min path delay (data must not change too early)."},
 {"q":"The (forbidden / invalid) input combination of an SR latch is:","opts":["S=R=0","S=0, R=1","S=1, R=0","S=R=1"],"a":3,
  "ex":"S=R=1 drives both cross-coupled outputs toward 0 at once — indeterminate/prevented. This is exactly why the JK flip-flop was invented."},
 {"q":"Which code is self-complementing (9's complement = bit-flip)?","opts":["BCD","Excess-3","Gray code","Sign-magnitude"],"a":1,
  "ex":"Excess-3 code = BCD + 3 is self-complementing: complementing bits gives the 9's complement. Pure BCD is not."},
 {"q":"The Gray code corresponding to binary 1011 is:","opts":["1110","1101","1011","1001"],"a":0,
  "ex":"G₃=1; G₂=1⊕0=1; G₁=0⊕1=1; G₀=1⊕1=0 → 1110. Gray of 10 is 1111 and of 11 is 1110 — one bit apart, as required."},
]
SUBJECT = {
 "code": "S02", "title": "Digital Logic",
 "subtitle": "GATE CS 2027 · 7 marks · Boolean & K-map, combinational/sequential design, number systems, CMOS & timing",
 "weight_note": "GATE CS 2027 · Digital Logic section (7 marks)",
 "sections": S, "quiz": QUIZ,
}
