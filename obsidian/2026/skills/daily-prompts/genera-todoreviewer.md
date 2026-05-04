---
title: Prompt — Genera el Todoreviewer (Minimalista)
tags:
  - prompt
  - daily-prompts
  - todoreviewer
  - obsidian
tipo: prompt
estado: activo
---

# Prompt — Genera el Todoreviewer (Minimalista)

Versión reducida. Tabla de 3 líneas, score, 1 riesgo máximo.

```text
Genera el todoreviewer minimalista para {{DIA_SEMANA}}.

Objetivo:
Crear `obsidian/2026/Abril/Semana {{N}}/{{dia}}-todoreviewer.md` en 2 minutos de lectura.

Antes de escribir:
1. Lee `{{dia}}-todolist.md`
2. Lee `{{dia}}-checkin.md` (si existe)

Formato:

---
tags: [todolist, {{dia}}, reviewer]
fecha: {{YYYY-MM-DD}}
dia: {{dia}}
total_estimado: parcial
tipo: todoreviewer
relacionado: "[[{{dia}}-todolist]]"
---

# 📋 Todoreviewer — {{Dia}}, {{DD}} de {{Mes}} de {{YYYY}}

## Resultado real

[✓] Top 1: Tarea — resultado concreto
[✗] Top 2: Tarea — pendiente
[~] Top 3: Tarea — avance parcial

## Score: {{PORCENTAJE}}%

> Frase honesta de 1 línea: qué se logró, qué quedó abierto.

## Banderas

⚠️ 1 riesgo máximo — solo si hay evidencia real.

## Pendientes mañana

- [ ] Pendiente 1
- [ ] Pendiente 2

---

_Generado con `todo-reviewer` · [[{{dia}}-todolist]] · [[{{dia}}-checkin]]_
```

Reglas:
- No tabla de ejecución, no porcentaje calculado, no orden de ejecución.
- Score = simple: cumplidos/total del Top 3.
- 1 bandera de riesgo máximo, no más.
- Si no hay riesgo evidente, omite Banderas.
- Pendientes mañana: solo lo que el check-in dice o el todolist no marcó.
