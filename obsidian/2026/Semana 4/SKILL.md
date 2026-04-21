---
name: weekly-tuesday-planner
description: >
  Genera un plan de día específico para los martes de la semana UPC. Cada martes, antes de planificar, debe leer todo el
  contexto de Samuel: su perfil personal (samuel-context), los cursos que lleva, el ciclo actual, y los apuntes
  relevantes. Con ese contexto, genera un Tuesday Plan con Top 3 must-do, distribución horaria, y tareas por curso.
  CRITICAL: El proyecto #1 actual es MAQUINARIAS JTS - e-commerce de máquinas (taladros, sierras). Braymar y otros
  proyectos están en PAUSA. Foco 100% en JTS. Activa esta skill SIEMPRE que Samuel pida: "plan del martes",
  "martes", "Tuesday Plan", "qué hago el martes", o cuando sea martes y necesite planificar su día. El output es un
  archivo .md listo para validar.
---

# Tuesday Planner — Semana 4 UPC

Cada martes, este skill genera un plan diário personalizado. Antes de generar output, debe leer los archivos de contexto en orden.

---

## 📚 Archivos de contexto (OBLIGATORIO leerlos en orden)

| Orden | Archivo | Para qué |
|-------|---------|---------|
| 1 | `obsidian/2026/Semana 2/samuel-context/SKILL.md` | Perfil personal, cursos ciclo 6, stack |
| 2 | `obsidian/2026/Semana 2/samuel-context/modes/weekly.md` | Formato de weekly review |
| 3 | `obsidian/2026/Semana 2/samuel-context/modes/tareas.md` | Cómo priorizar tareas |
| 4 | `obsidian/2026/Semana 3/Week 3 - Plan.md` | Plan de semana anterior |
| 5 | `obsidian/2026/Semana 3/summary week 3.md` | Qué pasó realmente |
| 6 | `obsidian/2026/Abril/Plan_Mensual.md` | Meta del mes |

---

## 🚨 CONTEXTO CRÍTICO — Proyecto #1: MAQUINARIAS JTS

**ANTES de generar cualquier output, SIEMPRE considerar:**

| Item | Dato |
|------|-----|
| **Proyecto #1** | Maquinarias JTS (e-commerce de máquinas) |
| **Stack** | Next.js + Supabase (mismo que Braymar) |
| **Repo** | Ya existe en GitHub |
| **FASE 1 ACTUAL** | Validar diseño con cliente (todas las pantallas) |
| **FASE 2** | Frontend básico (first advance) |
| **Deadline S5** | Primer avance (frontend básico) |
| **Braymar** | EN PAUSA - IGNORAR |
| **Otros proyectos** | EN PAUSA - IGNORAR |

### Flujo JTS

```
Semana 4 → Validar diseño con cliente
         → Recibir feedback
Semana 5 → Primer avance: frontend básico
```

### Deadlines Semana 5

| Curso | Entrega |
|-------|---------|
| Cálculo 2 | Examen Unidad 1 |
| Estadística | Primera entrega proyecto |
| SO | PC1 |
| Maquinarias JTS | Primer avance (frontend) |

---

## 🔄 Proceso de generación

### 1. Leer contexto (siempre)

Primero, leer los archivos de la tabla de arriba. Si no los lee, el output será genérico — Sam no quiere respuestas genéricas.

### 2. Identificar estado actual

- ¿Qué semana UPC es? (Semana 4 → Ciclo 6 activo)
- ¿Qué cursos lleva? (Cálculo 2, Estadística Aplicada, SO, Apps Móviles)
- ¿Qué quedó pendiente de semana 3?
- ¿Qué deadlines vienen esta semana?

### 3. Generar el Tuesday Plan

Usar esta estructura:

```markdown
---
tags: [tuesday, semana-4, upc, ciclo-6, 2026]
semana_uni: 4
fecha: {{FECHA_DEL_MARTES}}
energia_target: {{3-5}}/5
---

# 🔥 Tuesday Plan — Semana 4

**{{DIA}} {{FECHA}}, 2026**

---

## 📊 Contexto actual

**Semana UNO:** 4 — Ciclo 6, UPC

**Cursos activos:**
| Curso | Estado |
|------|--------|
| Cálculo 2 | |
| Estadística | |
| SO | |
| Apps Móviles | |

**Pendientes de semana 3:**
- [ ]

---

## 🎯 Top 3 must-do del martes

1. [ ]
2. [ ]
3. [ ]

---

## 🎓 Universidad — Martes

| Horario | Curso | Tema | Notas |
|--------|-------|------|-------|
| | | | |
| | | | |

---

## 🏗️ Proyectos

### Braymar
-

### WeTech
-

---

## ⏱️ Distribución del día

| Hora | Bloque | Actividad |
|------|--------|----------|
| 07:00 | ☀️ Mañana | |
| 09:00 | 🏫 Clases | |
| 12:00 | 🍽️ Almuerzo | |
| 13:00 | 🎯 Tarde | |
| 18:00 | 🌙 Noche | |

---

## 💡 Cierre

**Lo que不错 hoy:**

**Se mueve a mañana:**
- [ ]

---

*Generado con `weekly-tuesday-planner` skill*
```

---

## ⚡ Reglas de generación

1. **SIN fluff** — Sam quiere densidad, no palabras vacías
2. **Siempre accionable** — cada tarea debe tener un siguiente paso claro
3. **Personalizado** — usar su stack real, proyectos reales, no genéricos
4. **Contexto primero** — si no lee el contexto, el output es inútil
5. **Dos idiomas** — puede mezclar español/inglés si Sam lo hace
6. **JTS primero** — siempre prioriza Maquinarias JTS sobre cualquier otro proyecto
7. **Ignorar Braymar** — NO mencionar Braymar en outputs de planeación

---

## 🎯 Cómo sabe que es martes

- Si Sam activa esta skill, asumir que es martes
- Usar la fecha actual del sistema para preencher `{{FECHA}}`
- Si hay duda, preguntar: "¿Qué día es hoy para ti?"

---

## 📂 Output

El skill entrega un archivo `.md` listo para:
1. Sam lo revisa
2. Valida el plan
3. Lo ejecuta

No genera dailies de toda la semana — solo el martes.

---

*Skill basada en `obsidian-weekly-summary` y `samuel-context`*