# CLAUDE.md - Guía de Desarrollo para Claude en Personal

Este archivo define comandos de compilación/test e instrucciones de estilo para el proyecto Personal.

## Comandos de Desarrollo Comunes
- No hay comandos automáticos de compilación para este proyecto. Utilizar scripts en el directorio si existen.
- Para verificar sintaxis de Python (si aplica): `python3 -m py_compile *.py`

## Reglas de Estilo e Instrucciones
1. **Comportamiento General**: Sé extremadamente conciso, técnico y directo.
2. **Sistema de Archivos**: Siempre usa rutas absolutas en lugar de relativas.
3. **Manejo de Errores**: Robustez primero. Si faltan recursos u observaciones, maneja el caso de manera segura y silenciosa o informando con [INFO]/[WARNING] sin lanzar excepciones.
4. **Sincronización**: Mantener el contexto sincronizado a través de los archivos del proyecto (`CONTEXT.md`, `DECISIONS.md`).
