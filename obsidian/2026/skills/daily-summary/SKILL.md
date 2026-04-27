---
name: daily-summary
description: >
  Generador de resumen ejecutivo diario para Samuel Bonifacio — toma las respuestas de un
  daily check-in completado (o una nota daily existente) y produce un archivo "{dia}-summary.md"
  compacto, narrativo y listo para Obsidian. Activa esta skill SIEMPRE que Samuel diga frases
  como: "genera el summary del día", "crea mi resumen de hoy", "genera jueves-summary",
  "genera {día}-summary", "quiero el summary", "resumen ejecutivo del día", "daily summary",
  "summary de hoy", o cuando comparta respuestas de check-in y pida generar un archivo de
  resumen distinto al daily completo. También actívala si menciona "summary para Obsidian",
  "nota resumen del día", o cualquier variante de querer un resumen condensado del día.
  Esta skill es el complemento narrativo del daily-checkin — úsala sin dudar cuando el
  objetivo es un resumen corto y accionable, no el check-in con checkboxes completo.
---

# 📋 Daily Summary Generator

Genera un resumen ejecutivo del día de Samuel — compacto, narrativo, sin checkboxes, listo
para Obsidian. Es el complemento del `daily-checkin`: donde el check-in es granular y exhaustivo,
el summary es el **extracto de alto nivel** que Samuel puede releer en 30 segundos.

---

## Input esperado

Acepta cualquiera de estos formatos:

1. **Respuestas crudas del check-in** (como las que el Simio recibe) — el formato que Samuel
   pega después de completar el interrogatorio.
2. **Nota daily generada** (el `.md` completo del daily-checkin) — la procesa y condensa.
3. **Texto libre** — "hoy hice X, Y, no avancé Z" — lo interpreta y genera el summary.

Si el input incluye una sección `🐒 Nota:` o `🐒 Pendiente:`, úsala como fuente primaria
para los logros y pendientes.

---

## Output: `{dia}-summary.md`

**Nombre de archivo sugerido:** `{dia-semana}-summary.md` (ej: `jueves-summary.md`)
O con fecha ISO si Samuel lo prefiere: `2026-04-23-summary.md`

Lee `references/plantilla-summary.md` para el template exacto.

---

## Reglas de generación

### 1. Extracto narrativo (no checkboxes)
Escribe en **prosa corta** — máx 3-4 oraciones. Describe qué pasó en el día de forma
humana: qué se logró, qué no se tocó, cuál fue el factor dominante del día.

### 2. Logros del día
- Lista de 2-5 bullets con los logros **concretos** — no "avancé Cálculo", sino
  "repaso completo de EU1 Cálculo 2 antes del CV1".
- Si hubo un logro excepcional (20/20 en tarea, deploy exitoso, etc.), márcalo con 🏆.
- Orden: académico → proyectos → técnico → personal.

### 3. Bloqueadores
- Lista concisa (1-3 items) de lo que frenó el día — técnico, físico, o de contexto.
- Si no hubo bloqueadores, omitir la sección (no poner "ninguno").

### 4. Pendientes activos
- Extrae de las respuestas o de la sección `🐒 Pendiente:` los TODOs pendientes.
- Formato: `- [ ] item` — para que Obsidian los renderice como checkboxes interactivos.
- Prioriza por urgencia si hay contexto suficiente.

### 5. Score y mood
- **Score:** hereda del daily-checkin si está disponible. Si no, infiere:
  `Score = (logros completados / total ítems activos del día) × 10`
- **Mood tag:** uno de `#dia/productivo`, `#dia/intenso`, `#dia/regular`, `#dia/flojo`
- Criterio:
  - `productivo` → score ≥ 7, varios ítems clave completados
  - `intenso` → académico pesado o muchas cosas a la vez, aunque agotador
  - `regular` → score 4-6, mezcla de hecho/no hecho
  - `flojo` → score ≤ 3, poco completado o día descarrilado

### 6. Una línea de cierre
Frase honesta de máx 12 palabras que capture la esencia del día. No motivacional genérica.
Ejemplos: *"Día sólido en lo académico, proyectos en deuda."*

---

## Integración con otros archivos en el vault

El summary debe linkar automáticamente a otros archivos del vault generados ese día:

```
[[{dia}-checkin]] | [[{dia}-todolist]] | [[{dia}-todoreviewer]]
```

Solo incluir los que Samuel mencionó que creó.

---

## Notas de tono

- **Conciso:** si el daily-checkin ya tiene 80 líneas de detalle, el summary tiene 20.
- **Sin fluff:** nada de "fue un gran día de aprendizaje" si no lo fue.
- **Específico:** "20/20 en Tarea 3 Estadística" > "avancé Estadística".
- **PM voice:** habla como un PM revisando el sprint del día — preciso, sin dramatismo.

---

## Referencias

| Archivo                           | Cuándo leerlo                            |
| --------------------------------- | ---------------------------------------- |
| `references/plantilla-summary.md` | **Siempre** — antes de generar el output |