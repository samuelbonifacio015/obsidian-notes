---
name: obsidian-vault-automation
description: >-
  Use when Samuel asks to analyze, automate, or maintain his Obsidian vault at
  /home/samuel/obsidian-notes/obsidian — vault health scans, script generation
  (Python/Codex), weekly tracker consolidation, broken wikilink validation,
  Plan_Mensual population, daily note generators, git sync cron, UPC calendar
  bridge, or any vault-wide automation strategy.
---

# Obsidian Vault Automation

Automation toolkit for Samuel's Obsidian vault at `/home/samuel/obsidian-notes/obsidian/`.
Encompasses vault analysis, script generation (via Codex CLI), cron/webhook setup,
and ongoing maintenance of the daily/weekly tracking system.

---

## Vault Overview

**Path:** `/home/samuel/obsidian-notes/obsidian/`
**Git remote:** `https://github.com/samuelbonifacio015/obsidian-notes.git`
**Size:** ~84+ `.md` notes
**Structure:**

```
obsidian/
├── Home.md                              # Index — broken [[Inbox]] [[Daily]] [[Ideas clave]]
├── Plan_Mensual.md                      # Empty template — needs population
├── 2026/
│   ├── Abril/                           # Current month
│   │   ├── Semana 4/                    # 4-file daily pattern
│   │   │   ├── lunes-todolist.md
│   │   │   ├── lunes-checkin.md         # (or viernes-checkin.md)
│   │   │   ├── lunes-summary.md
│   │   │   └── lunes-todoreviewer.md
│   │   └── Semana 5/                    # Current week (live)
│   ├── Daily/                           # Standalone daily notes
│   │   └── 2026-04-08.md
│   ├── Gastos & Finanzas/
│   └── skills/                          # Vault-native agent skills
│       ├── daily-checkin/               # "El Simio" — accountability partner
│       ├── daily-summary/
│       ├── daily-prompts/               # Reusable Codex prompts
│       └── week-tracker/                # Weekly consolidation
├── Excalidraw/
└── Universidad/
    ├── Aplicaciones Moviles/
    ├── Calculo/
    └── Estadistica/
```

---

## The 4-File Daily Pattern

Each day in a Semana folder should have up to 4 files:

| File | Purpose | Created by |
|------|---------|------------|
| `{dia}-todolist.md` | Actionable plan for the day | Codex/agent |
| `{dia}-checkin.md` | Granular check-in ("El Simio") | daily-checkin skill |
| `{dia}-todoreviewer.md` | Review todolist vs reality | Codex/agent |
| `{dia}-summary.md` | Executive daily summary | daily-summary skill |

**Naming convention:** `{dia}-{type}.md` where `{dia}` is lowercase English:
`lunes`, `martes`, `miercoles`, `jueves`, `viernes`, `sabado`, `domingo`

**KNOWN ISSUE:** Semana 3 used inconsistent naming (`Lun, Apr 13 - Todo List.md`, `summary week 3.md`) — break the pattern and automations break.

---

## Automation Phases (Prioritized)

### Phase 1 — Fix Broken Items (scripts in vault)

1. **Wikilink Validator** — Python script that scans all `.md` files, extracts `[[links]]`, checks they resolve to existing files in the vault, and reports broken ones.
   - Found broken: `[[Inbox]]`, `[[Daily]]`, `[[Ideas clave]]` in Home.md
   - Also catches orphan notes (files not linked from any index)

2. **Plan_Mensual Populator** — Read all weekly plans + summaries for the month, extract achievements, and fill `Plan_Mensual.md` with real data instead of the empty template.

3. **Home.md Auto-Dashboard** — Regenerate Home.md with live links: last active week, active projects, week score, quick stats.

### Phase 2 — Weekly Automation (Python scripts)

4. **Week-Tracker Consolidator** — Core script. Scans a `Semana N/` folder, reads checkins/todolists/summaries/todoreviewers, cross-references frontmatter, detects contradictions, calculates real weekly score (not 0%), updates `week-tracker.md` without duplication, validates wikilinks. Output: `week-tracker-live.md`.

5. **Daily Starter Generator** — Creates `{dia}-todolist.md` pre-populated with pending tasks from yesterday's todoreviewer, upcoming UPC deadlines, and recurring items.

### Phase 3 — Recurring Automation (cron)

6. **Git Auto-Sync** — Daily add/commit/push all vault changes (via Hermes cron).

7. **UPC Calendar Bridge** — Parse UPC plan-calendario PDF from vault, inject exam/deadline dates into todolists automatically.

8. **Week Tracker Cron** — Every Sunday evening or Monday morning, generate the week-tracker for the upcoming week.

---

## Known Vault Issues (Current)

| Issue | Location | Severity |
|-------|----------|----------|
| Broken wikilinks | `Home.md`: [[Inbox]], [[Daily]], [[Ideas clave]] | High |
| Empty Plan_Mensual | Root | High |
| Week 5 tracker at 0% | `Semana 5/week-tracker.md` | Medium |
| Inconsistent filenames | `Semana 3/` | Medium |
| Orphan note | `2026-04-22.md` (outside weekly folders) | Low |
| University notes unlinked | `Universidad/` not linked from weekly notes | Low |
| .agents/skills/ not referenced | External skills disconnected from daily prompts | Low |

---

## Delegating to Codex CLI

For building production-grade scripts (not one-shot Hermes tasks), delegate to Codex:

```bash
codex exec 'Build a Python script that scans Semana N/ folders, reads frontmatter from checkins/todolists/summaries/todoreviewers, cross-references for contradictions, calculates a real weekly score, and outputs week-tracker-live.md. Use path /home/samuel/obsidian-notes/obsidian/2026/Abril/. Handle missing days gracefully.' --full-auto
```

**Always use `pty=true` when running Codex via terminal.**
For Hermes-managed delegation, use the `codex` skill: load with `skill_view(name='codex')`.

---

## Setting Up Cron Jobs in Hermes

```bash
# Git auto-sync: daily at midnight
hermes cron create "0 0 * * *" --prompt "cd /home/samuel/obsidian-notes/obsidian && git add -A && git commit -m 'auto-sync vault' && git push"

# Week tracker refresh: every Sunday 8 PM
hermes cron create "0 20 * * 0" --prompt "Run the week-tracker consolidator for the current semana, update week-tracker.md, validate wikilinks"

# Daily starter: every morning 7 AM
hermes cron create "0 7 * * *" --prompt "Generate today's todolist in the current Semana folder with pending tasks from yesterday"
```

Cron jobs use `deliver` to send results. See `hermes cron create --help` for details.

---

## Common Pitfalls

1. **Running scripts outside the vault root.** Always use absolute path `/home/samuel/obsidian-notes/obsidian/` or change to that directory.

2. **Assuming consistent naming.** Always scan the actual folder before processing. Semana 3 proved naming can vary. Use glob patterns and fallbacks.

3. **Overwriting manual content.** The week-tracker consolidator must never duplicate sections. Preserve user's manual edits if they don't contradict recent data.

4. **Inventing data for missing days.** Mark as `sin registro` — never synthesize activity.

5. **Forgetting `pty=true` for Codex.** Codex CLI needs a pseudo-terminal. Without it, interactive prompts hang.

6. **Home.md has dead links.** Any automation that updates Home.md must first run the wikilink validator.

7. **Plan_Mensual.md is a template, not a note.** Don't try to read it as finished content. Check frontmatter before quoting it.

---

## Verification Checklist

- [ ] Scripts are saved in the vault (`obsidian/2026/scripts/`) so Codex can find them later
- [ ] Git commit + push made after any vault modification
- [ ] Cron jobs tested once before setting recurring schedule
- [ ] Wikilink validator passes with 0 broken links before regenerating Home.md
- [ ] Week tracker shows real score (not 0%) after consolidation
- [ ] Semana folder naming is consistent across all days
- [ ] No orphan notes outside organized folders
