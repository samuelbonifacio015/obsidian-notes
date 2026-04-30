---
name: obsidian-commit-convention
description: >
  Convencion de commits y push automatico para el vault Obsidian de Samuel Bonifacio.
  Usar cuando Codex cree, actualice, elimine, reorganice o mantenga notas, templates,
  carpetas, skills, prompts o configuracion del vault, y deba cerrar el trabajo con
  git commit convencional y git push a GitHub. Activar despues de cualquier feature,
  creacion de archivo, actualizacion o eliminacion realizada por Codex dentro del
  repositorio obsidian-notes.
---

# Obsidian Commit Convention

Usa este skill para cerrar cambios hechos por Codex en el vault `obsidian-notes`
con commits convencionales y push automatico a GitHub.

## Regla Principal

Despues de cualquier feature, creacion de archivo, actualizacion, eliminacion o
reorganizacion realizada por Codex en el vault:

1. Ejecuta `git status --short --branch`.
2. Identifica solo los archivos tocados por Codex en la tarea actual.
3. Stagia unicamente esos archivos.
4. Crea un commit convencional segun la tabla de tipos.
5. Ejecuta `git push` hacia la rama actual; normalmente `git push origin main`.
6. Reporta el hash del commit, el mensaje usado y el resultado del push.

No pidas confirmacion adicional para commit/push si el usuario ya pidio crear,
actualizar, eliminar o implementar contenido con Codex, salvo que haya una
instruccion explicita de no hacerlo o un bloqueo real.

## Tipos De Commit

| Tipo | Usar cuando |
| --- | --- |
| `feat(vault): ...` | Nuevos archivos, plantillas, carpetas, skills, prompts o flujos del vault. |
| `update(vault): ...` | Actualizacion de notas, skills, prompts o archivos existentes. |
| `chore(obsidian): ...` | Configuracion, plugins, metadata, mantenimiento tecnico o archivos auxiliares. |
| `delete(vault): ...` | Eliminacion de notas, configuraciones, templates, carpetas o recursos. |
| `fix(vault): ...` | Correcciones de contenido, frontmatter, enlaces, nombres o errores del vault. |
| `docs(vault): ...` | Documentacion interna del vault o instrucciones de uso. |
| `refactor(vault): ...` | Reorganizacion sin cambio sustancial de contenido. |
| `style(vault): ...` | Formato Markdown, espaciado o limpieza visual sin cambio semantico. |

## Ejemplos

```text
feat(vault): add weekly planning template
feat(vault): add obsidian commit convention skill
update(vault): refresh daily checkin prompt
chore(obsidian): update plugin settings
delete(vault): remove obsolete review note
fix(vault): repair broken calculus wikilinks
docs(vault): document daily summary workflow
refactor(vault): reorganize april week notes
style(vault): normalize markdown spacing
```

## Protecciones

- Nunca incluyas cambios preexistentes, manuales o no relacionados con la tarea actual.
- Nunca uses `git add .` si hay archivos ajenos modificados o sin trackear.
- Nunca reviertas cambios del usuario para limpiar el estado del repo.
- No commitees secretos, tokens, credenciales, archivos privados sensibles ni dumps grandes.
- Si detectas secretos o archivos dudosos, detente y pide confirmacion antes de stagear.
- Si `git push` falla por autenticacion, remoto ausente, rechazo remoto o conflicto,
  deja el commit local intacto, explica el bloqueo y muestra el comando recomendado para resolverlo.

## Flujo Recomendado

```powershell
git status --short --branch
git add -- <archivos-tocados-por-codex>
git commit -m "<tipo(scope): resumen>"
git push origin <rama-actual>
git status --short --branch
```

Usa rutas explicitas en `git add`. Si solo se creo una nota nueva, stagea solo esa nota.
Si se creo un skill, stagea solo la carpeta o archivo del skill creado en esa tarea.
