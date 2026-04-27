# Modo: Weekly Review / Resumen Semanal

Activar cuando Samuel pida su resumen semanal, weekly review, o nota de la semana.

Este modo complementa la skill `obsidian-weekly-summary` con contexto personal profundo.
Si esa skill está disponible, usar este modo para personalizar el output.

---

## Qué capturar de la semana de Samuel

### Dimensiones a revisar

**1. Proyectos**
- Braymar: features completadas, PRs mergeados, bugs resueltos, blockers
- WeTech: decisiones tomadas, avances del equipo, reuniones importantes
- Side projects: cualquier progreso en Listalico, FInovate, exploración IA

**2. Universidad**
- Entregas realizadas y pendientes
- Exámenes dados o próximos
- Conceptos nuevos aprendidos (útiles o no)
- Algo de clase que conectó con su trabajo real

**3. IA & Herramientas**
- Nuevas herramientas exploradas
- Modelos probados en Ollama
- Workflows de Claude Code que funcionaron o no
- Skills de Obsidian usadas

**4. Personal**
- Energía de la semana (¿fue sostenible la carga?)
- Algo aprendido fuera del código
- Gastos significativos (si usa obsidian-finance-advisor)
- Ideas que surgieron y quiere capturar

---

## Formato del weekly para Samuel

```markdown
---
tags: [weekly-review, semana-{{N}}, {{año}}]
semana: {{YEAR}}-W{{NUM}}
fecha_inicio: {{lunes}}
fecha_fin: {{domingo}}
energia: {{1-5}} ⚡
---

# Weekly Review — W{{NUM}} {{año}}

## Una línea de la semana
> [La frase que describe esta semana en ≤15 palabras]

---

## 🏗️ Proyectos

### Braymar
- ✅ [completado]
- 🔄 [en progreso]
- ❌ [bloqueado / pendiente]

### WeTech / WeRide
- [actividad]

### Otros
- [side projects / exploración]

---

## 🎓 Universidad

| Curso | Actividad | Estado |
|-------|-----------|--------|
| Cálculo | [tarea/examen] | ✅/🔄/⬜ |
| Sistemas Operativos | | |
| Estadística Aplicada | | |
| Aplicaciones Móviles | | |

**Próximos deadlines:**
- [ ] [fecha] — [entrega]

---

## 🤖 IA & Workflow

- [herramienta/modelo explorado] → [qué aprendió o logró]

---

## 💡 Ideas de la semana

- [idea 1 — con suficiente contexto para entenderla en 3 meses]
- [idea 2]

---

## ⚡ Energía y carga

- Nivel de energía: {{N}}/5
- Lo que más consumió tiempo: [X]
- Lo que más vale la pena repetir: [Y]

---

## ⏭️ La semana que viene

**Objetivo único:** [una sola cosa que define el éxito de la semana]

**Must-do:**
- [ ] [tarea 1]
- [ ] [tarea 2]

**Explícitamente NO:**
- [cosa que conscientemente deja para después]

---

*[[{{PREV_WEEK}}]] ← W{{NUM}} → [[{{NEXT_WEEK}}]]*
```

---

## Inferencia cuando faltan datos

Si Samuel no da detalles explícitos de la semana, inferir de memorias y preguntar
solo lo crítico:

> "No tengo el detalle de lo que hiciste esta semana — ¿me das una lista rápida de
> los highlights (proyectos + uni) y genero el weekly con eso?"

No generar un weekly vacío lleno de placeholders — mejor pedir los datos primero.
