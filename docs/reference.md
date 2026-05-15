# Pi Agent — Referencia de Skills, Prompts y Extensiones

> Última actualización: 2026-05-14 · Pi v0.74.0

## Skills

### Paquete `gentle-pi` v0.3.0

#### branch-pr
Crea PRs con disciplina Gentle AI: verifica que haya issue aprobado (`status:approved`),
usa conventional commits, asigna un solo `type:*` label, corre shellcheck, y usa el
template de PR. El PR **no pasa** sin issue linkage.

**Reglas clave:**
- Branch naming: `^(feat|fix|chore|docs|...)/[a-z0-9._-]+$`
- Commit: `type(scope): description`
- PR body debe linkear issue con `Closes #N`

---

#### chained-pr
Divide PRs que superan **400 líneas** cambiadas en PRs encadenados (stacked PRs a main
o feature branch chain con tracker). Cada slice debe ser revisable en ≤60 min.
Protege al reviewer del burnout.

**Decision gates:**
- ≤400 líneas → single PR
- \>400, slices independientes → Stacked PRs
- \>400, feature integrada → Feature Branch Chain

---

#### cognitive-doc-design
Diseñá documentación que reduce la carga cognitiva. Patrones: lead with the answer,
progressive disclosure, chunking, signposting, recognition over recall, review empathy.
Ideal para READMEs, RFCs, guías de onboarding, arquitectura, PR descriptions.

---

#### comment-writer
Escribí comentarios cálidos, directos y colaborativos. Fórmula:
observación directa → por qué importa → próxima acción concreta.
En español, voseo rioplatense (`podés`, `tenés`, `fijate`, `dale`).
Para PR feedback, issues, Slack, Discord.

---

#### gentle-ai
El harness principal de el Gentleman. Disciplina SDD/OpenSpec, TDD estricto,
delegación a subagentes, reglas de triggers obligatorios:
- **4-file rule**: leer 4+ archivos → delegar exploración
- **Multi-file write rule**: tocar 2+ archivos → usar worker + fresh review
- **PR rule**: antes de commit/PR → fresh review
- **Incident rule**: después de errores de tooling/worktree → fresh audit
- **Long-session rule**: acumulación de complejidad → delegar

---

#### issue-creation
Creá issues de GitHub con templates (bug report o feature request).
Todo issue arranca con `status:needs-review`; un maintainer debe poner
`status:approved` antes de que se pueda abrir un PR. Las preguntas van a
Discussions, no a issues.

---

#### judgment-day
Revisión adversarial ciega: lanza **dos jueces en paralelo** que revisan el
mismo target sin verse entre sí. Clasifica hallazgos en categorías:
- **Confirmed**: ambos jueces coinciden
- **Suspect**: solo uno lo encuentra
- **Contradiction**: veredictos opuestos
- **INFO**: warnings teóricos o sugerencias

Terminal states: `JUDGMENT: APPROVED ✅` o `JUDGMENT: ESCALATED ⚠️`

---

#### work-unit-commits
Planeá commits como unidades de trabajo revisables. Cada commit debe:
- Tener un propósito claro
- Incluir tests con el código que verifican
- Ser candidate a PR independiente
- Contar una historia que el reviewer entienda

**No hagas commits por tipo de archivo** (`add models`, `add services`, `add tests`).
Hacé commits por comportamiento: `feat(auth): add token validation domain model and tests`.

---

### Paquete `pi-subagents` v0.24.2

#### pi-subagents
El sistema de delegación a subagentes. Modos: single, chain, parallel, async,
forked-context.

**Agentes builtin:**

| Agente | Propósito |
|--------|-----------|
| `scout` | Reconocimiento rápido de codebase |
| `planner` | Crea planes de implementación |
| `worker` | Implementación single-writer |
| `reviewer` | Revisión adversarial de código |
| `context-builder` | Construye handoffs de contexto |
| `researcher` | Investigación web |
| `oracle` | Revisión de decisiones y drift |
| `delegate` | Delegación genérica liviana |

**Workflows comunes:**
- `clarify → planner → worker → parallel reviewers → fix worker`
- `scout → planner → worker` (chain mode)
- Parallel review: 3 reviewers fresh-context con ángulos distintos

---

### Paquete `pi-intercom` v0.6.0

#### pi-intercom
Coordinación entre sesiones de Pi en la misma máquina. Mensajería 1:1:
- `send`: fire-and-forget
- `ask`: bloqueante hasta respuesta (timeout 10 min)
- `reply`: responde al ask activo
- `list`: sesiones conectadas con estado
- `pending`: asks sin resolver

Patrones: planner-worker, pair debugging, broadcast, subagent escalations.

---

### Paquete `@tmustier/pi-ralph-wiggum` v0.2.1

#### pi-ralph-wiggum
Loops de desarrollo iterativos largos con checkpoints.
Usá `ralph_start` para comenzar, `ralph_done` para avanzar cada iteración.
Ideal para tareas con muchos pasos discretos. No para one-shots.

---

### Paquete `gentle-engram` v0.1.5

#### (Herramientas de memoria Engram — no skill, sino tools inyectadas)
- `mem_save`: Guardar observaciones con título, tipo, contenido, topic_key
- `mem_search`: Buscar observaciones por query
- `mem_context`: Obtener contexto relevante del proyecto
- `mem_session_summary`: Resumen de sesión al cerrar
- `mem_session_start` / `mem_session_end`: Ciclo de vida de sesión

---

### Paquete `pi-lens`

#### (Herramientas de navegación — no skill, sino tools inyectadas)
- `ast_grep_search`: Búsqueda semántica con patrones AST
- `ast_grep_replace`: Reemplazo semántico con patrones AST
- `lsp_navigation`: Navegación LSP (definition, references, hover, implementation, etc.)

---

### Skills de usuario (`~/.agents/skills/`)

Estas skills están instaladas localmente y no vienen de un paquete npm:

#### context7-mcp
Activa cuando el usuario pregunta sobre librerías, frameworks, referencias API o necesita
ejemplos de código. Usa el servidor MCP Context7 para obtener docs actualizados.

---

#### go-testing
Patrones de testing en Go, incluyendo Bubbletea TUI testing. Trigger: cuando se escriben
tests en Go, se usa teatest, o se agrega cobertura de tests.

---

#### sdd-init / sdd-explore / sdd-propose / sdd-spec / sdd-design / sdd-tasks / sdd-apply / sdd-verify / sdd-archive / sdd-onboard
Flujo completo de Spec-Driven Development. Cada skill corresponde a una fase:
- **sdd-init**: Inicializa contexto SDD (detecta stack, convenciones, testing)
- **sdd-explore**: Investigación antes de comprometerse con un cambio
- **sdd-propose**: Crea propuesta de cambio (intención, alcance, enfoque)
- **sdd-spec**: Escribe especificaciones con requerimientos y escenarios
- **sdd-design**: Documento de diseño técnico con decisiones de arquitectura
- **sdd-tasks**: Desglose en checklist de implementación
- **sdd-apply**: Implementa tareas del cambio, escribiendo código real
- **sdd-verify**: Valida que la implementación coincide con specs, diseño y tasks
- **sdd-archive**: Sincroniza delta specs a main specs y archiva el cambio
- **sdd-onboard**: Walkthrough guiado end-to-end del flujo SDD completo

---

#### skill-creator
Creá o actualizá skills de Pi. Estructura recomendada:
```
mi-skill/
├── SKILL.md         # Frontmatter YAML + cuerpo markdown
├── README.md        # Opcional: resumen humano + instalación
├── scripts/         # Opcional: ejecutables
├── references/      # Opcional: docs largos cargados on-demand
└── assets/          # Opcional: templates/boilerplate
```

---

#### skill-registry
Crea o actualiza el skill registry del proyecto. Escanea skills de usuario y convenciones
del proyecto, escribe `.atl/skill-registry.md`, y guarda en Engram si está disponible.

---

#### special-instruction
Guía para crear prompts, skills, agentes o herramientas usando el template correcto.

---

#### change-review
Revisión de cambios con enfoque estructurado.

#### improvement-loop
Loop de mejora iterativa para código existente.

#### local-retrospective
Retrospectiva local de sesión para capturar aprendizajes.

#### memory-fallback
Fallback de memoria cuando Engram no está disponible.

#### rule-migration
Migración de reglas y convenciones de proyecto.

#### sdd-govplan
Planificación de gobernanza en el flujo SDD.

#### workflow-builder
Constructor de workflows personalizados.

---

## Prompts (Shortcuts)

### `/gcl` — Audit Changelog
**Paquete:** gentle-pi
**Argumento:** ninguno
Audita changelogs antes de release. Revisa todos los commits desde el último
tag, verifica que cada paquete afectado tenga entrada en CHANGELOG.md, y
chequea duplicación cross-package.

### `/gis` — GitHub Issue Solve
**Paquete:** gentle-pi
**Argumento:** `<issue>`
Analiza GitHub issues (bugs o feature requests). Pone label `inprogress`, lee
todo, traza código, encuentra root cause real (no confía en análisis previos),
propone fix. **No implementa**, solo analiza y propone.

### `/gpr` — GitHub PR Review
**Paquete:** gentle-pi
**Argumento:** `<PR-URL>`
Revisa PRs desde URLs. Pone `inprogress`, lee todo (descripción, comments,
commits, diff), identifica issues linkeados, revisa changelog, y devuelve
structured review en formato **Good / Bad / Ugly**.

### `/gwr` — Git Wrap
**Paquete:** gentle-pi
**Argumento:** `[instructions]`
"Wrap it" — finaliza la tarea end-to-end: actualiza changelog, postea comment
final (si es GitHub), commitea solo archivos cambiados en la sesión, y pushea
(solo desde `main`).

### `/gather-context-and-clarify`
**Paquete:** pi-subagents
**Argumento:** ninguno
Lanza `scout` + `researcher` (si hace falta), sintetiza hallazgos, y usa
`interview` para hacer preguntas clarificadoras antes de planear o implementar.

### `/parallel-cleanup`
**Paquete:** pi-subagents
**Argumento:** ninguno
Lanza 2 reviewers fresh-context en paralelo: uno para "deslop" (eliminar
AI-slop, redundancia) y otro para "verbosity" (simplificar). Review-only;
el padre decide qué aplicar.

### `/parallel-context-build`
**Paquete:** pi-subagents
**Argumento:** ninguno
Corre 2-3 `context-builder` agents en chain-parallel mode con distintos
ángulos (request/scope, codebase/patterns, validation/risks). Cada uno genera
un archivo + meta-prompt. El padre sintetiza todo.

### `/parallel-handoff-plan`
**Paquete:** pi-subagents
**Argumento:** ninguno
Combina `researcher` (evidencia externa) + `context-builder` (código local)
+ `context-builder` (estrategia) en chain-parallel, y luego un `context-builder`
de síntesis que escribe un handoff plan final con meta-prompt listo para
implementar.

### `/parallel-research`
**Paquete:** pi-subagents
**Argumento:** ninguno
Combina `researcher` (docs oficiales, specs, benchmarks) con `scout` (repo
local, patrones, constraints). Para preguntas que necesitan tanto evidencia
externa como implicaciones locales.

### `/parallel-review`
**Paquete:** pi-subagents
**Argumento:** ninguno
Lanza 2-3 `reviewer` agents fresh-context en paralelo con ángulos distintos
(correctness/regressions, tests/validation, simplicity/maintainability).
Sintetiza hallazgos antes de aplicar fixes.

---

## Extensiones

### Core del Sistema

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| `gentle-ai.ts` | gentle-pi v0.3.0 | Core de el Gentleman: system prompt, reglas de delegación, SDD workflow |
| `sdd-init.ts` | gentle-pi | Inicialización de artefactos SDD (`.pi/agents/sdd-*.md`, `.pi/chains/sdd-*.chain.md`) |
| `skill-registry.ts` | gentle-pi | Registro de skills del proyecto (`.atl/skill-registry.md`) |
| `startup-banner.ts` | gentle-pi | Banner de inicio con estado de el Gentleman al arrancar sesión |

### Subagentes y Coordinación

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| Runtime de subagentes | pi-subagents v0.24.2 | Modos: single, chain, parallel, async, forked-context |
| Intercom broker + bridge | pi-intercom v0.6.0 | Mensajería entre sesiones Pi en la misma máquina |
| Ralph Wiggum runtime | @tmustier/pi-ralph-wiggum v0.2.1 | Loops iterativos con `ralph_start` / `ralph_done` |

### Memoria

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| Engram tools | gentle-engram v0.1.5 | `mem_save`, `mem_search`, `mem_context`, `mem_session_summary`, etc. |

### Navegación y Búsqueda

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| LSP + AST | pi-lens | `ast_grep_search`, `ast_grep_replace`, `lsp_navigation` |
| Web access | pi-web-access | `web_search`, `code_search`, `fetch_content`, `get_search_content` |

### Integraciones

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| MCP adapter | pi-mcp-adapter v2.5.4 | Adaptador MCP — conecta Pi con servidores MCP externos |
| Glance | @modemdev/glance-pi v0.1.0 | Captura de pantalla live vía `glance.sh` |

### TUI y UI (pi-extensions — git:github.com/tmustier/pi-extensions)

Arcade extensions deshabilitadas en la config actual (`-arcade/picman.ts`, `-arcade/ping.ts`,
`-arcade/spice-invaders.ts`, `-arcade/tetris.ts`, `-arcade/mario-not/mario-not.ts`).

| Extensión | Descripción |
|-----------|-------------|
| `agent-guidance` | Guía contextual para agentes según modo |
| `code-actions` | Acciones de código en TUI (refactors, quick fixes) |
| `files-widget` | Widget de archivos modificados |
| `raw-paste` | Pegado raw de texto (sin procesar markdown) |
| `tab-status` | Estado visual de tabs/pestañas |
| `session-recap` | Recapitulación de sesión al cerrar |
| `usage-extension` | Monitoreo de uso (tokens, tiempo, costos) |
| `pi-ralph-wiggum` | Runtime de Ralph Wiggum (también disponible como npm package independiente) |

### Powerbar

| Extensión | Descripción |
|-----------|-------------|
| `pi-powerbar` | Barra de estado en TUI (modelo, git, tokens, subagentes, etc.) |
| `powerbar-context` | Submódulo: contexto actual (archivo, rama) |
| `powerbar-git` | Submódulo: estado de git |
| `powerbar-model` | Submódulo: modelo activo |
| `powerbar-provider` | Submódulo: provider activo |
| `powerbar-sub` | Submódulo: estado de subagentes |
| `powerbar-tokens` | Submódulo: conteo de tokens |

### Herramientas de Usuario

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| `rpiv-ask-user-question` | @juicesharp/rpiv-ask-user-question | Cuestionarios estructurados en TUI |
| `rpiv-todo` | @juicesharp/rpiv-todo | Gestión de tareas con estados (pending → in_progress → completed) |
| `pi-manage-todo-list` | pi-manage-todo-list | Gestión de listas de tareas (implementación alternativa) |

### Planificación

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| `pi-plan` | @devkade/pi-plan | Planificación estructurada de tareas |

### Personalizadas (proyecto-local y global)

| Extensión | Ubicación | Descripción |
|-----------|-----------|-------------|
| `pi-sidebar-monitor.ts` | `~/.pi/agent/extensions/` y `.pi/extensions/` | Panel de monitoreo para desarrolladores: agente, git, modelo, tokens, skills, stats, stack detectado. Comandos: `/monitor`, `/monitor auto` |

### Dependencia Interna (no listada en packages pero requerida)

| Extensión | Paquete | Descripción |
|-----------|---------|-------------|
| `@marckrenn/pi-sub-core` | (dependencia de powerbar) | Core de subagentes alternativo |

---

## Paquetes Instalados (Resumen)

| Paquete | Versión | Skills | Prompts | Extensiones |
|---------|---------|--------|---------|-------------|
| `gentle-pi` | 0.3.0 | 8 (branch-pr, chained-pr, cognitive-doc-design, comment-writer, gentle-ai, issue-creation, judgment-day, work-unit-commits) | 4 (gcl, gis, gpr, gwr) | 4 (gentle-ai, sdd-init, skill-registry, startup-banner) |
| `gentle-engram` | 0.1.5 | — | — | Engram tools |
| `pi-subagents` | 0.24.2 | 1 (pi-subagents) | 6 (gather-context-and-clarify, parallel-*) | Runtime de subagentes |
| `pi-intercom` | 0.6.0 | 1 (pi-intercom) | — | Intercom broker |
| `pi-mcp-adapter` | 2.5.4 | — | — | MCP adapter |
| `pi-web-access` | latest | — | — | Web search tools |
| `pi-memory-md` | latest | — | — | Memory markdown tools |
| `pi-lens` | latest | — | — | LSP + AST tools |
| `pi-manage-todo-list` | latest | — | — | Todo tool |
| `@devkade/pi-plan` | latest | — | — | Plan tool |
| `@juanibiapina/pi-powerbar` | latest | — | — | Powerbar TUI |
| `@juicesharp/rpiv-todo` | latest | — | — | Todo TUI |
| `@juicesharp/rpiv-ask-user-question` | latest | — | — | Question TUI |
| `@tmustier/pi-ralph-wiggum` | 0.2.1 | 1 (pi-ralph-wiggum) | — | Ralph runtime |
| `@modemdev/glance-pi` | 0.1.0 | — | — | Glance screenshot |
| `pi-extensions` (git) | latest | 1 (extending-pi) | — | 7 extensions (+ 5 arcade disabled) |
| Pi Core | 0.74.0 | — | — | Agent runtime |

---

## Skills de Usuario Locales (no de paquetes)

| Skill | Directorio | Descripción |
|-------|-----------|-------------|
| `change-review` | `~/.agents/skills/` | Revisión de cambios |
| `context7-mcp` | `~/.agents/skills/` | Búsqueda de docs de librerías vía MCP Context7 |
| `go-testing` | `~/.agents/skills/` | Patrones de testing en Go / Bubbletea |
| `improvement-loop` | `~/.agents/skills/` | Loop de mejora iterativa |
| `local-retrospective` | `~/.agents/skills/` | Retrospectiva local de sesión |
| `memory-fallback` | `~/.agents/skills/` | Fallback de memoria |
| `rule-migration` | `~/.agents/skills/` | Migración de reglas |
| `sdd-*` (10 skills) | `~/.agents/skills/` | Flujo Spec-Driven Development |
| `skill-creator` | `~/.agents/skills/` | Creación de skills |
| `skill-registry` | `~/.agents/skills/` | Registro de skills del proyecto |
| `special-instruction` | `~/.agents/skills/` | Guía para crear prompts/skills/agentes |
| `workflow-builder` | `~/.agents/skills/` | Constructor de workflows |