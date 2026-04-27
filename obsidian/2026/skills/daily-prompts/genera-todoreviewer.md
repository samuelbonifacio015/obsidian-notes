---
title: Prompt — Genera el Todoreviewer
tags:
  - prompt
  - daily-prompts
  - todoreviewer
  - obsidian
tipo: prompt
estado: activo
---

# Prompt — Genera el Todoreviewer

Usa este prompt cuando quiera revisar que tanto se cumplio el todolist del dia.

```text
Genera el todoreviewer correspondiente para {{DIA_SEMANA}}.

Objetivo:
Crear `obsidian/2026/Abril/Semana {{N}}/{{dia}}-todoreviewer.md` como una revision honesta del archivo `{{dia}}-todolist.md`, cruzandolo con el check-in, summary y cualquier evidencia del vault.

Antes de escribir:
1. Lee obligatoriamente:
   - `obsidian/2026/Abril/Semana {{N}}/{{dia}}-todolist.md`
2. Si existen, lee tambien:
   - `{{dia}}-checkin.md`
   - `{{dia}}-summary.md`
   - `{{dia_anterior}}-todoreviewer.md`
   - `{{dia_anterior}}-summary.md`
3. Extrae:
   - tareas marcadas como completadas en el todolist
   - tareas no completadas
   - contradicciones entre todolist y check-in
   - pendientes que deben moverse al siguiente dia
   - riesgos academicos o de proyecto

Contexto de evaluacion:
- No confundas intencion con avance.
- Una tarea marcada `[x]` puede quedar como "completado parcial" si el check-in contradice el alcance.
- Si el todolist dice 8k pasos pero el check-in dice 6k, registra inconsistencia.
- Si se estudio [[Calculo II]] pero la preparacion sigue baja, marca avance real con riesgo activo.
- Si [[MaquinariasJyS]] avanzo, exige evidencia concreta: pantalla, componente, checklist, feedback o decision.

Formato requerido:

---
tags: [todolist, {{dia}}, reviewer]
fecha: {{YYYY-MM-DD}}
dia: {{dia}}
total_estimado: {{parcial|completo}}
tipo: todoreviewer
relacionado: "[[{{dia}}-todolist]]"
---

# 📋 Todoreviewer — {{Dia}}, {{DD}} de {{Mes}} de {{YYYY}}

## 🎯 Top Prioridades del dia

1. [x] **Area / nota** — lectura honesta del resultado.
2. [ ] **Area / nota** — si quedo pendiente, explica que falta.
3. [~] **Area / nota** — usa parcial si avanzo, pero no cerro.

## 📚 Universidad

- [x] [[Curso]] — resultado concreto.
- [ ] [[Curso]] — pendiente concreto.
- [~] [[Curso]] — avance parcial y siguiente paso.

## 🛠️ Proyectos

- [x] [[MaquinariasJyS]] — avance verificable.
- [ ] [[MaquinariasJyS]] — pendiente que se mueve.
- [ ] [[QRust - Klippr]] — solo si aplica.

## 🤖 IA & Dev

- [x] Claude Code / modelo local — uso concreto.
- [ ] Aprendizaje tecnico documentado — pendiente si no hubo nota.

## 🏃 Personal / Mantenimiento

- [x] Obsidian / check-in / summary — cierre documental.
- [ ] Energia / sueño / pasos — segun evidencia.

---

## 🔍 Orden de ejecucion registrado

| # | Tarea | Estado | Lectura del avance |
|---|---|---|---|
| 1 | Tarea del todolist | Completado / Parcial / Pendiente | Lectura breve, concreta y verificable. |

---

## ⚠️ Banderas de riesgo

- ⚠️ Riesgo 1 — explica por que importa para mañana.
- ⚠️ Riesgo 2 — solo si hay evidencia real.
- ⚠️ Riesgo 3 — maximo tres banderas.

---

## 🕐 Resultado del dia: {{PORCENTAJE}}% efectivo

> Una frase honesta de PM: que se logro, que quedo abierto y cual es el cuello de botella.

---

## 🔗 Notas relacionadas a crear/linkear hoy

- [[{{dia}}-checkin]]
- [[{{dia}}-summary]]
- [[{{dia_siguiente}}-todolist]]
- otras notas relevantes

---

_Generado con `todo-reviewer` · [[{{dia}}-todolist]] · [[{{dia_anterior}}-todoreviewer]] ← → [[{{dia_siguiente}}-todoreviewer]]_

Reglas:
- No maquilles el resultado.
- Si falta check-in, di que el reviewer queda inferido desde el todolist.
- Usa `[~]` para avance parcial cuando sea mas honesto que `[x]`.
- Calcula el porcentaje segun completados reales, no solo checkboxes marcados.
- Prioriza riesgos que afecten examenes, entregas UPC o [[MaquinariasJyS]].
- Conserva wikilinks y nombres exactos de notas.
```
