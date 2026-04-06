---
name: obsidian-weekly-summary
description: >
  Genera resúmenes semanales para Obsidian en formato Markdown estructurado, basándose en la actividad del usuario durante la semana: proyectos tocados, avances técnicos, herramientas de IA usadas, actividades académicas, ideas capturadas y TODOs para la siguiente semana. Activa esta skill SIEMPRE que el usuario pida: "resumen de la semana", "weekly review", "nota semanal para Obsidian", "qué hice esta semana", "genera mi weekly", "resumen semanal", "crea mi weekly note" o frases similares. También actívala cuando el usuario mencione querer registrar su semana, generar una nota de retrospectiva, o hacer un balance semanal — aunque no mencione explícitamente Obsidian. El output siempre es un archivo .md listo para copiar o descargar directamente en la vault de Obsidian.
---

# Obsidian Weekly Summary Skill

Genera una **Weekly Review Note** para Obsidian, lista para pegar o descargar. El archivo sigue un formato consistente semana a semana para permitir navegación tipo `[[2026-W13]] ← → [[2026-W15]]`.

---

## Proceso de generación

### 1. Recopilar contexto de la semana

Obtén la información de la semana del usuario usando estas fuentes en orden de prioridad:

1. **Transcripts de conversaciones** → revisar `/mnt/transcripts/` si hay archivos disponibles
2. **Memorias del usuario** (`userMemories`) → proyectos activos, stack, contexto académico/laboral
3. **Lo que el usuario mencione explícitamente** en el mensaje actual

Si el usuario no proporciona detalles específicos de la semana, usa las memorias para inferir actividad probable y **claramente indica** qué fue inferido vs. confirmado.

### 2. Calcular semana ISO

```python
from datetime import datetime, timedelta
import subprocess

# Obtener fecha actual
result = subprocess.run(['date', '+%Y-%V'], capture_output=True, text=True)
week_label = result.stdout.strip()  # e.g. "2026-W14"

# Calcular lunes y domingo de la semana
today = datetime.today()
monday = today - timedelta(days=today.weekday())
sunday = monday + timedelta(days=6)
```

### 3. Generar el archivo Markdown

Usa la plantilla de `/references/template.md`. Rellena cada sección con el contexto recopilado.

**Reglas de llenado:**
- Si una sección no tiene actividad → escribe `*(sin actividad registrada)*`, no la elimines
- Las tareas pendientes van como `- [ ] tarea`
- Las completadas van como `- [x] tarea`
- Usa emojis de sección consistentes (ver plantilla)
- El frontmatter YAML siempre incluye: `tags`, `semana`, `fecha_inicio`, `fecha_fin`, `estado`

### 4. Guardar y entregar

```bash
# Guardar en working directory
FILENAME="YYYY-W##.md"  # e.g. 2026-W14.md
cp /home/claude/weekly-note.md /mnt/user-data/outputs/$FILENAME
```

Usa `present_files` para entregar el archivo al usuario.

---

## Secciones de la nota

| Sección | Emoji | Descripción |
|---------|-------|-------------|
| Snapshot | 📊 | Tabla resumen de áreas tocadas |
| Proyectos | 🏗️ | Avances por proyecto activo |
| IA & Herramientas | 🤖 | Modelos, APIs, herramientas nuevas usadas |
| Universidad | 🎓 | Solo si aplica al usuario |
| Ideas & Reflexiones | 💡 | Insights, decisiones, aprendizajes |
| Próxima semana | ⏭️ | TODOs accionables con checkboxes |
| Links & Recursos | 🔗 | Repos, URLs, referencias relevantes |

---

## Personalización por perfil de usuario

Si el usuario es desarrollador/estudiante (como Samuel en UPC + WeTech):
- Incluir sección de **Universidad** con cursos activos
- Incluir sección de **Startup / Side projects**
- Mencionar herramientas de IA usadas en desarrollo

Si el usuario es solo profesional:
- Omitir sección Universidad
- Expandir sección de Proyectos y Trabajo

---

## Lecturas adicionales

- Ver `/references/template.md` para la plantilla completa
- Ver `/references/frontmatter-guide.md` para convenciones de tags y metadatos

---

## Notas importantes

- **Nunca inventar actividad** que no puedas inferir de memorias o contexto — marca claramente con `*(inferido)*` lo que no fue confirmado
- El archivo debe ser **autocontenido**: alguien que lo lea en 3 meses debe entender qué pasó esa semana
- Mantener **consistencia de formato** semana a semana para que los links `[[2026-W##]]` funcionen en Obsidian
- Si el usuario tiene la skill `obsidian-finance-advisor` activa, se puede incluir una mini-sección de gastos relevantes de la semana