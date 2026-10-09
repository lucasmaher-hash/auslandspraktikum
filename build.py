"""Baut docs/index.html (GitHub Pages) aus index.html (Artifact-Quelle).

Die Artifact-Plattform legt beim Veröffentlichen selbst ein HTML-Gerüst um die
Seite. Für GitHub Pages fehlt das, also ergänzt dieses Skript Doctype, Charset,
Viewport und die zwei Reset-Regeln, auf die sich die Seite verlässt.

Aufruf: python3 build.py
"""
from pathlib import Path

root = Path(__file__).parent
src = (root / "index.html").read_text(encoding="utf-8")

split = src.index("</style>") + len("</style>")
head, body = src[:split], src[split:]

page = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>body{{margin:0}}[hidden]{{display:none!important}}</style>
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""

out = root / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding="utf-8")
print(f"geschrieben: {out}")
