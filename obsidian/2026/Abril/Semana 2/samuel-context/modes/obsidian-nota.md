# Modo: Nota Obsidian (Genérica)

Activar cuando Samuel pida crear una nota para Obsidian sin encajar en weekly, apuntes,
o planificación — por ejemplo: nota de reunión, idea desarrollada, referencia técnica,
reflexión personal, resumen de algo que leyó o vio.

---

## Tipos de notas frecuentes en su vault

### 📋 Nota de reunión (cliente, equipo, etc.)
```markdown
---
tags: [reunión, {{proyecto}}, {{fecha}}]
tipo: meeting-note
proyecto: {{Braymar | WeTech | etc}}
---

# Reunión — {{título}}
**Fecha:** {{fecha}}  
**Participantes:** {{nombres}}

## Contexto
[Para qué era esta reunión]

## Decisiones tomadas
- [decisión 1]
- [decisión 2]

## Action items
- [ ] [Samuel] [acción] — deadline: [fecha]
- [ ] [Otro] [acción]

## Próxima reunión
[fecha / condición]
```

---

### 💡 Idea desarrollada
```markdown
---
tags: [idea, {{área}}, {{fecha}}]
estado: 🌱 seedling | 🌿 developing | 🌳 mature
---

# [Nombre de la idea]

## El insight central
[Una oración que captura la idea core]

## Contexto donde surgió
[Qué estaba haciendo cuando se le ocurrió]

## Por qué podría importar
[Impacto potencial]

## Preguntas abiertas
- [qué necesita validar]

## Conexiones
- [[nota relacionada 1]]
- [[nota relacionada 2]]
```

---

### 🔧 Referencia técnica personal
```markdown
---
tags: [referencia, {{tecnología}}, {{tema}}]
tipo: tech-reference
---

# [Tema técnico]

## TL;DR
[Una oración: qué es y cuándo usarlo]

## Código base
\`\`\`[lenguaje]
// snippet que siempre olvida
\`\`\`

## Gotchas
- [error frecuente 1]
- [error frecuente 2]

## Links
- [doc oficial]
- [thread/post que lo explica bien]
```

---

### 📖 Resumen de contenido (artículo, video, libro)
```markdown
---
tags: [lectura, {{tema}}, {{fecha}}]
fuente: [URL o título]
tipo: content-summary
---

# [Título del contenido]

## En una oración
[De qué trata y por qué importa]

## Las 3 ideas que más importan
1. [idea 1 + por qué le importa a Samuel]
2. [idea 2]
3. [idea 3]

## Cómo lo aplica a su contexto
[Conexión directa con Braymar, WeTech, UPC, o su vida]

## Cita favorita
> "[cita si aplica]"
```

---

## Reglas de formato para el vault de Samuel

- **Siempre frontmatter YAML** — facilita búsqueda y filtros en Obsidian
- **Tags en kebab-case:** `sistemas-operativos`, `braymar`, `weekly-review`
- **Links internos con [[doble corchete]]** cuando referencie otro archivo del vault
- **Headers H2 (##) como máximo** dentro de una nota — mantiene jerarquía limpia
- **Emojis en headers de sección** — hace el vault visualmente escaneable
- **Estado de ideas** con emojis estándar: 🌱 seedling → 🌿 developing → 🌳 mature → 🗄️ archived
