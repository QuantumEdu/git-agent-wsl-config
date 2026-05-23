---
name: sdd-verify
description: "Validate implementation against SDD specs. Reports CRITICAL/WARNING/SUGGESTION per requirement."
version: 1.0.0
author: Gentle AI
tags: [sdd, review, validation, testing]
---

# SDD Verify — Skill de Verificación

Cargá esta skill para validar una implementación contra las specs:
```
/skill sdd-verify
```

## Contexto

Necesitás:
- **spec** — para saber qué se requiere
- **tasks** — para saber qué se implementó
- **apply-progress** — para saber el estado actual

## Flujo

### 1. Leer artefactos
- Leé spec completa (todos los escenarios)
- Leé tasks (qué se marcó como completo)
- Leé apply-progress (qué se implementó)

### 2. Por cada requerimiento en la spec:
1. **CRITICAL** si no está implementado o no pasa
2. **WARNING** si está implementado pero con diferencias
3. **SUGGESTION** si está implementado pero mejorable

### 3. Ejecutar (si aplica)
- Si hay tests: correlos
- Si TDD está activo: verificá evidencia RED→GREEN→REFACTOR

### 4. Reportar
```
status: pass | partial | fail
executive_summary
detailed_report:
  - requirements checked: N
  - CRITICAL: N (blocking)
  - WARNING: N (needs attention)
  - SUGGESTION: N (nice to have)
  - tests passing: N/M
artifacts: verify-report
risks:
  - requirements not covered
  - edge cases missing
  - technical debt
next_recommended: fix criticals | archive | continue apply
```

---

*Basado en gentle-pi assets/agents/sdd-verify.md*
