---
name: samuel-context
description: >
  Perfil personal profundo de Samuel Bonifacio — desarrollador de software de 20 años, estudiante de
  Ingeniería de Software en UPC (Lima, Perú) y Founder + Tech Lead de WeTech/WeRide. Activa esta skill
  SIEMPRE que Samuel pida algo que se beneficie de contexto personal: consejo de vida/carrera,
  resumen semanal, apuntes de cursos universitarios, planificación de tareas, análisis de proyectos,
  reflexiones personales, decisiones técnicas o cualquier output que deba sonar como si Claude lo
  conociera de verdad. También actívala cuando mencione UPC, WeTech, Braymar, Listalico, su laptop,
  su PC gamer, Obsidian, sus cursos, su equipo, Lima, o cualquier elemento de su vida diaria.
  Esta skill es el "yo soy Samuel" — úsala para dar respuestas que no suenen genéricas.
---

# Samuel Bonifacio — Perfil Personal Completo

Esta skill convierte a Claude en alguien que *conoce a Samuel de verdad*. Antes de generar cualquier
output, lee las secciones relevantes según el tipo de solicitud. El índice de referencias está al final.

---

## 👤 Quién es Samuel

**Samuel Bonifacio**, 20 años, Lima, Perú (distrito San Isidro).
Generación Z. Mentalidad de builder — prefiere construir antes que teorizar.
Lenguaje: español nativo, inglés fluido. Responde bien en ambos.
Comunicación: directa, densa, sin fluff. Prefiere respuestas de alta señal.

**Identidad técnica:**
- Estudiante de 3er año de Ingeniería de Software en **UPC** (Universidad Peruana de Ciencias Aplicadas)
- **Founder & Tech Lead** de WeTech / WeRide — su propio startup
- Builder full-stack con inclinación hacia sistemas backend robustos y productos reales

**Carácter:**
- Proactivo. Si tiene una idea, la ejecuta.
- Le gusta la intersección entre tecnología y problemas sociales a escala
- Gestiona su conocimiento en **Obsidian** (vault personal)
- Sigue su presupuesto personal en soles (S/)
- Tiene hambre de crecer rápido — no se conforma con "aprender", quiere *construir y deployar*

---

## 🎓 Universidad — UPC, Ciclo 6

**Carrera:** Ingeniería de Software  
**Ciclo actual:** 6to (de 10)  
**Institución:** UPC — sede San Isidro / Lima

### Cursos activos este ciclo

| Curso | Tipo | Notas |
|-------|------|-------|
| **Cálculo** | Matemática | Derivadas, integrales, series |
| **Sistemas Operativos** | CS Core | Procesos, hilos, memoria, scheduling |
| **Estadística Aplicada** | Matemática | Probabilidad, distribuciones, inferencia |
| **Aplicaciones Móviles** | Desarrollo | Mobile dev (probablemente React Native o Flutter) |

**Logros académicos:**
- Beca de Honor (mérito académico) — incluida en su CV

**Estilo de aprendizaje:**
- Aprende haciendo. Los apuntes teóricos puros no le enganchan.
- Prefiere ejemplos de código real, analogías con proyectos que ya conoce.
- Si es Sistemas Operativos → analogías con Docker, procesos Linux.
- Si es Estadística → analogías con métricas de producto o análisis de datos reales.

---

## 💻 Stack técnico completo

### Lenguajes
`Java` · `TypeScript` · `Python` · `JavaScript` · `SQL`

### Frontend
`Next.js 14` · `React` · `Angular` · `Vue.js` · `shadcn/ui` · `Tailwind CSS` · `Vite`

### Backend
`Spring Boot` · `Node.js` · `FastAPI` · `Express`

### Bases de datos
`PostgreSQL` · `MySQL` · `Supabase` (Postgres + Auth + Storage)

### DevOps & Cloud
`Docker` · `Azure` · `AWS` · `Railway` · `Render` · `Vercel`

### IA / ML
`Claude API` (Anthropic) · `Claude Code` · `Ollama` (local LLMs) · `faster-whisper`
`OpenAI API` · `Gemini API` (Nano Banana / Flash Image)

### Herramientas
`Git` · `GitHub` · `Linux (Arch + Ubuntu)` · `Obsidian` · `Postman`

---

## 🖥️ Hardware

| Dispositivo | Specs | Uso |
|-------------|-------|-----|
| **Laptop HP 530** | 8GB RAM, Arch Linux | Desarrollo diario, clases |
| **PC Gamer** | RTX? / GTX 1660 Super (6GB VRAM), 32GB RAM, Linux | Modelos locales, proyectos pesados |

**Limitaciones a considerar:**
- La laptop es su workstation principal — recursos limitados
- La gaming PC puede correr modelos Ollama hasta ~7-8B params (6GB VRAM)
- Conexión a internet con historial de alta latencia/packet loss (ISP Lima)

---

## 🚀 Proyectos activos

### Braymar *(proyecto cliente principal)*
Sistema de gestión de inventario para una distribuidora grande de útiles escolares en Lima.
- **Stack:** Next.js 14 + TypeScript + shadcn/ui + Supabase
- **Repo:** `samuelbonifacio015/Braymar-frontend`
- **Estado:** En desarrollo activo — integraciones Supabase, modos de vista, metric cards
- **Skill relacionada:** `braymar-domain` (leer para contexto de negocio)
- Claude Code está integrado como copiloto en este repo

### WeTech / WeRide *(startup propio)*
Startup fundado por Samuel. Rol: Founder + Tech Lead.
- Lidera un equipo pequeño
- Stack operativo: Java, Spring Boot, Node.js, TypeScript, Angular, Vue.js
- Estado: activo, en desarrollo de producto

### Listalico
App de notas con dictado por voz. Transcripción near-realtime.
- **Frontend:** Vite + React → Vercel (`listalico.vercel.app`)
- **Backend:** FastAPI + faster-whisper (modelo `base`, CPU-only) → Render
- **Implementación:** `MediaRecorder` con chunks de 5 segundos
- Estado: deployado ✅

### FInovate *(backend personal finance)*
Backend de finanzas personales con CQRS.
- **Stack:** FastAPI + SQLAlchemy + MySQL (Railway) → Render
- **Arquitectura:** CQRS, modelado sobre AlToqueBackendApi
- Estado: scaffolded, en pausa

---

## 🛠️ Flujo de trabajo personal

- **Editor principal:** cualquier IDE en Linux (VSCode, IntelliJ)
- **Gestión de conocimiento:** Obsidian vault personal
  - Skills instaladas: `obsidian-weekly-summary`, `obsidian-finance-advisor`
- **Presupuesto:** rastreado en soles (S/) — es sensible al costo
- **IA integrada al workflow:** Claude como copiloto principal, Claude Code en repos activos
- **Deploy preferido:** Vercel (frontend) + Render/Railway (backend) — free tier first

---

## 🧠 Cómo generar outputs para Samuel

Lee la sección relevante en `/modes/` según lo que pida:

| Si pide... | Leer |
|------------|------|
| Consejo (carrera, vida, decisiones) | `modes/consejo.md` |
| Resumen semanal / weekly review | `modes/weekly.md` |
| Apuntes de un curso universitario | `modes/apuntes.md` |
| Planificación de tareas / sprint | `modes/tareas.md` |
| Análisis de proyecto o decisión técnica | `modes/tecnico.md` |
| Nota para Obsidian (genérica) | `modes/obsidian-nota.md` |

Si no encaja en ninguna categoría, aplica el **perfil personal** de esta SKILL.md
para personalizar el tono y los ejemplos. Nunca respondas genéricamente.

---

## ⚡ Reglas de oro para responder a Samuel

1. **Sin fluff** — no repitas lo que dijo, ve directo al punto
2. **Alta densidad** — prefiere mucho valor en pocas palabras
3. **Analogías concretas** — usa proyectos reales suyos como referencia
4. **Siempre accionable** — si das un consejo, que tenga un siguiente paso claro
5. **Respeta su stack** — no sugieras tecnologías incompatibles con lo que ya usa
6. **Habla como alguien que lo conoce** — no como un asistente genérico
7. **Cuando haya duda de idioma** — el contexto dicta; si mezcla español/inglés, él también mezcla
