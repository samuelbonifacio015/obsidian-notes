---

## tags: [weekly-plan, semana-2, upc, ciclo-6, 2026] semana: 2026-W16 semana-uni: Semana 2 UPC — Ciclo 6 fecha_inicio: 2026-04-13 fecha_fin: 2026-04-19 estado: 🔄 en curso

# 📅 Plan Semanal — Semana 2 UPC | W16

## 🎯 El objetivo único de esta semana

> Tener los cuadernos de Cálculo 2 y Estadística en NotebookLM, los temas de Apps Móviles y SO definidos, y al menos 1 feature de Braymar mergeada.

---

## 📊 Vista rápida

|Área|Foco principal|Carga est.|
|---|---|---|
|📱 Apps Móviles|Componentes básicos + StyleSheet (Semana 2)|~3hr|
|💻 Sistemas Operativos|Gestión de procesos — PCB, estados (Semana 2)|~3hr|
|🧮 Cálculo 2|Tema semana 2 _(a confirmar con el profe)_|~2hr|
|📊 Estadística|Tema semana 2 _(a confirmar con el profe)_|~2hr|
|🏗️ Braymar|Completar componentes post context-compaction|~8hr|
|🚀 WeTech|Revisión técnica semanal con equipo|~3hr|
|🧠 Obsidian|Diario diario + esta nota|~1hr/día|

**Total estimado:** ~28hr en 7 días — manejable si Braymar no tiene blockers.

---

## 🎓 Universidad — Semana 2

### 📱 Aplicaciones Móviles

**Tema inferido semana 2:** Componentes básicos de React Native — `View`, `Text`, `StyleSheet`, `TouchableOpacity`

> _Si el profe ve otro tema, actualizar aquí._

**Recursos:**

- [React Native — Core Components](https://reactnative.dev/docs/components-and-apis)
- [Expo — Getting Started](https://docs.expo.dev/get-started/introduction/)
- Slides del curso (subir a NotebookLM cuando las tengas)

**Conexión con tu stack:** Ya sabes JSX de React y Braymar — el salto a RN es cambiar `div→View`, `p→Text`, CSS→StyleSheet. El mental model es el mismo.

**Tareas:**

- [ ] Asistir a clase y tomar apuntes
- [ ] Crear nota `apuntes-movil-s2.md` en Obsidian con el tema visto
- [ ] Hacer el ejercicio/práctica que dejen
- [ ] Confirmar si usan React Native o Flutter y actualizar este plan

---

### 💻 Sistemas Operativos

**Tema semana 2:** Gestión de procesos — estados del proceso, PCB, transiciones de estado

> Basado en syllabus típico UPC. Confirmar con el profe/sílabo.

**Analogía directa para ti:**

- PCB (Process Control Block) → el objeto que devuelve `ps aux` o `docker inspect <container>`
- Estados (new → ready → running → waiting → terminated) → lifecycle de un request en FastAPI: llega (new) → entra a la queue de uvicorn (ready) → ejecuta la función (running) → espera a Supabase (waiting) → devuelve response (terminated)

**Recursos:**

- Operating Systems: Three Easy Pieces (OSTEP) — [ostep.org](https://ostep.org/) (gratis, excelente)
- Capítulo 4: "The Abstraction: The Process"
- Slides del curso

**Tareas:**

- [ ] Asistir a clase
- [ ] Leer cap. 4 de OSTEP antes o después de clase
- [ ] Crear nota `apuntes-so-s2.md` con el diagrama de estados del proceso
- [ ] Hacer ejercicios de práctica si dejan

---

### 🧮 Cálculo 2

**Tema:** _(a confirmar — revisar sílabo o preguntarle al profe)_

**NotebookLM — acción esta semana:**

- [ ] Abrir [NotebookLM](https://notebooklm.google.com/)
- [ ] Crear notebook: `UPC | Cálculo 2 | Semana 2 — [Tema]`
- [ ] Subir: slides del profe + apuntes Obsidian de semana 1 (si los tienes)
- [ ] Verificar que el chat del notebook responde bien preguntas del tema

**Tareas académicas:**

- [ ] Asistir a clase
- [ ] Resolver ejercicios del tema _(mínimo los del libro/slides)_
- [ ] Subir apuntes a Obsidian y al notebook de NotebookLM

---

### 📊 Estadística Aplicada

**Tema:** _(a confirmar — revisar sílabo)_

**NotebookLM — acción esta semana:**

- [ ] Abrir [NotebookLM](https://notebooklm.google.com/)
- [ ] Crear notebook: `UPC | Estadística | Semana 2 — [Tema]`
- [ ] Subir: slides + apuntes de semana 1
- [ ] Test: hacerle una pregunta al notebook del tema anterior para validar que entiende el material

**Tareas académicas:**

- [ ] Asistir a clase
- [ ] Resolver ejercicios
- [ ] Apuntes a Obsidian

---

## 🏗️ Proyectos

### Braymar

**Foco:** Auditar componentes incompletos (post context-compaction de Claude Code) y completar al menos 1

**Antes de tocar código nuevo:**

- [ ] Revisar qué quedó pendiente en la última sesión de Claude Code
- [ ] Listar componentes rotos o sin terminar en un comentario TODO
- [ ] Decidir cuál tiene más impacto completar primero

**Desarrollo:**

- [ ] Completar componente(s) identificados
- [ ] Verificar que Supabase integration funciona end-to-end
- [ ] PR / commit con descripción clara

**Deploy:**

- [ ] Push a Vercel — confirmar que el build no está roto

### WeTech / WeRide

- [ ] Reunión / sync con el equipo si toca esta semana
- [ ] Revisar PRs pendientes del equipo
- [ ] Definir prioridad técnica de la semana para el equipo

---

## 📆 Distribución por día

|Día|Mañana|Tarde|Noche|
|---|---|---|---|
|**Lun 13**|Clase(s) UPC|Braymar: audit de componentes|Apuntes SO en Obsidian|
|**Mar 14**|Clase(s) UPC|Braymar: completar componente|Apuntes Apps Móviles|
|**Mié 15**|Clase(s) UPC|WeTech: sync + revisión|Ejercicios Cálculo/Estadística|
|**Jue 16**|Clase(s) UPC|Braymar: PR + Vercel deploy|NotebookLM: Cálculo 2 setup|
|**Vie 17**|Clase(s) UPC|Cierre semanal: checklist|NotebookLM: Estadística setup|
|**Sáb 18**|Deep work: Braymar / WeTech|Continúa|Libre / exploración|
|**Dom 19**|Revisión semanal|Prep semana 3|Weekly review Obsidian|

---

## 🔥 Must-do inamovibles

- [ ] **Temas definidos** para Apps Móviles y SO (confirmar con sílabo/profe)
- [ ] **NotebookLM Cálculo 2** — notebook creado con material de semana 2
- [ ] **NotebookLM Estadística** — notebook creado con material de semana 2
- [ ] **Braymar** — al menos 1 componente completado y en Vercel
- [ ] **Diario Obsidian** — cada noche, máx. 10 minutos (7/7 días)

## ❌ Explícitamente fuera esta semana

- FInovate — en pausa, no tocar
- Exploración de modelos Ollama — semana siguiente si hay tiempo
- Refactor grande en Braymar — solo completar lo que está incompleto, no iniciar nada nuevo

---

## 🧠 Setup de Obsidian esta semana

Archivos a crear en el vault:

```
📁 Universidad/Ciclo-6/
  ├── apuntes-movil-s2.md
  ├── apuntes-so-s2.md
  ├── apuntes-calculo2-s2.md
  └── apuntes-estadistica-s2.md

📁 Diarios/2026/
  ├── diario-2026-04-13.md  (Lunes)
  ├── diario-2026-04-14.md  (Martes)
  ├── diario-2026-04-15.md  (Miércoles)
  ├── diario-2026-04-16.md  (Jueves)
  ├── diario-2026-04-17.md  (Viernes)
  ├── diario-2026-04-18.md  (Sábado)
  └── diario-2026-04-19.md  (Domingo)

📁 Planes/
  └── 2026-W16-plan.md  ← este archivo
```

---

## 🔗 Links rápidos

- Braymar repo: [`samuelbonifacio015/Braymar-frontend`](https://github.com/samuelbonifacio015/Braymar-frontend)
- NotebookLM: [notebooklm.google.com](https://notebooklm.google.com/)
- OSTEP (SO): [ostep.org](https://ostep.org/)
- React Native Docs: [reactnative.dev](https://reactnative.dev/)
- Expo Docs: [docs.expo.dev](https://docs.expo.dev/)

---

[[2026-W15-plan]] ← **W16 · Semana 2 UPC** → [[2026-W17-plan]]