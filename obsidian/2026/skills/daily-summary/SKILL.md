---
name: daily-summary
description: >
  Generador de resumen diario minimalista para Samuel Bonifacio — toma el check-in
  y produce un summary de 5 líneas. Activa esta skill cuando Samuel diga "genera el
  summary", "resumen del día", o "{día}-summary".
---

# 📋 Daily Summary — Versión Minimalista

Genera un resumen de 5 líneas. Nada de logros, bloqueadores ni secciones separadas.

---

## Input esperado

- `{dia}-checkin.md` recién generado

## Output: `{dia}-summary.md`

Lee `references/plantilla-summary.md` para el template.

## Reglas

1. **Máximo 5 líneas de contenido** — no más.
2. **NARRATIVA_CORTA:** 2-3 oraciones. Qué dominó el día, qué no se tocó.
3. **CIERRE_UNA_LINEA:** Máximo 12 palabras. Honesta.
4. **Pendientes:** máximo 2. Solo los más urgentes.
5. **Score:** hereda del check-in. No recalculas.
6. **Barra visual:** ASCII ██████░░░░

### Mood tag
- `productivo`: score ≥ 7
- `regular`: score 4-6
- `flojo`: score ≤ 3
