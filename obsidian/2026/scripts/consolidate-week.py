#!/usr/bin/env python3
"""Consolidate a week folder into a live week-tracker.md.

Scans all checkins, todolists, todoreviewers, and summaries in a Semana N folder,
cross-references checkboxes vs checkin responses, calculates a real score,
and updates week-tracker.md.

Usage:
    python consolidate-week.py --week 5 --month Abril --year 2026
    python consolidate-week.py --all  # scan all weeks in current month
    python consolidate-week.py --week 5 --dry-run
"""

import argparse
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

VAULT = Path(__file__).resolve().parent.parent.parent  # obsidian/
SCRIPTS_DIR = Path(__file__).resolve().parent

# Day mapping
DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
CHECKBOX_RE = re.compile(r"- \[([ x])\] (.+)")
SCORE_RE = re.compile(r"score:\s*(\d+)/10", re.IGNORECASE)


def extract_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter into a dict."""
    result = {}
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not m:
        return result
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def find_day_files(week_dir: Path) -> dict[str, dict[str, Path]]:
    """Group files by day. Returns {dia: {tipo: path}}."""
    days: dict = {}
    for f in week_dir.glob("*.md"):
        if f.name == "week-tracker.md" or f.name == "SKILL.md":
            continue
        name = f.stem.lower()
        for dia in DIAS:
            if name.startswith(dia):
                if dia not in days:
                    days[dia] = {}
                # Determine type
                for tipo in ["checkin", "todolist", "todoreviewer", "summary"]:
                    if tipo in name or tipo in f.name:
                        days[dia][tipo] = f
                        break
                else:
                    # Generic plan or other
                    if "plan" in name or "tuesday" in name:
                        days[dia]["plan"] = f
                    else:
                        days[dia]["other"] = f
    return days


def score_from_files(files: dict) -> float | None:
    """Extract score from summary or checkin files."""
    for tipo in ["summary", "checkin"]:
        if tipo in files:
            text = files[tipo].read_text(encoding="utf-8")
            fm = extract_frontmatter(text)
            if "score" in fm:
                m = re.search(r"(\d+)", fm["score"])
                if m:
                    return float(m.group(1))
    return None


def extract_mood(text: str) -> str | None:
    """Extract mood tag from frontmatter."""
    fm = extract_frontmatter(text)
    tags = fm.get("tags", "")
    # Check frontmatter tags
    for tag in re.split(r"[\[\],\s]+", tags):
        if tag.startswith("dia/") or tag.startswith("#dia/"):
            return tag.replace("#", "")
    # Check body
    m = re.search(r"(dia/productivo|dia/intenso|dia/regular|dia/flojo)", text)
    if m:
        return m.group(1)
    return None


def extract_checkboxes(text: str) -> list[dict]:
    """Extract all checkboxes with their text and state."""
    items = []
    for m in CHECKBOX_RE.finditer(text):
        items.append({
            "state": "done" if m.group(1) == "x" else "pending",
            "text": m.group(2).strip(),
            "wikilinks": WIKILINK_RE.findall(m.group(2)),
        })
    return items


def extract_completed_tasks(text: str) -> list[str]:
    """Extract only completed checkbox texts."""
    return [
        m.group(2).strip()
        for m in CHECKBOX_RE.finditer(text)
        if m.group(1) == "x"
    ]


def day_names_from_files(files: dict) -> list[str]:
    """Return ordered list of days that have any file."""
    present = []
    for dia in DIAS:
        if dia in files and files[dia]:
            present.append(dia)
    return present


def calculate_score(days_data: dict) -> dict:
    """Calculate weekly score and metrics from day data."""
    total_items = 0
    done_items = 0
    days_with_data = set()
    day_scores = []

    for dia, data in days_data.items():
        if not data:
            continue
        days_with_data.add(dia)

        # From todolist vs checkin/summary
        if "todolist" in data:
            todolist_text = data["todolist"].read_text(encoding="utf-8")
            todo_checkboxes = extract_checkboxes(todolist_text)
            # Only count real tasks, not meta-tasks
            real_items = [c for c in todo_checkboxes if c["text"] and not any(
                kw in c["text"].lower() for kw in
                ["generar", "crear", "preparar", "revisar que", "cerrar el dia"]
            )]
            
            if "checkin" in data:
                checkin_text = data["checkin"].read_text(encoding="utf-8")
                # Check which tasks are confirmed in checkin
                for item in real_items:
                    total_items += 1
                    # If checkbox is [x] in todolist AND mentioned positively in checkin
                    for wl in item["wikilinks"]:
                        if wl in checkin_text:
                            # Check if it's positively mentioned
                            idx = checkin_text.find(wl)
                            context = checkin_text[max(0, idx-60):idx+60+len(wl)]
                            if any(kw in context.lower() for kw in ["sí", "si ", "avancé", "completé", "hice", "terminé", "entregué"]):
                                done_items += 1
                                break
            elif "summary" in data:
                summary_text = data["summary"].read_text(encoding="utf-8")
                summary_tasks = extract_completed_tasks(summary_text)
                for item in real_items:
                    total_items += 1
                    item_lower = item["text"].lower()
                    for task in summary_tasks:
                        if any(w.lower() in task.lower() for w in item["wikilinks"]):
                            done_items += 1
                            break
            else:
                # Infer from todolist checkboxes only
                for item in real_items:
                    total_items += 1
                    if item["state"] == "done":
                        done_items += 1

        # Day score from summary
        day_score = score_from_files(data)
        if day_score is not None:
            day_scores.append(day_score)

    score_percent = round((done_items / max(total_items, 1)) * 100)
    avg_day_score = round(sum(day_scores) / max(len(day_scores), 1), 1) if day_scores else 0

    return {
        "score_percent": score_percent,
        "avg_day_score": avg_day_score,
        "total_items": total_items,
        "done_items": done_items,
        "days_with_data": len(days_with_data),
        "day_scores": day_scores,
    }


def determine_mood(metrics: dict, days_data: dict) -> str:
    """Infer week mood from metrics."""
    score = metrics["score_percent"]
    if score >= 80:
        return "#semana/productiva"
    elif score >= 60:
        return "#semana/intensa"
    elif score >= 40:
        return "#semana/regular"
    else:
        return "#semana/flojo"


def build_recap(days_data: dict) -> list[tuple[str, str]]:
    """Build a recap line per day."""
    recap = []
    for dia in DIAS:
        if dia in days_data and days_data[dia]:
            parts = []
            data = days_data[dia]
            if "checkin" in data:
                parts.append("✅ checkin")
            if "todolist" in data:
                parts.append("📋 todolist")
            if "todoreviewer" in data:
                parts.append("🔍 review")
            if "summary" in data:
                parts.append("📊 summary")
            if "plan" in data:
                parts.append("📝 plan")
            recap.append((dia, ", ".join(parts) if parts else "sin registro"))
        else:
            recap.append((dia, "sin registro"))
    return recap


def build_risks(days_data: dict, week_dir: Path) -> list[str]:
    """Detect recurring risks from week data."""
    risks = []
    pending_tracker = defaultdict(list)

    for dia, data in days_data.items():
        if "todolist" in data:
            text = data["todolist"].read_text(encoding="utf-8")
            for item in extract_checkboxes(text):
                if item["state"] == "pending":
                    for wl in item["wikilinks"]:
                        pending_tracker[wl].append(dia)

    for target, dias in pending_tracker.items():
        if len(dias) >= 2:
            risks.append(f"`[[{target}]]` aparece pendiente {len(dias)} días ({', '.join(dias)})")

    if not risks:
        risks.append("Sin riesgos detectados automáticamente")
    return risks[:4]  # max 4 risks


def detect_projects(days_data: dict) -> dict[str, str]:
    """Detect active projects from wikilinks in week files."""
    project_mentions = defaultdict(int)
    
    # Known projects
    known_projects = [
        "MaquinariasJyS", "QRust", "Klippr", "QRust Org", "QRust - Klippr",
        "Braymar", "WeTech", "WeRide", "Listalico"
    ]
    
    for dia, data in days_data.items():
        for tipo, f in data.items():
            try:
                text = f.read_text(encoding="utf-8")
            except Exception:
                continue
            for wl in WIKILINK_RE.finditer(text):
                target = wl.group(1).split("|")[0].split("#")[0].strip()
                if target in known_projects:
                    project_mentions[target] += 1
    
    status = {}
    for proj, count in sorted(project_mentions.items(), key=lambda x: -x[1]):
        if count >= 5:
            status[proj] = "activo" if proj in ("MaquinariasJyS",) else "mencionado"
        elif count >= 2:
            status[proj] = "mencionado"
    
    return status


def is_same_week(date_str: str, target_monday: str) -> bool:
    """Check if a date string falls in the same week as target_monday."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        # Get the Monday of that date's week
        monday = d - timedelta(days=d.weekday())
        return monday.strftime("%Y-%m-%d") == target_monday
    except (ValueError, TypeError):
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int, default=None)
    parser.add_argument("--month", default=None)
    parser.add_argument("--year", default=None)
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--path", default=None, help="Direct path to Semana folder")
    args = parser.parse_args()

    if args.path:
        week_dir = Path(args.path)
    elif args.week:
        month = args.month or "Abril"
        year = args.year or "2026"
        week_dir = VAULT / year / month / f"Semana {args.week}"
    elif args.all:
        month = args.month or "Abril"
        year = args.year or "2026"
        base = VAULT / year / month
        for d in sorted(base.glob("Semana */")):
            process_week(d, args.dry_run)
        sys.exit(0)
    else:
        print("ERROR: Need --week N or --all or --path", file=sys.stderr)
        sys.exit(2)

    if not week_dir.exists():
        print(f"ERROR: Week folder not found: {week_dir}", file=sys.stderr)
        sys.exit(1)

    process_week(week_dir, args.dry_run)


def process_week(week_dir: Path, dry_run: bool = False):
    """Process a single week folder."""
    week_name = week_dir.name
    parent = week_dir.parent
    print(f"\n{'='*60}")
    print(f"📂 Processing: {week_name}")
    print(f"{'='*60}")

    # Gather files by day
    days_data = find_day_files(week_dir)
    present_days = day_names_from_files(days_data)

    print(f"   Days with files: {', '.join(present_days) if present_days else 'NONE'}")

    # Detect projects
    projects = detect_projects(days_data)
    print(f"   Projects detected: {', '.join(projects.keys()) if projects else 'none'}")

    # Calculate metrics
    metrics = calculate_score(days_data)
    print(f"   Score: {metrics['score_percent']}% ({metrics['done_items']}/{metrics['total_items']} items)")

    mood = determine_mood(metrics, days_data)
    recap = build_recap(days_data)
    risks = build_risks(days_data, week_dir)

    # Build recap text
    recap_lines = []
    for dia, summary in recap:
        recap_lines.append(f"- {dia.capitalize()}: {summary}")
    
    # Build projects section
    proj_lines = []
    for proj, status in projects.items():
        if status == "activo":
            proj_lines.append(f"- [[{proj}]]: activo")
        else:
            proj_lines.append(f"- [[{proj}]]: mencionado ({status})")
    if not proj_lines:
        proj_lines.append("- Sin proyectos detectados")

    # Context for agents
    total_days = len(present_days)
    context = (
        f"Semana {week_name.split()[-1]} — {total_days} días registrados "
        f"de 7. Score: {metrics['score_percent']}%. "
        f"Foco principal inferido de archivos presentes. "
        f"{'Sin check-ins completados — score basado en todolists.' if not any('checkin' in d for d in days_data.values()) else ''}"
    )

    # Read existing tracker to preserve any manual content
    tracker_file = week_dir / "week-tracker.md"
    existing_text = ""
    if tracker_file.exists():
        existing_text = tracker_file.read_text(encoding="utf-8")

    # Extract dates from existing tracker frontmatter if available
    fm = extract_frontmatter(existing_text)
    fecha_inicio = fm.get("fecha_inicio", "desconocido")
    fecha_fin = fm.get("fecha_fin", "desconocido")

    # Build the updated content — preserve existing header if present
    content = f"""---
title: Week Tracker - {week_name}
tags:
  - week-tracker
  - semana-{week_name.split()[-1]}
  - upc
  - tracker
fecha_inicio: {fecha_inicio}
fecha_fin: {fecha_fin}
score_semana: {metrics['score_percent']}%
estado: {"en-curso" if total_days < 5 else "por-cerrar"}
foco_principal: {', '.join(projects.keys())[:80] if projects else 'Por determinar'}
riesgo_principal: {risks[0].replace('`', '')[:80] if risks and 'Sin riesgos' not in risks[0] else 'N/A'}
---

# {week_name}: {metrics['score_percent']}% | {', '.join(list(projects.keys())[:2]) if projects else 'Sin foco'} | Score basado en {metrics['done_items']}/{metrics['total_items']} items

---

## Score

- [[Score]]: {metrics['score_percent']}%
- [[Foco Principal]]: {', '.join(projects.keys())[:80] if projects else 'Pendiente'}
- [[Riesgo Principal]]: {risks[0].replace('`', '').replace('[', '').replace(']', '')[:80] if risks and 'Sin riesgos' not in risks[0] else 'Sin riesgos detectados'}
- [[Dias Registrados]]: {total_days}/7
- [[Mood Semana]]: {mood}

---

## Boards

### Universidad

- [[Calculo II]]: {"activo" if "Calculo" in str([d for d in days_data.values()]) else "pendiente de revisar"}
- [[Estadistica Aplicada]]: {"activo" if "Estadistica" in str([d for d in days_data.values()]) else "pendiente de revisar"}
- [[Sistemas Operativos]]: {"revisar estado" if "Sistemas" in str([d for d in days_data.values()]) else "pendiente"}
- [[Aplicaciones Moviles]]: {"confirmar pendientes" if "Aplicaciones" in str([d for d in days_data.values()]) else "pendiente"}

### Proyectos

{chr(10).join(proj_lines)}

### IA & Dev

- Claude Code: {"uso detectado" if "claude" in str([d for d in days_data.values()]).lower() else "sin registro"}
- Modelos locales / APIs: {"sin registro"}

### Personal

- Sueno: {"registrar" if total_days > 0 else "sin inicio"}
- Energia: {"por evaluar"}
- Pasos / ejercicio: {"sin datos"}
- Bloqueos: {"sin reporte"}

---

## Recap De La Semana

{chr(10).join(recap_lines)}

---

## Contexto Operativo Para Agentes

{context}

---

## Riesgos Activos

{chr(10).join(f"- [ ] {r}" for r in risks)}

---

## Proximas Acciones

- [ ] Completar check-ins de dias faltantes
- [ ] Generar summaries y todoreviewers pendientes
- [ ] Actualizar tracker al cerrar cada dia

---

## Links

{chr(10).join(f"[[{f.stem}]]" for f in sorted(week_dir.glob("*.md")) if f.stem not in ("SKILL", "week-tracker", "Tuesday-Plan-W4"))}

---

*Generado con `scripts/consolidate-week.py` · {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""

    # Preserve manual content from Snippets / Learning Journal section if it exists
    if existing_text:
        # Find the Snippets section
        m = re.search(r"(## Snippets / Learning Journal.*?)(?=## |$)", existing_text, re.DOTALL)
        if m:
            snippets = m.group(1).strip()
            if snippets and "{{CONCEPTOS}}" not in snippets:
                # Append it before the Links section
                content = content.replace("## Links", f"{snippets}\n\n---\n\n## Links")

    if dry_run:
        print("\n--- GENERATED OUTPUT ---")
        print(content)
        sys.exit(0)

    tracker_file.write_text(content, encoding="utf-8")
    print(f"\n✅ week-tracker.md updated: {tracker_file}")
    print(f"   Score: {metrics['score_percent']}% ({metrics['done_items']}/{metrics['total_items']})")
    print(f"   Days: {total_days}/7")
    print(f"   Risks: {len(risks)}")


if __name__ == "__main__":
    main()
