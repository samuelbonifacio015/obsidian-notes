---
tags: [daily-checkin, {{MOOD_TAG}}]
fecha: {{FECHA_ISO}}
dia: {{DIA_SEMANA}}
score: {{SCORE}}/10
---

# 🐒 Daily Check-in — {{FECHA_LARGA}}

> {{REFLEXION_UNA_LINEA}}

---

## 📊 Score del día: {{SCORE}}/10

```
{{BARRA_VISUAL}}
```

---

## 🎓 Académico

- [{{AC_01}}] **Cálculo** — {{AC_01_DETALLE}}
- [{{AC_02}}] **Blackboard UPC** — {{AC_02_DETALLE}}
- [{{AC_03}}] **Estadística Aplicada** — {{AC_03_DETALLE}}
- [{{AC_04}}] **Sistemas Operativos** — {{AC_04_DETALLE}}
- [{{AC_05}}] **Aplicaciones Móviles** — {{AC_05_DETALLE}}
- [{{AC_06}}] **Entregas / exámenes próximos** — {{AC_06_DETALLE}}

---

## 🛠️ Proyectos

- [{{PR_01}}] **MaquinariasJyS** — {{PR_01_DETALLE}}
- [{{PR_02}}] **Kliprr** — {{PR_02_DETALLE}}
- [{{PR_03}}] **Proyecto nuevo / puntual** — {{PR_04_DETALLE}}

---

## 🤖 IA & Dev

- [{{AI_01}}] **Claude Code** — {{AI_01_DETALLE}}
- [{{AI_02}}] **Ollama / modelo local** — {{AI_02_DETALLE}}
- [{{AI_03}}] **Aprendizaje técnico** — {{AI_03_DETALLE}}

---

## 📋 Productividad

- [{{PD_01}}] **Diario Obsidian** — {{PD_01_DETALLE}}
- [{{PD_02}}] **Notas Obsidian** — {{PD_02_DETALLE}}
- [{{PD_03}}] **Plan semanal** — {{PD_03_DETALLE}}
- [{{PD_04}}] **Somnolencia post-almuerzo** — {{PD_04_DETALLE}}

---

## 💼 Carrera *(solo si aplica esta semana)*

- [{{CA_01}}] **LinkedIn** — {{CA_01_DETALLE}}
- [{{CA_02}}] **Contenido / Speaker** — {{CA_02_DETALLE}}
- [{{CA_03}}] **Networking** — {{CA_03_DETALLE}}
- [{{CA_04}}] **Aspiración speaker** — {{CA_04_DETALLE}}

---

## 🏃 Personal

- [{{PE_01}}] **Ejercicio** — {{PE_01_DETALLE}}
- [{{PE_02}}] **Sueño** — {{PE_02_DETALLE}}
- [{{PE_03}}] **Bloqueo emocional / mental** — {{PE_03_DETALLE}}

---

## 💬 Reflexión

{{REFLEXION_COMPLETA}}

---

## 🎯 Intención para mañana

> **{{INTENCION_MANANA}}**

---

## 🔗 Links del día *(opcional)*

- {{LINKS_O_OMITIR}}

---

*Generado con la skill `daily-checkin` · [[{{AYER}}]] ← → [[{{MANANA}}]]*
```

---

### Guía de llenado para el modelo

**{{BARRA_VISUAL}}** → genera una barra de progreso ASCII basada en el score:
```
Score 10/10 → ██████████ 10/10
Score 8/10 → ████████░░ 8/10
Score 5/10 → █████░░░░░ 5/10
Score 3/10 → ███░░░░░░░ 3/10
```

**Checkboxes** → usa `x` si completado, ` ` (espacio) si no:
- `[x]` = hecho
- `[ ]` = no hecho / sin actividad

**Preguntas semanales / puntuales** → incluir solo si aplican según `preguntas.md.md`:
- `semanal`: solo lunes, salvo que Samuel dé contexto explícito.
- `puntual`: incluir mientras `activa: true`.

**{{MOOD_TAG}}** → infiere uno de:
- `dia/productivo` — score ≥ 7 y varios proyectos tocados
- `dia/intenso` — académico pesado o muchas cosas pero agotador
- `dia/regular` — score 4-6, mezcla de hecho/no hecho
- `dia/flojo` — score ≤ 3, poco o nada completado

**{{REFLEXION_UNA_LINEA}}** → máx 15 palabras, honesta. Ejemplos:
- *"Día cargado de Cálculo, Braymar sin tocar."*
- *"Productivo en proyectos, académico flojo."*
- *"Buena energía hoy, casi todo completo."*

**{{REFLEXION_COMPLETA}}** → 2-3 líneas. Menciona lo más significativo del día —
qué avanzó, qué quedó pendiente, y una observación honesta (no motivacional genérica).

**{{INTENCION_MANANA}}** → 1 acción concreta. Elige la más urgente o más rezagada de hoy.
Formato: verbo + objeto + contexto. Ejemplo:
- *"Avanzar ProductTable en Braymar — completar el componente incompleto."*
- *"Estudiar Series de Taylor en Cálculo — hay ejercicios sin resolver."*

**Fechas:**
- `{{FECHA_ISO}}` → `2026-04-22`
- `{{FECHA_LARGA}}` → `Miércoles, 22 de Abril de 2026`
- `{{DIA_SEMANA}}` → `miércoles`
- `{{AYER}}` → `2026-04-21-daily`
- `{{MANANA}}` → `2026-04-23-daily`
