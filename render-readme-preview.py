#!/usr/bin/env python3
"""Render README.md to a GitHub-like paginated PDF for visual review."""

from pathlib import Path

import markdown
from weasyprint import HTML


HERE = Path(__file__).resolve().parent
README = HERE / "README.md"
OUT = HERE / "assets" / "qc" / "README-preview.pdf"

body = markdown.markdown(
    README.read_text(encoding="utf-8"),
    extensions=["fenced_code", "tables", "sane_lists"],
)

css = r"""
@page { size: 1180px 1700px; margin: 0; }
* { box-sizing: border-box; }
html { background: #f6f8fa; }
body {
  margin: 0;
  padding: 48px 70px 72px;
  color: #1f2328;
  background: #ffffff;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-size: 18px;
  line-height: 1.58;
}
h1, h2, h3 { line-height: 1.25; font-weight: 650; }
h1 { margin: 0 0 26px; padding-bottom: 12px; font-size: 42px; border-bottom: 1px solid #d0d7de; }
h2 { margin: 38px 0 16px; padding-bottom: 9px; font-size: 29px; border-bottom: 1px solid #d8dee4; }
h3 { margin: 28px 0 12px; font-size: 23px; }
p { margin: 0 0 18px; }
a { color: #0969da; text-decoration: none; }
img { display: block; max-width: 100%; height: auto; margin: 22px auto; border-radius: 8px; }
code { padding: .15em .35em; background: #eff1f3; border-radius: 5px; font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 88%; }
pre { margin: 18px 0; padding: 18px 20px; overflow: hidden; background: #f6f8fa; border-radius: 8px; }
pre code { padding: 0; background: transparent; font-size: 15px; line-height: 1.5; }
ul, ol { margin: 0 0 18px; padding-left: 34px; }
li { margin: 5px 0; }
table { width: 100%; margin: 18px 0 26px; border-collapse: collapse; font-size: 15px; }
th, td { padding: 9px 12px; border: 1px solid #d0d7de; text-align: left; }
th { background: #f6f8fa; font-weight: 650; }
tr:nth-child(even) td { background: #fbfcfd; }
blockquote { margin: 18px 0; padding: 0 18px; color: #59636e; border-left: 4px solid #d0d7de; }
hr { height: 1px; margin: 30px 0; border: 0; background: #d8dee4; }
"""

document = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
OUT.parent.mkdir(parents=True, exist_ok=True)
HTML(string=document, base_url=str(HERE)).write_pdf(OUT)
print(OUT)
