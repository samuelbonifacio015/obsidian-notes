# Plan: Obsidian Vault Automation

**Goal:** Automate vault health scanning, daily note generation, week consolidation, and git sync for Samuel Bonifacio's Obsidian vault.

**Vault root:** `/home/samuel/obsidian-notes/obsidian/`
**Git root:** `/home/samuel/obsidian-notes/`
**Scripts location:** `obsidian/2026/scripts/` (inside vault, versioned with git)

---

## Fase 1 — Sanear lo roto (scripts correctivos)

### 1.1 Wikilink Validator (`scripts/validate-wikilinks.py`)

**Input:** Recorre recursivamente `obsidian/` todos los `.md`
**Proceso:**
- Extrae TODOS los `[[wikilinks]]` con regex
- Por cada link: checkea si `{link}.md` existe en el vault
- Si el link tiene alias `[[real|alias]]`, usa `real`
- Si el link es a un heading `[[nota#heading]]` o bloque `[[nota^id]]`, usa la parte antes de `#` o `^`
- Ignora links a archivos existentes en Excalidraw, images, etc.
**Output:** `scripts/repors/wikilink-report.md` con:
  - Total wikilinks encontrados
  - Total wikilinks rotos
  - Lista detallada: `[archivo_origen] → [[link_roto]]` (línea exacta)
  - Sugerencia de archivos a crear o links a corregir

**Regla:** No modifica archivos, solo reporta.

### 1.2 Home Page Regenerator (`scripts/update-home.py`)

**Input:** `obsidian/2026/Home.md`
**Proceso:**
- Escanea el vault por:
  - Última semana activa (carpeta `2026/{Mes}/Semana N/` con más archivos recientes)
  - Último week-tracker generado → extrae score, foco, riesgo
  - Proyectos activos (notas con `tags: [proyecto]` o menciones en week-trackers)
  - Cursos activos del ciclo (Calculo II, Estadistica, SO, Apps Moviles)
- Reemplaza el contenido de Home.md con un dashboard vivo:
  ```markdown
  ---
  tags: [home, dashboard, vault]
  last_updated: {{FECHA_ISO}}
  ---
  
  # 🏠 Samuel's Vault Dashboard
  
  ## 📅 Semana Activa: Semana N
  - Score: X% | Foco: ... | Riesgo: ...
  
  ## 📚 Cursos Activos — Ciclo 6
  - [[Calculo II]]
  - [[Estadistica Aplicada]]
  - [[Sistemas Operativos]]
  - [[Aplicaciones Moviles]]
  
  ## 🛠️ Proyectos
  - [[MaquinariasJyS]]
  - [[QRust - Klippr]]
  
  ## 📊 Vault Stats
  - Total notas: N
  - Semanas activas: N
  - Skills nativos: N
  
  ## 🔗 Accesos Rápidos
  - [[Plan_Mensual]]
  - Último week-tracker: [[...]]
  - Último summary: [[...]]
  ```
**Regla:** Mantiene el frontmatter actualizado con `last_updated`. Solo modifica Home.md.

### 1.3 Plan Mensual Compiler (`scripts/compile-plan-mensual.py`)

**Input:** `obsidian/2026/Abril/Plan_Mensual.md` (template vacío)
**Proceso:**
- Lee todos los Week Plans y Week Summaries del mes actual
- Extrae logros reales, objetivos cumplidos, aprendizajes
- Completa las secciones del Plan_Mensual:
  - `🎯 Goals` → inferidos de los objetivos semanales
  - `✨ Things I Achieved` → consolidado de summaries
  - `🧠 Things I Learned` → de week summaries / learning journal
  - `🔧 Things to Improve` → de riesgos semanales recurrentes
  - `💭 Memories` → frase representativa del mes
- Pisa el archivo con el contenido completo

**Regla:** Si una sección ya tiene contenido manual, no la sobrescribe (merge conservador).

---

## Fase 2 — Automatizar lo recurrente (scripts de ejecución)

### 2.1 Week-Tracker Consolidator (`scripts/consolidate-week.py`)

**Input:** path a carpeta `Semana N/` (argumento CLI: `--week N --month Abril --year 2026`)
**Proceso:**
1. Lee todos los archivos de la semana: checkins, todolists, todoreviewers, summaries
2. Extrae frontmatter de cada uno (score, fecha, tags, estado)
3. Cruza checkboxes del todolist con respuestas del checkin:
   - Checkbox `[x]` + checkin confirma → ✅ completado
   - Checkbox `[x]` + checkin no menciona → ⚠️ parcial (inferido)
   - Checkbox vacío + checkin confirma → ✅ completado pero sin planificar
   - Checkbox vacío + checkin no menciona → ❌ sin registro
4. Calcula score semanal real:
   - Peso 40% académico, 30% proyectos, 20% IA/dev, 10% personal
   - Score = (completados con evidencia / total ítems) × 100
5. Valida [[wikilinks]] en los archivos de la semana
6. Detecta riesgos: tareas pendientes 2+ días, score bajo recurrente, contradicciones
7. Genera/actualiza `week-tracker.md` usando la plantilla del skill nativo

**CLI usage:**
```bash
python consolidate-week.py --week 5 --month Abril --year 2026
# → Lee Semana 5/ → actualiza week-tracker.md
```

**Modo batch:**
```bash
python consolidate-week.py --all
# → Escanea todas las semanas del mes activo → actualiza todas
```

### 2.2 Daily Starter Creator (`scripts/start-day.py`)

**Input:** Ninguno (usa fecha actual)
**Proceso:**
1. Detecta día de la semana y semana ISO actual
2. Determina carpeta `{Mes}/Semana N/`
3. Lee el último todoreviewer/summary disponible (día anterior)
4. Extrae pendientes que NO estén marcados como completados
5. Filtra: solo los que tengan sentido arrastrar (no fechas únicas ya vencidas)
6. Genera `{dia}-todolist.md` con:
   - Top 3 prioridades (arrastradas + nuevo día)
   - Universidad: cursos activos
   - Proyectos: solo activos
   - IA & Dev: placeholder
   - Personal: pasos, sueño
   - Cierre: checkin + summary + reviewer
7. Si el archivo ya existe, NO lo sobrescribe

**Regla:** Solo genera si el archivo no existe. No modifica nada existente.

### 2.3 Git Auto-Sync Script (`scripts/git-sync.sh`)

**Proceso:**
```bash
#!/bin/bash
cd /home/samuel/obsidian-notes
# Detecta cambios
if [[ -n $(git status --porcelain) ]]; then
  git add -A
  git commit -m "chore(vault): auto-sync $(date +%Y-%m-%dT%H:%M)"
  git push origin main
fi
```

---

## Fase 3 — Automatización recurrente (cron jobs)

### 3.1 Cron: Git Sync Diario
```cron
30 22 * * * /home/samuel/obsidian-notes/obsidian/2026/scripts/git-sync.sh
```

### 3.2 Cron: Week-Tracker Nocturno (domingos)
```cron
0 23 * * 0 cd /home/samuel/obsidian-notes && python obsidian/2026/scripts/consolidate-week.py --week $(date +%V) --month $(date +%B) --year $(date +%Y)
```

---

## Archivos a crear (resumen)

| Archivo | Propósito | Fase |
|---------|-----------|------|
| `obsidian/2026/scripts/validate-wikilinks.py` | Validador de wikilinks rotos | 1 |
| `obsidian/2026/scripts/update-home.py` | Regenera Home dashboard | 1 |
| `obsidian/2026/scripts/compile-plan-mensual.py` | Compila Plan_Mensual desde semanas | 1 |
| `obsidian/2026/scripts/consolidate-week.py` | Consolidación semanal → week-tracker | 2 |
| `obsidian/2026/scripts/start-day.py` | Genera todolist del día desde arrastres | 2 |
| `obsidian/2026/scripts/git-sync.sh` | Auto-sync git | 2 |
| `obsidian/2026/scripts/reports/` | Carpeta para reportes | 1 |

---

## Reglas transversales

1. **No destructivo** — ningún script borra contenido existente sin preguntar
2. **Wikilinks** — todos los scripts preservan y generan `[[wikilinks]]` correctos
3. **Conservador** — si un archivo ya tiene contenido manual, mergear no pisar
4. **Reportes** — los scripts de análisis guardan output en `scripts/reports/`
5. **Logging** — cada script imprime qué hizo, qué encontró, en cuanto tiempo
6. **Exit code** — 0 = éxito, 1 = error controlado, 2 = error crítico
7. **Python 3.11+** — solo stdlib + pathlib, sin dependencias externas
8. **Comentarios** — cada función tiene docstring explicando qué hace
