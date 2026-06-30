"""Build the Session 13 AIML assignment HTML/PDF with code and outputs."""

from __future__ import annotations

import html
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
HTML_FILE = ROOT / "session_13_aiml_assignment_solutions.html"
PDF_FILE = ROOT / "session_13_aiml_assignment_solutions.pdf"

ASSIGNMENTS = [
    {
        "title": "Q1. Basic Array Creation",
        "file": "q13_01_basic_array_creation.py",
        "input": "",
    },
    {
        "title": "Q2. np.zeros() and np.ones()",
        "file": "q13_02_zeros_ones.py",
        "input": "",
    },
    {
        "title": "Q3. np.arange()",
        "file": "q13_03_arange.py",
        "input": "",
    },
    {
        "title": "Q4. np.linspace()",
        "file": "q13_04_linspace.py",
        "input": "",
    },
    {
        "title": "Q5. Random Arrays",
        "file": "q13_05_random_arrays.py",
        "input": "",
    },
    {
        "title": "Q6. Vectors and Basic Operations",
        "file": "q13_06_vectors_operations.py",
        "input": "",
    },
    {
        "title": "Q7. Matrices and Operations",
        "file": "q13_07_matrices_operations.py",
        "input": "",
    },
    {
        "title": "Q8. Properties of Arrays",
        "file": "q13_08_array_properties.py",
        "input": "",
    },
    {
        "title": "Q9. Combined - Random + Reshape + Statistics",
        "file": "q13_09_random_reshape_statistics.py",
        "input": "",
    },
    {
        "title": "Q10. Mini Project - NumPy Application",
        "file": "q13_10_statistics_calculator.py",
        "input": "12\n",
    },
]

STUDENT_DETAILS = {
    "project": "Assignment 13 NumPy",
    "name": "Vaishnavi Dnyanoba Surnar",
    "github": "https://github.com/vaishnavisurnar/assignment13_numpy",
    "domain": "AI/ML",
    "college": "Zeal College Of Polytechnic Pune",
}


def run_python(file_name: str, input_text: str) -> str:
    """Run an assignment script and return stdout/stderr."""
    completed = subprocess.run(
        [sys.executable, str(ROOT / file_name)],
        input=input_text,
        text=True,
        capture_output=True,
        cwd=ROOT,
        check=False,
    )
    output = completed.stdout
    if completed.stderr:
        output += "\nSTDERR:\n" + completed.stderr
    return output.strip()


def build_html() -> None:
    """Create the printable HTML assignment document."""
    sections: list[str] = []

    for item in ASSIGNMENTS:
        source = (ROOT / item["file"]).read_text(encoding="utf-8").rstrip()
        output = run_python(item["file"], item["input"])

        sections.append(
            f"""
            <article class="question">
              <h2># {html.escape(item["title"])}</h2>
              <pre>{html.escape(source)}</pre>
              <h3>Output :-</h3>
              <pre>{html.escape(output)}</pre>
            </article>
            """
        )

    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Assignment 13 NumPy Project File</title>
  <style>
    @page {{
      size: A4;
      margin: 18mm 16mm;
    }}
    * {{
      box-sizing: border-box;
    }}
    body {{
      color: #111111;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 14px;
      line-height: 1.45;
      margin: 0;
      background: #ffffff;
    }}
    .cover {{
      margin-bottom: 18px;
    }}
    h1 {{
      font-size: 16px;
      font-weight: 700;
      margin: 0 0 8px;
    }}
    h2 {{
      font-size: 18px;
      font-weight: 700;
      margin: 18px 0 8px;
    }}
    h3 {{
      font-size: 16px;
      font-weight: 700;
      margin: 18px 0 8px;
    }}
    .details {{
      font-size: 16px;
      font-weight: 700;
      margin: 0 0 8px;
    }}
    .question {{
      margin-bottom: 24px;
    }}
    .question + .question {{
      break-before: page;
      page-break-before: always;
    }}
    a {{
      color: #0645ad;
      text-decoration: underline;
    }}
    pre {{
      background: #ffffff;
      border: 0;
      color: #111827;
      font-family: Consolas, "Courier New", monospace;
      font-size: 11px;
      line-height: 1.45;
      margin: 0 0 12px;
      overflow-wrap: break-word;
      padding: 0;
      white-space: pre-wrap;
      word-break: break-word;
    }}
  </style>
</head>
<body>
  <header class="cover">
    <p class="details">Project :-</p>
    <p class="details">Name:- {html.escape(STUDENT_DETAILS["name"])}</p>
    <p class="details">GitHub Link:- <a href="{html.escape(STUDENT_DETAILS["github"])}">{html.escape(STUDENT_DETAILS["github"])}</a></p>
    <p class="details">Domain :- {html.escape(STUDENT_DETAILS["domain"])}</p>
    <p class="details">College Name:- {html.escape(STUDENT_DETAILS["college"])}</p>
    <h1># {html.escape(STUDENT_DETAILS["project"])}</h1>
  </header>
  {"".join(sections)}
</body>
</html>
"""
    HTML_FILE.write_text(document, encoding="utf-8")


def find_chrome() -> Path | None:
    """Return a local Chromium-based browser path when available."""
    candidates = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def build_pdf() -> None:
    """Print the HTML file to PDF using headless Chrome or Edge."""
    browser = find_chrome()
    if browser is None:
        print("Created session_13_aiml_assignment_solutions.html")
        print("PDF was not created because Chrome/Edge was not found.")
        return

    command = [
        str(browser),
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_FILE}",
        HTML_FILE.as_uri(),
    ]
    subprocess.run(command, cwd=ROOT, check=True)
    print("Created session_13_aiml_assignment_solutions.html")
    print("Created session_13_aiml_assignment_solutions.pdf")


def main() -> None:
    build_html()
    build_pdf()


if __name__ == "__main__":
    main()
