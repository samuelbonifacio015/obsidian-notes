---
name: week-tracker
description: >
  Skill nativo para Samuel Bonifacio que crea, actualiza y mantiene un tracker semanal vivo en Obsidian.
  Usalo cuando Samuel pida "week tracker", "tracker semanal", "estado de la semana", "actualiza mi semana",
  "que llevo esta semana", "board semanal", "seguimiento semanal", "parametros de la semana", "contexto actual",
  o cuando necesite consolidar dailies, todolists, summaries, todoreviewers, cursos UPC, proyectos activos,
  habitos, metricas, riesgos y prioridades en una sola nota operativa. Este skill debe leer el vault antes de
  responder y usar los archivos recientes como fuente de verdad.
---

# Week Tracker

Manten una nota semanal viva que funcione como centro de control de Samuel:
que esta haciendo, que esta pendiente, que esta en riesgo, que cambio y que debe saber otro agente antes de ayudarlo.

No reemplaza:
- `daily-checkin`: captura granular del dia.
- `daily-summary`: resumen ejecutivo diario.
- `obsidian-weekly-summary`: retrospectiva final de semana.

Si complementa:
- todolists diarios.
- todoreviewers.
- summaries.
- planificacion UPC.
- seguimiento de proyectos activos.

---

## Flujo De Operacion

```text
FASE 1 -> Cargar contexto real del vault
FASE 2 -> Extraer estado semanal
FASE 3 -> Calcular metricas y riesgos
FASE 4 -> Generar o actualizar tracker semanal
FASE 5 -> Dejar proximos pasos accionables
```

---

## FASE 1 - Carga De Contexto

Antes de generar o actualizar un tracker, lee en este orden:

1. Dailies/check-ins de la semana actual.
2. Todolists de la semana actual.
3. Todoreviewers de la semana actual.
4. Summaries diarios de la semana actual.
5. `samuel-context` si el pedido requiere contexto personal amplio.
6. Skills activas relacionadas:
   - `daily-checkin`
   - `daily-summary`
   - `obsidian-weekly-summary`
   - `calculo-asistente`, si el foco es Calculo
   - `obsidian-markdown`, si se va a escribir nota Obsidian

Si falta un dia, marcalo como `sin registro`, no inventes actividad.

---

## FASE 2 - Extraccion Semanal

Extrae y normaliza estas dimensiones:

### Academico UPC
- [[Calculo II]]
- [[Estadistica Aplicada]]
- [[Sistemas Operativos]]
- [[Aplicaciones Moviles]]
- Blackboard UPC
- entregas, examenes, PC, TB, CV o sustentaciones

### Proyectos
- [[MaquinariasJyS]] como proyecto activo principal.
- [[QRust - Klippr]] si hay feedback, cierre o decisiones pendientes.
- [[QRust Org]] si hay merges, ramas o decisiones tecnicas.
- Braymar solo si vuelve a aparecer explicitamente; por defecto esta en pausa.

### IA & Dev
- Claude Code
- modelos locales / Ollama / llama.cpp
- Deepseek, OpenAI, Gemini u otras APIs
- aprendizajes tecnicos documentables

### Productividad
- Obsidian vault
- check-ins generados
- summaries generados
- todolists y todoreviewers
- inconsistencias entre plan y realidad

### Personal
- sueno
- energia
- pasos / ejercicio
- somnolencia post-almuerzo
- bloqueos mentales o emocionales

---

## FASE 3 - Metricas Semanales

Calcula o infiere:

- `score_semana`: porcentaje global de ejecucion.
- `dias_registrados`: numero de dias con check-in, summary o todolist.
- `top_focus`: area dominante de la semana.
- `riesgo_principal`: cuello de botella mas importante.
- `avance_academico`: progreso real en cursos UPC.
- `avance_proyectos`: progreso real en proyectos.
- `ritmo_personal`: energia, sueno, pasos, consistencia.
- `contexto_para_agentes`: resumen operativo que otro agente debe leer antes de actuar.

Usa criterio:
- Si el usuario reporta readiness numerico, conservalo.
- Si hay contradiccion entre todolist y check-in, prioriza check-in/reviewer.
- Si algo aparece varios dias como pendiente, subelo a riesgo semanal.

---

## FASE 4 - Output

Genera o actualiza un archivo semanal:

```text
obsidian/2026/{Mes}/Semana {N}/week-tracker.md
```

Usa `references/template-week-tracker.md`.

El tracker debe ser denso, escaneable y accionable.

Debe incluir:
- Header con score, foco, riesgo y frase de estado.
- Boards por area.
- Recap dia por dia.
- Tabla de metricas.
- Contexto operativo actual.
- Riesgos.
- Proximas acciones.
- Links a notas del vault.

---

## FASE 5 - Reglas De Actualizacion

Cuando el tracker ya existe:
- Actualiza sin duplicar secciones.
- Preserva contenido manual del usuario si no contradice fuentes recientes.
- Anade nuevos dias en orden cronologico.
- Manten links Obsidian con `[[wikilinks]]`.
- No conviertas el tracker en summary largo; debe servir como tablero.

---

## Tono

Directo, denso, sin motivacion generica.

Aceptable:
- "Calculo sigue siendo el cuello de botella."
- "MJYS avanzo, pero falta evidencia funcional."
- "Semana intensa, no necesariamente cerrada."

Evitar:
- "Gran semana de aprendizaje."
- "Sigue asi."
- "Todo va bien" si hay riesgos abiertos.

---

## Referencias

| Archivo | Cuando leerlo |
|---|---|
| `references/template-week-tracker.md` | Siempre antes de generar output |
| `references/extraction-rules.md` | Cuando haya multiples fuentes o contradicciones |
| `references/current-context-schema.md` | Cuando se actualicen parametros semanales |
