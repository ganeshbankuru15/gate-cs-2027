# CONTENT SPEC — GATE CS 2027 Notes (subject content modules)

You are writing ONE content module for an existing, working notes website.
The website engine (`notes_engine.py`) and the reference subject (`subject_01_engmath.py`)
already exist. **Do not modify them.** You only create a new content module file.

---

## 1. The file you must create

Write exactly one file, using Python's `write_file` tool, at the path assigned to you, e.g.:

```
/home/rl/gate-cs-notes/build/subject_05_algorithms.py
```

It must be **valid Python 3** and import cleanly.

---

## 2. Exact module contract

Your file MUST define exactly three names: `S`, `QUIZ`, `SUBJECT`.
Use this skeleton verbatim (only the content changes):

```python
# -*- coding: utf-8 -*-
"""Subject 05 — Algorithms (10 marks, GATE CS)."""

S = []
CH = lambda i, t, h: {"id": i, "title": t, "html": h}

S.append({
    "id": "unique-slug",            # lowercase, a-z 0-9 and dashes ONLY, unique in this file
    "title": "Section Title",       # rendered as the big heading + TOC entry
    "html": """
    ... your content HTML here ...
    """
})

# A section may instead/additionally have children (rendered as sub-headings):
S.append({
    "id": "another-slug", "title": "Another Section",
    "children": [
        CH("sub-slug", "Sub Topic Title", """
        ... content ...
        """),
    ]
})

QUIZ = [
    {"q": "Question text?", "opts": ["Option A", "Option B", "Option C", "Option D"],
     "a": 2, "ex": "Explanation of why option C is correct."},
    # ... exactly 20 items ...
]

SUBJECT = {
    "code": "S05",
    "title": "Algorithms",
    "subtitle": "GATE CS 2027 · 10 marks · <short one-line description of coverage>",
    "weight_note": "GATE CS 2027 · Algorithms (10 marks)",
    "sections": S,
    "quiz": QUIZ,
}
```

**Critical rules about the structure:**
- `S` is a list. Each element is a section object.
- A section object MUST have `id` and `title`. It should have EITHER `html` OR `children` (or both).
- `children` is a list of `CH(id, title, html)` results. The engine renders each child's
  `title` as an `<h3>` heading **automatically** — so **do NOT repeat the title inside the child's html**.
- Every `id` in the file must be unique (engine builds anchor links from them).
- `a` is the **0-based index** of the correct option (0=A, 1=B, 2=C, 3=D).

---

## 3. Content requirements (per subject)

- **8–12 top-level sections** covering the ENTIRE official syllabus below. Nothing omitted.
- **14–22 total sub-topics** across the sections (use `children` for the main sub-topics).
- **At least 6 worked examples**, each wrapped in a collapsible block:
  ```html
  <details><summary>Worked example — <what it shows></summary>
  <div class="dc">
  <p>Step-by-step solution...</p>
  </div></details>
  ```
- **At least 4 formula/property boxes** using:
  ```html
  <div class="box formula"><div class="lbl">Box title</div>
  <p>Formulas...</p>
  </div>
  ```
- **At least 1 "GATE trap" box per major section** — the mistakes examiners exploit:
  ```html
  <div class="box trap"><div class="lbl">GATE trap</div><p>...</p></div>
  ```
- **At least 2 "tip" boxes** somewhere in the subject:
  ```html
  <div class="box tip"><div class="lbl">Shortcut / tip</div><p>...</p></div>
  ```
- **At least 4 reference tables** (`<table>` with `<tr><th>...</th></tr>` header row).
- A final section titled **"One-Page Formula Sheet"** — a single dense `<table>` of every
  formula/fact worth memorising for that subject.
- A final section titled **"Exam Strategy"** — how to attempt this subject, common time sinks,
  what to skip under time pressure.

---

## 4. Quiz requirements

- **Exactly 20 questions.**
- Mix of conceptual, numerical and "which statement is true" style — like real GATE.
- Every question has exactly **4 options** and a **correct `a` index**.
- `ex` must actually explain the reasoning (1–3 sentences). No empty explanations.
- **Correctness matters more than difficulty.** Do not invent facts. If unsure, pick a
  well-established standard fact.
- Difficulty spread: roughly 8 easy, 8 medium, 4 hard.

---

## 5. HTML vocabulary — use ONLY these

| Purpose | Markup |
|---|---|
| Keyword/inline code | `<code>x</code>` |
| Multi-line code | `<pre><code>...</code></pre>` |
| Formula/property box | `<div class="box formula"><div class="lbl">Title</div>...</div>` |
| Warning box | `<div class="box trap"><div class="lbl">GATE trap</div>...</div>` |
| Tip box | `<div class="box tip"><div class="lbl">Tip</div>...</div>` |
| Plain box | `<div class="box">...</div>` |
| Collapsible solution | `<details><summary>Worked example — X</summary><div class="dc">...</div></details>` |
| Table | `<table><tr><th>H1</th><th>H2</th></tr><tr><td>a</td><td>b</td></tr></table>` |
| Fact chips row | `<div class="kv"><span class="chip">Weight <b>10 marks</b></span></div>` |
| Headings *inside* html | `<h4>...</h4>` (and `<h3>` sparingly) |

**Do NOT use:** `<script>`, `<style>`, `<html>`, `<head>`, `<body>`, `<link>`, `<img>`,
external URLs, MathJax/LaTeX (`$...$`, `\frac`), or any CSS class not in the table above.
External images and external fonts will not load offline.

**Math notation:** use plain Unicode and HTML — e.g. `O(n log n)`, `Σ`, `Θ`, `⌈n/2⌉`, `x²`,
`2ⁿ`, `≤`, `≥`, `≠`, `→`, `⟹`, `∈`, `∪`, `∩`, `⌊x⌋`. Use `<sub>`/`<sup>` for scripts.
Inside `<pre>` use plain ASCII only.

---

## 6. Writing style

- Exam-focused and dense. No filler, no "in this section we will learn".
- Every claim should be the kind of thing that earns marks.
- Prefer tables and boxes over long prose paragraphs.
- Use `<b>` to bold key terms.
- Assume a competent engineering student, not a beginner.
- Write plain, simple, clear English.

---

## 7. Validation you MUST run before finishing

From `/home/rl/gate-cs-notes/build/`:

```bash
cd /home/rl/gate-cs-notes/build && python3 -c "
import importlib.util, sys
spec = importlib.util.spec_from_file_location('m', 'subject_XX_yourname.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
print('sections:', len(m.S))
print('quiz:', len(m.QUIZ))
ids = [s['id'] for s in m.S] + [c['id'] for s in m.S for c in s.get('children', [])]
assert len(ids) == len(set(ids)), 'DUPLICATE IDS'
assert len(m.QUIZ) == 20
assert all(0 <= q['a'] < 4 and len(q['opts']) == 4 for q in m.QUIZ)
assert m.SUBJECT['code'].startswith('S')
print('ALL CHECKS PASSED')
"
```

Fix any error and re-run until it prints **ALL CHECKS PASSED**. Do not finish before that.

---

## 8. Official GATE CS 2027 syllabus — your assigned subject only

- **S02 Digital Logic (7 marks):** Boolean algebra and minimisation — algebraic technique,
  Karnaugh map, tabular (Quine–McCluskey) method. Design of combinational and sequential circuits.
  Number representation and arithmetic. Logic gates and static CMOS. Multiplexers, decoders,
  code converters. Latches and flip-flops, counters, shift registers, finite state machines.
  Propagation delay, setup and hold time, critical path delay, data hazards.
- **S03 Computer Organization & Architecture (8 marks):** Machine instructions and addressing
  modes, ALU, data-path and control unit, instruction pipelining, pipeline hazards, memory
  hierarchy (cache, main memory, secondary storage), I/O interface (interrupt and DMA mode).
- **S04 Programming & Data Structures (9 marks):** Programming in C, recursion, arrays, stacks,
  queues, linked lists, trees, binary search trees, binary heaps, graphs.
- **S05 Algorithms (10 marks):** Searching, sorting, hashing, asymptotic worst-case time and
  space complexity, algorithm design techniques (greedy, dynamic programming, divide and
  conquer), graph traversals, minimum spanning trees, shortest paths.
- **S06 Theory of Computation (8 marks):** Regular expressions and finite automata, context-free
  grammars and push-down automata, regular and context-free languages, pumping lemma, Turing
  machines and undecidability.
- **S07 Compiler Design (6 marks):** Lexical analysis, parsing, syntax-directed translation,
  runtime environments, intermediate code generation, local optimisation, data-flow analyses
  (constant propagation, liveness analysis, common subexpression elimination).
- **S08 Operating Systems (8 marks):** System calls, processes, threads, inter-process
  communication, concurrency and synchronisation, deadlock, CPU and I/O scheduling, memory
  management and virtual memory, file systems.
- **S09 Databases (8 marks):** ER-model, relational model (relational algebra, tuple calculus,
  SQL), integrity constraints, normal forms, file organisation, indexing (B and B+ trees),
  transactions and concurrency control.
- **S10 Computer Networks (8 marks):** Principles of layering; basics of switching (circuit,
  packet, virtual circuit) and performance metrics; data link layer (error detection, Medium
  Access Control, Ethernet); routing (distance vector and link state); IP addressing, CIDR,
  IPv4, NAT, ARP/DHCP/ICMP; transport layer (flow control, congestion control, UDP, TCP,
  sockets); application layer (DNS, SMTP, HTTP, FTP).

---

## 9. Reference implementation

Read `/home/rl/gate-cs-notes/build/subject_01_engmath.py` for the **structure and style**
(do not copy its content). Match its density, box usage and tonal quality.
