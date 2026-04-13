---
tags:
  - weekly-plan
  - upc
  - ciclo-6
  - semana-3
  - 2026-W17
semana_uni: 3
semana_iso: 2026-W16
fecha_inicio: 2026-04-20
fecha_fin: 2026-04-26
objetivo: Entregar DD1 de Estadística, rendir CV2 de Cálculo y dejar LinkedIn auditado
energia_target: 4/5
---

# 📅 Plan Semana 3 — UPC Ciclo 6
**Lunes 13 Abr → Domingo 19 Abr, 2026**

---

## 🎯 Objetivo único de la semana
> **Cerrar las dos obligaciones académicas críticas (DD1 + CV2) sin que nada las bloquee, y dejar LinkedIn auditado con Claude como activo de carrera.**

*Si solo pudieras hacer una cosa esta semana, sería terminar el DD1 de Estadística antes del jueves.*

---

## 🔥 Must-do (non-negotiable)

- [ ] 📊 **DD1 Estadística Aplicada** — completar y entregar antes del vencimiento
- [x] 🧮 **CV2 Cálculo 2** — estudiar y rendir (regla de la cadena + derivadas implícitas)
- [ ] 🔍 **Auditoría LinkedIn con Claude** — perfil, headline, about, proyectos revisados
- [ ] 📱 **Repo Kotlin guardado** — repositorio de práctica de clase commiteado en GitHub
- [ ] 📝 **Apuntes Estadística en Obsidian** — nota `apuntes-estadistica-s3.md` creada

---

## 🎓 Universidad — Semana 3

### Temas por curso

| Curso                  | Tema Semana 3                                                                      | Recurso principal                                                      | Estado |
| ---------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------ |
| 📱 Apps Móviles        | Componentes básicos en Android (Kotlin) — Activities, Views, Layouts *(propuesto)* | [Android Docs](https://developer.android.com/guide) · Repo de práctica | ⬜      |
| 💻 Sistemas Operativos | Hilos (Threads) — modelos de hilos, ventajas vs procesos *(propuesto)*             | OSTEP cap. 26-27                                                       | ⬜      |
| 🧮 Cálculo 2           | Regla de la cadena + derivadas implícitas *(propuesto)*                            | NotebookLM + PDF clase                                                 | ⬜      |
| 📊 Estadística         | Variables aleatorias discretas — PMF, esperanza, varianza *(propuesto)*            | NotebookLM + PDF clase                                                 | ⬜      |

> *Temas marcados como `(propuesto)` → confirmar con sílabo o profe y actualizar.*

---

### 📋 Entregas y evaluaciones

| Qué                       | Curso                | Fecha límite               | Estado |
| ------------------------- | -------------------- | -------------------------- | ------ |
| **DD1 — Tarea 1**         | Estadística Aplicada | *(confirmar fecha exacta)* | ⬜      |
| **CV2 — Control 2**       | Cálculo 2            | *(confirmar fecha exacta)* | ⬜      |
| **Repo práctica Kotlin**  | Apps Móviles         | En clase / esta semana     | ⬜      |
| **Doc Markdown proyecto** | Apps Móviles         | Avance parcial             | ⬜      |

---

### 🧮 Cálculo 2 — Prep CV2

**Tema CV2:** Regla de la cadena · Derivadas implícitas

**Plan de estudio express:**
- [ ] Revisar slides del profe + apuntes de semana 3 después de clase
- [ ] Resolver mínimo 5 ejercicios de regla de la cadena (función compuesta)
- [ ] Resolver 3 ejercicios de derivadas implícitas (F(x,y)=0 → dy/dx)
- [ ] Verificar resultados con `sympy` en Python:
  ```python
  from sympy import *
  x, y = symbols('x y')
  f = x**2 * sin(x**3)  # ejemplo regla de cadena
  print(diff(f, x))
  ```
- [ ] Subir apuntes a NotebookLM `Cálculo 2 — Ciclo 6` después de clase

**Analogía para ti:** la regla de la cadena es básicamente composición de funciones — el mismo concepto de `middleware → handler → response` en Express/FastAPI. Si `h(x) = f(g(x))`, entonces `h'(x) = f'(g(x)) · g'(x)`. Un request que pasa por 2 middlewares y cada uno transforma el output del anterior.

---

### 📊 Estadística Aplicada — DD1

**Tema:** Variables aleatorias discretas — PMF, E[X], Var(X)

**Plan para el DD1:**
- [ ] Leer el enunciado completo del DD1 y descomponerlo en subproblemas
- [ ] Identificar qué tipo de variable aleatoria discreta pide cada problema (Bernoulli / Binomial / Poisson / general)
- [ ] Resolver con fórmulas y verificar con Python:
  ```python
  from scipy import stats
  import numpy as np

  # Ejemplo: P(X=k) para Binomial(n=10, p=0.3)
  dist = stats.binom(n=10, p=0.3)
  print(dist.pmf(3))       # P(X=3)
  print(dist.mean())       # E[X]
  print(dist.var())        # Var(X)
  ```
- [ ] Documentar proceso en `apuntes-estadistica-s3.md` en Obsidian
- [ ] Subir material a NotebookLM `Estadística Aplicada — Ciclo 6`
- [ ] **Entregar** antes del deadline

---

### 📱 Aplicaciones Móviles

**Contexto:** El curso usa **Kotlin + Android nativo** (confirmado por la práctica en clase).

**Kotlin ≠ React Native** — el mental model cambia: en vez de `useState` → ViewModel + LiveData; en vez de Flexbox → XML Layouts o Jetpack Compose.

**Tareas:**
- [ ] Durante clase: seguir la práctica y codear el repositorio junto con el profe
- [ ] Al terminar clase: subir repo a GitHub
  ```bash
  # Si no tienes el repo inicializado aún:
  git init
  git add .
  git commit -m "feat: práctica semana 3 - [tema de la clase]"
  git remote add origin https://github.com/samuelbonifacio015/[nombre-repo]
  git push -u origin main
  ```
- [ ] **Documentación Markdown del proyecto** — avanzar con:
  - `README.md` con descripción, stack, cómo correrlo
  - Sección de arquitectura (si aplica)
  - Screenshots o GIFs del flujo principal
  - [ ] Al menos 50% de la doc completada esta semana

**Recursos:**
- [Kotlin Docs — Android Basics](https://developer.android.com/courses/android-basics-kotlin/course)
- [Jetpack Compose (si lo usan)](https://developer.android.com/jetpack/compose)

---

### 💻 Sistemas Operativos

**Tema semana 3:** Hilos (Threads) — modelos, ventajas vs procesos *(propuesto)*

**Analogía directa:**
- Thread vs Process → como goroutines de Go o `asyncio.create_task()` en Python — comparten memoria del proceso padre, más ligeros que crear un proceso nuevo
- En tu Listalico: el backend FastAPI + uvicorn usa hilos para manejar múltiples requests. La transcripción por chunks es un caso real de concurrencia.

**Tareas:**
- [ ] Asistir a clase y tomar apuntes
- [ ] Leer OSTEP cap. 26 ("Concurrency: An Introduction")
- [ ] Crear `apuntes-so-s3.md` en Obsidian con diagrama de estados de hilos

---

### 📓 NotebookLM — tareas de la semana

- [ ] Subir apuntes de Cálculo 2 (después de clase)
- [ ] Subir material del DD1 de Estadística + resolución
- [ ] Subir slides de SO semana 3
- [ ] Verificar que los notebooks responden bien queries del tema actual

---

## 🔍 Auditoría LinkedIn con Claude

**Por qué esta semana:** Con tu perfil en movimiento (UPC Beca de Honor + Braymar + WeTech + Listalico), LinkedIn es tu activo de carrera más descuidado. Una auditoría bien hecha = más visibilidad para practicante roles.

**Checklist de auditoría (hacer con Claude en otra sesión):**

### Perfil
- [ ] **Foto** — profesional, buena luz, fondo limpio
- [ ] **Banner** — personalizado (no el default de LinkedIn)
- [ ] **Headline** — ¿dice "Estudiante" solo? → mejorar a algo como: *"Software Engineer · Founder @WeTech · Next.js · TypeScript · Building real products"*
- [ ] **About (extracto)** — ¿tienes uno? ¿dice algo concreto?

### Experiencia
- [ ] **WeTech / WeRide** — ¿está listado como Founder & Tech Lead?
- [ ] **Braymar** — ¿aparece como proyecto cliente (Freelance Dev)?
- [ ] **Listalico** — ¿aparece como proyecto personal deployado?

### Skills & Proyectos
- [ ] Skills actualizadas: Next.js, TypeScript, Supabase, FastAPI, Spring Boot, Docker
- [ ] Proyectos añadidos con links (Listalico en Vercel, portfolio)

### Visibilidad
- [ ] URL personalizada (linkedin.com/in/samuel-bonifacio o similar)
- [ ] Open to Work activado (si buscas practicante)

**Prompt para la auditoría con Claude:**
```
Actúa como un recruiter técnico senior en Lima, Perú. Voy a compartirte mi perfil de LinkedIn
y necesito un análisis crítico: qué está bien, qué está mal, y qué cambiaría exactamente
(con reescrituras concretas del headline, about y descripciones de experiencia).
Soy un dev de 20 años, estudiante UPC, Founder de WeTech, y busco practicante roles en Lima.
```

---

## 🏗️ Proyectos

### Braymar
**Sprint semana 3:** Mantenimiento mínimo — la semana está cargada con DD1 + CV2

- [ ] Si hay un bug crítico reportado → resolverlo (máx. 2hr)
- [ ] Si no hay urgencia → postponer features nuevas a semana 4
- [ ] Revisar el estado del repo rápido (5 min): ¿hay algún PR abierto que se pueda mergear fácil?

**Status:** Feature development en pausa esta semana. DD1 y CV2 primero.

### WeTech / WeRide
- [ ] Sync rápido con el equipo (si toca esta semana) — máx. 1hr
- [ ] Revisar PRs pendientes del equipo sin bloquearlos

---

## 📆 Distribución diaria

| Día | Mañana | Tarde | Noche |
|-----|--------|-------|-------|
| **Lun 20** | Clases UPC | DD1 Estadística: leer enunciado + resolver 50% | Apuntes SO + Obsidian daily |
| **Mar 21** | Clases UPC | DD1 Estadística: terminar + revisión final | Apuntes Estadística en Obsidian |
| **Mié 22** | Clases UPC | CV2 prep: regla de la cadena (ejercicios) | Auditoría LinkedIn con Claude |
| **Jue 23** | Clases UPC + **CV2** | Repo Kotlin: subir a GitHub post-clase | Obsidian daily + descanso |
| **Vie 24** | Clases UPC | Documentación Markdown Apps Móviles | NotebookLM: subir materiales semana |
| **Sáb 25** | Documentación Móviles (terminar 50%) | Buffer / catch-up pendientes | Libre / exploración |
| **Dom 26** | Descanso real | Weekly review Obsidian | Prep semana 4 |

> ⚠️ El **DD1** tiene prioridad absoluta Lunes y Martes. No toques Braymar hasta que esté entregado.

---

## 💡 Ideas para listas de tareas (T4 — si sobra tiempo)

Estas son listas que puedes construir en Obsidian como notas persistentes — no son para esta semana, son activos de largo plazo:

### 1. 🛠️ `lista-skills-tecnicas-2026.md`
Skills que quieres dominar antes de terminar el año:
- Kotlin / Android nativo (ya empezaste)
- Docker Compose avanzado (multi-service)
- Testing con Jest + Vitest en Next.js
- Redis (caching para Braymar)
- CI/CD con GitHub Actions

### 2. 🏗️ `braymar-backlog.md`
Features y deuda técnica de Braymar, ordenadas por impacto:
- Completar `ProductGrid`, `ProductCardList`, `ProductLocations`
- Añadir paginación al inventario
- Dashboard con métricas (ventas, stock bajo)
- Export a PDF/Excel para gerencia
- RLS (Row Level Security) en Supabase

### 3. 🤝 `linkedin-conexiones-target.md`
Personas de Lima a conectar en LinkedIn:
- CTOs / Tech Leads de startups peruanas
- Reclutadores tech de empresas como Rappi, Yape, Interbank, BCP
- Alumni de UPC que ya están trabajando en tech
- Mentores potenciales en Kotlin / mobile

### 4. 📚 `recursos-tecnicos-pendientes.md`
Libros, cursos y papers en tu radar:
- OSTEP completo (ya lo estás usando en SO)
- "Designing Data-Intensive Applications" — DDIA
- Road to React (actualización con React 19)
- FastAPI advanced patterns (dependency injection, background tasks)

### 5. 🚀 `side-projects-ideas.md`
Ideas de proyectos para buildear este año:
- CLI tool para generar estructura de proyectos Next.js + Supabase
- Bot de Telegram para tracking de gastos en soles (FInovate v2)
- Dashboard de métricas para WeTech
- App móvil Android + Spring Boot (cruce de habilidades Kotlin + Java)

---

## 🌱 Si sobra tiempo (T4)

- [ ] Explorar Jetpack Compose básico (futuro del Android dev en Kotlin)
- [ ] Actualizar `samuelbonifacio.vercel.app` — agregar Braymar y el repo Kotlin como proyectos
- [ ] Leer OSTEP cap. 26 con más profundidad (hilos)

---

## ❌ Explícitamente NO esta semana

- **Braymar features nuevas** — DD1 + CV2 tienen prioridad absoluta
- **FInovate** — sigue en pausa
- **Ollama / modelos locales** — exploración para otra semana
- **Refactors grandes** en cualquier repo

---

## 🧠 Setup de Obsidian esta semana

```
📁 Universidad/Ciclo-6/Semana-3/
  ├── apuntes-estadistica-s3.md   ← DD1 + teoría variables discretas
  ├── apuntes-calculo-s3.md       ← CV2 prep: regla de cadena + impl.
  ├── apuntes-movil-s3.md         ← Kotlin en clase + doc proyecto
  └── apuntes-so-s3.md            ← Hilos: modelos y estados

📁 Carrera/
  └── linkedin-auditoria-2026.md  ← Resultados de auditoría con Claude

📁 Proyectos/Apps-Moviles/
  └── doc-proyecto-movil.md       ← README + arquitectura del proyecto

📁 Diarios/2026/
  ├── diario-2026-04-20.md
  ├── diario-2026-04-21.md
  ├── diario-2026-04-22.md
  ├── diario-2026-04-23.md
  ├── diario-2026-04-24.md
  ├── diario-2026-04-25.md
  └── diario-2026-04-26.md

📁 Planes/
  └── 2026-W17-plan.md  ← este archivo
```

---

## 🔗 Links rápidos

- Repo práctica Kotlin: `github.com/samuelbonifacio015/[nombre-por-definir]`
- Braymar repo: [`samuelbonifacio015/Braymar-frontend`](https://github.com/samuelbonifacio015/Braymar-frontend)
- NotebookLM: [notebooklm.google.com](https://notebooklm.google.com)
- OSTEP (SO): [ostep.org](https://ostep.org)
- Android Kotlin Docs: [developer.android.com](https://developer.android.com/guide)
- LinkedIn: [linkedin.com/in/](https://linkedin.com/in/)

---

*[[2026-W15-plan]] ← **W16 · Semana 3 UPC** → [[2026-W17-plan]]*
