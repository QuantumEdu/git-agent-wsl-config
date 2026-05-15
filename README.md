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
├── settings.json          # Settings global (packages, tema, modelo)
├── mcp.json               # Servidores MCP (Engram)
├── agent/
│   ├── settings.json      # Settings del agente (packages completo)
│   ├── models.json        # Providers/models custom (Ollama local)
│   ├── agents/
│   │   └── python-reviewer.md
│   ├── skills/
│   │   └── deploy-staging/
│   └── extensions/        # (en ~/.pi/agent/extensions/ global)
├── agents/                # Agentes SDD
├── chains/                # Cadenas SDD
└── gentle-ai/             # Gentle AI (alma compartida + TDD)

hermes/                    # Configuración de Hermes Agent
├── SOUL.md                # Alma del agente principal
├── USER.md                # Contexto del usuario Qu@ntum
├── profiles/
│   ├── devopsia/           # DevOpsIA — El Constructor
│   ├── secopsh4ck/        # Mayor Motoko Kusanagi — La Protectora
│   └── mentor_q/           # mentor_Q — El Guía
├── skills/
│   └── image-reader/       # OCR para imágenes
└── docs/                  # Guías de instalación y uso
```

## Paquetes instalados

| Paquete | Versión | Rol |
|---------|---------|-----|
| `gentle-pi` | 0.3.0 | Harness de el Gentleman (skills, extensions, prompts) |
| `gentle-engram` | 0.1.5 | Memoria persistente Engram |
| `pi-subagents` | 0.24.2 | Delegación a subagentes |
| `pi-intercom` | 0.6.0 | Comunicación entre sesiones |
| `pi-mcp-adapter` | 2.5.4 | Adaptador MCP |
| `pi-web-access` | latest | Acceso web y búsqueda |
| `pi-memory-md` | latest | Memoria persistente en markdown |
| `@devkade/pi-plan` | latest | Planificación |
| `@juanibiapina/pi-powerbar` | latest | Powerbar TUI |
| `@tmustier/pi-ralph-wiggum` | 0.2.1 | Loops iterativos Ralph Wiggum |
| `@juicesharp/rpiv-todo` | latest | Gestión de tareas TUI |
| `@juicesharp/rpiv-ask-user-question` | latest | Cuestionarios TUI |
| `pi-manage-todo-list` | latest | Gestión de listas de tareas |
| `pi-lens` | latest | LSP y AST navigation |
| `@modemdev/glance-pi` | 0.1.0 | Captura de pantalla live |
| `pi-extensions` (git) | latest | Extensiones TUI (arcade deshabilitadas) |

## Extensiones destacadas

- **gentle-ai.ts** — Core de el Gentleman: system prompt, delegación, SDD
- **sdd-init.ts** — Inicialización de artefactos SDD
- **skill-registry.ts** — Registro de skills del proyecto
- **startup-banner.ts** — Banner de inicio con estado
- **pi-sidebar-monitor.ts** — Panel de monitoreo para desarrolladores
- **agent-guidance** — Guía contextual por modo
- **code-actions** — Acciones de código en TUI
- **files-widget** — Widget de archivos modificados
- **usage-extension** — Monitoreo de uso (tokens, tiempo, costos)
- **session-recap** — Recapitulación de sesión

## Referencia

- [Skills, Prompts y Extensiones — guía completa](docs/reference.md)