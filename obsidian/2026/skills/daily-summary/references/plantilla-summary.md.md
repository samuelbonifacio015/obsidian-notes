---
tags: [daily-summary, {{MOOD_TAG}}]
fecha: {{FECHA_ISO}}
dia: {{DIA_SEMANA}}
score: {{SCORE}}/10
tipo: summary
relacionado: "[[{{CHECKIN_LINK}}]]"
---

# 📋 Summary — {{FECHA_LARGA}}

> *{{CIERRE_UNA_LINEA}}*

---

## ⚡ Resumen del día

{{NARRATIVA_CORTA}}

---

## 🏆 Logros

{{LOGROS_LISTA}}

---

## 🚧 Bloqueadores

{{BLOQUEADORES_LISTA}}

---

## 📌 Pendientes activos

{{PENDIENTES_CHECKBOXES}}

---

## 📊 Score: {{SCORE}}/10 — {{MOOD_TAG}}

```
{{BARRA_VISUAL}}
```

---

## 🔗 Notas del día

{{LINKS_VAULT}}

---

*Generado con la skill `daily-summary` · [[{{AYER}}-summary]] ← → [[{{MANANA}}-summary]]*

---

### Guía de llenado para el modelo

**{{NARRATIVA_CORTA}}** → 2-4 oraciones en prosa. Qué dominó el día, qué no se tocó,
factor externo relevante. Ejemplo:
*"Día enfocado en lo académico: repaso de Cálculo EU1 y entrega de Estadística completada
con nota perfecta. Los proyectos quedaron en pausa — WeTech sin actividad y MJYS sin tocar.
La alergia frenó un poco el ritmo pero no descarriló el día."*

**{{LOGROS_LISTA}}** → bullets concretos, orden: académico → proyectos → técnico → personal.
Marca con 🏆 logros excepcionales. Ejemplo:
```
- Repaso completo de EU1 Cálculo 2 (preparación CV1)
- 🏆 20/20 en Tarea 3 de Estadística Aplicada
- Merge y actualización de QRust Org
- Aprendió despliegue en nube y ventanas de contexto en LLMs
- 5,647 pasos — sin somnolencia post-almuerzo
```

**{{BLOQUEADORES_LISTA}}** → máx 3 bullets. Si no hubo, omitir sección completa. Ejemplo:
```
- Alergia/resfriado redujo capacidad de concentración
- Límite de Claude Code alcanzado — sin sesión de dev
```

**{{PENDIENTES_CHECKBOXES}}** → formato `- [ ] item`. Ejemplo:
```
- [ ] Frontend y 5 pantallas restantes de MJYS
- [ ] MVP y PRD de MJYS
- [ ] Aplicaciones Móviles — sin actividad hoy
```

**{{BARRA_VISUAL}}** → barra ASCII según score:
```
Score 10/10 → ██████████ 10/10
Score 8/10 → ████████░░ 8/10
Score 6/10 → ██████░░░░ 6/10
Score 4/10 → ████░░░░░░ 4/10
```

**{{LINKS_VAULT}}** → links a archivos creados ese día en Obsidian. Ejemplo:
```
[[jueves-checkin]] | [[jueves-todolist]] | [[jueves-todoreviewer]]
```

**Fechas:**
- `{{FECHA_ISO}}` → `2026-04-23`
- `{{FECHA_LARGA}}` → `Jueves, 23 de Abril de 2026`
- `{{DIA_SEMANA}}` → `jueves`
- `{{CHECKIN_LINK}}` → `jueves-checkin` (o nombre del archivo daily del día)
- `{{AYER}}` → `miercoles`
- `{{MANANA}}` → `viernes`