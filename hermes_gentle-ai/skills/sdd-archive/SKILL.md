---
name: sdd-archive
description: "Close a completed SDD change. Syncs delta specs to main specs and archives the change folder."
version: 1.0.0
author: Gentle AI
tags: [sdd, archive, close]
---

# SDD Archive — Skill de Cierre

Cargá esta skill para archivar un cambio completado:
```
/skill sdd-archive
```

## Contexto

Necesitás todos los artefactos del cambio:
- proposal
- spec (delta)
- design
- tasks (completas)
- apply-progress
- verify-report (pass)

## Flujo

### 1. Sync specs
Si usás artifact store `openspec`:
- Aplicá los cambios del delta spec al spec canónico
- ADDED requirements → agregar al canónico
- MODIFIED requirements → reemplazar en el canónico
- REMOVED requirements → eliminar del canónico

### 2. Archivar
Mové la carpeta del cambio a `openspec/changes/archive/YYYY-MM-DD-{change}/`

### 3. Reportar
```
status: ok | blocked
executive_summary
artifacts: archive location
risks: (none for archive)
next_recommended: start next change | done
```

---

*Basado en gentle-pi assets/agents/sdd-archive.md*
