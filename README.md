# 🐍 git-agent-wsl-config

Configuración completa del ecosistema de agentes AI para WSL/Ubuntu:
**Pi Coding Agent** (el Gentleman) + **Hermes Agent** (ecosistema Qu@ntum).

## 🧠 Ecosistema de Agentes

| Plataforma | Rol | Agentes |
|-----------|-----|--------|
| **Pi Coding Agent** | Desarrollo controlado (SDD, TDD, subagentes) | el Gentleman (orquestador) |
| **Hermes Agent** | Agentes especializados autónomos | DevOpsIA, Mayor Motoko Kusanagi, mentor_Q |

### Almas de los Agentes

Todos los agentes comparten un alma común definida en [`pi/gentle-ai/support/agentes-soul.md`](pi/gentle-ai/support/agentes-soul.md):
- 🗣️ Español empático, alegre y proactivo
- 🧠 PNL implícita (reencuadre, anclaje, puente al futuro)
- 🎩 Pensamiento lateral (Seis Sombreros de De Bono)
- 🧘 Filosofía Zen (Shoshin, Kaizen, Wabi-sabi, Ikigai)
- 📈 Mejora continua (PDCA, ODDE, 5S)

## Estructura

```
pi/                       # Configuración de Pi Coding Agent
├── settings.json
├── mcp.json
├── agent/
│   ├── settings.json
│   ├── models.json
│   ├── agents/
│   ├── skills/
│   └── git/
├── agents/                # Agentes SDD
├── chains/                # Cadenas SDD
└── gentle-ai/             # Gentle AI (alma compartida + TDD)

hermes/                    # Configuración de Hermes Agent
├── SOUL.md                # Alma del agente principal
├── USER.md                # Contexto del usuario Qu@ntum
├── profiles/
│   ├── devopsia/          # DevOpsIA — El Constructor
│   ├── secopsh4ck/        # Mayor Motoko Kusanagi — La Protectora
│   └── mentor_q/          # mentor_Q — El Guía
├── skills/
│   └── image-reader/      # OCR para imágenes
└── docs/                  # Guías de instalación y uso
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
