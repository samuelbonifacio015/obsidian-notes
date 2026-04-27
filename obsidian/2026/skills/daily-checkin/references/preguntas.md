# 🐒 Banco de Preguntas — Daily Check-in

> Este archivo es la fuente de verdad del Simio.
> Edítalo directamente o dile a Claude: "agrega pregunta: [texto]" durante el check-in.
> 
> Frecuencias válidas: `diaria` | `semanal` (solo lunes) | `puntual` (siempre activa mientras activa: true) | `aleatoria` (banco rotativo elegido por IA)
> Para desactivar una pregunta sin borrarla: cambia `activa: true` → `activa: false`
>
> Las preguntas `aleatoria` no se hacen todas juntas. Los agentes de IA, especialmente Codex,
> deben escoger una muestra pequeña y distinta en cada check-in según el contexto reciente.

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

## 🎲 BANCO ALEATORIO / ROTATIVO

> Este bloque agrega variación al check-in. Codex debe elegir aleatoriamente entre 2 y 4 preguntas
> activas de este banco por día, priorizando lo que venga más caliente del contexto reciente.
> No reemplaza las preguntas diarias base; las complementa.
>
> Criterio sugerido: 1 académica, 1 de proyectos o IA/dev, y 1 de energía/cierre si aplica.

```yaml
- id: rx-ac-01
  categoria: academico
  pregunta: "¿Qué tema de Cálculo II necesita hoy evidencia real, no solo sensación de avance?"
  followup: "¿Puedes nombrar un ejercicio, tipo de problema o simulación que lo pruebe?"
  frecuencia: aleatoria
  peso: alto
  contexto: "Cálculo II EU1, superficies, dominios, gráficas, razonamiento cuantitativo, simulación de examen"
  activa: true

- id: rx-ac-02
  categoria: academico
  pregunta: "Si mañana tuvieras práctica de Cálculo, ¿qué punto te haría perder más puntos?"
  followup: "¿Lo atacaste hoy o sigue abierto?"
  frecuencia: aleatoria
  peso: alto
  contexto: "readiness 5/10 en Cálculo II"
  activa: true

- id: rx-ac-03
  categoria: academico
  pregunta: "¿Hiciste algún ejercicio de Cálculo sin guía de ChatGPT o IA?"
  followup: "¿Dónde te trabaste cuando ya no había ayuda paso a paso?"
  frecuencia: aleatoria
  peso: alto
  contexto: "uso de ChatGPT/mentor IA para EU1"
  activa: true

- id: rx-ac-04
  categoria: academico
  pregunta: "¿Qué quedó pendiente de Estadística Aplicada y por qué volvió a quedar fuera?"
  followup: "¿Es falta de urgencia, energía o claridad sobre el siguiente tema?"
  frecuencia: aleatoria
  peso: medio
  contexto: "Estadística Aplicada sin avance en varios cierres"
  activa: true

- id: rx-ac-05
  categoria: academico
  pregunta: "¿Qué curso UPC quedó más vulnerable hoy: Cálculo, Estadística, Sistemas Operativos o Aplicaciones Móviles?"
  followup: "¿Cuál es la acción mínima para que no se vuelva deuda mañana?"
  frecuencia: aleatoria
  peso: medio
  contexto: "balance académico UPC"
  activa: true

- id: rx-pr-01
  categoria: proyectos
  pregunta: "¿MaquinariasJyS avanzó en algo verificable visualmente o solo en intención?"
  followup: "¿Qué pantalla, componente o flujo quedó listo para revisar?"
  frecuencia: aleatoria
  peso: alto
  contexto: "MaquinariasJyS, admin/orders, pantallas finales, tracker"
  activa: true

- id: rx-pr-02
  categoria: proyectos
  pregunta: "¿El avance de MaquinariasJyS necesita captura, demo o nota técnica para no perder contexto?"
  followup: "¿Dónde debería quedar documentado?"
  frecuencia: aleatoria
  peso: medio
  contexto: "tracker de pantallas y cierre visual"
  activa: true

- id: rx-pr-03
  categoria: proyectos
  pregunta: "¿Quedó algún feedback o decisión de QRust/Klippr que todavía no esté registrado?"
  followup: "¿Es feedback del profesor, decisión de equipo o ajuste técnico?"
  frecuencia: aleatoria
  peso: medio
  contexto: "QRust - Klippr, sustentación, entrega TB1"
  activa: true

- id: rx-ai-01
  categoria: ia-dev
  pregunta: "¿La IA te ayudó hoy a estudiar o a evitar estudiar?"
  followup: "¿Qué parte hiciste tú sin delegarla?"
  frecuencia: aleatoria
  peso: alto
  contexto: "ChatGPT, mentor de Cálculo II, Deepseek V4-Pro-Max"
  activa: true

- id: rx-ai-02
  categoria: ia-dev
  pregunta: "¿Probaste algún modelo, API o herramienta nueva con un resultado concreto?"
  followup: "¿Qué aprendiste que valga una nota en Obsidian?"
  frecuencia: aleatoria
  peso: medio
  contexto: "llama.cpp, Ollama, modelos locales, Deepseek"
  activa: true

- id: rx-ai-03
  categoria: ia-dev
  pregunta: "¿Claude Code se usó para cerrar trabajo o para abrir más frentes?"
  followup: "¿Qué repo y qué entregable concreto salió?"
  frecuencia: aleatoria
  peso: medio
  contexto: "Claude Code en MaquinariasJyS y límites de uso"
  activa: true

- id: rx-pd-01
  categoria: productividad
  pregunta: "¿El todolist de hoy coincide con lo que realmente pasó?"
  followup: "¿Hay alguna tarea marcada como completa que el check-in contradice?"
  frecuencia: aleatoria
  peso: alto
  contexto: "inconsistencia 8k pasos vs 6k pasos, reviewer diario"
  activa: true

- id: rx-pd-02
  categoria: productividad
  pregunta: "¿Qué nota de Obsidian debería existir después de lo que hiciste hoy?"
  followup: "¿Es summary, todoreviewer, apunte académico o tracker de proyecto?"
  frecuencia: aleatoria
  peso: medio
  contexto: "cierre de vault, summaries, todoreviewers"
  activa: true

- id: rx-pd-03
  categoria: productividad
  pregunta: "¿Cuál fue el pendiente que más se arrastró desde días anteriores?"
  followup: "¿Lo resolviste, lo moviste o lo estás evitando?"
  frecuencia: aleatoria
  peso: alto
  contexto: "Cálculo, Estadística, MJYS, pendientes UPC"
  activa: true

- id: rx-pe-01
  categoria: personal
  pregunta: "¿Tu energía real del día justificó el nivel de exigencia que te pusiste?"
  followup: "¿Dormiste, caminaste y comiste como para sostener ese ritmo?"
  frecuencia: aleatoria
  peso: medio
  contexto: "sueño 12:30AM, buena energía, pasos"
  activa: true

- id: rx-pe-02
  categoria: personal
  pregunta: "¿Hubo una diferencia entre sentirte bien y rendir bien?"
  followup: "¿En qué tarea se notó más?"
  frecuencia: aleatoria
  peso: medio
  contexto: "buen amanecer, Cálculo 5/10, avance parcial"
  activa: true
```

---

## 🔧 Instrucciones de edición

Para **agregar** una pregunta nueva:
```yaml
- id: [categoria]-[siguiente_numero]
  pregunta: "[tu pregunta]"
  followup: "[pregunta de seguimiento, o null]"
  frecuencia: diaria | semanal | puntual | aleatoria
  activa: true
```

Para **desactivar** sin borrar: cambia `activa: true` → `activa: false`

Para **suspender una semana**: cambia `frecuencia: diaria` → `frecuencia: puntual` y `activa: false`
