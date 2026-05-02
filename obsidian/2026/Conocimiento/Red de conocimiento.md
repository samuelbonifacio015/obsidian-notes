---
title: Red de conocimiento
tags:
  - knowledge/moc
  - vault/knowledge-graph
tipo: indice
estado: activo
created: 2026-05-01
---

# Red de conocimiento

Este indice separa el conocimiento estable del seguimiento diario. Los diarios pueden seguir registrando avance, pero los conceptos, decisiones y mapas deben vivir dentro de clusters por dominio.

## Clusters por dominio

Esta nota funciona como guia conceptual, no como supernodo del grafo. Para navegar visualmente los clusters, usa Graph View con el filtro:

```text
path:Conocimiento -file:"Red de conocimiento"
```

Clusters activos:

- Calculo II: MOC, bitacora y conceptos atomicos.
- Estadistica Aplicada: MOC, bitacora y conceptos atomicos.
- MaquinariasJyS: MOC, bitacora, decisiones e integraciones.
- QRust: MOC, bitacora, arquitectura y revisiones.
## Regla de enlace

- Los `*-todolist`, `*-checkin` y `*-summary` deberian enlazar a la bitacora del dominio, no al MOC ni a cada concepto.
- Cada bitacora deberia enlazar al MOC de su dominio.
- Cada MOC deberia enlazar conceptos, decisiones, fuentes y preguntas abiertas del mismo dominio.
- Los indices globales deberian evitar wikilinks directos a todos los clusters para no unir visualmente el grafo.

## Siguiente expansion

- Aplicaciones Moviles.
- Sistemas Operativos.
- Obsidian - Vault.
