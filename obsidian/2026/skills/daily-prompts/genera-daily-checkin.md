---
title: Prompt — Genera el Daily Check-in
tags:
  - prompt
  - daily-prompts
  - daily-checkin
  - obsidian
tipo: prompt
estado: activo
---

# Prompt — Genera el Daily Check-in

Usa este prompt cuando quiera generar el check-in del dia desde un todolist, respuestas sueltas o contexto de la conversacion.

```text
Genera el daily-checkin correspondiente para {{DIA_SEMANA}}.

Objetivo:
Crear `obsidian/2026/Abril/Semana {{N}}/{{dia}}-checkin.md` como nota estructurada de rendicion de cuentas diaria, usando la skill `daily-checkin` y el contexto real del dia.

Previo a escribir "R": 
- "R" va en negrita, de esta forma: "**R**"
- Todo de dentro de "R" lo escribirá el usuario (Samuel), no autocompletar bajo ninguna circustancia. A excepción de que el usuario explícitamente pida completar alguna sección.
- **Respuesta Conceta** indica la respuesta del usuario.

Antes de escribir:
1. Lee obligatoriamente:
   - `obsidian/2026/skills/daily-checkin/SKILL.md`
   - `obsidian/2026/skills/daily-checkin/references/preguntas.md`
   - `obsidian/2026/skills/daily-checkin/references/plantilla.md`
2. Lee el archivo base del dia si existe:
   - `obsidian/2026/Abril/Semana {{N}}/{{dia}}-todolist.md`
3. Usa como contexto adicional:
   - `{{dia_anterior}}-checkin.md`
   - `{{dia_anterior}}-summary.md`
   - `{{dia_anterior}}-todoreviewer.md`
   - notas de proyecto o curso mencionadas en el todolist.

Modo de trabajo:
- Si te doy respuestas explicitas, usalas como fuente principal.
- Si solo existe el todolist, genera un check-in inferido desde los checkboxes y marca como pendiente lo que no se pueda confirmar.
- Si el todolist contradice el check-in o summary, prioriza el check-in.
- No inventes logros que no esten en el todolist, check-in previo, summary o contexto que yo haya dado.

Contexto prioritario:
- Cursos UPC: [[Calculo II]], [[Estadistica Aplicada]], [[Sistemas Operativos]], [[Aplicaciones Moviles]].
- Proyecto principal: [[MaquinariasJyS]].
- [[QRust - Klippr]] solo si hay feedback, sustentacion, entrega o decision pendiente.
- IA/dev: Claude Code, modelos locales, Deepseek, Ollama, aprendizaje tecnico documentable.
- Productividad: Obsidian, todolist, todoreviewer, summary, plan semanal.
- Personal: pasos, sueño, energia, somnolencia post-almuerzo, bloqueo mental.

Formato requerido:

---
tags: [daily-checkin]
fecha: {{YYYY-MM-DD}}
dia: {{dia}}
estado: {{completado|inferido-desde-todolist|en progreso}}
relacionado: "[[{{dia}}-todolist]]"
---

# 🐒 Daily Check-in — {{Dia}}, {{DD}} de {{Mes}} de {{YYYY}}

> 🐒 Check-in del {{dia}}, {{DD}} de {{mes}}.
> Base tomada de [[{{dia}}-todolist]] y contexto disponible.
>
> Una linea con el foco real del dia.

---

## 🎓 Académico

### Cálculo II — si fue foco del dia

**[ac-01]** ¿Avanzaste algo de Cálculo hoy? ¿Qué tema exacto estudiaste?

> R: Respuesta concreta.

**[ac-02]** ¿Revisaste el Blackboard de UPC hoy? ¿Había algo nuevo?

> R: Respuesta concreta.

**[ac-03]** ¿Tocaste Estadística Aplicada?

> R: Respuesta concreta.

**[ac-04]** ¿Avanzaste en Sistemas Operativos?

> R: Respuesta concreta.

**[ac-05]** ¿Tocaste Aplicaciones Móviles?

> R: Respuesta concreta.

**[ac-06]** ¿Hay alguna entrega o examen próximo que debas preparar?

> R: Respuesta concreta.

---

## 🛠️ Proyectos

**[pr-01]** ¿Tocaste MaquinariasJyS hoy?

> R: Pantalla, componente, decision, feedback o siguiente paso.

**[pr-02]** ¿Algún feature nuevo para Klippr?

> R: Solo si aplica.

**[pr-04]** ¿Hay algún proyecto nuevo?

> R: No registrado / respuesta concreta.

---

## 🤖 IA & Dev

**[ai-01]** ¿Usaste Claude Code hoy en algún repo?

> R: Repo, objetivo y resultado.

**[ai-03]** ¿Aprendiste algún concepto técnico nuevo hoy?

> R: Concepto y si quedo documentado.

**[ai-04]** ¿Avanzaste algun modulo o aprendizaje de IA?

> R: Herramienta, modelo o curso.

Incluye 1-2 preguntas aleatorias relevantes del banco rotativo si aportan contexto real.

---

## 📋 Productividad

**[pd-01]** ¿Escribiste en tu diario de Obsidian hoy?

> R: Notas creadas o actualizadas.

**[pd-02]** ¿Actualizaste o creaste alguna nota en Obsidian?

> R: Notas concretas.

**[pd-03]** ¿Revisaste o actualizaste tu plan semanal?

> R: Solo si aplica.

**[pd-04]** ¿Tuviste somnolencia post-almuerzo?

> R: Respuesta concreta o no registrado.

---

## 🏃 Personal

**[pe-01]** ¿Hiciste ejercicio hoy?

> R: Pasos, caminata o no registrado.

**[pe-02]** ¿A qué hora dormiste y cómo amaneciste?

> R: Respuesta concreta o pendiente.

**[pe-03]** ¿Hubo bloqueo emocional o mental?

> R: Respuesta concreta.

---

## 🐒 Nota de cierre

- Logro principal del dia:
- Pendiente mas urgente:
- Observacion honesta del dia:

🐒 **Pendiente:**

- [ ] Pendiente 1
- [ ] Pendiente 2
- [ ] Generar [[{{dia}}-summary]]
- [ ] Generar [[{{dia}}-todoreviewer]] si falta

---

_Generado con la skill `daily-checkin` · [[{{dia_anterior}}-checkin]] ← → [[{{dia_siguiente}}-checkin]]_

Reglas:
- Si el archivo es inferido, usa `estado: inferido-desde-todolist`.
- Si hay respuestas completas, usa `estado: completado`.
- Distingue "no registrado" de "no hecho".
- Usa pendientes con checkbox al final.
- Conserva el tono directo del Simio, pero no agregues interrogatorio si el usuario pidio crear archivo directamente.
- Usa wikilinks exactos y paths reales.
```
