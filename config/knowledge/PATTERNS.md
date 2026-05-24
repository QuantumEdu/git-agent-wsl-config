# PATTERNS.md - Patrones de Diseño Verificados

## Patrón Hexagonal en FastAPI
- Separación estricta de dominios, puertos y adaptadores.
- Los modelos de base de datos no deben contaminar las entidades del dominio de negocio.

## Manejo de Conexiones SQLite FTS5
- Optimizar búsquedas usando MATCH sobre tablas virtuales.
