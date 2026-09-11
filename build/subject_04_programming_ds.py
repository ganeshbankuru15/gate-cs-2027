# -*- coding: utf-8 -*-
"""Subject 04 — Programming & Data Structures (9 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

# ---------------------------------------------------------------- 1. Overview
S.append({
 "id": "pds-overview", "title": "Overview & Weightage",
 "html": """
<div class="kv">
  <span class="chip">Marks <b>9 / 100</b></span>
  <span class="chip">Typical Qs <b>7–9</b></span>
  <span class="chip">Core skill <b>Output prediction in C</b></span>
  <span class="chip">Scoring <b>High, but trap-heavy</b></span>
</div>
<p>Programming &amp; Data Structures is the only subject you are asked to <b>execute</b> by hand: a
starter block of C asks you to predict output or the value of a variable, and the rest asks for
data-structure behaviour and complexity. The C part <b>decides your score</b> — it is concrete,
mechanical, and fully learnable, whereas data-structure questions mostly test whether you can
trace insertion/deletion and quote standard complexities.</p>

<h3>What it contains</h3>
<table>
<tr><th>Block</th><th>Typical marks</th><th>Difficulty</th><th>Priority</th></tr>
<tr><td>Programming in C (pointers, recursion, storage)</td><td>3–4</td><td>Medium</td><td>★★★★★</td></tr>
<tr><td>Recursion &amp; its analysis</td><td>1–2</td><td>Medium</td><td>★★★★★</td></tr>
<tr><td>Linear DS: arrays, stacks, queues, linked lists</td><td>2–3</td><td>Easy–Medium</td><td>★★★★★</td></tr>
<tr><td>Non-linear DS: trees, BSTs, heaps, graphs</td><td>2–3</td><td>Medium–Hard</td><td>★★★★☆</td></tr>
</table>

<div class="box tip"><div class="lbl">How to study this for GATE 2027</div>
<ol>
<li><b>Master C pointer arithmetic and output prediction first</b> — it is 3–4 near-guaranteed marks.</li>
<li><b>Learn every recursion trace</b> by expanding the recurrence — never by intuition.</li>
<li><b>Memorise the complexity table</b> for every structure (insert/delete/search/space).</li>
<li><b>Practise one hand-trace of each insertion/deletion</b> (BST, heap, queue) so exam traces are instant.</li>
<li>Draw each ADT with its <b>worst case</b> in mind — GATE rarely asks best case.</li>
</ol>
</div>

<div class="box trap"><div class="lbl">The C trap that costs everyone</div>
In C, <b>arrays, pointers and sizes</b> interact in ways that look identical but are not:
<code>sizeof(arr)</code> inside the declaring function gives the whole array, but the same array passed
to a function decays to a pointer, so <code>sizeof</code> there gives only 8 bytes. GATE asks this
verbatim. Always ask: <b>"am I in the declaring scope, or has the array decayed?"</b>
</div>
"""
})

# ------------------------------------------------- 2. Pointers & arrays
S.append({
 "id": "pds-pointers", "title": "Programming in C — Pointers, Arrays, Storage", "children": [
  CH("ptr", "Pointers & Pointer Arithmetic", """
<p>Every GATE C question reduces to tracking <b>addresses</b>. A pointer holds an address; the type
tells the compiler how many bytes to move when you apply arithmetic.</p>
<div class="box formula"><div class="lbl">Pointer arithmetic (the single rule)</div>
<p>If <code>p</code> points to an element of type <code>T</code> occupying <code>k</code> bytes, then</p>
<p><b>p + n</b> = address + <b>n×k</b>, not + n bytes.<br>
<b>p − p′</b> = (address difference) / <b>k</b> → a signed integer <b>count of elements</b>, not bytes.<br>
<code>*p</code> dereferences; <code>&amp;x</code> takes the address of x; <code>*&amp;x == x</code>.</p>
</div>
<p>A <b>double pointer</b> <code>int **p</code> stores the address of an <code>int*</code> — used for
arrays of pointers and for modifying a pointer inside a function. A <b>function pointer</b>
<code>int (*fp)(int,int)</code> stores a function's address (note the brackets are mandatory —
<code>int *fp(int,int)</code> instead declares a function returning <code>int*</code>).</p>

<table>
<tr><th>Expression</th><th>Value</th></tr>
<tr><td><code>int a[4], *p=a</code></td><td>p points to a[0]</td></tr>
<tr><td><code>p+2</code></td><td>address of a[2] (skips 2×4 bytes)</td></tr>
<tr><td><code>*(p+2)</code></td><td>a[2] (value)</td></tr>
<tr><td><code>p[i]</code></td><td>identical to <code>*(p+i)</code></td></tr>
<tr><td><code>&amp;a[2] − p</code></td><td>2 (element count, not 8 bytes)</td></tr>
</table>

<details><summary>Worked example — output of pointer prints</summary>
<div class="dc">
<p><code>int a[]={10,20,30,40}, *p=a; printf("%d %d", *p, *(p+3));</code></p>
<p><code>*p</code> = a[0] = <b>10</b>; <code>*(p+3)</code> skips 3 elements = a[3] = <b>40</b>.</p>
<p>Now <code>p++;</code> (p→a[1]) then <code>printf("%d", *p)</code> → <b>20</b>. Pointer
arithmetic is by element size, so this is always 4 bytes per step, not 1.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — uninitialised and NULL pointers</div>
Dereferencing a <b>NULL</b> or wildcard pointer is undefined behaviour and usually crashes. Also
note <code>NULL == 0</code> in integer context, so <code>int *p = 0;</code> is legal and equals NULL.
<code>void*</code> cannot be dereferenced or arithmetically advanced — it must be cast first.
</div>
"""),
  CH("arrptr", "Arrays vs Pointers", """
<p>Arrays and pointers are <b>related but not interchangeable</b>. The famous GATE distinction:</p>
<table>
<tr><th>Property</th><th>Array <code>int a[4]</code></th><th>Pointer <code>int *p</code></th></tr>
<tr><td>Resizable?</td><td>No — fixed by declaration</td><td>Yes — can point anywhere</td></tr>
<tr><td>Assignment</td><td><code>a = p</code> is <b>illegal</b> (a is not an lvalue)</td><td><code>p = a</code> is legal</td></tr>
<tr><td><code>sizeof</code></td><td>4×4 = <b>16</b> in declaring scope</td><td><b>8</b> (pointer size) everywhere</td></tr>
<tr><td>As argument</td><td colspan="2">decays to a pointer — <code>sizeof</code> inside callee = 8</td></tr>
<tr><td><code>a+1</code></td><td colspan="2">both advance by one element</td></tr>
</table>
<div class="box formula"><div class="lbl">Array decay rule</div>
<p>When used in an expression (except under <code>sizeof</code>, <code>&amp;</code>, and string
literals initialising a char array), the array name <b>decays</b> to a pointer to its first
element, type <code>T*</code>. Consequently <code>int a[4];</code> gives <code>&amp;a == &amp;a[0]</code>
(address equal) — but <code>&amp;a</code> has type <code>int(*)[4]</code>.</p>
</div>
<details><summary>Worked example — classic sizeof trap</summary>
<div class="dc">
<p><code>void f(int a[3]){ printf("%zu", sizeof(a)); }</code></p>
<p>Despite the "<code>[3]</code>", the parameter is a <b>pointer</b> — the array decays on entry.
<code>sizeof(a)</code> = pointer size = <b>8</b>. Replacing the signature with <code>int *a</code>
changes nothing: they are the same type.</p>
<p>But inside <code>main</code>, where <code>int a[3]</code> is declared, <code>sizeof(a)=12</code> —
the full array. This scope difference is a direct (and repeated) GATE question.</p>
</div></details>
"""),
  CH("storage", "Storage Classes & Scope", """
<p>Storage classes fix two things: <b>where</b> a variable lives and <b>how long</b> it lives.</p>
<table>
<tr><th>Keyword</th><th>Storage</th><th>Initial value</th><th>Lifetime</th></tr>
<tr><td><code>auto</code></td><td>stack (RAM)</td><td>garbage</td><td>block scope</td></tr>
<tr><td><code>register</code></td><td>CPU register (hint)</td><td>garbage</td><td>block scope</td></tr>
<tr><td><code>static</code></td><td>data segment</td><td><b>zero</b></td><td>entire program run</td></tr>
<tr><td><code>extern</code></td><td>data segment</td><td>—</td><td>entire program</td></tr>
</table>
<p><b>Key facts:</b> a <code>static</code> local keeps its value between calls (initialised once).
<b>Static vs global:</b> a global is visible to other files (with <code>extern</code>), a
<code>static</code> global is <b>file-private</b> but still lifetime-of-program. A global is
zero-initialised automatically, a static local is too.</p>

<details><summary>Worked example — count calls with static</summary>
<div class="dc">
<pre><code>int f(void){ static int c = 0; return ++c; }
printf("%d %d %d", f(), f(), f());</code></pre>
<p><code>c</code> is initialised to 0 <b>once</b>, before <b>main</b>. Each call increments the
same persistent variable: <code>++c</code> → 1, then 2, then 3, so output is <b>"1 2 3"</b>.
Without <code>static</code>, automatic <code>c</code> would be re-created (garbage) each call.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — scope diffusion</div>
<b>Global variables can always be declared anywhere</b>; C90 required declarations at the top of a
block, C99 allows them anywhere. The trap is <b>shadowing</b>: a local variable with the same name
as a global <b>hides</b> the global inside the block, and a <code>static</code> global is
<b>invisible</b> outside its own file. Never assume the global is reachable just because it exists.
</div>
"""),
  CH("strings", "Strings & <code>char</code> handling", """
<p>A string in C is a <code>char[]</code> <b>terminated by '\0'</b>. GATE loves the
<code>sizeof</code> vs <code>strlen</code> difference.</p>
<table>
<tr><th>Expression</th><th>Result</th></tr>
<tr><td><code>char s[]="GATE";</code></td><td>size 5, chars 'G','A','T','E','\\0'</td></tr>
<tr><td><code>sizeof(s)</code></td><td><b>5</b></td></tr>
<tr><td><code>strlen(s)</code></td><td><b>4</b> (stops before '\0')</td></tr>
<tr><td><code>char *p = "GATE"</code></td><td>p points to a <b>string literal</b> (read-only region, size 5 incl. '\0')</td></tr>
</table>
<p>String functions (<code>strcpy</code>, <code>strcmp</code>, <code>strcat</code>) require the
destination to be a <b>writable array</b>, not a pointer to a literal. <code>strcmp</code> returns
0 when equal, negative/positive on less/greater — a favourite condition bug.</p>

<details><summary>Worked example — strlen of a pointer</summary>
<div class="dc">
<p><code>char *p = "GATE"; printf("%d %d", sizeof(p), strlen(p));</code></p>
<p><code>sizeof(p)</code> = size of the <b>pointer</b> = <b>8</b> (never the string length).
<code>strlen(p)</code> walks to the '\0' and returns <b>4</b>. Pedantically, <code>%d</code> with
<code>sizeof</code> (type <code>size_t</code>) is a format mismatch — but GATE ignores that and
asks for the values: 8 and 4.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — the string literal copy error</div>
<code>char *q; strcpy(q, "GATE");</code> is a <b>bug</b>: q points to a literal (or is uninitialised),
so writing through it is illegal. Correct is <code>char q[5];</code> or a <code>malloc</code>ed buffer.
Also <code>"=="</code> on two <code>char*</code> to literals compares <b>addresses</b>, not contents —
only <code>strcmp</code> compares values.
</div>
""")]})

# ------------------------------------------------- 3. Structures & unions
S.append({
 "id": "pds-struct", "title": "Structures, Unions & Typedef",
 "html": """
<p>A <code>struct</code> allocates each member its own storage; a <code>union</code> makes all
members <b>share the same starting address</b> so its size is the largest member.</p>
<table>
<tr><th>Feature</th><th><code>struct</code></th><th><code>union</code></th></tr>
<tr><td>Size</td><td>sum of members (+ padding)</td><td>max member size</td></tr>
<tr><td>Member access</td><td>all members usable at once</td><td>only one member at a time</td></tr>
<tr><td>Memory</td><td>each member separate</td><td>members overlap (write one → others overwritten)</td></tr>
</table>
<div class="box formula"><div class="lbl">Struct size = sum + padding</div>
<p>Members are aligned to their natural boundary. If <code>struct {char c; int i;}</code> has a 1-byte
<code>char</code> followed by a 4-byte <code>int</code>, 3 bytes of <b>padding</b> are inserted, so
the struct is <b>8</b> bytes — not 5. GATE asks this directly, at least once a year.</p>
</div>
<p><b>Typedef</b> just creates an alias:
<code>typedef struct node Node;</code> then declare <code>Node *head;</code> without the
<code>struct</code> keyword. <b>Self-referential</b> structs (a struct containing a pointer to its
own type) are how linked lists and trees are built.</p>

<div class="box tip"><div class="lbl">Shortcut — union vs struct size</div>
A union's size is simply the largest member; a struct's is the sum of members <b>rounded up to the
largest member's alignment</b>. If all members are the same type, struct = union × count.
</div>

<details><summary>Worked example — union output</summary>
<div class="dc">
<pre><code>union u { char c; int i; short s; };
union u v; v.i = 0x41424344; printf("%c", v.c);</code></pre>
<p>All members share the lowest address. On a <b>little-endian</b> machine the least-significant byte
<code>0x44</code> sits at the lowest address, so <code>v.c</code> reads <code>0x44</code> = <b>'D'</b>.
On big-endian it would be <code>0x41</code> = 'A'. The union's size is <code>int</code> = <b>4</b> bytes.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — union overwrites silently</div>
In a union, assigning to one member <b>overwrites the bits of every other member</b> with no error.
GATE gives a union, writes two members in sequence, then reads the first: the value is whatever the
later write left in those shared bytes. Track the <b>last</b> write, never both.
</div>
"""
})

# ------------------------------------------------- 4. Recursion
S.append({
 "id": "pds-recursion", "title": "Recursion", "children": [
  CH("recbase", "Recursion Fundamentals & Tracing", """
<p>Recursion solves a problem in terms of a <b>smaller instance</b> of itself, with a <b>base case</b>
that terminates it. A recursive call must make progress toward the base case or the stack overflows.</p>
<div class="box formula"><div class="lbl">Factorial recursion</div>
<p>f(n) = n × f(n−1) for n&gt;0, with f(0)=1. Expanding: f(4) = 4·3·2·1·f(0) = <b>24</b>.<br>
Recursion depth = number of nested live frames (n for factorial); total work = number of calls.</p>
</div>
<p>Two shapes dominate GATE: <b>linear recursion</b> (one recursive call, e.g. factorial) and
<b>tree recursion</b> (two calls, e.g. Fibonacci) — the latter makes the call count explode
exponential because the same subproblem is computed repeatedly.</p>

<h4>Tracing discipline</h4>
<ol>
<li>Write the recurrence <b>before</b> evaluating: e.g. T(n) = T(n−1) + c.</li>
<li>Expand one level at a time until you hit the base case, then unwind values top-down.</li>
<li>Count <b>calls</b> (nodes) for output questions, and count <b>depth</b> for stack/space.</li>
</ol>

<details><summary>Worked example — how many ways differ? f(5)</summary>
<div class="dc">
<pre><code>int f(int n){ if(n<=1) return 1; return f(n-1) + f(n-2); }</code></pre>
<p>This is Fibonacci-style tree recursion. f(5) = f(4)+f(3), f(4)=f(3)+f(2), … Expanding gives
f(5)=<b>8</b>. The number of calls to compute f(n) is ≈ <b>2<sup>n/2</sup></b> (roughly Fibonacci),
each tiny call recomputing overlapping values — the reason naive Fibonacci is exponential.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — the "print-order" trap</div>
Code that <b>prints after</b> the recursive call prints on the way <b>up</b> (unwinding), in the
reverse order of the calls; code that prints <b>before</b> prints going <b>down</b>. The classic
"print n then recurse" gives n, n−1, …, 1, but "recurse then print n" gives 1, 2, …, n. GATE pads
both with <code>static</code> counters to catch students who ignore call order.
</div>
"""),
  CH("recan", "Recurrence-based Complexity of Recursions", """
<p>Every recursive routine maps to a recurrence T(n). Solve it for a complexity answer.</p>
<div class="box formula"><div class="lbl">Recurrence → complexity (fast rules)</div>
<ul>
<li>T(n) = T(n−1) + c  →  <b>O(n)</b> (linear recursion)</li>
<li>T(n) = T(n−1) + n  →  <b>O(n²)</b> (nested loop equivalent)</li>
<li>T(n) = 2T(n/2) + n  →  <b>O(n log n)</b> (divide &amp; conquer, merge sort)</li>
<li>T(n) = 2T(n−1) + c  →  <b>O(2ⁿ)</b> (tree recursion, doubling calls)</li>
<li>T(n) = T(n/2) + c  →  <b>O(log n)</b> (divide by constant, binary search)</li>
<li>Space (stack depth): linear recursion O(n); binary-search/tail style O(log n)</li>
</ul>
</div>
<table>
<tr><th>Recursive function</th><th>Time</th><th>Stack space</th></tr>
<tr><td>factorial(n)</td><td>O(n)</td><td>O(n)</td></tr>
<tr><td>naive fib(n)</td><td>O(2<sup>n</sup>)</td><td>O(n) (deepest path)</td></tr>
<tr><td>binary search</td><td>O(log n)</td><td>O(log n)</td></tr>
<tr><td>merge sort</td><td>O(n log n)</td><td>O(n)</td></tr>
</table>
<p><b>Tail recursion</b> — the recursive call is the <b>last</b> operation. Compilers can optimise it
into a loop, keeping call stack O(1); a <b>non-tail</b> call (e.g. <code>n * f(n−1)</code>, multiply
after) must keep its frame, so stack is O(n).</p>

<div class="box trap"><div class="lbl">GATE trap — space ≠ number of calls</div>
The <b>maximum stack space</b> is the recursion <b>depth</b> (longest chain of live frames), not the
total number of calls. For tree recursion fib(n), total calls are exponential, but stack depth is
only O(n) — one branch is fully unwound before the next starts. Many candidates write O(2ⁿ) for space.
</div>
""")]})

# ------------------------------------------------- 5. Linear structures
S.append({
 "id": "pds-linear", "title": "Arrays, Stacks & Queues", "children": [
  CH("arrays", "Arrays: Static vs Dynamic, Complexity", """
<p>An array stores elements in <b>contiguous</b> memory — random access to index i is
<b>O(1)</b> because the address is <code>base + i×k</code>. Its cost is the spread of
insert/delete.</p>
<table>
<tr><th>Operation (on n elements)</th><th>Static array</th><th>Dynamic array (e.g. C++ vector)</th></tr>
<tr><td>Access a[i]</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Insert at end</td><td>O(1) if room</td><td>amortised O(1)</td></tr>
<tr><td>Insert at index 0</td><td>O(n) — shift all</td><td>O(n)</td></tr>
<tr><td>Delete at index 0</td><td>O(n) — shift all</td><td>O(n)</td></tr>
<tr><td>Search</td><td>O(n) linear; O(log n) if sorted (binary search)</td><td>same</td></tr>
</table>
<div class="box formula"><div class="lbl">Array address formula</div>
<p>Address of a[i] = base + i × sizeof(T). For a 2D array stored row-major,
address of a[i][j] = base + (i × C + j) × sizeof(T), where C = number of columns. GATE asks this
with byte sizes to force a precise numeric answer.</p>
</div>
<div class="box trap"><div class="lbl">GATE trap — array bounds in C</div>
C does <b>not</b> bounds-check arrays. Accessing <code>a[5]</code> past a 4-element array reads
neighbouring memory with <b>undefined behaviour</b> — it may print garbage, even work, or crash;
its "value" is not a legal answer. In contrast, static/dynamic arrays in C++/Java throw or check.
</div>
"""),
  CH("stackqueue", "Stacks & Queues (ADTs)", """
<p>A <b>stack</b> is LIFO: push and pop only at the top. A <b>queue</b> is FIFO: enqueue at the
rear, dequeue from the front. Both can be built on arrays or linked lists.</p>
<table>
<tr><th>Operation</th><th>Array stack</th><th>LL stack</th><th>Array queue (ring)</th><th>LL queue</th></tr>
<tr><td>push/enqueue</td><td>O(1)</td><td>O(1)</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>pop/dequeue</td><td>O(1)</td><td>O(1)</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>peek/front</td><td>O(1)</td><td>O(1)</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Is empty? / size</td><td>O(1)</td><td>O(1)</td><td>O(1)</td><td>O(1)</td></tr>
</table>
<p><b>Circular queue:</b> an array queue must wrap the rear index with <code>(rear+1) % SIZE</code>,
reserving one slot to tell full from empty. A stack can <b>simulate a queue</b> with 2 stacks
(enqueue = push to s1; dequeue = move s1→s2 then pop) in O(1) amortised — a recurring GATE design
question.</p>

<details><summary>Worked example — stack permutation check</summary>
<div class="dc">
<p>Can the output <b>2 1 3</b> be produced by pushing 1,2,3 in that order onto a stack? </p>
<p>Push 1, push 2 → pop 2 → pop 1 → push 3 → pop 3: <b>yes</b>, output "2 1 3".<br>
Can we get <b>3 1 2</b>? Pop 3 requires pushing all three, but then 2 is above 1, so 1 cannot be
output before 2 → <b>impossible</b>. Stack outputs are exactly the permutations with no
<code>i&lt;j&lt;k</code> appearing as <code>k, i, j</code> (no 312 pattern).</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — overflow check</div>
A circular queue is "full" when <code>(rear+1)%SIZE == front</code> (one unused slot), and "empty"
when <code>front == rear</code>. Many candidates confuse the two conditions — full relies on the
<b>next</b> position matching front, empty on the exact equality. Both, on overflow, otherwise
look identical.
</div>
"""),
  CH("stackapps", "Applications: Parentheses, Infix/Postfix", """
  <p>Stacks and queues earn GATE questions through their <b>applications</b>, not raw operations.</p>
  <table>
  <tr><th>Problem</th><th>Structure</th><th>Key idea</th></tr>
  <tr><td>Balanced parentheses</td><td>stack</td><td>push openers, pop on closer; mismatch or leftover ⇒ unbalanced</td></tr>
  <tr><td>Infix → postfix</td><td>stack</td><td>output operands; push operators by precedence, pop higher-or-equal on a new operator</td></tr>
  <tr><td>Postfix evaluation</td><td>stack</td><td>push operands, pop two and push result on each operator</td></tr>
  <tr><td>BFS traversal</td><td>queue</td><td>level-order expansion</td></tr>
  <tr><td>Undo / function calls</td><td>stack</td><td>LIFO matches call/undo semantics</td></tr>
  </table>
  <p>Postfix (Reverse Polish) needs <b>no parentheses or precedence</b> — the operator applies to the two
  operands just before it. Infix→postfix uses the operator stack; a lower-precedence incoming operator
  pops all higher-or-equal operators off first.</p>

  <details><summary>Worked example — evaluate 2 3 4 × + 5 − (postfix)</summary>
  <div class="dc">
  <p>Scan left→right with a stack. Push 2, push 3, push 4.</p>
  <p>× : pop 4, 3 → 3×4 = 12, push 12. Stack now [2, 12].<br>
  + : pop 12, 2 → 2+12 = 14, push 14. Stack [14].<br>
  Push 5 → [14, 5]. − : pop 5, 14 → 14−5 = <b>9</b>. Result <b>9</b>.</p>
  </div></details>

  <div class="box trap"><div class="lbl">GATE trap — basic done once, prefix vs postfix order</div>
  For <b>postfix a b op</b> the operands are used as <code>a op b</code> (first popped is the right
  operand). For <b>prefix op a b</b> it is immediately <code>a op b</code>. With a <b>non-commutative</b>
  operator like − or /, reversing the operands flips the answer — GATE plants this more than altimeter
  approaches. Track which value was pushed first.
  </div>
  """), CH("linkedlist", "Linked Lists: Singly, Doubly, Circular", """
<p>A <b>singly linked list</b> is a chain of nodes each holding data and a <code>next</code> pointer.
Access is sequential: finding the k-th node costs <b>O(k)</b>; the list has no random access like an
array.</p>
<table>
<tr><th>Operation</th><th>Singly LL</th><th>Doubly LL</th><th>Circular LL</th></tr>
<tr><td>Insert at head</td><td>O(1)</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Delete at head</td><td>O(1)</td><td>O(1)</td><td>O(1) (adjust tail)</td></tr>
<tr><td>Insert at tail (with tail ptr)</td><td>O(1)</td><td>O(1)</td><td>O(1)</td></tr>
<tr><td>Insert in middle / by value</td><td>O(n) search + O(1)</td><td>O(n)</td><td>O(n)</td></tr>
<tr><td>Delete middle node</td><td>O(n) find prev</td><td>O(1) (prev pointer)</td><td>O(n)</td></tr>
<tr><td>Space per node</td><td>1 pointer</td><td>2 pointers</td><td>1 pointer (+ last links to head)</td></tr>
</table>
<p><b>Doubly linked</b> lists add a <code>prev</code> pointer enabling O(1) deletion of a node whose
address is known (no need to walk for predecessor). <b>Circular</b> lists link the tail back to the
head — used where you must keep cycling (round-robin).</p>

<details><summary>Worked example — delete the middle node without the head</summary>
<div class="dc">
<p>For a <b>singly</b> linked list, deleting the node <code>p</code> (whose address you know) without
the head: you cannot find <code>p</code>'s predecessor, so the usual trick is to <b>copy</b>
<code>p→next</code> data into <code>p</code>, then unlink <code>p→next</code>. This is a standard
<code>O(1)</code> "delete middle" hack that works for any node except the last.</p>
<p>In a <b>doubly</b> linked list you simply do <code>p→prev→next = p→next</code> and
<code>p→next→prev = p→prev</code> in O(1) — no copy trick needed.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — LL vs array insertion</div>
People blurt "linked-list insertion is O(1) so it beats arrays". That is only true <b>at the
edges</b>. Middle insertion still costs <b>O(n)</b> just to <i>reach</i> the node, same as the
array's O(n) shift, so for middle operations they are equal — and the array wins on random
<b>access</b> (O(1) vs O(n)). Answer the exact operation, not the data structure.
</div>
""")]})

# ------------------------------------------------- 6. Trees & BSTs
S.append({
 "id": "pds-trees", "title": "Trees & Binary Search Trees", "children": [
  CH("tree", "Binary Trees & Traversals", """
<p>A binary tree node has data + left + right children. The <b>height</b> of a tree is the longest
root→leaf path (edges); for a full note, height of a single node = 0, empty tree = −1.</p>
<table>
<tr><th>Quantity</th><th>Formula</th></tr>
<tr><td>Max nodes, height h</td><td>2<sup>h+1</sup> − 1</td></tr>
<tr><td>Nodes at depth d (root = 0)</td><td>2<sup>d</sup></td></tr>
<tr><td>Min height for n nodes</td><td>⌊log₂(n+1)⌋ − 1 (balanced)</td></tr>
<tr><td>Full/complete tree with n nodes</td><td>⌈log₂(n+1)⌉ levels (root at level 1)</td></tr>
<tr><td>Internal vs leaf in full binary tree (each node 0 or 2 children)</td><td>leaves = internal + 1</td></tr>
</table>
<div class="box formula"><div class="lbl">Three depth-first traversals</div>
<ul>
<li><b>Preorder</b> (VLR): visit node → left → right. Root first.</li>
<li><b>Inorder</b> (LVR): left → node → right. Gives sorted order <b>in a BST</b>.</li>
<li><b>Postorder</b> (LRV): left → right → node. Root last.</li>
</ul>
<p>A <b>level-order</b> (BFS) traversal uses a queue; the others use the recursion stack (or an
explicit stack). Knowing <b>preorder+inorder</b> (or postorder+inorder) uniquely reconstructs a
binary tree; preorder+postorder alone do <b>not</b>.</p>
</div>

<details><summary>Worked example — reconstruct from post+inorder</summary>
<div class="dc">
<p>Postorder: <b>D H I E B F C G A</b> &nbsp;·&nbsp; Inorder: <b>D B H E I A F C G</b></p>
<p>Postorder's last element is the <b>root</b>: A. In inorder, A splits into left
<b>[D B H E I]</b> and right <b>[F C G]</b>. Recurse: in the left, postorder's last of that slice is
B (root of left subtree), etc. Reconstruct to find the tree — a fast GATE staple solved by always
animating root = last-of-postorder, then splitting inorder.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — preorder+postorder is ambiguous</div>
Two different binary trees can share the same preorder <b>and</b> postorder (e.g. a chain of left-only
children vs right-only children). Only <b>one</b> of them, paired with <b>inorder</b>, pins down the
tree. GATE explicitly tests that preorder+postorder is insufficient.
</div>
"""),
  CH("bst", "Binary Search Trees (BST)", """
<p>A BST is a binary tree where, for every node, <b>all left-descendant keys &lt; node &lt; all
right-descendant keys</b>. This yields O(log n) <b>average</b> search/insert/delete, but the worst
case (a degenerate "left chain") is <b>O(n)</b>.</p>
<table>
<tr><th>Operation</th><th>Average</th><th>Worst case (degenerate)</th></tr>
<tr><td>Search</td><td>O(log n)</td><td>O(n)</td></tr>
<tr><td>Insert</td><td>O(log n)</td><td>O(n)</td></tr>
<tr><td>Delete</td><td>O(log n)</td><td>O(n)</td></tr>
<tr><td>Find min / max</td><td>O(log n)</td><td>O(n)</td></tr>
<tr><td>Inorder traversal</td><td colspan="2">O(n) always — outputs sorted keys</td></tr>
</table>
<p><b>BST deletion (3 cases):</b> leaf → unlink; one child → replace with that child;
two children → replace with the <b>inorder successor</b> (leftmost in the right subtree) or
predecessor, then delete that copy. The successor always has at most one child, so the follow-up
delete is easy.</p>

<div class="box tip"><div class="lbl">Shortcut — number of shaped BSTs</div>
The number of structurally distinct BSTs on n keys = the <b>Catalan number</b>
C<sub>n</sub> = C(2n,n)/(n+1). For n = 3 that is 5. This shows up verbatim as a straight count.
</div>

<details><summary>Worked example — BST delete two-child node</summary>
<div class="dc">
<p>Delete 10 from: 10 (root), left child 5, right child 15 (with children 12, 20).</p>
<p>Node 10 has two children. Find its inorder <b>successor</b> = smallest in the right subtree =
<b>12</b> (leftmost node of 15). Replace 10's key with 12, then delete the node carrying 12 from the
right subtree (that node, "12", is itself a leaf there). The resulting root key is 12. This keeps
the BST invariant sound.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — insertion order builds the tree</div>
The shape (and therefore efficiency) of a BST depends <b>entirely on insertion order</b>. Inserting
1,2,3,… produces a degenerate right chain of height O(n). Inserting a median-first order produces a
balanced tree of height O(log n). Saying "BSTs are O(log n)" without qualifying <b>average case</b>
is a mark-losing blunder.
</div>
""")]})

# ------------------------------------------------- 7. Heaps
S.append({
 "id": "pds-heaps", "title": "Binary Heaps",
 "html": """
<p>A <b>binary heap</b> is a complete binary tree (all levels full except possibly the last, filled
left-to-right) stored <b>contiguously in an array</b>. For node at index i (1-based):</p>
<div class="box formula"><div class="lbl">Heap index arithmetic (1-based array)</div>
<ul>
<li>Left child = 2i · Right child = 2i+1 · Parent = ⌊i/2⌋.</li>
<li><b>0-based</b>: left = 2i+1, right = 2i+2, parent = ⌊(i−1)/2⌋.</li>
<li>Max-heap: parent ≥ children. Min-heap: parent ≤ children.</li>
</ul>
</div>
<table>
<tr><th>Operation</th><th>Complexity</th><th>Why</th></tr>
<tr><td>Find max/min</td><td>O(1)</td><td>root</td></tr>
<tr><td>Insert (heapify-up)</td><td>O(log n)</td><td>append then sift up height log n</td></tr>
<tr><td>Delete root (extract max/min)</td><td>O(log n)</td><td>swap with last, sift down</td></tr>
<tr><td>Decrease/increase key</td><td>O(log n)</td><td>sift up / down</td></tr>
<tr><td>Build heap from n keys</td><td><b>O(n)</b> (tight bound)</td><td>sift down from ⌊n/2⌋ down to 1</td></tr>
<tr><td>Heap sort</td><td>O(n log n)</td><td>build O(n) + n extracts O(log n)</td></tr>
</table>
<p><b>Key subtlety:</b> heap sort's <b>best, average and worst</b> are all O(n log n), although heap
sort is not stable. Building a heap is O(n), not O(n log n), because earlier levels do less work.</p>

<details><summary>Worked example — build a max-heap from {4,1,3,7,5,6,2}</summary>
<div class="dc">
<p>Place in array (1-based): [4,1,3,7,5,6,2]. Sift-down from index ⌊7/2⌋=3 downward.</p>
<p>i=3: nodes 6,2 vs 3 → swap 3 with 6 → [4,1,6,7,5,3,2].<br>
i=2: node 7 (left, 2i=4) and 5 (right, biggest 7) vs 1 → swap 1 with 7 → [4,7,6,1,5,3,2].<br>
i=1: children 7 and 6, biggest 7 vs 4 → swap 4 with 7 → [7,4,6,1,5,3,2]; now 7 stays as root.<br>
Final max-heap: <b>[7,4,6,1,5,3,2]</b> — root is 7 (max), each parent ≥ its children. Total swaps
bounded by tree height across all nodes = O(n).</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — a heap is not a sorted array</div>
A max-heap guarantees only that the <b>root is the maximum</b> and each parent ≥ its children. The
array is <b>not</b> sorted — siblings are unordered and the right subtree may exceed the left.
Similarly, "delete root" returns the max but does <b>not</b> leave the remaining array sorted without
one full extract pass. Ordering is only guaranteed by the heap-sort output.
</div>
"""
})

# ------------------------------------------------- 8. Graphs
S.append({
 "id": "pds-graphs", "title": "Graphs: Representations & Traversals",
 "children": [
  CH("grep", "Adjacency Matrix vs List", """
<p>Two standard representations trade memory against lookup speed.</p>
<table>
<tr><th>Metric</th><th>Adjacency matrix (n×n)</th><th>Adjacency list</th></tr>
<tr><td>Space</td><td>O(n²) always</td><td>O(n + m), m = edges</td></tr>
<tr><td>Check edge (u,v)</td><td>O(1)</td><td>O(deg(u)) ≤ O(n)</td></tr>
<tr><td>List neighbours of u</td><td>O(n)</td><td>O(deg(u)) — direct</td></tr>
<tr><td>Add edge</td><td>O(1)</td><td>O(1) (append)</td></tr>
<tr><td>Better for</td><td>dense graphs</td><td>sparse graphs</td></tr>
</table>
<p><b>Degree:</b> in an undirected graph, Σdeg(v) = 2m (handshaking — even number of odd-degree
vertices). In a directed graph, indegree gives in-edges, outdegree gives out-edges, and
Σindeg = Σoutdeg = m.</p>
<p>A graph has an <b>Euler circuit</b> iff it is connected and every vertex has <b>even</b> degree;
an <b>Euler path</b> (not circuit) iff exactly <b>two</b> vertices have odd degree. A <b>Hamiltonian
path/cycle</b> visits every vertex once — no simple criterion, NP-hard to decide.</p>
"""),
  CH("traversal", "BFS & DFS", """
<p><b>BFS</b> (breadth-first) uses a <b>queue</b>, visits in order of distance from the source, and
gives the <b>shortest path</b> in an unweighted graph. <b>DFS</b> (depth-first) uses a <b>stack</b>
(recursion or explicit) and explores a branch fully before backtracking.</p>
<table>
<tr><th>Feature</th><th>BFS</th><th>DFS</th></tr>
<tr><td>Data structure</td><td>queue</td><td>stack</td></tr>
<tr><td>Visit order by</td><td>level (distance)</td><td>depth</td></tr>
<tr><td>Time (matrix/list)</td><td>O(n²) / O(n+m)</td><td>O(n²) / O(n+m)</td></tr>
<tr><td>Space (worst)</td><td>O(n) queue</td><td>O(n) stack</td></tr>
<tr><td>Shortest unweighted path?</td><td><b>yes</b></td><td>no (not guaranteed)</td></tr>
<tr><td>Connectivity / components, cycles</td><td>✓</td><td>✓</td></tr>
<tr><td>Detection of cycles in a directed graph (back edge)</td><td>no</td><td><b>yes</b></td></tr>
</table>
<p><b>DFS edge classification:</b> tree edges, back edges (to ancestor ⇒ cycle), forward edges, and
cross edges. A directed graph has a cycle iff DFS finds a <b>back edge</b>. A <b>topological order</b>
of a DAG is the reverse of DFS finishing times.</p>

<details><summary>Worked example — BFS tree of a small graph</summary>
<div class="dc">
<p>Graph: edges 1−2, 1−3, 2−4, 3−4, 3−5. BFS from vertex 1.</p>
<p>Visit 1 (distance 0). Queue neighbours → 2, 3 (dist 1). Dequeue 2, enqueue its unvisited neighbour
4 (dist 2). Dequeue 3, enqueue 5 (dist 2; 4 already visited). Dequeue 4 — no new neighbours (5 seen).
Dequeue 5. Final BFS order: <b>1, 2, 3, 4, 5</b>, and the shortest distance 1→5 is 2 via 3. BFS gives
both the order and the shortest-path distances for unweighted edges.</p>
</div></details>

<div class="box trap"><div class="lbl">GATE trap — BFS vs DFS order is input-order dependent</div>
Both BFS and DFS orders depend on the <b>order neighbours are listed</b> in the adjacency list —
different adjacency orders yield different (yet valid) traversal orders. GATE always specifies or
pins the adjacency order (often sorted). Never "find the" traversal; find <b>the</b> one for the given
input order, including the initial source vertex.
</div>
""")]})

# ------------------------------------------------- 9. Formula sheet
S.append({
 "id": "pds-formulas", "title": "One-Page Formula Sheet (Revise Before Exam)",
 "html": """
<table>
<tr><th>Topic</th><th>Formula / fact</th></tr>
<tr><td>Pointer arithmetic</td><td>p+n → address+n×sizeof(T); p−p′ → element count</td></tr>
<tr><td>Array decay</td><td>array→pointer in expressions; sizeof gives 8 in callee, full size in decl scope</td></tr>
<tr><td>Strings</td><td><code>sizeof("GATE")=5</code>; <code>strlen=4</code>; char[] size includes '\\0'</td></tr>
<tr><td>Storage classes</td><td>auto/register=stack+garbage; static=zero-init, program lifetime; extern=global</td></tr>
<tr><td>Struct size</td><td>sum of members + padding to max alignment</td></tr>
<tr><td>Union size</td><td>largest member; all members share address, last write wins</td></tr>
<tr><td>Linear recursion</td><td>T(n)=T(n−1)+c → O(n); +n → O(n²); 2T(n−1) → O(2ⁿ)</td></tr>
<tr><td>Divide &amp; conquer</td><td>T(n)=2T(n/2)+n → O(n log n); T(n/2)+c → O(log n)</td></tr>
<tr><td>Recursion space</td><td>= depth (longest live chain), not total calls</td></tr>
<tr><td>Array access</td><td>base + i×sizeof(T); row-major a[i][j]=base+(i×C+j)×k</td></tr>
<tr><td>Stack/Queue</td><td>all core ops O(1); circular queue full=(rear+1)%S==front, empty=front==rear</td></tr>
<tr><td>Linked list</td><td>edge ops O(1), middle O(n); doubly O(1) delete known node; circular links tail→head</td></tr>
<tr><td>Binary tree max nodes</td><td>2^(h+1) − 1 at height h; nodes at depth d = 2^d</td></tr>
<tr><td>Traversals</td><td>VLR=pre, LVR=in (sorted in BST), LRV=post; pre+in uniquely reconstruct, pre+post do NOT</td></tr>
<tr><td>BST</td><td>avg O(log n), worst O(n) degenerate; delete 2-child → successor copy then delete</td></tr>
<tr><td># BSTs on n keys</td><td>Catalan C(2n,n)/(n+1)</td></tr>
<tr><td>Heap ops</td><td>find-min/max O(1), insert/delete O(log n), <b>build O(n)</b>, heap sort O(n log n)</td></tr>
<tr><td>Heap index</td><td>1-based: children 2i,2i+1, parent ⌊i/2⌋</td></tr>
<tr><td>Graph space/time</td><td>matrix O(n²)&nbsp;&amp; O(1) edge check; list O(n+m)&nbsp;&amp; O(n+m) traversal</td></tr>
<tr><td>Euler</td><td>circuit: connected + all even degree; path: exactly two odd-degree</td></tr>
<tr><td>Handshaking</td><td>Σdeg = 2m or 2|E|; # odd-degree vertices is even</td></tr>
<tr><td>BFS/DFS</td><td>BFS=queue→unweighted shortest path; DFS=stack→cycle detect via back edge; time O(n+m)</td></tr>
</table>
"""
})

# ------------------------------------------------- 10. Exam strategy
S.append({
 "id": "pds-strategy", "title": "Exam Strategy",
 "html": """
<div class="box tip"><div class="lbl">Attempt order for maximum marks</div>
<ol>
<li><b>C output/pointer questions first</b> — highest accuracy, mechanical, worth 3–4 marks.</li>
<li><b>Recursion + complexity</b> — 1–2 marks, fast if you write the recurrence.</li>
<li><b>Linear DS complexity</b> — table look-ups, near-free.</li>
<li><b>Trees/heaps/graphs</b> — attempt only if you can hand-trace cleanly; skip the ambiguous ones.</li>
</ol>
</div>
<h3>Common time sinks</h3>
<ul>
<li><b>Hand-tracing a long C recursion</b> — if the depth exceeds ~6, you are likely mis-tracing.
Re-derive from the recurrence instead.</li>
<li><b>Reconstructing a tree</b> — do it column-by-column (root = last postorder / first preorder,
split inorder); never redraw the whole tree.</li>
<li><b>Heap deletion</b> — trace one extract, mentally; a second extract doubles time with no extra
marks.</li>
<li><b>BFS/DFS with unstated neighbour order</b> — if the order isn't given, the question is
ambiguous; skip it rather than guess.</li>
</ul>
<h3>What to skip under time pressure</h3>
<ul>
<li>Questions with <b>undefined behaviour</b> (out-of-bounds array read, uninitialised pointer) —
the "value" is not a well-defined answer.</li>
<li>Any C question requiring <b>endianness</b> unless explicitly stated — it flips the answer.</li>
<li><b>Traversal-order ambiguities</b> — save them for the end.</li>
<li>Pick the safer interpretation of "height": GATE consistently uses <b>edges</b> (single node =
height 0, empty tree = height −1). If unsure, both factor into the options you can reject.</li>
</ul>
"""
})

QUIZ = [
 {"q":"int a[]={1,2,3,4}, *p=a; printf(\"%d\", *(p+2));","opts":["1","2","3","4"],"a":2,
  "ex":"p points to a[0]; p+2 advances by 2 elements (not 2 bytes), so *(p+2) = a[2] = 3."},
 {"q":"void f(int a[3]){ printf(\"%zu\", sizeof(a)); }  What does this print?","opts":["12","8","3","24"],"a":1,
  "ex":"Array parameters decay to pointers. sizeof(a) measures the pointer, 8 bytes on 64-bit, never the array size."},
 {"q":"char s[]=\"GATE\"; The value of sizeof(s) is:","opts":["4","5","8","3"],"a":1,
  "ex":"s holds 'G','A','T','E' plus the terminating '\\0', so sizeof(s) = 5. strlen(s) = 4."},
 {"q":"In C, a static local variable is initialised to:","opts":["garbage","0","undefined value","1"],"a":1,
  "ex":"Static and global variables are zero-initialised before main runs; automatic variables hold garbage."},
 {"q":"int f(void){ static int c=0; return ++c; } printf(\"%d %d\", f(), f());","opts":["1 1","1 2","0 1","2 2"],"a":1,
  "ex":"Static c is initialised once to 0. First call increments to 1; second call increments the same variable to 2, so output is '1 2'."},
 {"q":"The size of union {char c; int i; short s;} on a typical 32-bit machine is:","opts":["7 bytes","8 bytes","4 bytes","2 bytes"],"a":2,
  "ex":"A union's size is its largest member. int is 4 bytes, larger than char(1) and short(2), so the union is 4 bytes."},
 {"q":"struct {char c; int i;} — the size on a typical 32-bit machine is:","opts":["5 bytes","8 bytes","6 bytes","7 bytes"],"a":1,
  "ex":"The int must be 4-byte aligned. 3 bytes of padding follow the char, so total = 1+3+4 = 8 bytes."},
 {"q":"int f(int n){ if(n<=0) return 0; return n + f(n-1); } f(4) = ?","opts":["10","7","6","24"],"a":0,
  "ex":"Linear recursion: 4+3+2+1+0 = 10. Each call adds n and recurses on n-1 down to 0."},
 {"q":"The time complexity of the recurrence T(n) = T(n−1) + n is:","opts":["O(n)","O(n log n)","O(n²)","O(2ⁿ)"],"a":2,
  "ex":"Unrolling: n+(n-1)+...+1 = n(n+1)/2 = O(n²)."},
 {"q":"Maximum stack space used by naive recursive fib(n) is:","opts":["O(2ⁿ)","O(n)","O(log n)","O(n²)"],"a":1,
  "ex":"Space equals recursion depth (longest live chain), which is O(n) even though total calls are O(2ⁿ)."},
 {"q":"Which DFS traversal of a BST yields keys in sorted order?","opts":["Preorder","Postorder","Inorder","Level-order"],"a":2,
  "ex":"Inorder (left, node, right) visits the BST in ascending key order."},
 {"q":"A binary tree of height 4 (root height 0) has at most how many nodes?","opts":["15","16","31","32"],"a":2,
  "ex":"Max nodes = 2^(h+1) − 1 = 2^5 − 1 = 31."},
 {"q":"Preorder + postorder of a binary tree:","opts":["always uniquely determine the tree","never determine the tree","do not necessarily uniquely determine the tree","determine only leaf nodes"],"a":2,
  "ex":"Two different trees (e.g. all-left vs all-right chains) share the same preorder and postorder, so together they are ambiguous. You need inorder."},
 {"q":"Number of structurally distinct BSTs on 4 keys is:","opts":["8","10","14","4"],"a":2,
  "ex":"Catalan number C₄ = C(8,4)/5 = 70/5 = 14."},
 {"q":"In a max-heap stored 1-based, the index of the parent of node i is:","opts":["i/2","2i","2i+1","⌈i/2⌉"],"a":0,
  "ex":"In the standard 1-based array heap, children of i are 2i and 2i+1, so parent of i is ⌊i/2⌋ (integer i/2)."},
 {"q":"Time to build a binary heap of n keys from an arbitrary array is:","opts":["O(n log n)","O(n²)","O(n)","O(log n)"],"a":2,
  "ex":"Building by sifting down from ⌊n/2⌋ to 1 is O(n) — the tight bound, even though each sift is O(log n)."},
 {"q":"Which data structure gives the shortest path in an unweighted graph?","opts":["DFS stack","BFS queue","Both equally","Neither"],"a":1,
  "ex":"BFS visits vertices in order of distance from the source, so the first time a vertex is found is its shortest distance. DFS does not guarantee this."},
 {"q":"Handshaking lemma: the number of odd-degree vertices in any graph is:","opts":["always odd","always even","always zero","can be anything"],"a":1,
  "ex":"Σdeg = 2m is even, so odd-degree vertices must come in pairs — an even count."},
 {"q":"A connected graph has an Euler circuit iff:","opts":["all vertices have even degree","exactly two vertices have odd degree","it is a tree","it is bipartite"],"a":0,
  "ex":"Connected + all even degrees gives an Euler circuit. Exactly two odd degrees gives only an Euler path, not a circuit."},
 {"q":"Which is the amortised cost of insertion at the end of a dynamic array?","opts":["O(n)","O(log n)","O(1)","O(n log n)"],"a":2,
  "ex":"Doubling on overflow spreads the occasional O(n) copy, giving amortised O(1) per append."},
]

SUBJECT = {
 "code": "S04", "title": "Programming & Data Structures",
 "subtitle": "GATE CS 2027 · 9 marks · Programming in C, recursion, arrays, stacks, queues, linked lists, trees, BSTs, heaps, graphs",
 "weight_note": "GATE CS 2027 · Programming & Data Structures section (9 marks)",
 "sections": S, "quiz": QUIZ,
}