# 🎩 Gentle-AI para Hermes

Configuración completa de **Gentle-AI / el Gentleman** para **Hermes Agent** (perfil quantum).

## Estructura

```
hermes_gentle-ai/
├── SOUL.md                        ← Personalidad: el Gentleman + Qu@ntum
├── config.yaml                    ← Config: gemma4 removido, SDD routing, Engram MCP
│
└── skills/
    ├── gentle-ai-harness/         ← Harness: routing, delegación, SDD flow
    ├── gentle-ai-support/         ← Alma compartida + TDD estricto
    ├── sdd-init/                  ← Inicializar contexto SDD
    ├── sdd-explore/               ← Explorar idea de cambio
    ├── sdd-proposal/              ← Propuesta de cambio
    ├── sdd-spec/                  ← Especificaciones con escenarios
    ├── sdd-design/                ← Diseño técnico
    ├── sdd-tasks/                 ← Desglose de tareas + forecast
    ├── sdd-apply/                 ← Implementación (TDD)
    ├── sdd-verify/                ← Verificación contra specs
    ├── sdd-archive/               ← Cierre y archivo
    └── sdd-onboard/               ← Guía interactiva del ciclo SDD
```

## Instalación

```bash
# 1. Respaldar
cp -r ~/.hermes ~/backups/hermes-$(date +%Y%m%d)

# 2. SOUL.md
cp SOUL.md ~/.hermes/profiles/quantum/SOUL.md

# 3. Config.yaml (revisar diff primero, contiene API keys y modelo default)
#    Extraer solo las secciones: mcp_servers, SDD Phase Routing
#    Borrar gemma4 del config actual

# 4. Skills
cp -r skills/* ~/.hermes/profiles/quantum/skills/

# 5. Recargar
#    En Hermes: /reload-skills
#    En Hermes: /reload-mcp   (para Engram)
#    En Hermes: /gentle-ai-harness
```

## Cambios respecto al perfil original

| Cambio | Detalle |
|--------|---------|
| Modelos gemma4 | Eliminados (gemma4:e4b, gemma4:26b) |
| SDD Phase Routing | Documentación de modelo por fase SDD |
| MCP Servers | Engram (`engram mcp --tools=agent`) |
| SOUL.md | Fusión Gentle-AI + Qu@ntum (253 líneas) |
| Skills | 11 skills SDD + 1 harness + 3 support |

## Ciclo SDD

```
/reload-skills
/gentle-ai-harness     ← reglas del harness
/sdd-init              ← inicializar
/sdd-explore           ← explorar
/sdd-proposal          ← proponer
/sdd-spec              ← especificar
/sdd-design            ← diseñar
/sdd-tasks             ← desglosar tareas
/sdd-apply             ← implementar
/sdd-verify            ← verificar
/sdd-archive           ← archivar
```

Para más detalle: `../gentle-ai/backysoporte/gentle-ai-incorporacion.html`
