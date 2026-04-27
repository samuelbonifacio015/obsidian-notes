---
title: Daily Prompts
tags:
  - prompt
  - daily-prompts
  - obsidian
tipo: index
estado: activo
---

# Daily Prompts

Prompts reutilizables para pedirle a Codex que genere notas diarias del vault con contexto suficiente.

## Prompts disponibles

- [[genera-todolist]] — crea el plan accionable del dia.
- [[genera-todoreviewer]] — revisa el todolist contra lo que realmente paso.
- [[genera-daily-checkin]] — crea el check-in granular del dia.
- [[genera-daily-summary]] — crea el resumen ejecutivo del dia.

## Regla de uso

Cuando uses uno de estos prompts, reemplaza variables como:

- `{{DIA_SEMANA}}`
- `{{dia}}`
- `{{dia_anterior}}`
- `{{dia_siguiente}}`
- `{{YYYY-MM-DD}}`
- `{{N}}`

Si no pasas todas las variables, Codex debe inferirlas desde la fecha actual, la carpeta semanal y los archivos vecinos.
