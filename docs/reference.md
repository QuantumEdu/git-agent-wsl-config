# Pi Agent — Referencia de Skills, Prompts y Extensiones

## Skills

### ast-grep
Búsqueda y reemplazo de código **semántico** (entiende estructura AST, no solo texto).
Usalo en vez de grep cuando buscás funciones, imports, llamadas a métodos, clases.
Si falla 2 veces, caé a grep común. Soporta patrones compuestos (inside/has) y metavariables.

**Tools:** `ast_grep_search`, `ast_grep_replace`

---

### branch-pr
Crea PRs con disciplina Gentle AI: verifica que haya issue aprobado (`status:approved`),
usa conventional commits, asigna un solo `type:*` label, corre shellcheck, y usa el
template de PR. El PR **no pasa** sin issue linkage.

**Reglas clave:**
- Branch naming: `^(feat|fix|chore|docs|...)/[a-z0-9._-]+$`
- Commit: `type(scope): description`
- PR body debe linkear issue con `Closes #N`

---

### chained-pr
Divide PRs que superan **400 líneas** cambiadas en PRs encadenados (stacked PRs a main
o feature branch chain con tracker). Cada slice debe ser revisable en ≤60 min.
Protege al reviewer del burnout.

**Decision gates:**
- ≤400 líneas → single PR
- \>400, slices independientes → Stacked PRs
- \>400, feature integrada → Feature Branch Chain

---

### cognitive-doc-design
Diseñá documentación que reduce la carga cognitiva. Patrones: lead with the answer,
progressive disclosure, chunking, signposting, recognition over recall, review empathy.
Ideal para READMEs, RFCs, guías de onboarding, arquitectura, PR descriptions.

---

### comment-writer
Escribí comentarios cálidos, directos y colaborativos. Fórmula:
observación directa → por qué importa → próxima acción concreta.
En español, voseo rioplatense (`podés`, `tenés`, `fijate`, `dale`).
Para PR feedback, issues, Slack, Discord.

---

### deploy-staging
Flujo de deploy con Docker Compose:
1. Verificar entorno (`docker compose ps`)
2. Build sin cache (`docker compose build --no-cache`)
3. Levantar (`docker compose up -d`)
4. Verificar logs y health check

---

### extending-pi
Guía para extender Pi: te ayuda a decidir entre **Skill**, **Extension**,
**Prompt Template**, **Theme**, **Context File** o **Custom Model**.
Incluye scaffolding mínimo, validación y publicación como paquete.

| Goal | Build a… |
|------|----------|
| Enseñar workflow/API/CLI | Skill |
| Nuevo tool/command/runtime | Extension |
| Reutilizar prompt con variables | Prompt Template |
| Guidelines de proyecto | Context File (`AGENTS.md`) |
| Apariencia visual | Theme |
| Modelo/provider nuevo | Custom Model |

---

### gentle-ai
El harness principal de el Gentleman. Disciplina SDD/OpenSpec, TDD estricto,
delegación a subagentes, reglas de triggers obligatorios:
- **4-file rule**: leer 4+ archivos → delegar exploración
- **Multi-file write rule**: tocar 2+ archivos → usar worker + fresh review
- **PR rule**: antes de commit/PR → fresh review
- **Incident rule**: después de errores de tooling/worktree → fresh audit
- **Long-session rule**: acumulación de complejidad → delegar

---

### issue-creation
Creá issues de GitHub con templates (bug report o feature request).
Todo issue arranca con `status:needs-review`; un maintainer debe poner
`status:approved` antes de que se pueda abrir un PR. Las preguntas van a
Discussions, no a issues.

---

### judgment-day
Revisión adversarial ciega: lanza **dos jueces en paralelo** que revisan el
mismo target sin verse entre sí. Clasifica hallazgos en categorías:
- **Confirmed**: ambos jueces coinciden
- **Suspect**: solo uno lo encuentra
- **Contradiction**: veredictos opuestos
- **INFO**: warnings teóricos o sugerencias

Terminal states: `JUDGMENT: APPROVED ✅` o `JUDGMENT: ESCALATED ⚠️`

---

### librarian
Investigación de librerías open-source con **evidencia y permalinks a GitHub**.
Clona repos, hace grep/blame/log, y construye links con SHA exacto a líneas
de código. Clasifica requests en: conceptual, implementación, contexto/historia,
o comprensivo. Cada claim debe tener permalink.

---

### lsp-navigation
Navegación de código con LSP. Es el **PRIMARY** para code intelligence.
Usalo antes que grep/ast-grep para entender código.

| Pregunta | Operación |
|----------|-----------|
| "¿Dónde se define?" | `definition` |
| "¿Quién lo usa?" | `references` |
| "¿Qué tipo es?" | `hover` |
| "¿Quién llama a esto?" | `prepareCallHierarchy` → `incomingCalls` |
| "¿Qué llama esto?" | `prepareCallHierarchy` → `outgoingCalls` |
| "¿Quién implementa esta interfaz?" | `implementation` |
| "Renombrar símbolo" | `rename` |
| "Símbolos en archivo" | `documentSymbol` |
| "Buscar símbolo en proyecto" | `workspaceSymbol` |

---

### memory-import
Importa conocimiento durable desde URLs, carpetas o archivos a `pi-memory-md`.
Analiza primero, pregunta foco, y genera memorias con el skill `memory-write`.
No importa: boilerplate, marketing copy, secrets, logs, o archivos fuente completos.

---

### memory-init
Inicializa el repositorio de memoria: clona el repo git, crea estructura de
directorios (`core/project/`), copia templates (`USER.md`, `TASK.md`), e
importa preferencias desde `AGENTS.md`.

---

### memory-write
Crea o actualiza archivos de memoria `pi-memory-md` con frontmatter YAML
(description, tags, created, updated). Usa el script `memory-write.sh` para
resolver paths y templates.

---

### pi-intercom
Coordinación entre sesiones de Pi en la misma máquina. Mensajería 1:1:
- `send`: fire-and-forget
- `ask`: bloqueante hasta respuesta (timeout 10 min)
- `reply`: responde al ask activo
- `list`: sesiones conectadas con estado
- `pending`: asks sin resolver

Patrones: planner-worker, pair debugging, broadcast, subagent escalations.

---

### pi-ralph-wiggum
Loops de desarrollo iterativos largos con checkpoints.
Usá `ralph_start` para comenzar, `ralph_done` para avanzar cada iteración.
Ideal para tareas con muchos pasos discretos. No para one-shots.

---

### pi-subagents
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

### skill-creator
Creá o actualizá skills de Pi. Estructura recomendada:
```
mi-skill/
├── SKILL.md         # Frontmatter YAML + cuerpo markdown
├── README.md        # Opcional: resumen humano + instalación
├── scripts/         # Opcional: ejecutables
├── references/      # Opcional: docs largos cargados on-demand
└── assets/          # Opcional: templates/boilerplate
```

Reglas: nombre 1-64 chars, lowercase letters/digits/hyphens. Directorio = `name`.

---

### work-unit-commits
Planeá commits como unidades de trabajo revisables. Cada commit debe:
- Tener un propósito claro
- Incluir tests con el código que verifican
- Ser candidate a PR independiente
- Contar una historia que el reviewer entienda

**No hagas commits por tipo de archivo** (`add models`, `add services`, `add tests`).
Hacé commits por comportamiento: `feat(auth): add token validation domain model and tests`.

---

## Prompts (Shortcuts)

### /gather-context-and-clarify
Lanza `scout` + `researcher` (si hace falta), sintetiza hallazgos, y usa
`interview` para hacer preguntas clarificadoras antes de planear o implementar.

### /gcl — Audit Changelog
Audita changelogs antes de release. Revisa todos los commits desde el último
tag, verifica que cada paquete afectado tenga entrada en CHANGELOG.md, y
chequea duplicación cross-package.

### /gis — GitHub Issue Solve
Analiza GitHub issues (bugs o feature requests). Pone label `inprogress`, lee
todo, traza código, encuentra root cause real (no confía en análisis previos),
propone fix. **No implementa**, solo analiza y propone.

### /gpr — GitHub PR Review
Revisa PRs desde URLs. Pone `inprogress`, lee todo (descripción, comments,
commits, diff), identifica issues linkeados, revisa changelog, y devuelve
structured review en formato **Good / Bad / Ugly**.

### /gwr — Git Wrap
"Wrap it" — finaliza la tarea end-to-end: actualiza changelog, postea comment
final (si es GitHub), commitea solo archivos cambiados en la sesión, y pushea
(solo desde `main`).

### /parallel-cleanup
Lanza 2 reviewers fresh-context en paralelo: uno para "deslop" (eliminar
AI-slop, redundancia) y otro para "verbosity" (simplificar). Review-only;
el padre decide qué aplicar. `autofix` aplica fixes automáticamente.

### /parallel-context-build
Corre 2-3 `context-builder` agents en chain-parallel mode con distintos
ángulos (request/scope, codebase/patterns, validation/risks). Cada uno genera
un archivo + meta-prompt. El padre sintetiza todo.

### /parallel-handoff-plan
Combina `researcher` (evidencia externa) + `context-builder` (código local)
+ `context-builder` (estrategia) en chain-parallel, y luego un `context-builder`
de síntesis que escribe un handoff plan final con meta-prompt listo para
implementar.

### /parallel-research
Combina `researcher` (docs oficiales, specs, benchmarks) con `scout` (repo
local, patrones, constraints). Para preguntas que necesitan tanto evidencia
externa como implicaciones locales.

### /parallel-review
Lanza 2-3 `reviewer` agents fresh-context en paralelo con ángulos distintos
(correctness/regressions, tests/validation, simplicity/maintainability).
Sintetiza hallazgos antes de aplicar fixes. `autofix` aplica automáticamente.

---

## Extensiones

### Core del Sistema

| Extensión | Descripción |
|-----------|-------------|
| `gentle-pi:gentle-ai.ts` | Core de el Gentleman: system prompt, reglas de delegación, SDD workflow |
| `gentle-pi:sdd-init.ts` | Inicialización de artefactos SDD (`.pi/agents/sdd-*.md`, `.pi/chains/sdd-*.chain.md`) |
| `gentle-pi:skill-registry.ts` | Registro de skills del proyecto (`.atl/skill-registry.md`) |
| `gentle-pi:startup-banner.ts` | Banner de inicio con estado de el Gentleman al arrancar sesión |

### Subagentes y Coordinación

| Extensión | Descripción |
|-----------|-------------|
| `pi-subagents:src/extension` | Runtime de subagentes: single, chain, parallel, async, forked-context |
| `pi-intercom` | Mensajería entre sesiones Pi en la misma máquina |

### Memoria

| Extensión | Descripción |
|-----------|-------------|
| `gentle-engram` | Memoria persistente Engram: `mem_save`, `mem_search`, `mem_context`, `mem_session_summary` |
| `pi-memory-md` | Memoria en archivos markdown: `memory_write`, `memory_search`, `memory_check`, `memory_sync` |

### Navegación y Búsqueda

| Extensión | Descripción |
|-----------|-------------|
| `pi-lens` | Análisis estático: `ast_grep_search`, `ast_grep_replace`, `lsp_navigation` |
| `pi-web-access` | Acceso web: `web_search`, `code_search`, `fetch_content`, `get_search_content` |

### TUI y UI

| Extensión | Descripción |
|-----------|-------------|
| `@juanibiapina/pi-powerbar:dist/powerbar` | Barra de estado en TUI (modelo, git, tokens, subagentes, etc.) |
| `...powerbar-context` | Submódulo: contexto actual (archivo, rama) |
| `...powerbar-git` | Submódulo: estado de git |
| `...powerbar-model` | Submódulo: modelo activo |
| `...powerbar-provider` | Submódulo: provider activo |
| `...powerbar-sub` | Submódulo: estado de subagentes |
| `...powerbar-tokens` | Submódulo: conteo de tokens |
| `tmustier/pi-extensions:agent-guidance` | Guía contextual para agentes según modo |
| `tmustier/pi-extensions:code-actions` | Acciones de código en TUI (refactors, quick fixes) |
| `tmustier/pi-extensions:files-widget` | Widget de archivos modificados |
| `tmustier/pi-extensions:raw-paste` | Pegado raw de texto (sin procesar markdown) |
| `tmustier/pi-extensions:tab-status` | Estado visual de tabs/pestañas |
| `tmustier/pi-extensions:session-recap` | Recapitulación de sesión al cerrar |
| `tmustier/pi-extensions:usage-extension` | Monitoreo de uso (tokens, tiempo, costos) |

### Herramientas deUsuario

| Extensión | Descripción |
|-----------|-------------|
| `@juicesharp/rpiv-ask-user-question` | Cuestionarios estructurados en TUI |
| `@juicesharp/rpiv-todo` | Gestión de tareas con estados (pending → in_progress → completed) |
| `pi-manage-todo-list:src` | Gestión de listas de tareas (implementación legacy) |

### Planificación y Loops

| Extensión | Descripción |
|-----------|-------------|
| `@devkade/pi-plan:src` | Planificación estructurada de tareas |
| `tmustier/pi-extensions:pi-ralph-wiggum` | Runtime de Ralph Wiggum: loops iterativos con `ralph_start`/`ralph_done` |

### Integración

| Extensión | Descripción |
|-----------|-------------|
| `pi-mcp-adapter@2.5.4` | Adaptador MCP — conecta Pi con servidores MCP externos |
| `@marckrenn/pi-sub-core` | Core de subagentes alternativo (dependencia de powerbar) |
