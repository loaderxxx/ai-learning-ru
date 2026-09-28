"""Check this track's Markdown file links and RU/EN module pairs; no network.

This is a small checker for inline links, not a complete Markdown parser.
It does not validate external URLs, fragment anchors, or translation accuracy.
"""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SLUGS = ["00-start", "01-foundations", "02-contracts", "03-model-api", "04-routing",
         "05-tools", "06-workflows", "07-retrieval", "08-mcp", "09-evals",
         "10-reliability", "11-security", "12-delivery", "13-observability",
         "14-specialization", "15-capstone"]


def check(root: Path) -> dict:
    errors = []
    files = sorted(set((root / "ai-in-code").rglob("*.md")) |
                   set((root / "engineers").rglob("*.md")) |
                   {root / "README.md", root / "README.en.md"})
    internal_links = 0
    for slug in SLUGS:
        for suffix in (".md", ".en.md"):
            p = root / "ai-in-code" / "modules" / (slug + suffix)
            if not p.is_file():
                errors.append(f"Missing module: {p.relative_to(root)}")
    for p in files:
        if not p.is_file():
            errors.append(f"Missing page: {p.relative_to(root)}")
            continue
        content = p.read_text(encoding="utf-8")
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = match.group(1).strip().split()[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            internal_links += 1
            dest = (p.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():
                errors.append(f"Broken file link: {p.relative_to(root)} -> {target}")
    return {"pages_checked": len(files), "module_pairs": len(SLUGS),
            "internal_file_links": internal_links, "errors": errors,
            "not_checked": ["external URL availability", "anchor fragments", "translation accuracy"]}


if __name__ == "__main__":
    result = check(ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(1 if result["errors"] else 0)
