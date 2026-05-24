# LESSONS.md - Errores conocidos y soluciones rápidas

## Error de dependencias en entornos de contenedores
- **Problema:** Desfase de versiones entre docker builder y ejecutor local.
- **Solución:** Bloquear dependencias estrictamente usando lockfiles (poetry.lock / cargo.lock).
