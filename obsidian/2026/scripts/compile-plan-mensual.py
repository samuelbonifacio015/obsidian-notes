#!/usr/bin/env python3
"""Compile Plan_Mensual.md from weekly plans, summaries, and trackers.

Scans all weeks within a given month, extracts goals, achievements,
learnings, and friction points, then fills in Plan_Mensual.md.

Usage:
    python compile-plan-mensual.py --month Abril --year 2026
    python compile-plan-mensual.py --all          # current month
    python compile-plan-mensual.py --month Abril --year 2026 --dry-run
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parent.parent.parent  # obsidian/


def find_week_folders(vault: Path, month: str, year: str) -> list[Path]:
    """Find all Semana N folders within a given month/year."""
    base = vault / year / month
    if not base.exists():
        print(f"  ⚠️ Month path not found: {base}", file=sys.stderr)
        return []
    return sorted(base.glob("Semana */"))


def extract_frontmatter_field(text: str, field: str) -> str | None:
    """Extract a YAML frontmatter field value by key."""
    m = re.search(rf"^{field}:\s*(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None


def extract_goals_from_weekly_plan(plan_text: str) -> list[str]:
    """Extract goal-like statements from a weekly plan."""
    goals = []
    # Look for top priorities or objetivo field
    objetivo = extract_frontmatter_field(plan_text, "objetivo")
    if objetivo:
        goals.append(objetivo)
    # Also look for checkboxes with key tasks
    for m in re.finditer(r"- \[ \] (.+)", plan_text):
        line = m.group(1).strip()
        if any(kw in line.lower() for kw in ["[x]", "top", "prioridad", "must"]):
            continue
        if len(line) > 20 and not line.startswith("_"):
            goals.append(line)
    return goals


def extract_achievements_from_weekly_plan(plan_text: str) -> list[str]:
    """Extract completed items (checkbox with [x]) from a weekly plan."""
    achievements = []
    for m in re.finditer(r"- \[x\] (.+)", plan_text):
        line = m.group(1).strip()
        if len(line) > 10:
            achievements.append(line)
    return achievements


def extract_learnings(text: str) -> list[str]:
    """Extract learning/concept statements from text."""
    learnings = []
    for m in re.finditer(r"(?:Aprendizaje|Learning|Concepto|Concept|📚|🧠|📖)\s*:?\s*(.+?)(?:\n|$)", text):
        learnings.append(m.group(1).strip())
    # Also look for "Things I Learned" sections
    in_section = False
    for line in text.split("\n"):
        if "Things I Learned" in line or "Aprendí" in line or "🧠" in line:
            in_section = True
            continue
        if in_section:
            if line.strip().startswith("-") or line.strip().startswith("*"):
                learnings.append(line.strip().lstrip("-*").strip())
            elif line.strip() == "" or line.strip().startswith("##"):
                in_section = False
    return learnings


def extract_frictions(text: str) -> list[str]:
    """Extract friction/bottleneck statements from text."""
    frictions = []
    for m in re.finditer(r"(?:Fricción|Friction|Riesgo|Risk|Bloqueador|Bottleneck|cuello de botella|⚠️)\s*:?\s*(.+?)(?:\n|$)", text):
        frictions.append(m.group(1).strip())
    return frictions


def extract_memories(text: str) -> list[str]:
    """Extract reflective/emotional statements."""
    memories = []
    for m in re.finditer(r"(?:💭|Reflexión|Reflection|Memor|Mood|How Do I Feel)\s*:?\s*(.+?)(?:\n|$)", text):
        memories.append(m.group(1).strip())
    return memories


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", default=None, help="Month name (e.g. Abril)")
    parser.add_argument("--year", default=None, help="Year (e.g. 2026)")
    parser.add_argument("--all", action="store_true", help="Use current month/year")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    args = parser.parse_args()

    if args.all or not args.month:
        now = datetime.now()
        args.month = now.strftime("%B")  # English month name
        args.year = str(now.year)
    
    # Map Spanish months
    month_map = {
        "January": "Enero", "February": "Febrero", "March": "Marzo",
        "April": "Abril", "May": "Mayo", "June": "Junio",
        "July": "Julio", "August": "Agosto", "September": "Septiembre",
        "October": "Octubre", "November": "Noviembre", "December": "Diciembre",
    }
    
    # Map English months to Spanish if needed
    if args.month in month_map:
        month_spanish = month_map[args.month]
    else:
        month_spanish = args.month

    # Find the plan mensual file
    plan_file = VAULT / args.year / month_spanish / "Plan_Mensual.md"
    if not plan_file.exists():
        print(f"⚠️ Plan_Mensual.md not found at: {plan_file}")
        print(f"   Looking for: {args.year}/{month_spanish}/Plan_Mensual.md")
        # Try with English name
        plan_file = VAULT / args.year / args.month / "Plan_Mensual.md"
        if not plan_file.exists():
            print(f"   Also not at: {plan_file}")
            sys.exit(1)

    # Read existing plan to preserve manual content
    existing_text = ""
    if plan_file.exists():
        existing_text = plan_file.read_text(encoding="utf-8")

    week_folders = find_week_folders(VAULT, month_spanish, args.year)
    print(f"📂 Found {len(week_folders)} week folders in {month_spanish} {args.year}")

    all_achievements = []
    all_learnings = []
    all_frictions = []
    all_memories = []
    all_goals = []
    week_plans_found = 0
    week_summaries_found = 0

    for week_dir in week_folders:
        print(f"  Scanning: {week_dir.name}")
        for f in week_dir.glob("*.md"):
            try:
                text = f.read_text(encoding="utf-8")
            except Exception:
                continue

            if "Summary" in f.name or "summary" in f.name:
                week_summaries_found += 1
                all_achievements.extend(extract_achievements_from_weekly_plan(text))
                all_learnings.extend(extract_learnings(text))
                all_memories.extend(extract_memories(text))
                all_frictions.extend(extract_frictions(text))

            if "Plan" in f.name:
                week_plans_found += 1
                goals = extract_goals_from_weekly_plan(text)
                all_goals.extend(goals)
                all_achievements.extend(extract_achievements_from_weekly_plan(text))

    # Deduplicate while preserving order
    def unique_preserve(items):
        seen = set()
        result = []
        for item in items:
            key = item.lower().strip()
            if key not in seen and len(key) > 5:
                seen.add(key)
                result.append(item)
        return result

    all_goals = unique_preserve(all_goals)[:6]
    all_achievements = unique_preserve(all_achievements)[:8]
    all_learnings = unique_preserve(all_learnings)[:6]
    all_frictions = unique_preserve(all_frictions)[:5]
    all_memories = unique_preserve(all_memories)[:4]

    # Build content
    goals_text = "\n".join(f"- [ ] {g}" for g in all_goals) if all_goals else "- [ ] "
    achievements_text = "\n".join(f"- {a}" for a in all_achievements) if all_achievements else "- "
    learnings_text = "\n".join(f"- {l}" for l in all_learnings) if all_learnings else "- "
    frictions_text = "\n".join(f"- {f}" for f in all_frictions) if all_frictions else "- "
    memories_text = "\n".join(f"> {m}" for m in all_memories) if all_memories else "> "

    # Only fill sections that are currently empty/template in the existing plan
    def section_is_empty(text: str, section_header: str) -> bool:
        """Check if a section in the existing plan has meaningful content."""
        lines = text.split("\n")
        in_section = False
        content_lines = 0
        for line in lines:
            if section_header in line:
                in_section = True
                continue
            if in_section:
                if line.strip().startswith("##") or line.strip().startswith("---"):
                    break
                stripped = line.strip().lstrip("-*> ")
                if stripped and stripped not in ("", "-", ">", "Things I Achieved", "Things I Learned",
                                                  "Things I Need to Improve", "Memories", "How Do I Feel"):
                    content_lines += 1
        return content_lines < 2

    lines = existing_text.split("\n")
    new_lines = []
    in_goals = False
    in_achievements = False
    in_learnings = False
    in_improve = False
    in_memories = False

    goals_filled = False
    achievements_filled = False
    learnings_filled = False
    frictions_filled = False
    memories_filled = False

    for line in lines:
        if "## 🎯 Goals" in line or "## ⚡ Priorities" in line:
            in_goals = True
        elif "## ✅ To Do" in line:
            in_goals = False
        elif "## ✨ Things I Achieved" in line or "## Logros" in line:
            in_achievements = True
        elif "## 🧠 Things I Learned" in line or "## Aprendizaje" in line:
            in_learnings = True
        elif "## 🔧 Things I Need to Improve" in line or "## 🔧 Fricción" in line:
            in_improve = True
        elif "## 💭 Memories" in line or "## How Do I Feel" in line:
            in_memories = True

        if in_goals and not goals_filled and (line.strip().startswith("- [ ]") or line.strip().startswith("1.")):
            if all_goals:
                new_lines.append(goals_text)
                goals_filled = True
                in_goals = False
                continue
            else:
                in_goals = False
        elif in_achievements and not achievements_filled and line.strip().startswith("-"):
            if all_achievements:
                new_lines.append(achievements_text)
                achievements_filled = True
                in_achievements = False
                continue
            else:
                in_achievements = False
        elif in_learnings and not learnings_filled and line.strip().startswith("-"):
            if all_learnings:
                new_lines.append(learnings_text)
                learnings_filled = True
                in_learnings = False
                continue
            else:
                in_learnings = False
        elif in_improve and not frictions_filled and line.strip().startswith("-"):
            if all_frictions:
                new_lines.append(frictions_text)
                frictions_filled = True
                in_improve = False
                continue
            else:
                in_improve = False
        elif in_memories and not memories_filled and line.strip().startswith(">"):
            if all_memories:
                new_lines.append(memories_text)
                memories_filled = True
                in_memories = False
                continue
            else:
                in_memories = False

        new_lines.append(line)

    output = "\n".join(new_lines)

    if args.dry_run:
        print(output)
        sys.exit(0)

    plan_file.write_text(output, encoding="utf-8")
    print(f"\n✅ Plan_Mensual.md updated: {plan_file}")
    print(f"   {len(week_folders)} weeks scanned")
    print(f"   {week_plans_found} plans, {week_summaries_found} summaries found")
    print(f"   Goals: {len(all_goals)} | Achievements: {len(all_achievements)} | Learnings: {len(all_learnings)}")
    print(f"   Frictions: {len(all_frictions)} | Memories: {len(all_memories)}")
    sys.exit(0)


if __name__ == "__main__":
    main()
