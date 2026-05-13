# git-agent-wsl-config

Configuración de Pi Coding Agent para WSL/Ubuntu.

## Estructura

```
pi/
├── settings.json          # Configuración del runtime de Pi
├── mcp.json               # Servidores MCP activos
├── agent/
│   ├── settings.json      # Configuración del agente (modelos, paquetes, tema, etc.)
│   ├── models.json        # Proveedores y modelos configurados
│   ├── agents/            # Agentes personalizados
│   ├── skills/            # Skills personalizadas
│   └── git/               # Extensiones desde git (pi-extensions)
├── agents/                # Agentes SDD
├── chains/                # Cadenas SDD
└── gentle-ai/             # Soporte para Gentle AI (TDD estricto)
```

## Paquetes instalados

- `pi-subagents` — Delegación a subagentes
- `pi-mcp-adapter` — Adaptador MCP
- `pi-web-access` — Acceso web y búsqueda
- `pi-memory-md` — Memoria persistente en markdown
- `pi-plan` — Planificación
- `pi-powerbar` — Powerbar
- `gentle-pi` — Gentle AI harness
- `gentle-engram` — Memoria Engram
- `pi-intercom` — Comunicación entre sesiones
- `pi-lens` — LSP y AST navigation
- `pi-manage-todo-list` — Gestión de tareas
- `rpiv-todo` / `rpiv-ask-user-question` — Componentes RPiV

## Extensiones

Extensiones desde `git:github.com/tmustier/pi-extensions` (arcade deshabilitadas).

## Referencia

- [Skills, Prompts y Extensiones — guía completa](docs/reference.md)
