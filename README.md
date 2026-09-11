# GATE CS 2027 — Complete Notes & Research

A self-contained, offline study website for **GATE Computer Science & Information Technology 2027**
plus supporting research documents.

**Live site:** https://YOUR-USERNAME.github.io/gate-cs-2027/ *(once GitHub Pages is enabled)*

---

## What's inside

### 📘 Notes website — 10 subjects, 85 of 100 marks

| Code | Subject | Marks | Sections | Quiz Qs |
|------|---------|-------|----------|---------|
| S01 | Engineering Mathematics | 13 | 11 | 20 |
| S02 | Digital Logic | 7 | 10 | 20 |
| S03 | Computer Organization & Architecture | 8 | 11 | 20 |
| S04 | Programming & Data Structures | 9 | 10 | 20 |
| S05 | Algorithms | 10 | 12 | 20 |
| S06 | Theory of Computation | 8 | 12 | 20 |
| S07 | Compiler Design | 6 | 10 | 20 |
| S08 | Operating Systems | 8 | 10 | 20 |
| S09 | Databases | 8 | 11 | 20 |
| S10 | Computer Networks | 8 | 10 | 20 |

**Totals:** 107 sections · 200 quiz questions · ~110 worked examples · ~150 formula boxes · 130+ reference tables.

Every subject includes: concept notes, formula boxes, "GATE trap" warnings, collapsible worked
examples, a one-page formula sheet, an exam-strategy section, and a 20-question quiz with
instant feedback.

**Features:** dark/light theme · collapsible solutions · per-section progress tracking ·
print-to-PDF · subject-to-subject navigation · fully offline (no external requests).

### 📄 Research

- `research/psu-guide/` — PSU recruitment guide for GATE CS (24 PSUs, cutoffs, salaries,
  bonds, eligibility, sources).

---

## How to use

**Online:** open the GitHub Pages URL above — works on any device, anywhere.

**Offline:** clone or download the repo, then open `index.html` in any browser.
No server, no internet, no dependencies.

```bash
git clone https://github.com/YOUR-USERNAME/gate-cs-2027.git
cd gate-cs-2027
# open index.html in your browser
```

---

## Repository layout

```
.
├── index.html                  # hub: all subjects + study plan
├── 01-engineering-mathematics.html
├── 02-digital-logic.html
├── ...
├── 10-computer-networks.html
├── manifest.json               # machine-readable index of coverage
├── assets/                     # preview screenshots
├── research/
│   └── psu-guide/              # PSU recruitment research
├── build/                      # source: build scripts + content modules
│   ├── notes_engine.py         # HTML/CSS/JS template + renderer
│   ├── build.py                # builds every subject page + index
│   ├── subject_*.py            # content modules (one per subject)
│   └── CONTENT_SPEC.md         # spec used to author content modules
└── .github/workflows/pages.yml # CI/CD: rebuild checks + deploy to Pages
```

## Rebuilding the site

```bash
cd build
python3 build.py      # regenerates all HTML pages + index
```

Requires only Python 3 (standard library). The content lives in `build/subject_*.py`;
the presentation lives in `build/notes_engine.py`.

---

## ⚠️ Accuracy disclaimer — please read

These notes are **AI-generated study material**.

- **Coverage is reliable** — every subject was built against the official IIT Madras
  GATE 2027 CS syllabus.
- **Explanations, formulas, worked examples and quiz answers are AI output and are NOT
  textbook-verified.** They can contain errors, including confident-sounding ones.

**Always cross-check numericals and edge cases** against an official GATE previous-year
paper with its published answer key, or a standard textbook:

- Algorithms — CLRS
- Operating Systems — Galvin / Silberschatz
- Databases — Korth / Navathe
- Computer Networks — Tanenbaum / Kurose-Ross
- Compilers — Aho / Ullman (the Dragon Book)
- Digital Logic — Morris Mano
- Engineering Mathematics — Kreyszig / standard GATE references

Use this as a **structure and revision map**, not as an unquestioned source.

---

## GATE 2027 key dates

| Event | Date |
|-------|------|
| Notification | 20 July 2026 |
| Registration opens | 27 August 2026 |
| **Registration closes** | **27 September 2026** (late fee till 5 Oct) |
| Exam | 6, 7, 13, 14, 20, 21 February 2027 |
| Result | 19 March 2027 |

**Pattern:** 65 questions · 100 marks · 3 hours
General Aptitude 15 + Engineering Mathematics 13 + Core CS 72

**Gap:** General Aptitude (15 marks) is not yet covered — the notes currently cover
the 85 technical marks.

---

## License

Study material compiled for personal GATE 2027 preparation. No warranty of accuracy.
