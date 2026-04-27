---
title: Prompt — Genera el Daily Summary
tags:
  - prompt
  - daily-prompts
  - daily-summary
  - obsidian
tipo: prompt
estado: activo
---

# Prompt — Genera el Daily Summary

Usa este prompt cuando quiera generar el resumen ejecutivo del dia desde el check-in.

```text
Genera el daily summary correspondiente para {{DIA_SEMANA}}.

Objetivo:
Crear `obsidian/2026/Abril/Semana {{N}}/{{dia}}-summary.md` como resumen ejecutivo breve, accionable y listo para Obsidian.

Antes de escribir:
1. Lee obligatoriamente:
   - `obsidian/2026/skills/daily-summary/SKILL.md`
   - `obsidian/2026/skills/daily-summary/references/plantilla-summary.md`
2. Lee la fuente primaria del dia:
   - `obsidian/2026/Abril/Semana {{N}}/{{dia}}-checkin.md`
3. Si existen, lee tambien:
   - `{{dia}}-todolist.md`
   - `{{dia}}-todoreviewer.md`
   - `{{dia_anterior}}-summary.md`

Jerarquia de fuentes:
1. `{{dia}}-checkin.md`
2. seccion `🐒 Nota de cierre` y `🐒 Pendiente`
3. `{{dia}}-todoreviewer.md`
4. `{{dia}}-todolist.md`
5. contexto conversacional dado por Samuel

Objetivo editorial:
- El summary no es otro check-in.
- Debe ser legible en 30 segundos.
- Debe decir que domino el dia, que se logro, que quedo abierto y cual es el cuello de botella.
- Usa voz de PM: concreta, honesta, sin motivacion generica.

Formato requerido:

---
tags: [daily-summary, {{MOOD_TAG}}]
fecha: {{YYYY-MM-DD}}
dia: {{dia}}
score: {{SCORE}}/10
tipo: summary
relacionado: "[[{{dia}}-checkin]]"
---

# 📋 Summary — {{Dia}}, {{DD}} de {{Mes}} de {{YYYY}}

> *Cierre de una linea, maximo 12 palabras.*

---

## ⚡ Resumen del día

2-4 oraciones. Menciona:
- foco dominante
- avance concreto
- lo que quedo sin tocar
- factor de riesgo o contexto relevante

---

## 🏆 Logros

- Logro academico concreto.
- Logro de proyecto concreto.
- Logro tecnico o de IA/dev concreto.
- Logro personal o de productividad concreto.

---

## 🚧 Bloqueadores

- Maximo 3 bloqueadores reales.
- Omite esta seccion solo si no hubo bloqueadores.

---

## 📌 Pendientes activos

- [ ] Pendiente urgente 1.
- [ ] Pendiente urgente 2.
- [ ] Pendiente urgente 3.

---

## 📊 Score: {{SCORE}}/10 — {{MOOD_TAG}}

```
{{BARRA_VISUAL}} {{SCORE}}/10
```

---

## 🔗 Notas del día

[[{{dia}}-checkin]] | [[{{dia}}-todolist]] | [[{{dia}}-todoreviewer]]

---

*Generado con la skill `daily-summary` · [[{{dia_anterior}}-summary]] ← → [[{{dia_siguiente}}-summary]]*

Criterios de score:
- 8-10: dia productivo, varios cierres reales y pocos pendientes criticos.
- 6-7: dia intenso o util, con avance fuerte pero pendientes importantes.
- 4-5: dia regular, mezcla de avances y deudas.
- 1-3: dia flojo o descarrilado.

Mood tag:
- `dia/productivo`: score >= 7 y varios cierres concretos.
- `dia/intenso`: mucho foco academico/proyecto, aunque queden pendientes.
- `dia/regular`: avance mixto.
- `dia/flojo`: poco completado.

Reglas:
- No repitas todas las preguntas del check-in.
- No inventes logros.
- Si el check-in fue inferido desde todolist, dilo indirectamente con cautela: "quedo registrado", "se marco", "queda pendiente confirmar".
- Mantén los pendientes como checkboxes interactivos.
- Conserva wikilinks exactos.
- No incluyas notas inexistentes en "Notas del dia" salvo que el archivo exista o se este creando en esta misma sesion.
```
