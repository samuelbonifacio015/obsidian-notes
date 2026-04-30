#!/usr/bin/env python3
"""Generate a todolist for today (or a specified day) from carried-over pending tasks.

Scans the previous day's todoreviewer, summary, and checkin for uncompleted
items, then generates {dia}-todolist.md with prioritized tasks.

Usage:
    python start-day.py                        # today
    python start-day.py --date 2026-04-30      # specific date
    python start-day.py --today --dry-run       # preview without writing
    python start-day.py --day jueves --week 5   # midweek override
"""

import argparse
import re
import sys
from datetime import datetime, date
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent  # obsidian/

DIAS = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
DIAS_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def extract_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter."""
    result = {}
    m = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not m:
        return result
    for line in m.group(1).split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def extract_pending_tasks(text: str) -> list[str]:
    """Extract incomplete checkbox items."""
    tasks = []
    for m in re.finditer(r"- \[ \] (.+)", text):
        line = m.group(1).strip()
        if line and not any(kw in line.lower() for kw in ["generar ", "crear ", "preparar "]):
            tasks.append(line)
    return tasks


def extract_completed_tasks(text: str) -> list[str]:
    """Extract completed checkbox items."""
    return [m.group(1).strip() for m in re.finditer(r"- \[x\] (.+)", text)]


def get_today_info() -> tuple[str, str, str]:
    """Return (spanish_day, english_day, iso_date) for today."""
    today = date.today()
    dia_en = today.strftime("%A")
    idx = DIAS_EN.index(dia_en)
    dia_es = DIAS[idx]
    return dia_es, dia_en, today.isoformat()


def detect_current_week(vault: Path, today: date) -> tuple[Path, str, str]:
    """Find the current week folder based on today's date."""
    year = str(today.year)
    
    # Spanish month names
    meses_es = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    month_es = meses_es[today.month - 1]
    
    month_dir = vault / year / month_es
    
    if not month_dir.exists():
        # Try alternative months
        for alt in ["Abril"]:  # fallback to Abril for now
            alt_dir = vault / year / alt
            if alt_dir.exists():
                month_dir = alt_dir
                month_es = alt
                break
    
    if not month_dir.exists():
        return None, month_es, "desconocido"
    
    # Find the right week folder
    week_num = today.isocalendar()[1]
    # Scan existing week folders
    week_folders = sorted(month_dir.glob("Semana */"))
    
    best_match = None
    for wf in week_folders:
        # Check if any file in this folder is from this week
        for f in wf.glob("*.md"):
            try:
                text = f.read_text(encoding="utf-8")
                fm = extract_frontmatter(text)
                fecha = fm.get("fecha", "")
                if fecha:
                    try:
                        d = date.fromisoformat(fecha)
                        if d.isocalendar()[1] == week_num and d.year == today.year:
                            best_match = wf
                            break
                    except ValueError:
                        pass
            except Exception:
                continue
    
    if not best_match and week_folders:
        # Last resort: use the most recent week folder
        best_match = week_folders[-1]
    
    return best_match, month_es, week_num


def yesterday_info(today: date) -> tuple[str, date]:
    """Get yesterday's day name and date."""
    y = today - __import__("datetime").timedelta(days=1)
    idx = DIAS_EN.index(y.strftime("%A"))
    return DIAS[idx], y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="ISO date for target day")
    parser.add_argument("--day", default=None, help="Spanish day name (e.g., jueves)")
    parser.add_argument("--week", type=int, default=None, help="Week number")
    parser.add_argument("--today", action="store_true", help="Use today's date")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    args = parser.parse_args()

    # Determine target date
    if args.date:
        target = date.fromisoformat(args.date)
        dia_es, _, _ = get_today_info()
        # Override day from date
        idx = target.weekday()
        dia_es = DIAS[idx]
    elif args.day and args.week:
        # Custom day+week
        today = date.today()
        # Try to find the right date
        iso_year = today.isocalendar()[0]
        # Use a generic approach
        target = today
        dia_es = args.day
    else:
        # Default: today
        today = date.today()
        target = today
        dia_es, _, _ = get_today_info()

    # Find week folder
    week_dir, month_es, week_num = detect_current_week(VAULT, target)
    if not week_dir:
        print(f"⚠️ Could not determine current week folder for {target}", file=sys.stderr)
        # Create a default path
        month_es = "Abril"
        week_dir = VAULT / "2026" / month_es / f"Semana {args.week or target.isocalendar()[1]}"
        week_dir.mkdir(parents=True, exist_ok=True)
        print(f"   Created: {week_dir}")

    target_file = week_dir / f"{dia_es}-todolist.md"
    if target_file.exists() and not args.dry_run:
        print(f"⏭️  Already exists: {target_file}")
        print(f"   Remove or rename it first to regenerate.")
        sys.exit(0)

    yesterday_name, y_date = yesterday_info(target)
    yesterday_summary = week_dir / f"{yesterday_name}-summary.md"
    yesterday_reviewer = week_dir / f"{yesterday_name}-todoreviewer.md"
    yesterday_checkin = week_dir / f"{yesterday_name}-checkin.md"

    # Collect pending tasks from yesterday
    pending_tasks = []
    for src_file, label in [
        (yesterday_reviewer, "todoreviewer"),
        (yesterday_summary, "summary"),
        (yesterday_checkin, "checkin"),
    ]:
        if src_file.exists():
            text = src_file.read_text(encoding="utf-8")
            tasks = extract_pending_tasks(text)
            # Filter out meta-tasks
            real_tasks = [t for t in tasks if not any(
                kw in t.lower() for kw in
                ["generar", "crear", "preparar [[", "cerrar el dia"]
            )]
            for t in real_tasks:
                pending_tasks.append((t, label))
            print(f"   Found {len(real_tasks)} pending from {label}")

    # Also check the week-tracker for pending items
    week_tracker = week_dir / "week-tracker.md"
    if week_tracker.exists():
        text = week_tracker.read_text(encoding="utf-8")
        tasks = extract_pending_tasks(text)
        for t in tasks[:5]:  # limit to top 5
            if not any(t == pt[0] for pt in pending_tasks):
                pending_tasks.append((t, "tracker"))

    # Build the todolist
    today_name_en = DIAS_EN[DIAS.index(dia_es)]
    today_iso = target.isoformat()
    
    # Determine next day
    next_idx = (DIAS.index(dia_es) + 1) % 7
    next_dia = DIAS[next_idx]

    content = f"""---
title: {dia_es.capitalize()} Todolist
tags:
  - todo
  - semana-{week_num}
  - {dia_es}
  - upc
fecha: {today_iso}
---

# {dia_es.capitalize()} Todolist

"""

    # Top 3
    # Format top 3 with cleaner text
    raw_top3 = [t[0] for t in pending_tasks[:3]] if pending_tasks else [
        "Definir prioridad del día",
        "Revisar estado de cursos UPC",
        "Avanzar proyecto activo",
    ]
    top3 = []
    for t in raw_top3:
        # Clean up tracker-style text
        clean = re.sub(r"`\[\[(.+?)\]\]`", r"[[\1]]", t)
        clean = re.sub(r"`← tracker`", "", clean)
        clean = re.sub(r" aparece pendiente.*?\(.*?\)", "", clean).strip()
        top3.append(clean if clean else t)
    
    content += "## Top 3\n\n"
    for t in top3[:3]:
        content += f"- [ ] {t}\n"

    # University section
    content += f"""
## Universidad

- [ ] [[Calculo II]] — accion concreta
- [ ] [[Estadistica Aplicada]] — accion concreta
- [ ] [[Sistemas Operativos]] — accion concreta
- [ ] [[Aplicaciones Moviles]] — accion concreta
- [ ] Blackboard UPC — revisar anuncios, fechas y materiales nuevos

## Proyectos

- [ ] [[MaquinariasJyS]] — accion concreta y verificable
- [ ] [[MaquinariasJyS]] — siguiente paso tecnico o visual
"""

    # Carried over tasks
    if pending_tasks:
        content += "\n## Pendientes arrastrados\n\n"
        seen = set()
        for task, source in pending_tasks:
            clean = re.sub(r"`\[\[(.+?)\]\]`", r"[[\1]]", task)
            clean = re.sub(r"`← .+?`", "", clean).strip()
            # Deduplicate
            key = clean.lower().strip()
            if key not in seen and len(key) > 5:
                seen.add(key)
                content += f"- [ ] {clean}\n"

    content += f"""
## IA & Dev

- [ ] Claude Code — accion concreta segun disponibilidad
- [ ] Modelo local / Deepseek / Ollama — solo si aporta al objetivo del dia
- [ ] Documentar aprendizaje tecnico en Obsidian si aparece uno real

## Personal

- [ ] Pasos / caminata / energia
- [ ] Dormir a una hora razonable

## Cierre

- [ ] Revisar que queda pendiente para {next_dia}
- [ ] Generar [[{dia_es}-checkin]] al cierre del dia
- [ ] Generar [[{dia_es}-summary]] si aplica

---
*Generado con `scripts/start-day.py` · Pendientes arrastrados desde {yesterday_name}*
"""

    if args.dry_run:
        print(content)
        sys.exit(0)

    target_file.write_text(content, encoding="utf-8")
    print(f"✅ Created: {target_file}")
    print(f"   Top 3 + {len(pending_tasks)} carried-over tasks")
    sys.exit(0)


if __name__ == "__main__":
    main()
