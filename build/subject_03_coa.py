# -*- coding: utf-8 -*-
"""Subject 03 — Computer Organization & Architecture (8 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

# ---------------------------------------------------------------- 1. Overview
S.append({
 "id": "coa-overview", "title": "Overview & Weightage",
 "html": """
<div class="kv">
  <span class="chip">Marks <b>8 / 100</b></span>
  <span class="chip">Typical Qs <b>4–6</b></span>
  <span class="chip">Signature topic <b>Pipelining + Cache</b></span>
  <span class="chip">Scoring <b>High, formula-driven</b></span>
</div>
<p>COA is one of the most <b>reliable sources of numeric marks</b> in GATE CS. A large fraction of the
questions are one-line computations about <b>cache performance, average memory access time, accumulator
CPI, and pipelining speedup</b> — learn the three or four formulas and you convert raw facts into marks.
It also overlaps with <b>OS (virtual memory/MMU)</b> and <b>Digital Logic (ALU/data-path)</b>.</p>

<h3>What it contains</h3>
<table>
<tr><th>Topic</th><th>Typical marks</th><th>Difficulty</th><th>Priority</th></tr>
<tr><td>Instruction formats &amp; addressing modes</td><td>1–2</td><td>Easy</td><td>★★★★★</td></tr>
<tr><td>ALU, data-path &amp; control unit</td><td>1–2</td><td>Easy–Medium</td><td>★★★★☆</td></tr>
<tr><td>Pipelining &amp; hazards</td><td>2–3</td><td>Medium–Hard</td><td>★★★★★</td></tr>
<tr><td>Memory hierarchy &amp; cache</td><td>2–3</td><td>Medium</td><td>★★★★★</td></tr>
<tr><td>I/O — interrupt &amp; DMA</td><td>1</td><td>Easy</td><td>★★★☆☆</td></tr>
</table>

<div class="box tip"><div class="lbl">How to study this for GATE 2027</div>
<ol>
<li><b>Cache + AMAT first</b> — the single highest-yield numeric cluster.</li>
<li><b>Pipelining speedup/CPI next</b> — second guaranteed numeric cluster.</li>
<li><b>Addressing modes and control unit</b> — quick conceptual marks.</li>
<li><b>I/O (interrupt/DMA)</b> — pure memorisation, finish late.</li>
<li><b>Practise past questions</b> — GATE reuses the same cache and pipeline patterns with different numbers.</li>
</ol>
</div>

<div class="box trap"><div class="lbl">Negative marking reality</div>
MCQs carry −1/3 (1-mark) and −2/3 (2-mark); <b>NAT (numeric) questions have no negative marking</b>.
The cache AMAT and pipeline speedup questions are frequently asked as NATs — if you can bound the
value, always attempt them; never blind-guess MCQs.
</div>
"""
})

# --------------------------------------- 2. Machine instructions & addressing
S.append({
 "id": "instructions", "title": "Machine Instructions & Addressing Modes", "children": [
  CH("instfmt", "Instruction Formats", """
<p>An <b>instruction</b> = <b>opcode</b> (what operation) + one or more <b>address/operand fields</b>
(where the data is). Edward Sutherland's observation: an instruction is 8/9 opcode and 1/9 operands —
most instruction bits are consumed by addresses.</p>

<h4>Instruction-set design philosophies</h4>
<table>
<tr><th>Feature</th><th>RISC</th><th>CISC</th></tr>
<tr><td>Instruction length</td><td>Fixed (e.g. 32-bit)</td><td>Variable</td></tr>
<tr><td>Operands</td><td>Register-only (load/store)</td><td>Memory operands allowed</td></tr>
<tr><td>Addressing modes</td><td>Few, simple</td><td>Many, complex</td></tr>
<tr><td>Example</td><td>MIPS, ARM, RISC-V</td><td>x86, 8086</td></tr>
<tr><td>Typical advantage</td><td>Easier pipelining</td><td>Denser code</td></tr>
</table>

<div class="box formula"><div class="lbl">Instruction length vs operand count</div>
For a memory.I/O-less register machine: <b>instruction bits</b> = log<sub>2</sub>(#opcodes) +
r × log<sub>2</sub>(#registers) + immediate-width, where r = number of register operands.<br>
So with 64 opcodes, 3 register operands and 16 registers: 6 + 3×4 = <b>18 bits</b> (no immediate).
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
RISC is <b>not</b> "having fewer instructions" — it means fixed-length, register-based instructions that
enable deep pipelining. CISC is <b>not</b> simply "more instructions". Trap questions conflate fixed-length
with "simple" or "fewer opcodes".
</div>
"""),
  CH("addrmodes", "Addressing Modes & Effective Address", """
<p>The <b>effective address (EA)</b> is the final address actually used to reach the operand. Different
modes change only how the EA is computed — the opcode never changes.</p>
<table>
<tr><th>Mode</th><th>Effective address (EA)</th><th>Example / use</th></tr>
<tr><td>Immediate</td><td>operand is <b>in the instruction</b> (no EA)</td><td>ADD R1, #5</td></tr>
<tr><td>Direct (absolute)</td><td>EA = address field A</td><td>LOAD R1, 2000</td></tr>
<tr><td>Indirect</td><td>EA = M[A]</td><td>pointer to pointer</td></tr>
<tr><td>Register</td><td>operand in register R</td><td>ADD R1, R2</td></tr>
<tr><td>Register indirect</td><td>EA = content of register R</td><td>LOAD R1, (R2)</td></tr>
<tr><td>Displacement / Indexed</td><td>EA = A + (register)</td><td>array access, x[i]</td></tr>
<tr><td>Base + offset (stack)</td><td>EA = (base reg) + offset</td><td>local variables</td></tr>
<tr><td>PC-relative</td><td>EA = PC + offset</td><td>branch instructions</td></tr>
<tr><td>Auto-increment/-decrement</td><td>EA = (R), then R=R±k</td><td>stack push/pop</td></tr>
</table>

<div class="box formula"><div class="lbl">Memory references per operand</div>
Memory operands need <b>1 (direct)</b> or <b>2 (indirect)</b> memory accesses to fetch the operand
beyond the instruction fetch itself. Immediate and register modes need <b>zero</b> extra memory accesses —
this is why loop bodies are optimised to use registers.
</div>

<details><summary>Worked example — effective address and operand</summary>
<div class="dc">
<p>Instruction <code>ADD R1, 500(R2)</code> (displacement mode). Main memory M has M[504]=10,
M[1000]=40, M[1200]=25. Register R2 = 4.</p>
<p>EA = 500 + (R2) = 500 + 4 = <b>504</b>. Operand = M[504] = <b>10</b>.
Meaning: add the value 10 (not the address 504) into register R1.</p>
<p>Trap: students read M[500+R2]=M[504] but then report the <i>address</i> 504 instead of the
<i>operand value</i> M[504]=10.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
For <b>indirect</b> mode the operand is at <b>M[M[A]]</b> — two levels. For <b>register indirect</b> the
operand is at <b>M[(R)]</b>. Many questions give memory contents and ask for the operand value; always
read the value at the EA, do not stop at the address itself.
</div>
""")]
})

# ------------------------------------------------------ 3. ALU & representation
S.append({
 "id": "alu", "title": "ALU, Number Representation & Flags", "children": [
  CH("numrep", "Integer Representation & ALU Operations", """
<div class="box formula"><div class="lbl">2's complement — the only form that matters</div>
Range of n-bit 2's complement: <b>−2<sup>n−1</sup> … +2<sup>n−1</sup>−1</b>.<br>
Negate a number: invert all bits then add 1. <code>−x = ~x + 1</code>.<br>
The <b>ALU uses one adder and a selectable 2's-complement unit</b> — subtraction is just
<code>A + (~B + 1)</code> with Cin=1; there is no separate subtractor.
</div>
<p>Signed magnitude keeps a sign bit but wastes a pattern (−0) and needs separate add/sub logic —
2's complement has a <b>single representation of zero</b> and <b>one adder</b>, reasons it won.</p>
<ul>
<li><code>0000 0001</code> = 1 ; <code>1111 1111</code> = −1 ; <code>1000 0000</code> (8-bit) = <b>−128</b>.</li>
<li>Overflow in addition happens when the <b>carry into the sign bit ≠ carry out of the sign bit</b>.</li>
<li>Two positives never overflow into a <i>negative</i> result unless the sum exceeds the range.</li>
</ul>
<div class="box formula"><div class="lbl">ALU function units</div>
ALU = combinational circuit computing one of: <b>Add, Sub, AND, OR, NOR, XOR, Shift, Compare</b>.
The answer of every unit is computed in parallel and the <b>function-select lines pick one via a multiplexer</b>.
Shift left by k = multiply by 2<sup>k</sup>; shift right arithmetic (SAR) = divide by 2<sup>k</sup>
(preserving the sign bit).
</div>
<div class="box trap"><div class="lbl">GATE trap</div>
Overflow (incorrect result) is <b>not the same as carry-out</b>. A carry-out of the sign bit is discarded in
2's complement; overflow is a <i>separate</i> V flag set only when the signed result is out of range.
Arithmetic <b>right shift is not the same as logical right shift</b> — SAR fills with the sign bit.
</div>
"""),
  CH("flags", "Condition Codes (Flags)", """
<p>Flags are 1-bit outputs latched after every ALU operation, readable by the control unit for decisions.</p>
<table>
<tr><th>Flag</th><th>Meaning</th><th>Set when…</th></tr>
<tr><td>C (Carry)</td><td>unsigned overflow</td><td>carry out of the MSB (addition)</td></tr>
<tr><td>Z (Zero)</td><td>result is zero</td><td>all result bits are 0</td></tr>
<tr><td>N (Sign/Negative)</td><td>result is negative</td><td>MSB of result = 1</td></tr>
<tr><td>V (oVerflow)</td><td>signed overflow</td><td>carry-in ≠ carry-out at sign bit</td></tr>
<tr><td>P (Parity)</td><td>parity of result (even = 1)</td><td>based on XOR of result bits</td></tr>
</table>
<p>Comparisons and branch conditions built from flags: EQ ⇒ Z, NE ⇒ ¬Z, LT ⇒ N⊕V (signed),
unsigned LT ⇒ ¬C·Z etc.</p>

<details><summary>Worked example — overflow detection in 8-bit addition</summary>
<div class="dc">
<p>Add <code>0111 1111</code> (+127) and <code>0000 0001</code> (+1) → <code>1000 0000</code> (−128).</p>
<p>Carry into sign bit = 1, carry out = 0 → they differ ⇒ <b>V = 1 (signed overflow)</b>: result −128 is wrong;
true sum +128 is out of the 8-bit signed range.</p>
<p>As <b>unsigned</b> numbers: 127+1 = 128 fits in 8 bits, no unsigned overflow → C = 0.</p>
</div></details>
""")]
})

# ------------------------------------------------ 4. Data-path & control unit
S.append({
 "id": "datapath", "title": "Data-path & Control Unit", "children": [
  CH("dp", "Data-path Design", """
<p>The <b>data-path</b> is the network of registers, ALU and buses that instructions travel through; the
<b>control unit</b> fires the right control signals at the right clock edges.</p>
<h4>Core data-path components</h4>
<ul>
<li><b>PC</b> (program counter) — address of next instruction; PC-relative branch adds signed offset.</li>
<li><b>IR</b> (instruction register) — holds the fetched instruction while it is decoded/executed.</li>
<li><b>Register file</b> — two read ports + one write port.</li>
<li><b>ALU</b> — combinational arithmetic/logic with MUX-selected operands (register or sign-extended immediate).</li>
<li><b>Sign-extension unit</b> — extends 16-bit immediates to 32 bits before the ALU.</li>
<li><b>Multiplexers</b> — choose between register data and immediate (operand), and between ALU result and memory
data (write-back).</li>
</ul>

<div class="box formula"><div class="lbl">Single-cycle vs multi-cycle vs pipelined</div>
<table>
<tr><th>Model</th><th>Clock period</th><th>CPI</th><th>Throughput</th></tr>
<tr><td>Single-cycle</td><td>= slowest instruction (fixed, max)</td><td>1</td><td>1 instr/period (low)</td></tr>
<tr><td>Multi-cycle</td><td>= one step's delay (short)</td><td>variable (&gt;1)</td><td>better</td></tr>
<tr><td>Pipelined</td><td>= longest stage (short)</td><td>→ 1</td><td>≈ clock rate (high)</td></tr>
</table>
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
Single-cycle has CPI = 1 but its clock period is the <b>worst-case</b> instruction time — so it is
<i>not</i> fast. Multi-cycle uses a shorter clock but CPI &gt; 1. Pipelining claims the "one instruction
per cycle" figure <i>in steady state</i> only, ignoring filling/flushing and stalls.
</div>
"""),
  CH("ctl", "Hardwired vs Microprogrammed Control", """
<table>
<tr><th>Criterion</th><th>Hardwired</th><th>Microprogrammed</th></tr>
<tr><td>Control signals</td><td>Combinational logic from opcode + state</td><td>Stored as micro-instructions in a control store (ROM)</td></tr>
<tr><td>Speed</td><td>Fast (RISC)</td><td>Slower (reads control memory)</td></tr>
<tr><td>Flexibility / modifiability</td><td>Hard to change (rewire/fabricate)</td><td>Easy — edit microcode</td></tr>
<tr><td>Cost of complex instructions</td><td>Bleeds into logic</td><td>Handled by more micro-steps</td></tr>
<tr><td>Typical home</td><td>RISC, modern CPUs</td><td>CISC, early computers (VAX, 8086 microcode)</td></tr>
</table>
<p>A <b>micro-instruction</b> is one row of the control store; it controls one clock step, e.g.
<code>PCout → MARin</code>, with an explicit <b>next-address</b> field (branching/dispatch).</p>
<div class="box tip"><div class="lbl">Shortcut / tip</div>
Remember the trade-off as a clean dichotomy: <b>hardwired = speed, microprogrammed = flexibility</b>.
Any GATE question asking "which is faster" answers hardwired; "which is easier to modify" answers
microprogrammed.
</div>
"""
"")]
})

# ------------------------------------------------- 5. Instruction pipelining
S.append({
 "id": "pipelining", "title": "Instruction Pipelining & Speedup", "children": [
  CH("pipe", "The Pipeline Model", """
<p>A <b>pipeline</b> overlaps execution of consecutive instructions. The classic 5-stage MIPS pipeline:</p>
<table>
<tr><th>Stage</th><th>Name</th><th>Main function</th></tr>
<tr><td>IF</td><td>Instruction Fetch</td><td>read memory at PC; PC = PC + 4</td></tr>
<tr><td>ID</td><td>Instruction Decode</td><td>decode, read register file</td></tr>
<tr><td>EX</td><td>Execute</td><td>ALU operation / effective address</td></tr>
<tr><td>MEM</td><td>Memory Access</td><td>load / store data</td></tr>
<tr><td>WB</td><td>Write Back</td><td>write result to register file</td></tr>
</table>
<p>Each stage is bounded by <b>pipeline registers</b> (IF/ID, ID/EX, EX/MEM, MEM/WB) that hand data to the
next stage at the clock edge. The clock period becomes the <b>longest stage</b>, so stages should be
balanced.

<div class="box formula"><div class="lbl">Pipelining speedup (no stalls)</div>
n instructions through k stages: <b>clock cycles = k + (n − 1)</b>.<br>
Speedup = (time without pipeline) / (time with pipeline) = <b>(n·k) / (k + n − 1)</b>.<br>
As n → ∞ : speedup → <b>k</b> (ideal, the number of stages).<br>
Effective speedup when the pipeline runs at CPI = CPI<sub>eff</sub>: <b>Speedup = k / CPI<sub>eff</sub></b>
(with CPI<sub>eff</sub> = 1 + stalls-penalty under the ideal-k model).
</div>

<details><summary>Worked example — speedup for 100 instructions, 5 stages</summary>
<div class="dc">
<p>Non-pipelined: 100 × 5 = <b>500 cycles</b>. Pipelined (no stalls): 5 + (100−1) = <b>104 cycles</b>.</p>
<p>Speedup = 500 / 104 ≈ <b>4.81</b> (approaches the ideal 5 as n grows and stalls vanish).</p>
<p>Check with n = 4: 5 + 3 = 8 cycles; non-pipelined 20; speedup 20/8 = <b>2.5</b> — clearly n dependent.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Speedup = k is the limit <b>only for infinitely many ideal instructions</b>. For small n it is much less;
with stalls it is further reduced. Also the pipelined cycle count uses <b>k + (n−1)</b>, not n·k — students
who write n·k to the pipeline forget that only the first instruction pays the full k stages.
</div>
"""),
  CH("spd", "Throughput & Latency", """
<p>Use period = (longest stage) + register overhead for the pipeline clock; non-pipelined period = whole
instruction time. These two feed every throughput calculation.</p>
<div class="box formula"><div class="lbl">Throughput & latency</div>
<b>Throughput</b> = instructions/time = n / (k + n − 1) ≈ <b>1 instruction/cycle</b> in steady state.<br>
<b>Latency</b> of one instruction = k cycles (worst), i.e. 1 / clock.<br>
Absolute speedup against a single-cycle machine: S = T<sub>single</sub>/T<sub>pipeline</sub>; against a
multi-cycle machine use total cycles.
</div>

<details><summary>Worked example — effect of a stall on speedup</summary>
<div class="dc">
<p>5-stage pipeline, 1000 instructions, and every 10th instruction causes a 1-cycle stall (100 stalls).</p>
<p>Total cycles = 5 + (999) + 100 = <b>1104</b>. Non-pipelined = 5000 cycles.<br>
Speedup = 5000 / 1104 ≈ <b>4.53</b> (down from ideal 4.98 with zero stalls, i.e. 5+999=1004).</p>
<p>General rule: <b>each stall adds exactly its penalty in cycles</b>; stalls eat into the theoretical speedup.</p>
</div></details>
""")]
})

# ----------------------------------------------------- 6. Pipeline hazards
S.append({
 "id": "hazards", "title": "Pipeline Hazards & Handling", "children": [
  CH("haz", "Types of Hazards", """
<p>A <b>hazard</b> is any condition that prevents the next instruction from executing in the next cycle.</p>
<table>
<tr><th>Hazard</th><th>Cause</th><th>Classic example</th><th>Primary remedy</th></tr>
<tr><td>Structural</td><td>Resource conflict (e.g. one memory for IF and MEM)</td><td>load then branch needing memory</td><td>Separate I-cache / D-cache, harvard design</td></tr>
<tr><td>Data (RAW/WAW/WAR)</td><td>Instruction needs a value not yet written</td><td><code>add R1,..</code> then <code>sub ..,R1</code></td><td><b>Forwarding</b> (bypass), stalling</td></tr>
<tr><td>Control</td><td>Branch target not known until EX/MEM</td><td><code>beq</code> followed by instructions</td><td>Branch prediction, delay slot, flushing</td></tr>
</table>
<ul>
<li><b>RAW</b> (read-after-write) — the dangerous, forwardable hazard. <b>WAW</b> (write-after-write) and
<b>WAR</b> (write-after-read) are artifacts of out-of-order pipelines.</li>
<li><b>Forwarding/bypassing</b> sends the ALU result directly back to a later stage's ALU input, avoiding the stall.</li>
<li>When forwarding is impossible (a <b>load-use</b>: result needed in the immediately following cycle),
the pipeline <b>stalls (inserts a bubble)</b>.</li>
<li><b>Control hazard:</b> the instructions after a branch may be wrong; the entry is rolled back (flushed)
when the prediction fails.</li>
</ul>

<div class="box formula"><div class="lbl">Cost of a flush / wrong prediction</div>
Wrongly-predicted branch wastes <b>the number of stages between fetch and the branch decision</b> cycles
(= depth of resolution). Pipeline is flushed of those instructions' results. Perfect prediction, no penalty.
</div>

<div class="box trap"><div class="lbl">GATE trap</div>
Forwarding <b>removes</b> the RAW stall for <code>R1</code> ALU→ALU dependencies but <b>cannot</b> fix a
<code>load → use</code> in the immediately following cycle (the loaded value only arrives at the end of MEM,
one cycle late). That case still needs a stall/bubble. Don't claim forwarding fixes everything.
</div>
"""),
  CH("ctrlhaz", "Branch Handling & Branch Prediction", """
<p>Branch penalties rise with deeper pipelines. Four standard techniques from cheapest to most complex:</p>
<table>
<tr><th>Technique</th><th>Idea</th><th>Wasteful cycles</th></tr>
<tr><td>Freeze / stall</td><td>wait until branch resolves</td><td>branch-resolution depth</td></tr>
<tr><td>Predict not-taken / taken</td><td>fetch a fixed guess</td><td>only when wrong</td></tr>
<tr><td>Branch delay slot</td><td>always execute 1 instruction after branch (compiler-arranged)</td><td>~0 if slot filled</td></tr>
<tr><td>Dynamic prediction (BTB)</td><td>history-based; <b>branch target buffer</b> caches targets</td><td>only on misprediction</td></tr>
</table>
<p>Increasing pipeline depth raises both ideal speedup (k) and the <b>cost of each misprediction</b> — this
trade-off is the recurring GATE "depth vs penalty" question.</p>

<details><summary>Worked example — branch penalty with prediction</summary>
<div class="dc">
<p>5-stage pipeline, branch resolved at the end of EX (stage 3). No prediction: every branch (20% of
instructions) stalls every instruction 3 of its 4 successors → costly. With prediction: 20% of branches
are mispredicted (say 25% of branches mispredict ≈ 5% of instructions), each wrong guess wastes 2 cycles
(the fetch of the 2 wrong instructions).</p>
<p>CPI<sub>ideal</sub> = 1. Branch penalty contribution = 0.05 × 2 = 0.10 → CPI<sub>eff</sub> ≈ <b>1.10</b>
vs 1.0 + big penalty if always stalling. Shows why prediction is used even when imperfect.</p>
</div></details>

<div class="box tip"><div class="lbl">Shortcut / tip</div>
In a hazard table question, first classify <b>RAW = forwardable, control = predict/flush, structural =
resource change</b>. Then apply the numeric penalty: forward removes it; a bubble adds 1 cycle; a flush
adds the stage-depth. Do classification and penalty in two separate mental steps.
</div>
""")]
})

# ---------------------------------------------------- 7. Memory hierarchy/cache
S.append({
 "id": "cache", "title": "Memory Hierarchy & Cache", "children": [
  CH("memhier", "The Hierarchy & Cache Mapping", """
<p>Memory is arranged in a hierarchy trading <b>capacity against speed and cost</b>. Registers (fastest,
smallest) → L1 → L2 → L3 → Main (DRAM) → Disk (secondary storage, largest, cheapest).</p>
<table>
<tr><th>Level</th><th>Technology</th><th>Access time</th><th>Volatile?</th><th>Managed by</th></tr>
<tr><td>Registers</td><td>flip-flops</td><td>~1 ns</td><td>Yes</td><td>compiler</td></tr>
<tr><td>Cache (L1..L3)</td><td>SRAM</td><td>1–10 ns</td><td>Yes</td><td>hardware</td></tr>
<tr><td>Main memory</td><td>DRAM</td><td>50–100 ns</td><td>Yes</td><td>hardware + OS (partly)</td></tr>
<tr><td>Secondary</td><td>SSD / HDD</td><td>ms</td><td>No</td><td>OS</td></tr>
</table>

<h4>Cache mapping schemes</h4>
<table>
<tr><th>Scheme</th><th>Where a block can go</th><th>Replacement</th><th>Pros / Cons</th></tr>
<tr><td>Direct-mapped</td><td>exactly 1 set</td><td>none to choose</td><td>simple, fast, conflict misses</td></tr>
<tr><td>Fully associative</td><td>any set</td><td>LRU etc.</td><td>no conflict misses, costly tags</td></tr>
<tr><td>Set-associative (k-way)</td><td>any of k slots in the set</td><td>LRU among k</td><td>balance of the two</td></tr>
</table>

<div class="box formula"><div class="lbl">Cache geometry — the must-know equations</div>
<b>#sets</b> = cache_size / (block_size × associativity).<br>
<b>#blocks</b> (total) = cache_size / block_size.<br>
From a physical address of <b>B total bits</b>:<br>
<b>offset bits</b> = log<sub>2</sub>(block_size) &nbsp;·&nbsp;
<b>index bits</b> = log<sub>2</sub>(#sets) &nbsp;·&nbsp;
<b>tag bits</b> = B − index − offset.<br>
Block size 2<sup>o</sup> gives <b>o = log<sub>2</sub>(block_size)</b> low bits = offset.
</div>

<details><summary>Worked example — derive sets, index, tag, offset</summary>
<div class="dc">
<p>64 KB cache, 32-byte block, 4-way set associative, 32-bit physical addresses.</p>
<p>offset bits = log<sub>2</sub>32 = <b>5</b>.<br>
#sets = 65536 / (32 × 4) = 512 → index bits = log<sub>2</sub>512 = <b>9</b>.<br>
tag bits = 32 − 9 − 5 = <b>18</b>.</p>
<p>Address 29-bit? It doesn't matter here — tag is always total-bits minus index minus offset.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap</div>
Two classic slips: (1) computing sets as <code>cache/block</code> and forgetting to divide by
<code>associativity</code> first; (2) blurring <b>set</b> (index) bits with <b>block-offset</b> bits. In a
direct-mapped cache associativity = 1 so #sets = #blocks; many students carry that and err on
set-associative questions.
</div>
"""),
  CH("cacheperf", "Cache Performance & AMAT", """
<div class="box formula"><div class="lbl">The core performance formulas</div>
<b>AMAT (average memory access time)</b> = hit_time + miss_rate × miss_penalty.<br>
As an effective time: <b>t<sub>eff</sub> = h·t<sub>hit</sub> + (1−h)·t<sub>miss</sub></b>.<br>
Multi-level: AMAT = h<sub>L1</sub>·t<sub>L1</sub> + (1−h<sub>L1</sub>)·(taxonomy recursive).<br>
<b>CPI with memory stalls</b> = CPI<sub>base</sub> + (misses per instruction) × miss_penalty.<br>
misses per instruction = miss_rate × (memory-referencing instructions fraction).
</div>

<h4>Read the numbers as rates, not counts</h4>
<ul>
<li><b>miss rate</b> is often given as "fraction of all references" — if it is "1 in 100 references", rate = 0.01.</li>
<li>Some problems give <b>misses per instruction</b> directly — then CPI adds (misses/instr × penalty) with no extra multiplication.</li>
<li>L1 miss penalty is not the L1 time — it is the time spent <i>due to</i> the L1 miss (L2 lookup + fill), typically hits + next level.</li>
</ul>

<details><summary>Worked example — AMAT with L1 hit time and L2</summary>
<div class="dc">
<p>L1: hit time 2 cycles, miss rate 5% → L2: hit time 30 cycles, miss rate 10% → main 200 cycles.</p>
<p>AMAT = 2 + 0.05 × [30 + 0.10 × 200] = 2 + 0.05 × [30 + 20] = 2 + 0.05 × 50 = 2 + 2.5 = <b>4.5 cycles</b>.</p>
<p>The key trick: the L1 miss penalty <b>includes</b> the L2 access and its own miss going to main
memory — do not forget the recursive second level.</p>
</div></details>

<details><summary>Worked example — CPI including cache misses</summary>
<div class="dc">
<p>Base CPI 1.0. Memory-referencing instructions are 30% of the program. Miss rate 5%, miss penalty
100 cycles.</p>
<p>Misses per instruction = 0.30 × 0.05 = 0.015.<br>
CPI = 1.0 + 0.015 × 100 = 1.0 + 1.5 = <b>2.5</b>.</p>
<p>Trap: using 0.05 (raw), giving 1+5 = 6, is wrong — the miss rate must be weighted by the fraction of
instructions that actually access memory.</p>
</div></details>

<div class="box tip"><div class="lbl">Shortcut / tip</div>
Every cache numeric problem is two lines: (1) get <b>misses per instruction</b> (rate × referencing
fraction), (2) plug into <b>CPI = CPI<sub>base</sub> + misses/instr × penalty</b>, or for time
<b>AMAT = hit + miss_rate × penalty</b>. Skipping the fraction-weighting is the single most punished error.
</div>
""")]
})

# ---------------------------------------------- 8. Main memory & virtual memory
S.append({
 "id": "mainmem", "title": "Main Memory & Virtual Memory", "children": [
  CH("mm", "Main Memory Organisation", """
<table>
<tr><th>Type</th><th>Cell</th><th>Volatile</th><th>Refresh needed</th><th>Speed / use</th></tr>
<tr><td>SRAM</td><td>6-transistor latch</td><td>Yes</td><td>No</td><td>Fast, cache</td></tr>
<tr><td>DRAM</td><td>1-transistor capacitor</td><td>Yes</td><td><b>Yes</b> (static leakage)</td><td>Cheap/big, main memory</td></tr>
<tr><td>ROM / Flash / SSD</td><td>non-volatile cell</td><td>No</td><td>—</td><td>secondary storage</td></tr>
</table>
<ul>
<li><b>Word line</b> selects rows, <b>bit lines</b> carry data; DRAM reads destroy the charge → read is a
refresh (destructive read).</li>
<li><b>Byte-addressable</b> machines address each byte; a 32-bit data bus moves 4 bytes at a time.</li>
<li><b>Address space</b> = 2<sup>#address-bits</sup> addresses; 32-bit ⇒ 4&nbsp;GB, 48-bit ⇒ 256&nbsp;TB.</li>
</ul>

<div class="box trap"><div class="lbl">GATE trap</div>
SRAM and DRAM are <b>both volatile</b> — the difference is refresh (and cell cost/size), not volatility.
DRAM's destructive read is why reads trigger a refresh; SRAM reads do not. "Non-volatile" applies only to
ROM/Flash/SSD/hard disk.
</div>
"""),
  CH("vm", "Virtual Memory, Page Tables & TLB", """
<p><b>Virtual memory</b> lets a program use an address space larger than physical RAM; it is paged and
managed by the MMU (hardware) + OS (page table). The <b>TLB</b> (Translation Lookaside Buffer) is a
hardware cache of recent virtual→physical address translations — it makes paging fast.</p>
<div class="box formula"><div class="lbl">Address translation &amp; page geometry</div>
Virtual address (VA) = <b>VPN (page number)</b> + <b>offset</b>; offset stays unchanged across mapping.<br>
offset bits = log<sub>2</sub>(page_size).<br>
<b>PTE count</b> = VA size / page size. <b>Page table size</b> = PTE count × PTE bytes.<br>
TLB = cache on the VPN→PFN mapping; a TLB hit costs ~1 cycle, a page-fault ~millions (disk I/O).
</div>
<ul>
<li><b>Page fault</b> = page not in physical RAM → OS loads it from disk; detected by the MMU, handled by
software (the <i>OS</i>, not the DMA/hardware).</li>
<li><b>Locality</b> is why caches/TLB work: temporal (reuse now) + spatial (use nearby now).</li>
<li>Writes to memory use <b>write-through</b> (update main directly) or <b>write-back</b> (write cache, copy
dirty block later); write-allocate vs no-write-allocate govern fill on a write miss.</li>
</ul>

<details><summary>Worked example — page table size for a 32-bit system</summary>
<div class="dc">
<p>32-bit VA, 4 KB pages, PTE = 4 bytes.</p>
<p>#pages = 2<sup>32</sup> / 2<sup>12</sup> = 2<sup>20</sup> = 1 M pages.<br>
Page table (single-level) = 2<sup>20</sup> × 4 B = <b>4 MB</b>.</p>
<p>Fun fact used repeatedly: for 4 KB pages, page offset = 12 bits, VPN = 20 bits; people then compute
how much the page table grows when PTE = 8 bytes (→ 8 MB).</p>
</div></details>

<div class="box tip"><div class="lbl">Shortcut / tip</div>
For any "how many PTE / table size" question, always convert sizes to a common unit (bytes) and keep
2<sup>x</sup> form until the end — dividing powers of 2 is error-prone with decimals. Write page size as
2<sup>p</sup> and VA as 2<sup>v</sup>, then VPN bits = v − p, #pages = 2<sup>v−p</sup>.
</div>
""")]
})

# ---------------------------------------------------------- 9. I/O interface
S.append({
 "id": "iointerface", "title": "I/O Interface — Interrupt & DMA", "children": [
  CH("io", "Programmed & Interrupt-Driven I/O", """
<table>
<tr><th>Mode</th><th>Who moves each byte</th><th>CPU involvement</th><th>Efficiency</th></tr>
<tr><td>Programmed I/O (polling)</td><td>CPU polls status register</td><td>Busy-waits on every transfer</td><td>Poor</td></tr>
<tr><td>Interrupt-driven I/O</td><td>CPU is notified on device-ready</td><td>Only per transfer (interrupt handler)</td><td>Better</td></tr>
<tr><td>DMA</td><td><b>DMA controller</b> moves a block</td><td>Only at start and end of block</td><td>Best for blocks</td></tr>
</table>
<p><b>Interrupts</b> free the CPU from polling: the device raises an interrupt line, the CPU saves state
and jumps to an <b>ISR</b> (interrupt service routine). <b>Vectored</b> interrupts make the device supply a
<u>vector</u> (the address of its own handler) — no software polling for the device type. Priorities decide
which interrupt is serviced first; <b>masking</b> disables (certain) interrupts.</p>

<div class="box trap"><div class="lbl">GATE trap</div>
Interrupt-driven I/O still moves data <b>through the CPU</b> (one interrupt + handler per transfer) — it
reduces CPU waste but does not remove the CPU from the data path. <b>DMA is the mode that removes the CPU
from the per-word data path.</b> Also, a <b>vectored</b> interrupt hands the handler address directly; a
non-vectored one forces the CPU to poll for it.
</div>
"""),
  CH("dma", "DMA Transfer Modes", """
<p><b>DMA</b> (Direct Memory Access): a DMA controller (DMAC) transfers a whole block memory↔I/O directly
on the bus, interrupting the CPU only at the block's <b>start and end</b>.</p>
<h4>DMA modes</h4>
<table>
<tr><th>Mode</th><th>Bus behaviour</th><th>CPU impact</th></tr>
<tr><td>Burst / block</td><td>DMAC holds the bus for the whole block</td><td>CPU blocked for the block — fast, invasive</td></tr>
<tr><td>Cycle stealing</td><td>DMAC borrows the bus one word at a time</td><td>CPU slows but is not fully blocked</td></tr>
<tr><td>Transparent / interleave</td><td>DMA during cycles the CPU does not need the bus</td><td>Minimal CPU impact</td></tr>
</table>

<div class="box formula"><div class="lbl">DMA overhead estimate</div>
CPU overhead ≈ <b>block setup</b> (once) + <b>one interrupt</b> per block — negligible versus per-byte
polling. Compare: programmed I/O costs CPU time proportional to <b>n</b> bytes; DMA costs CPU time
proportional to <b>1</b> block regardless of block size n.
</div>

<details><summary>Worked example — why DMA scales</summary>
<div class="dc">
<p>Transfer 10<sup>6</sup> bytes, each byte needing ~1 µs of CPU in programmed I/O ⇒ ~1 s of CPU time.</p>
<p>With DMA: CPU spends only setup + interrupt, say ~100 µs. Even if DMA ties up the bus for 1 ms for the
block, the CPU is free for the other 99.9% — effective data path moves through the DMAC, not the CPU.</p>
</div></details>
""")]
})

# ---------------------------------------------- 10. One-page formula sheet
S.append({
 "id": "formulas", "title": "One-Page Formula Sheet (Revise Before Exam)",
 "html": """
<table>
<tr><th>Quantity</th><th>Formula</th></tr>
<tr><td>Pipeline cycle count (no stalls)</td><td>k + (n − 1)</td></tr>
<tr><td>Pipeline speedup</td><td>(n·k)/(k+n−1) → k as n→∞</td></tr>
<tr><td>Effective speedup with CPI</td><td>k / CPI<sub>eff</sub></td></tr>
<tr><td>With stalls added</td><td>cycles = k + (n−1) + stalls</td></tr>
<tr><td>AMAT</td><td>hit_time + miss_rate × miss_penalty</td></tr>
<tr><td>Effective access time</td><td>h·t<sub>hit</sub> + (1−h)·t<sub>miss</sub></td></tr>
<tr><td>CPI with memory stalls</td><td>CPI<sub>base</sub> + (misses/instr)×penalty</td></tr>
<tr><td>Misses per instruction</td><td>miss_rate × (fraction referencing memory)</td></tr>
<tr><td>#cache sets</td><td>cache_size / (block × associativity)</td></tr>
<tr><td>Offset bits</td><td>log<sub>2</sub>(block_size)</td></tr>
<tr><td>Index bits</td><td>log<sub>2</sub>(#sets)</td></tr>
<tr><td>Tag bits</td><td>address_bits − index − offset</td></tr>
<tr><td>Virtual memory</td><td>VPN bits = v − p ; #pages = 2<sup>v−p</sup> ; PTE size × count = page table size</td></tr>
<tr><td>2's complement range (n-bit)</td><td>−2<sup>n−1</sup> … +2<sup>n−1</sup>−1</td></tr>
<tr><td>Negate 2's complement</td><td>−x = ~x + 1</td></tr>
<tr><td>Arithmetic shift</td><td>SHL by k = ×2<sup>k</sup> ; SAR by k = ÷2<sup>k</sup></td></tr>
<tr><td>Overflow (signed add)</td><td>carry-in ≠ carry-out at sign bit</td></tr>
<tr><td>Instruction length (registers)</td><td>log<sub>2</sub>#opcodes + r·log<sub>2</sub>#regs + imm</td></tr>
<tr><td>Address space</td><td>2<sup>#address-bits</sup> bytes</td></tr>
</table>
<div class="box tip"><div class="lbl">Exam-day plan for COA</div>
Attack the four numeric clusters first — AMAT, cache geometry, CPI-with-stalls, pipeline
speedup — since they are NAT-friendly (no negative marking). Then the conceptual MCQs on
addressing modes, flags, interrupt/DMA. Leave nothing in the pipeline/cache family unanswered;
bound your answer and submit.
</div>
"""
})

# ---------------------------------------------------------------- 11. Exam strategy
S.append({
 "id": "strategy", "title": "Exam Strategy",
 "html": """
<h4>Master the 4 numeric families first</h4>
<table>
<tr><th>Family</th><th>1-line approach</th><th>Common time sink</th></tr>
<tr><td>Cache geometry</td><td>sets = size/(block×assoc); then tag/index/offset bits</td><td>Forgetting to divide by associativity</td></tr>
<tr><td>AMAT / t<sub>eff</sub></td><td>hit + miss_rate × miss_penalty; weight by referencing fraction</td><td>Not weighting miss rate by mem-referencing instructions</td></tr>
<tr><td>CPI + misses</td><td>CPI<sub>base</sub> + misses/instr × penalty</td><td>Using raw miss rate instead of misses/instr</td></tr>
<tr><td>Pipeline speedup</td><td>cycles = k + (n−1); speedup = n·k/that</td><td>Writing n·k for the pipeline cycle count</td></tr>
</table>

<h4>Attempt order under time pressure</h4>
<ul>
<li><b>Always attempt</b> the cache/pipeline/CPI numerics (NAT, no negative marking) — they are formula
plugs, the single fastest marks in COA.</li>
<li><b>Then</b> the conceptual MCQs: addressing modes, flags, SRAM/DRAM, hardwired vs microprogrammed,
interrupt/DMA.</li>
<li><b>Skip or defer</b> long multi-stage-pipeline-with-hazards diagrams and "which of I/II/III is true"
complex questions if short on time; classification questions are quick but branch-penalty deep-dives are not.</li>
</ul>

<div class="box trap"><div class="lbl">Final GATE trap</div>
Nearly all COA numeric errors are unit/scale mistakes: forgetting associativity in cache sets, not
multiplying miss rate by the memory-referencing fraction, using a 16-bit address where a 32-bit one was
given, and treating "miss penalty" as if it were the miss <i>time</i>. Re-check one dimension before you
commit a numeric answer.
</div>
"""
})

QUIZ = [
 {"q":"In which addressing mode is the operand itself stored inside the instruction?","opts":["Direct","Immediate","Indirect","Register indirect"],"a":1,
  "ex":"Immediate mode places the operand directly in the instruction field; no memory or register access for the operand is needed."},
 {"q":"For the instruction LOAD R1, (R2) (register indirect), the operand is located:","opts":["In register R1","In register R2","At the memory address contained in R2","Immediately inside the instruction"],"a":2,
  "ex":"Register indirect means the operand lives at memory M[(R2)]. R2 holds the address, not the data."},
 {"q":"A 64 KB cache uses 32-byte blocks and is 4-way set associative. How many sets does it have?","opts":["128","256","512","1024"],"a":2,
  "ex":"sets = cache_size/(block_size × associativity) = 65536/(32×4) = 512."},
 {"q":"If a cache block is 256 bytes, how many bits are needed for the block offset?","opts":["6","7","8","9"],"a":2,
  "ex":"Offset bits = log₂(block_size) = log₂(256) = 8 bits."},
 {"q":"A cache has hit time 2 ns, miss rate 5% and miss penalty 50 ns. The average memory access time (AMAT) is:","opts":["2.5 ns","4.5 ns","50 ns","52 ns"],"a":1,
  "ex":"AMAT = hit time + miss rate × miss penalty = 2 + 0.05×50 = 2 + 2.5 = 4.5 ns."},
 {"q":"L1 hit time is 1 cycle with 10% miss rate and L1 miss penalty 10 cycles; L2 never misses. AMAT is:","opts":["1.1","1.2","2.0","11"],"a":2,
  "ex":"AMAT = hit + miss_rate × penalty = 1 + 0.1×10 = 2.0 cycles."},
 {"q":"The ideal maximum speedup of a 5-stage pipeline (infinite instructions, no stalls) is:","opts":["2.5","4","5","20"],"a":2,
  "ex":"As n→∞, speedup → number of stages k = 5."},
 {"q":"Base CPI is 1; 25% of instructions reference memory with 5% miss rate and 40-cycle miss penalty. CPI including stalls is:","opts":["1.125","1.5","2.0","3.0"],"a":1,
  "ex":"misses/instruction = 0.25×0.05 = 0.0125; stall = 0.0125×40 = 0.5; CPI = 1 + 0.5 = 1.5."},
 {"q":"A 5-stage pipeline executes 4 instructions with no stalls. How many cycles does it take?","opts":["4","5","8","9"],"a":2,
  "ex":"Cycles = k + (n−1) = 5 + 3 = 8. First instruction pays all 5 stages, the rest add 1 each."},
 {"q":"A direct-mapped cache has 256 sets and 32-bit physical addresses. How many index bits are used?","opts":["4","8","16","24"],"a":1,
  "ex":"Index bits = log₂(#sets) = log₂(256) = 8."},
 {"q":"Operand forwarding (bypassing) is used to resolve which kind of hazard?","opts":["Structural","Data (RAW)","Control (branch)","None"],"a":1,
  "ex":"Forwarding sends the ALU result back to a later stage, eliminating the RAW stall for register ALU dependencies."},
 {"q":"Which memory technology requires periodic refreshing?","opts":["SRAM","DRAM","ROM","Flash"],"a":1,
  "ex":"DRAM stores charge in a capacitor that leaks, so it must be refreshed; SRAM is a latch and needs no refresh."},
 {"q":"DMA (Direct Memory Access) is most beneficial because it:","opts":["increases the cache hit rate","moves data without requiring CPU involvement for every word","replaces the CPU entirely","reduces the number of pipeline stages"],"a":1,
  "ex":"The DMA controller moves a whole block on the bus; the CPU is interrupted only at block start and end, not per word."},
 {"q":"The range of an 8-bit 2's complement number is:","opts":["−127 to 127","−128 to 127","−127 to 128","−255 to 255"],"a":1,
  "ex":"n-bit 2's complement spans −2ⁿ⁻¹ to +2ⁿ⁻¹−1, so 8-bit gives −128 to +127."},
 {"q":"A hardwired control unit is typically:","opts":["slower to execute and easier to modify","faster to execute but harder to modify","slower and harder to modify","faster and easier to modify"],"a":1,
  "ex":"Hardwired control is combinational logic from opcode+state, so it is fast but rigid (hard to modify by design)."},
 {"q":"In n-bit 2's complement addition, overflow (V) is flagged when:","opts":["there is any carry out of the MSB","the carry into the sign bit differs from the carry out","the result is negative","the addend is negative"],"a":1,
  "ex":"Signed overflow occurs exactly when carry-in ≠ carry-out at the sign bit; that detects a result out of signed range."},
 {"q":"A vectored interrupt is one in which the device:","opts":["supplies the address/vector of its own interrupt handler","disables all other interrupts","always has the highest priority","never uses a status register"],"a":0,
  "ex":"Vectoring means the device provides a vector identifying its handler, avoiding a software poll to discover which device interrupted."},
 {"q":"Base CPI is 1 (no other stalls); 1 in 10 instructions misses the cache with a 100-cycle penalty. The CPI including the miss stalls is:","opts":["2","11","101","1.1"],"a":1,
  "ex":"misses/instruction = 0.1; stall = 0.1×100 = 10; CPI = 1 + 10 = 11."},
 {"q":"In cycle-stealing DMA, the DMA controller transfers data:","opts":["in one long burst holding the bus","one word at a time, interleaved with CPU bus cycles","only when the CPU is idle for a full block","only after a cache flush"],"a":1,
  "ex":"Cycle stealing grabs the bus for single transfers between CPU bus cycles, so the CPU is slowed but not blocked entirely."},
 {"q":"When a page fault occurs, the fault is handled by:","opts":["the hardware MMU alone","the operating system via a software trap/handler","the DMA controller","the cache controller"],"a":1,
  "ex":"The MMU detects the fault and traps to the OS, which loads the page from disk into physical memory."},
]

SUBJECT = {
 "code": "S03", "title": "Computer Organization & Architecture",
 "subtitle": "GATE CS 2027 · 8 marks · Instructions & addressing, ALU/data-path/control, pipelining, memory hierarchy, I/O (interrupt & DMA)",
 "weight_note": "GATE CS 2027 · Computer Organization & Architecture (8 marks)",
 "sections": S, "quiz": QUIZ,
}