---
name: sdd-apply
description: "Implement code changes from SDD task definitions. Reads spec, design, tasks. Writes code, marks tasks complete."
version: 1.0.0
author: Gentle AI
tags: [sdd, implementation, coding]
---

# SDD Apply — Skill de Implementación

Cargá esta skill para implementar tareas de un cambio SDD:
```
/skill sdd-apply
```

## Contexto

Ya tenés:
- **spec** — escenarios y criterios de aceptación
- **design** — decisiones técnicas y arquitectura
- **tasks** — checklist de implementación

## Flujo

### 1. Leer artefactos
- Leé spec → criterios de aceptación
- Leé design → approach técnico
- Leé tasks → qué está pendiente
- Si existe apply-progress anterior, mergeá (no overwrite)

### 2. Por cada tarea:
1. Leé los escenarios relevantes de la spec
2. Leé las decisiones de diseño relevantes
3. Leé patrones existentes en el código del proyecto
4. Escribí el código:
   - Si TDD está activo: test falla → implementá → test pasa → refactor
   - Si no: implementá directo con cobertura
5. Marcá la tarea como completa [x]

### 3. Reportar
```
status: ok | blocked | failed
executive_summary
detailed_report:
  - files changed
  - tasks completed
  - tests added/modified
artifacts: apply-progress
risks:
  - deuda técnica detectada
  - edge cases no cubiertos
next_recommended: verify | new tasks | archive
```

## Reglas

- No modifiques código fuera del alcance de las tareas
- Si encontrás un bug fuera de alcance, reportalo pero no lo fixes
- Si una tarea requiere cambios en múltiples archivos, hace primero el análisis, después la implementación
- Si la implementación revela que la spec o design están incompletos, pausá y escalá

---

*Basado en gentle-pi assets/agents/sdd-apply.md*
