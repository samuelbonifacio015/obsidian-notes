#!/usr/bin/env python3
"""Validate all [[wikilinks]] in the Obsidian vault, reporting broken links.

Usage:
    python validate-wikilinks.py                  # scan entire vault
    python validate-wikilinks.py --path Semana\ 5 # scan specific folder
"""

import re
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent  # obsidian/
REPORTS_DIR = Path(__file__).resolve().parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def extract_wikilinks(text: str) -> list[str]:
    """Return list of target names from [[wikilinks]] in text.

    Strips aliases [[Real|alias]] → Real, headings [[nota#heading]] → nota,
    block refs [[nota^id]] → nota. Removes leading/trailing whitespace.
    """
    links = []
    for match in WIKILINK_RE.finditer(text):
        target = match.group(1).strip()
        # Strip heading/block references
        for sep in ("#", "^", "|"):
            if sep in target:
                target = target.split(sep)[0].strip()
        if target:
            links.append(target)
    return links


def extract_markdown_links(text: str) -> list[str]:
    """Return URL/file paths from [text](path) markdown links."""
    return [m.group(2) for m in LINK_RE.finditer(text)]


def vault_path_for(target: str, vault: Path) -> Path | None:
    """Resolve a wikilink target to a real file in the vault.

    Tries direct match, .md extension, and nested paths with spaces.
    """
    # Direct: target.md
    p = vault / f"{target}.md"
    if p.exists():
        return p
    # Subdirectories: search by name
    for ext in ("", ".md"):
        candidates = list(vault.rglob(f"{target}{ext}"))
        if candidates:
            return candidates[0]
    return None


def main():
    args = set(sys.argv[1:])
    if "--path" in args:
        idx = sys.argv.index("--path") + 1
        if idx < len(sys.argv):
            scan_path = VAULT / sys.argv[idx]
        else:
            scan_path = VAULT
    else:
        scan_path = VAULT

    if not scan_path.exists():
        print(f"ERROR: Path does not exist: {scan_path}", file=sys.stderr)
        sys.exit(2)

    md_files = list(scan_path.rglob("*.md"))
    print(f"Scanning {len(md_files)} .md files in {scan_path}...\n")

    total_links = 0
    broken_links: list[tuple[str, int, str, str]] = []  # (file, line_no, broken_target, full_line)

    for md_file in sorted(md_files):
        try:
            text = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"  SKIP {md_file.relative_to(VAULT)}: {e}", file=sys.stderr)
            continue

        lines = text.split("\n")
        for lineno, line in enumerate(lines, start=1):
            targets = extract_wikilinks(line)
            for target in targets:
                total_links += 1
                if not vault_path_for(target, VAULT):
                    broken_links.append((
                        str(md_file.relative_to(VAULT)),
                        lineno,
                        target,
                        line.strip(),
                    ))

    # Generate report
    report_lines = [
        "---",
        "title: Wikilink Validation Report",
        "tags: [report, wikilink, vault-health]",
        f"generated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "---",
        "",
        f"# 🔗 Wikilink Validation Report",
        "",
        f"**Total wikilinks found:** {total_links}",
        f"**Valid links:** {total_links - len(broken_links)}",
        f"**Broken links:** {len(broken_links)}",
        f"**Files scanned:** {len(md_files)}",
        "",
    ]

    if broken_links:
        report_lines.append("## ❌ Broken Links\n")
        # Group by source file
        from collections import defaultdict
        by_file: dict[str, list] = defaultdict(list)
        for filepath, lineno, target, line in broken_links:
            by_file[filepath].append((lineno, target, line))

        report_lines.append("| Source File | Line | Broken Wikilink | Context |")
        report_lines.append("|------------|------|----------------|---------|")
        for filepath in sorted(by_file):
            for lineno, target, line in by_file[filepath]:
                report_lines.append(
                    f"| `{filepath}` | {lineno} | `[[{target}]]` | `{line[:60]}` |"
                )

        report_lines.append("")
        report_lines.append("### Suggested fixes")
        report_lines.append("")
        for filepath in sorted(by_file):
            for lineno, target, line in by_file[filepath]:
                report_lines.append(f"- `{filepath}` line {lineno}: `[[{target}]]` → create `{target}.md` or fix link")

    # Also check for broken markdown links to local files
    report_lines.extend(["\n## 📎 Markdown Link Check (local files)\n", ""])

    for md_file in sorted(md_files):
        try:
            text = md_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        lines = text.split("\n")
        for lineno, line in enumerate(lines, start=1):
            urls = extract_markdown_links(line)
            for url in urls:
                if url.startswith("file://"):
                    local_path = Path(url.replace("file://", ""))
                    if not local_path.exists():
                        report_lines.append(
                            f"| `{md_file.relative_to(VAULT)}` | {lineno} | `{url}` | file not found |"
                        )

    report_text = "\n".join(report_lines)

    # Write report
    report_file = REPORTS_DIR / "wikilink-report.md"
    report_file.write_text(report_text, encoding="utf-8")
    print(report_text)

    # Console summary
    print(f"\n{'='*60}")
    print(f"📄 Report saved: {report_file.relative_to(VAULT.parent)}")
    print(f"{'='*60}")
    for filepath, lineno, target, line in broken_links:
        print(f"  ❌ {filepath}:{lineno} → [[{target}]]")

    if not broken_links:
        print("  ✅ All wikilinks valid!")

    sys.exit(0 if not broken_links else 1)


if __name__ == "__main__":
    main()
