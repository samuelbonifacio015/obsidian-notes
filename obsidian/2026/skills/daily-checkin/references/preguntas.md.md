# 🐒 Banco de Preguntas — Daily Check-in

> Este archivo es la fuente de verdad del Simio.
> Edítalo directamente o dile a Claude: "agrega pregunta: [texto]" durante el check-in.
> 
> Frecuencias válidas: `diaria` | `semanal` (solo lunes) | `puntual` (siempre activa mientras activa: true)
> Para desactivar una pregunta sin borrarla: cambia `activa: true` → `activa: false`

---

## 🎓 ACADÉMICO

```yaml
- id: ac-01
  pregunta: "¿Avanzaste algo de Cálculo hoy? ¿Qué tema?"
  followup: "¿Cuántas páginas/ejercicios? ¿Entendiste o quedó duda?"
  frecuencia: diaria
  activa: true

- id: ac-02
  pregunta: "¿Revisaste el Blackboard de UPC hoy?"
  followup: "¿Había algo nuevo — tarea, anuncio, material?"
  frecuencia: diaria
  activa: true

- id: ac-03
  pregunta: "¿Tocaste Estadística Aplicada?"
  followup: "¿Qué tema — distribuciones, inferencia, probabilidad?"
  frecuencia: diaria
  activa: true

- id: ac-04
  pregunta: "¿Avanzaste en Sistemas Operativos?"
  followup: "¿Procesos, hilos, memoria, scheduling?"
  frecuencia: diaria
  activa: true

- id: ac-05
  pregunta: "¿Tocaste Aplicaciones Móviles?"
  followup: "¿Practicaste algo de código o fue teoría?"
  frecuencia: diaria
  activa: true

- id: ac-06
  pregunta: "¿Hay alguna entrega o examen próximo que debas preparar?"
  followup: "¿Cuándo es y qué tan listo estás?"
  frecuencia: semanal
  activa: true
```

---

## 🛠️ PROYECTOS

```yaml
- id: pr-01
  pregunta: "¿Tocaste MaquinariasJyS hoy?"
  followup: "¿Qué componente o feature? ¿Fue código, diseño, o Supabase?"
  frecuencia: diaria
  activa: true

- id: pr-02
  pregunta: "¿Algún feature nuevo para Klippr?"
  followup: "¿Backend, frontend, landing page?"
  frecuencia: diaria
  activa: true

- id: pr-03
  pregunta: "¿Hiciste algo con tu porfolio?"
  followup: "¿Fix, feature, o solo revisaste?"
  frecuencia: semanal
  activa: true

- id: pr-04
  pregunta: "¿Hay algún proyecto nuevo que hayas empezado o planeado hoy?"
  followup: "¿Cuál, en qué stack?"
  frecuencia: puntual
  activa: true
```

---

## 🤖 IA & DEV

```yaml
- id: ai-01
  pregunta: "¿Usaste Claude Code hoy en algún repo?"
  followup: "¿En qué proyecto?"
  frecuencia: diaria
  activa: true

- id: ai-02
  pregunta: "¿Corriste algún modelo local en Ollama?"
  followup: "¿Qué modelo y para qué tarea?"
  frecuencia: semanal
  activa: true

- id: ai-03
  pregunta: "¿Aprendiste algún concepto técnico nuevo hoy — patrón, API, herramienta?"
  followup: "¿Lo documentaste en Obsidian?"
  frecuencia: diaria
  activa: true

- id: ai-04
  pregunta: "¿Avanzaste algún módulo o aprendizaje de IA?"
  followup: "¿Qué módulo? ¿De qué plataforma — YouTube, docs, curso?"
  frecuencia: diaria
  activa: true
```

---

## 📋 PRODUCTIVIDAD

```yaml
- id: pd-01
  pregunta: "¿Escribiste en tu diario de Obsidian hoy?"
  followup: "¿Fue una entrada larga o un par de líneas?"
  frecuencia: diaria
  activa: true

- id: pd-02
  pregunta: "¿Actualizaste o creaste alguna nota en Obsidian?"
  followup: "¿Qué nota — apuntes, idea, proyecto?"
  frecuencia: diaria
  activa: true

- id: pd-03
  pregunta: "¿Revisaste o actualizaste tu plan semanal?"
  followup: "¿Qué cambiaste o priorizaste?"
  frecuencia: semanal
  activa: true

- id: pd-04
  pregunta: "¿Tuviste somnolencia post-almuerzo? ¿Qué hiciste al respecto?"
  followup: "¿Caminaste, descansaste 10 min, o lo ignoraste?"
  frecuencia: diaria
  activa: true
```

---

## 💼 CARRERA

```yaml
- id: ca-01
  pregunta: "¿Tocaste algo de tu perfil de LinkedIn esta semana?"
  followup: "¿Qué sección — skills, about, actividad?"
  frecuencia: semanal
  activa: true

- id: ca-02
  pregunta: "¿Publicaste o preparaste contenido para LinkedIn hoy?"
  followup: "¿De qué tema?"
  frecuencia: semanal
  activa: true

- id: ca-03
  pregunta: "¿Hiciste networking o contactaste a alguien hoy?"
  followup: "¿Fue para oportunidades laborales, colaboración, o mentoría?"
  frecuencia: semanal
  activa: true

- id: ca-04
  pregunta: "¿Avanzaste algo relacionado a tu aspiración como speaker?"
  followup: "¿Preparaste material, investigaste eventos, o practicaste?"
  frecuencia: semanal
  activa: true
```

---

## 🏃 PERSONAL

```yaml
- id: pe-01
  pregunta: "¿Hiciste ejercicio hoy?"
  followup: "¿Qué tipo y cuánto tiempo?"
  frecuencia: diaria
  activa: true

- id: pe-02
  pregunta: "¿A qué hora dormiste anoche y cómo amaneciste?"
  followup: null
  frecuencia: diaria
  activa: true

- id: pe-03
  pregunta: "¿Hubo algo que te bloqueó emocionalmente o mentalmente hoy?"
  followup: "¿Lo procesaste o lo dejaste pendiente?"
  frecuencia: diaria
  activa: true
```

---

## 🔧 Instrucciones de edición

Para **agregar** una pregunta nueva:
```yaml
- id: [categoria]-[siguiente_numero]
  pregunta: "[tu pregunta]"
  followup: "[pregunta de seguimiento, o null]"
  frecuencia: diaria | semanal | puntual
  activa: true
```

Para **desactivar** sin borrar: cambia `activa: true` → `activa: false`

Para **suspender una semana**: cambia `frecuencia: diaria` → `frecuencia: puntual` y `activa: false`