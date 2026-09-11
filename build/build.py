# -*- coding: utf-8 -*-
"""Build the full GATE CS 2027 notes site.

Imports every subject content module that exists, renders each to HTML,
and writes the index hub. Safe to re-run any time.
"""
import importlib.util, json, os, pathlib, sys, traceback

BUILD = pathlib.Path(__file__).resolve().parent
# Repo root by default (parent of build/); overridable via NOTES_OUT so the
# same script works locally and on a CI runner (no hardcoded absolute paths).
OUT = pathlib.Path(os.environ.get("NOTES_OUT") or BUILD.parent)
OUT.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(BUILD))
import notes_engine as E

# code, title, marks, output filename, module name
SUBJECTS = [
    ("S01", "Engineering Mathematics",              13, "01-engineering-mathematics.html", "subject_01_engmath"),
    ("S02", "Digital Logic",                         7, "02-digital-logic.html",          "subject_02_digital_logic"),
    ("S03", "Computer Organization & Architecture",  8, "03-coa.html",                    "subject_03_coa"),
    ("S04", "Programming & Data Structures",         9, "04-programming-ds.html",         "subject_04_programming_ds"),
    ("S05", "Algorithms",                           10, "05-algorithms.html",             "subject_05_algorithms"),
    ("S06", "Theory of Computation",                 8, "06-toc.html",                    "subject_06_toc"),
    ("S07", "Compiler Design",                       6, "07-compiler-design.html",        "subject_07_compiler_design"),
    ("S08", "Operating Systems",                     8, "08-operating-systems.html",      "subject_08_operating_systems"),
    ("S09", "Databases",                             8, "09-databases.html",              "subject_09_databases"),
    ("S10", "Computer Networks",                     8, "10-computer-networks.html",      "subject_10_computer_networks"),
]


def load(modname):
    """Import a subject module by filename. Returns module or None."""
    path = BUILD / (modname + ".py")
    if not path.exists():
        return None
    try:
        spec = importlib.util.spec_from_file_location(modname, str(path))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        # structural validation
        assert isinstance(m.S, list) and len(m.S) > 0, "empty sections"
        assert isinstance(m.QUIZ, list) and len(m.QUIZ) > 0, "empty quiz"
        ids = []
        for s in m.S:
            ids.append(s["id"])
            for c in s.get("children", []):
                ids.append(c["id"])
        assert len(ids) == len(set(ids)), "duplicate ids"
        assert all(0 <= q["a"] < len(q["opts"]) for q in m.QUIZ), "bad quiz answer index"
        m.SUBJECT.setdefault("code", "S??")
        return m
    except Exception:
        print("  !! FAILED to load %s:" % modname)
        traceback.print_exc()
        return None


# ---- load everything -------------------------------------------------------
loaded = {}
for code, title, marks, fname, mod in SUBJECTS:
    m = load(mod)
    loaded[code] = (m, fname, title, marks)
    if m:
        n_sections = len(m.S)
        n_sub = sum(len(s.get("children", [])) for s in m.S)
        n_det = sum(s.get("html", "").count("<details>") for s in m.S) + \
                sum(c.get("html", "").count("<details>") for s in m.S for c in s.get("children", []))
        print("  ok  %s %-42s sections=%2d subs=%2d quiz=%2d examples=%d"
              % (code, title, n_sections, n_sub, len(m.QUIZ), n_det))

built_codes = [c for c, *_ in SUBJECTS if loaded[c][0]]

# ---- render subject pages --------------------------------------------------
for i, (code, title, marks, fname, mod) in enumerate(SUBJECTS):
    m, fname, title, marks = loaded[code]
    if not m:
        continue
    prevs = [c for c in SUBJECTS[:i] if loaded[c[0]][0]]
    nexts = [c for c in SUBJECTS[i + 1:] if loaded[c[0]][0]]
    nav = []
    if prevs:
        p = prevs[-1]
        nav.append('<a href="%s">← %s %s</a>' % (p[3], p[0], p[1]))
    else:
        nav.append('<span class="sp">← start</span>')
    nav.append('<a href="index.html">⌂ All subjects</a>')
    if nexts:
        n = nexts[0]
        nav.append('<a href="%s">%s %s →</a>' % (n[3], n[0], n[1]))
    else:
        nav.append('<span class="sp">end →</span>')

    html = E.render_subject(m.SUBJECT, len(built_codes), "".join(nav))
    (OUT / fname).write_text(html, encoding="utf-8")
    print("  wrote %-34s %7d bytes" % (fname, len(html)))

# ---- render index ----------------------------------------------------------
subj_meta = []
for code, title, marks, fname, mod in SUBJECTS:
    m = loaded[code][0]
    subj_meta.append({
        "code": code, "title": title, "marks": marks, "file": fname, "built": m is not None,
        "blurb": (m.SUBJECT.get("subtitle", "").split("·")[-1].strip() if m else
                  "Content module not yet built."),
    })

ROADMAP = """
<h2>📊 Coverage</h2>
<p>Total coverage: <b>%d of 100 marks</b> across <b>%d of 10 subjects</b>.</p>
<h2>🗓️ Study Plan — 149 days to GATE 2027</h2>
<p>Exam: <b>6–21 Feb 2027</b> (IIT Madras) · Registration closes <b>27 Sep 2026</b>, late fee till 5 Oct.</p>
<table>
<tr><th>Phase</th><th>When</th><th>Focus</th></tr>
<tr><td><b>0 · Register</b></td><td>now → 27 Sep 2026</td><td>GATE 2027 application on GOAPS — do not miss this</td></tr>
<tr><td><b>1 · Foundations</b></td><td>Sep–Oct 2026</td><td>S01 Eng Maths · S04 Prog &amp; DS · S02 Digital Logic</td></tr>
<tr><td><b>2 · Heavyweights</b></td><td>Nov 2026</td><td>S05 Algorithms · S08 OS · S03 COA</td></tr>
<tr><td><b>3 · Complete syllabus</b></td><td>Dec 2026</td><td>S06 TOC · S09 DBMS · S10 Networks · S07 Compilers</td></tr>
<tr><td><b>4 · Revision + PYQs</b></td><td>Jan 2027</td><td>Full mocks, previous-year papers, formula sheets</td></tr>
<tr><td><b>5 · Final sprint</b></td><td>1–5 Feb 2027</td><td>Formula sheets + weak topics only</td></tr>
</table>
<div class="box tip"><div class="lbl">How to use these notes</div>
<ol>
<li>Open a subject, read a concept box, then open the <b>Worked example</b> blocks.</li>
<li>Take the <b>20-question quiz</b> at the end of each subject — instant feedback and a score.</li>
<li>Tick the <b>“done”</b> checkbox on each section; your progress saves automatically.</li>
<li>Use <b>Print / PDF</b> to make an offline copy for revision.</li>
<li>Use the <b>← → subject</b> buttons in the header to move between subjects.</li>
</ol>
</div>
<h2>📚 Other Research</h2>
<div class="grid">
  <a class="card" href="research/psu-guide/GATE_CS_PSU_Complete_Guide.html"><div class="n">RESEARCH</div><div class="t">PSU Recruitment Guide (GATE CS)</div><div class="w">24 PSUs</div><p style="font-size:13px;color:var(--muted);margin:8px 0 0">Cutoffs, salaries, bonds, eligibility and sources for every major PSU hiring CSE engineers through GATE. Also available as <a href="research/psu-guide/GATE_CS_PSU_Complete_Guide.pdf">PDF</a>.</p></a>
</div>
<div class="box trap"><div class="lbl">Be honest about the numbers</div>
These are AI-compiled study notes. Concept explanations and formula sheets are reliable,
but <b>verify any numerical answer against an official GATE answer key</b> before you rely on it.
</div>
""" % (sum(s["marks"] for s in subj_meta if s["built"]),
       sum(1 for s in subj_meta if s["built"]))

(OUT / "index.html").write_text(E.render_index(subj_meta, ROADMAP), encoding="utf-8")
print("  wrote index.html")

(OUT / "manifest.json").write_text(json.dumps({
    "built": built_codes,
    "total_marks_covered": sum(s["marks"] for s in subj_meta if s["built"]),
    "subjects": subj_meta,
}, indent=2), encoding="utf-8")

print("\nDONE: %d/%d subjects, %d/100 marks"
      % (len(built_codes), len(SUBJECTS), sum(s["marks"] for s in subj_meta if s["built"])))
