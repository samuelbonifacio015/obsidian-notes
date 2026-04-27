---
title: Prompt — Genera el Todolist
tags:
  - prompt
  - daily-prompts
  - todolist
  - obsidian
tipo: prompt
estado: activo
---

# Prompt — Genera el Todolist

Usa este prompt cuando quiera que Codex cree el todolist de un dia especifico en Obsidian.

```text
Genera el todolist correspondiente para {{DIA_SEMANA}}.

Objetivo:
Crear una nota Obsidian lista para usar en `obsidian/2026/Abril/Semana {{N}}/{{dia}}-todolist.md`, usando el contexto real del vault y el estado actual de mis pendientes.

Antes de escribir:
1. Lee los archivos cercanos de la misma semana:
   - `{{dia_anterior}}-summary.md`
   - `{{dia_anterior}}-todoreviewer.md`
   - `{{dia_anterior}}-checkin.md`
   - cualquier plan semanal, tracker o skill relevante en la carpeta de la semana.
2. Si existen, revisa:
   - `obsidian/2026/skills/daily-checkin/references/preguntas.md`
   - `obsidian/2026/skills/daily-summary/SKILL.md`
   - `obsidian/2026/skills/week-tracker/SKILL.md`
3. Detecta:
   - semana UPC actual
   - cursos activos
   - entregas, examenes o evaluaciones cercanas
   - proyectos activos
   - pendientes arrastrados del dia anterior
   - tareas de Obsidian que falten cerrar

Contexto prioritario actual:
- Cursos UPC: [[Calculo II]], [[Estadistica Aplicada]], [[Sistemas Operativos]], [[Aplicaciones Moviles]].
- Proyecto principal: [[MaquinariasJyS]].
- [[QRust - Klippr]] solo si hay feedback, sustentacion, entrega o decision pendiente.
- Obsidian debe quedar sincronizado con checkin, summary y todoreviewer si aplica.
- Evita reactivar proyectos pausados salvo que yo los mencione explicitamente.

Formato requerido:
Usa este esquema:

---
title: {{Dia}} Todolist
tags:
  - todo
  - semana-{{N}}
  - {{dia}}
  - upc
fecha: {{YYYY-MM-DD}}
---

# {{Dia}} Todolist

## Top 3

- [ ] Tarea critica 1
- [ ] Tarea critica 2
- [ ] Tarea critica 3

## Universidad

- [ ] [[Calculo II]] - accion concreta
- [ ] [[Estadistica Aplicada]] - accion concreta
- [ ] [[Sistemas Operativos]] - accion concreta
- [ ] [[Aplicaciones Moviles]] - accion concreta
- [ ] Blackboard UPC - revisar anuncios, fechas y materiales nuevos

## Proyectos

- [ ] [[MaquinariasJyS]] - accion concreta y verificable
- [ ] [[MaquinariasJyS]] - siguiente paso tecnico o visual
- [ ] [[QRust - Klippr]] - solo si hay feedback o cierre pendiente

## IA & Dev

- [ ] Claude Code - accion concreta segun disponibilidad
- [ ] Modelo local / Deepseek / Ollama - solo si aporta al objetivo del dia
- [ ] Documentar aprendizaje tecnico en Obsidian si aparece uno real

## Personal

- [ ] Pasos / caminata / energia
- [ ] Dormir a una hora razonable para el dia siguiente
- [ ] Cerrar el dia con [[{{dia}}-checkin]]

## Cierre

- [ ] Revisar que queda pendiente para {{dia_siguiente}}
- [ ] Preparar [[{{dia_siguiente}}-todolist]]
- [ ] Generar [[{{dia}}-todoreviewer]] si el dia ya fue ejecutado
- [ ] Generar [[{{dia}}-summary]] si el check-in queda completo

Frase final:
Una linea corta y concreta que capture el foco del dia.

Reglas:
- No hagas una lista generica.
- Cada tarea debe tener un verbo claro y un resultado verificable.
- Si algo viene arrastrado de ayer, ponlo arriba.
- Si hay examen o entrega cercana, la universidad domina el Top 3.
- Si [[MaquinariasJyS]] tiene deadline de avance, debe aparecer en Top 3 o Proyectos.
- No marques tareas como completadas salvo que el contexto lo demuestre.
- Conserva wikilinks relevantes.
- Si falta informacion, infiere razonablemente desde los archivos cercanos y deja tareas accionables.
```
