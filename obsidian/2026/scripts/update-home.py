#!/usr/bin/env python3
"""Regenerate Home.md as a live dashboard for the Obsidian vault.

Scans the vault for the most recent active week, projects, courses,
and stats, then rewrites Home.md with current information.

Usage:
    python update-home.py              # regenerate Home.md
    python update-home.py --dry-run    # print output without writing
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent.parent  # obsidian/
HOME_FILE = VAULT / "2026" / "Home.md"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def count_md_files(vault: Path) -> int:
    """Count all .md files in the vault."""
    return len(list(vault.rglob("*.md")))


def find_latest_week_folder(vault: Path) -> Path | None:
    """Find the most recent week folder by scanning Semana N directories."""
    all_weeks = []
    for mes_dir in sorted(vault.glob("2026/*/")):
        if not mes_dir.is_dir():
            continue
        for semana_dir in sorted(mes_dir.glob("Semana */")):
            # Use modification time of most recent file in the folder
            files = list(semana_dir.rglob("*.md"))
            if files:
                mtime = max(f.stat().st_mtime for f in files)
                all_weeks.append((mtime, semana_dir))
    if not all_weeks:
        return None
    all_weeks.sort(reverse=True)
    return all_weeks[0][1]


def read_week_tracker(week_dir: Path) -> dict:
    """Extract score, focus, risk from week-tracker.md in a week folder."""
    tracker = week_dir / "week-tracker.md"
    if not tracker.exists():
        return {}
    
    text = tracker.read_text(encoding="utf-8")
    result = {}
    
    for key, label in [
        ("score_semana", "score"),
        ("foco_principal", "foco"),
        ("riesgo_principal", "riesgo"),
    ]:
        m = re.search(rf"^{key}:\s*(.+)$", text, re.MULTILINE)
        if m:
            result[label] = m.group(1).strip()
    
    # Extract estado
    m = re.search(r"^estado:\s*(.+)$", text, re.MULTILINE)
    if m:
        result["estado"] = m.group(1).strip()
    
    return result


def find_md_files_named(vault: Path, name: str) -> list[Path]:
    """Find .md files by name (case-insensitive) across vault."""
    return list(vault.rglob(f"*{name}*.md"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing")
    args = parser.parse_args()

    total_notes = count_md_files(VAULT)
    
    # Skills
    skills_dir = VAULT / "2026" / "skills"
    skill_count = len([p for p in skills_dir.glob("*/SKILL.md")]) if skills_dir.exists() else 0
    
    # Latest week
    latest_week = find_latest_week_folder(VAULT)
    week_info = {}
    week_name = "N/A"
    week_path_rel = ""
    week_rel_path = ""
    if latest_week:
        week_name = latest_week.name
        week_path_rel = str(latest_week.relative_to(VAULT))
        week_info = read_week_tracker(latest_week)
    
    # Active weeks this month
    active_weeks = []
    for semana_dir in sorted((VAULT / "2026" / "Abril").glob("Semana */")):
        files = list(semana_dir.rglob("*.md"))
        if files:
            active_weeks.append((semana_dir.name, len(files)))
    
    # Build content
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    score_display = week_info.get("score", "—")
    foco_display = week_info.get("foco", "—")
    riesgo_display = week_info.get("riesgo", "—")
    estado_display = week_info.get("estado", "—")
    
    if score_display and "%" not in score_display:
        score_display = f"{score_display}%"
    
    latest_week_link = f"[[{week_path_rel}/week-tracker|{week_name}]]" if week_path_rel else "—"
    
    content = f"""---
tags: [home, dashboard, vault]
last_updated: {now}
---

# 🏠 Samuel's Vault Dashboard

> Dashboard generado automáticamente · `scripts/update-home.py`

---

## 📅 Semana Activa: {week_name}

| Métrica | Valor |
|---------|-------|
| **Score** | {score_display} |
| **Foco** | {foco_display} |
| **Riesgo** | {riesgo_display} |
| **Estado** | {estado_display} |

📂 Ruta: `{week_path_rel or "—"}`
🔗 {latest_week_link}

---

## 📚 Cursos Activos — Ciclo 6 UPC

- [[Calculo II]]
- [[Estadistica Aplicada]]
- [[Sistemas Operativos]]
- [[Aplicaciones Moviles]]

---

## 🛠️ Proyectos

- [[MaquinariasJyS]] — Activo
- [[QRust - Klippr]] — Cerrado (TB1 entregado)
- [[QRust Org]] — Merge completado

---

## 📊 Vault Stats

| Métrica | Valor |
|---------|-------|
| Total notas | {total_notes} |
| Semanas activas (Abril) | {len(active_weeks)} |
| Skills nativos | {skill_count} |

"""

    if active_weeks:
        content += "### Semanas de Abril\n\n"
        for name, count in active_weeks:
            content += f"- **{name}**: {count} archivos\n"
    
    content += f"""

---

## 🔗 Accesos Rápidos

- [[Abril/Plan_Mensual|Plan Mensual]]
- [[Universidad/Calculo/Apuntes|Apuntes Cálculo]]
- [[Universidad/Estadistica/Apuntes|Apuntes Estadística]]
- [[Universidad/Aplicaciones Moviles|Aplicaciones Móviles]]

---

## 🔧 Scripts de Automatización

| Script | Propósito |
|--------|-----------|
| `scripts/validate-wikilinks.py` | Valida [[wikilinks]] en todo el vault |
| `scripts/update-home.py` | Este script — regenera el dashboard |
| `scripts/compile-plan-mensual.py` | Compila Plan Mensual desde semanas |
| `scripts/consolidate-week.py` | Consolida semana → week-tracker |
| `scripts/start-day.py` | Genera todolist del día desde arrastres |
| `scripts/git-sync.sh` | Auto-sync git |

---

*Generado: {now}*
"""

    if args.dry_run:
        print(content)
        return

    HOME_FILE.parent.mkdir(parents=True, exist_ok=True)
    HOME_FILE.write_text(content, encoding="utf-8")
    print(f"✅ Home.md regenerated: {HOME_FILE}")
    print(f"   Total notes: {total_notes}")
    print(f"   Latest week: {week_name} (score: {score_display})")
    print(f"   Skills: {skill_count}")
    print(f"   Active weeks: {len(active_weeks)}")
    sys.exit(0)


if __name__ == "__main__":
    main()
