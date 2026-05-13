# Tutorial - Hermes Agent: Slash Commands

> Comandos que se ejecutan dentro de una sesión interactiva de Hermes Agent.
> Algunos comandos son exclusivos del **CLI** o del **Gateway** (plataformas de mensajería).
>
> `*` = comando de uso frecuente entre usuarios.

---

## 1. Control de Sesión

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/new` o `/reset` * | Inicia una sesión completamente nueva | CLI, Gateway | `/new` |
| `/clear` | Limpia la pantalla + nueva sesión (CLI) | CLI | `/clear` |
| `/retry` * | Reenvía el último mensaje al modelo | CLI, Gateway | `/retry` |
| `/undo` * | Elimina el último intercambio de la conversación | CLI, Gateway | `/undo` |
| `/title [nombre]` * | Asigna un nombre a la sesión actual | CLI, Gateway | `/title mi-sesion-api` |
| `/compress` | Comprime manualmente el contexto para ahorrar tokens | CLI, Gateway | `/compress` |
| `/stop` * | Mata procesos en segundo plano | CLI, Gateway | `/stop` |
| `/rollback [N]` | Restaura un checkpoint de sistema de archivos | CLI, Gateway | `/rollback 3` |
| `/snapshot [sub]` | Crea o restaura snapshots del estado/config de Hermes | CLI | `/snapshot before-update` |
| `/background <prompt>` | Ejecuta un prompt en segundo plano | CLI | `/background Revisa logs y reporta errores` |
| `/queue <prompt>` | Encola un prompt para el siguiente turno | CLI | `/queue Despliega el servidor` |
| `/steer <prompt>` | Inyecta un mensaje después del próximo tool call sin interrumpir | CLI | `/steer Cambia a modelo deepseek` |
| `/agents` o `/tasks` | Muestra agentes activos y tareas en ejecución | CLI, Gateway | `/agents` |
| `/resume [nombre]` | Reanuda una sesión guardada por nombre | CLI | `/resume refactor-auth` |
| `/goal [texto\|sub]` * | Establece un objetivo permanente entre turnos (sub: status, pause, resume, clear) | CLI, Gateway | `/goal Terminar la API REST antes de salir` |
| `/redraw` | Fuerza un repintado completo del UI (CLI) | CLI | `/redraw` |

---

## 2. Configuración

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/config` | Muestra la configuración actual | CLI | `/config` |
| `/model [nombre]` * | Muestra o cambia el modelo/proveedor activo | CLI, Gateway | `/model anthropic/claude-sonnet-4` |
| `/personality [nombre]` | Establece una personalidad | CLI, Gateway | `/personality sarcastic` |
| `/reasoning [nivel]` * | Ajusta nivel de reasoning (none, minimal, low, medium, high, xhigh, show, hide) | CLI, Gateway | `/reasoning high` |
| `/verbose` | Cicla entre modos: off → new → all → verbose | CLI | `/verbose` |
| `/voice [on\|off\|tts]` | Controla el modo de voz | CLI, Gateway | `/voice on` |
| `/yolo` * | Activa/desactiva la aprobación de comandos peligrosos | CLI, Gateway | `/yolo` |
| `/busy [sub]` | Controla qué pasa con Enter mientras Hermes trabaja (sub: queue, steer, interrupt, status) | CLI | `/busy queue` |
| `/indicator [estilo]` | Cambia el estilo del indicador de actividad (kaomoji, emoji, unicode, ascii) | CLI | `/indicator kaomoji` |
| `/footer [on\|off]` | Activa/desactiva el footer de metadatos del gateway en respuestas finales | CLI, Gateway | `/footer on` |
| `/skin [nombre]` | Cambia el tema visual (CLI) | CLI | `/skin dracula` |
| `/statusbar` | Activa/desactiva la barra de estado (CLI) | CLI | `/statusbar` |

---

## 3. Tools & Skills

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/tools` | Gestiona herramientas habilitadas/deshabilitadas | CLI | `/tools` |
| `/toolsets` | Lista los toolsets disponibles | CLI | `/toolsets` |
| `/skills` | Busca e instala skills desde el hub | CLI | `/skills` |
| `/skill <nombre>` * | Carga una skill en la sesión actual | CLI, Gateway | `/skill writing-plans` |
| `/reload-skills` | Re-escannea ~/.hermes/skills/ por skills nuevas o eliminadas | CLI, Gateway | `/reload-skills` |
| `/reload` | Recarga las variables de entorno (.env) en la sesión activa | CLI | `/reload` |
| `/reload-mcp` | Recarga los servidores MCP | CLI, Gateway | `/reload-mcp` |
| `/cron` | Gestiona tareas programadas (cron jobs) | CLI | `/cron list` |
| `/curator [sub]` | Mantenimiento de skills (status, run, pin, archive) | CLI, Gateway | `/curator run` |
| `/kanban [sub]` | Tablero de trabajo multi-perfil (tasks, links, comments) | CLI, Gateway | `/kanban ls` |
| `/plugins` | Lista los plugins instalados | CLI | `/plugins` |

---

## 4. Gateway (Plataformas de Mensajería)

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/approve` | Aprueba un comando pendiente | Gateway | `/approve` |
| `/deny` | Rechaza un comando pendiente | Gateway | `/deny` |
| `/restart` * | Reinicia el gateway | Gateway | `/restart` |
| `/sethome` * | Establece el chat actual como canal principal | Gateway | `/sethome` |
| `/update` | Actualiza Hermes a la última versión | Gateway | `/update` |
| `/topic [sub]` | Gestiona sesiones de temas en Telegram DM | Gateway | `/topic new` |
| `/platforms` o `/gateway` | Muestra estado de conexión de las plataformas | Gateway | `/platforms` |

---

## 5. Utilidad

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/branch` o `/fork` | Crea una rama de la sesión actual | CLI, Gateway | `/branch feature-x` |
| `/fast` | Activa/desactiva el modo de procesamiento rápido | CLI, Gateway | `/fast` |
| `/browser` | Abre una conexión de navegador vía CDP | CLI, Gateway | `/browser` |
| `/history` | Muestra el historial de la conversación | CLI | `/history` |
| `/save` | Guarda la conversación a un archivo | CLI | `/save ~/chat-backup.json` |
| `/copy [N]` | Copia la última respuesta al portapapeles | CLI | `/copy 2` |
| `/paste` | Adjunta una imagen desde el portapapeles | CLI | `/paste` |
| `/image` | Adjunta un archivo de imagen local | CLI | `/image captura.png` |

---

## 6. Información

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/help` * | Muestra todos los comandos disponibles | CLI, Gateway | `/help` |
| `/commands [página]` | Navega por todos los comandos (paginado) | Gateway | `/commands 2` |
| `/usage` * | Muestra el uso de tokens de la sesión | CLI, Gateway | `/usage` |
| `/insights [días]` | Estadísticas de uso del agente | CLI, Gateway | `/insights 7` |
| `/gquota` | Muestra la cuota de Google Gemini Code Assist | CLI | `/gquota` |
| `/status` | Información de la sesión | Gateway | `/status` |
| `/profile` | Muestra información del perfil activo | CLI, Gateway | `/profile` |
| `/debug` | Sube un reporte de depuración (system info + logs) y genera enlaces | CLI, Gateway | `/debug` |

---

## 7. Salida

| Comando | Descripción | Disponible en | Ejemplo |
|---------|-------------|---------------|---------|
| `/quit` o `/exit` o `/q` | Sale de la CLI | CLI | `/quit` |

---

> **Nota:** El registro oficial de comandos está en `hermes_cli/commands.py`.
> Para la lista más actualizada en vivo, ejecuta `/help` dentro de cualquier sesión.
>
> Los marcados con `*` son los comandos de uso más frecuente entre usuarios de Hermes.

---

## Casos de Uso Reales (de mayor a menor frecuencia)

| # | Escenario | Quién lo usa | Cómo lo hace con Hermes |
|---|-----------|-------------|--------------------------|
| 1 | **Desarrollar features desde cero** | Dev backend/fullstack | `hermes` → pide toda la feature en lenguaje natural. Hermes crea archivos, corre tests y hace commits. Usa `/goal` para mantener el objetivo a través de múltiples turnos. |
| 2 | **Refactorizar y depurar código** | Dev de cualquier stack | Pega el error o el código problemático. Dice "refactoriza esto para que sea más mantenible" o "encuentra el bug". Usa `/undo` si el resultado no le sirve y `/retry` con instrucciones más específicas. |
| 3 | **Desplegar infraestructura (Docker, CI/CD)** | DevOps / SysAdmin | Pide "crea un Dockerfile con multi-stage build para mi app FastAPI" o "configura GitHub Actions para deploy a Railway". Hermes escribe los archivos y explica los pasos. |
| 4 | **Automatizar tareas repetitivas (scripts, backups)** | SysAdmin / Power user | Pide "haz un script que respalde la BD cada noche y suba el dump a S3". Hermes escribe el script y lo instala como cron job con `/cron create`. |
| 5 | **Investigar tecnologías o resolver dudas técnicas** | Cualquier perfil técnico | Pregunta directamente "¿cómo funciona Tailscale Funnel?" o "compara SQLite vs PostgreSQL para mi proyecto". Hermes busca en web con web_search, lee docs y da una respuesta estructurada con tabla. |
| 6 | **Administrar servidores y contenedores** | SysAdmin / SRE | Abre una sesión y da comandos como "conéctate por SSH, revisa los logs de Nginx, dime qué errores 500 hay" o "limpiar imágenes Docker huerfanas". Usa `/stop` si un proceso se cuelga. |
| 7 | **Crear APIs y microservicios** | Backend Dev | Pide "crea una API REST con FastAPI que tenga CRUD de usuarios con JWT". Hermes genera el proyecto completo con modelos, rutas, tests y docker-compose. |
| 8 | **Revisar PRs y hacer code review** | Tech Lead / Equipo | Usa `hermes skills install github-code-review`, luego pega el diff o la URL del PR. Hermes revisa seguridad, estilo, lógica y da comentarios inline. |
| 9 | **Escribir documentación técnica** | Dev / Technical Writer | Pega el código o la estructura y dice "genera un README profesional" o "documenta esta API con ejemplos". Hermes produce markdown estructurado. |
| 10 | **Automatizar respuestas en Telegram/Discord (Gateway)** | Community Manager / Equipo | Configura el gateway con `hermes gateway setup` y deja a Hermes respondiendo preguntas técnicas en un canal de Discord o Telegram. Usa `/sethome` para fijar el canal principal. |
| 11 | **Hacer análisis de seguridad y hardening** | Ciberseguridad | Pide "analiza este Dockerfile por malas prácticas de seguridad" o "haz hardening de este servidor Linux". Hermes enumera puertos abiertos, permisos incorrectos, secretos expuestos. |
| 12 | **Generar dashboards, infografías y contenido visual** | Creador de contenido / Educador | Usa skills como `architecture-diagram` o `excalidraw` y pide "genera un diagrama de arquitectura de mi sistema". Hermes produce SVG o JSON para Excalidraw. |
| 13 | **Multi-agente: dividir tareas grandes en paralelo** | Tech Lead / Arquitecto | Ejecuta `delegate_task(tasks=[{...}, {...}])` para que dos subagentes trabajen en paralelo: uno el frontend, otro el backend. Reduce horas a minutos. |
| 14 | **Programar reportes diarios/semanales (cron jobs)** | Manager / Freelancer | Configura un cron job con `cronjob(create, schedule="every day 9am", prompt="Resume los cambios del repo en las últimas 24h")`. Hermes entrega el resumen automático cada día. |
| 15 | **Migrar proyectos entre tecnologías** | Dev / Consultor | Pide "migra este proyecto de Express a FastAPI manteniendo la misma API pública". Hermes lee los archivos, traduce ruta por ruta y genera el proyecto nuevo. Usa `/rollback` si algo sale mal. |

---

### Perfiles típicos que más usan Hermes

| Perfil | Prioridad de uso | Lo que más valora |
|--------|-----------------|-------------------|
| **Dev fullstack / backend** | Muy alta | Velocidad para crear features, depuración, refactor |
| **DevOps / SRE** | Alta | Automatización, scripts, Docker, CI/CD, cron jobs |
| **Arquitecto / Tech Lead** | Alta | Multi-agente, code review, documentación, planificación |
| **SysAdmin** | Alta | Administración de servidores, logs, backups, hardening |
| **Ciberseguridad** | Media-alta | Auditoría, hardening, OSINT, análisis de configuraciones |
| **Freelancer / Consultor** | Media | Productividad, reportes automáticos, documentación para clientes |
| **Educador / Creador de contenido** | Media | Diagramas, infografías, automatización de contenido |
| **Community Manager técnico** | Baja-media | Gateway en Discord/Telegram, respuestas automáticas |
| **Data analyst** | Baja | Consultas a BD, generación de reportes, visualización |
| **Estudiante de tecnología** | Baja | Aprendizaje asistido, investigación, práctica con proyectos reales |

---

## 8. Orquestación Multi-Agente: Hermes ↔ Pi

Hermes y Pi pueden integrarse como un **sistema multi-agente** donde cualquiera de los dos actúa como orquestador y delega tareas al otro o a perfiles internos.

### 8.1 Arquitectura General

```
┌─────────────────────────────────────────────────────────┐
│                    ORQUESTADOR                          │
│  (Pi Gentleman o Hermes perfil principal)               │
│                                                         │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐           │
│   │ Perfil 1 │   │ Perfil 2 │   │ Perfil 3 │           │
│   │(Hermes)  │   │(Hermes)  │   │(Hermes)  │           │
│   └──────────┘   └──────────┘   └──────────┘           │
│                                                         │
│   ┌──────────┐                                          │
│   │   Pi     │  (como subagente vía MCP/ACP)            │
│   └──────────┘                                          │
└─────────────────────────────────────────────────────────┘
```

### 8.2 Pi Orquesta a Hermes

Pi (con el Gentleman harness) actúa como orquestador y delega tareas a perfiles de Hermes vía MCP.

**Configuración:**

1. Levantar cada perfil de Hermes como servidor MCP en puertos distintos:
   ```bash
   # Perfil 1
   hermes profile use secopsh4ck
   hermes mcp serve --port 9101 &

   # Perfil 2
   hermes profile use devopsia
   hermes mcp serve --port 9102 &

   # Perfil 3
   hermes profile use mentor_q
   hermes mcp serve --port 9103 &
   ```

2. Conectar Pi a los servidores MCP de Hermes (agregar en `mcp.json` de Pi).

3. Desde Pi, los perfiles de Hermes aparecen como herramientas MCP. El Gentleman delega según especialización:
   - `secopsh4ck` → tareas de seguridad y hardening
   - `devopsia` → infraestructura, CI/CD, Docker
   - `mentor_q` → revisión de código, documentación, mentoring

**Flujo típico:**
```
Usuario → Pi (Gentleman)
              │
              ├─ MCP → Hermes:secopsh4ck  (auditoría de seguridad)
              ├─ MCP → Hermes:devopsia    (Dockerfile + CI/CD)
              └─ MCP → Hermes:mentor_q    (code review + docs)
```

### 8.3 Hermes Orquesta a Pi y Otros Perfiles

El perfil principal de Hermes (ej. `quantum`) actúa como orquestador central.

**Opciones de delegación:**

| Mecanismo | Descripción | Cuándo usarlo |
|-----------|-------------|---------------|
| **Kanban multi-perfil** | Tablero SQLite compartido entre perfiles. Tareas se reclaman atómicamente. | Workflows con dependencias entre tareas |
| **`delegate_task`** | Hermes delega tareas a subagentes en paralelo. | Dividir trabajo grande en partes independientes |
| **MCP (Hermes → Pi)** | Conectar Pi como servidor MCP y delegarle tareas desde Hermes. | Usar capacidades específicas de Pi (SDD, subagentes) |
| **ACP** | Hermes corre como servidor ACP para integración con editores y otros agentes. | Integración con VS Code, Zed, JetBrains |

**Flujo típico (Hermes → perfiles + Pi):**
```
Usuario → Hermes:quantum (orquestador)
              │
              ├─ Kanban → Hermes:secopsh4ck  (pentesting)
              ├─ Kanban → Hermes:devopsia    (infraestructura)
              ├─ Kanban → Hermes:mentor_q    (documentación)
              └─ MCP ──→ Pi                  (SDD: diseño + implementación)
```

**Configurar Kanban multi-perfil:**
```bash
# Inicializar el tablero (una vez)
hermes kanban init

# Crear tablero para el proyecto
hermes kanban boards create mi-proyecto
hermes kanban boards switch mi-proyecto

# Crear tareas asignadas a perfiles específicos
hermes kanban create --title "Auditar seguridad del API" --assignee secopsh4ck
hermes kanban create --title "Configurar Docker multi-stage" --assignee devopsia
hermes kanban create --title "Escribir README y docs" --assignee mentor_q

# Despachar tareas (los perfiles las reclaman y ejecutan)
hermes kanban dispatch
```

### 8.4 Conexión Bidireccional Pi ↔ Hermes

Ambos sistemas pueden coexistir y delegarse mutuamente:

```
         ┌─────────┐         MCP         ┌──────────────┐
         │   Pi    │ ◄──────────────────► │   Hermes     │
         │(Gentle- │                      │  (quantum)   │
         │  man)   │                      │              │
         └────┬────┘                      └──────┬───────┘
              │                                  │
              │ MCP                              │ Kanban
              ▼                                  ▼
    ┌─────────────────┐              ┌───────────────────┐
    │ Hermes profiles │              │  Hermes profiles  │
    │ (como MCP tools)│              │  (kanban workers) │
    └─────────────────┘              └───────────────────┘
```

**Caso de uso real:**
1. El usuario le pide a Pi una feature completa.
2. Pi (Gentleman) ejecuta SDD: proposal → spec → design → tasks.
3. En la fase `apply`, Pi delega:
   - Backend → Hermes:devopsia (FastAPI + Docker)
   - Frontend → Hermes:secopsh4ck (React + revisión de seguridad)
   - Tests → Pi subagente `sdd-apply`
4. En la fase `verify`, Hermes:mentor_q revisa el diff final.
5. Pi recibe los resultados, los sintetiza y reporta al usuario.

### 8.5 Notas sobre Nombres de Perfil

- Los nombres de perfil deben cumplir: `[a-z0-9][a-z0-9_-]{0,63}`
- Solo minúsculas, números, guiones y underscores.
- `@` y otros caracteres especiales **no** están permitidos.
- Alternativas válidas para "quantum": `quantum`, `qu4ntum`, `qu-antum`, `qu_antum`.

```bash
# Renombrar el perfil default
hermes profile rename default quantum
```

### 8.6 Comparativa: Pi vs Hermes como Orquestador

Análisis detallado de cuál sistema conviene como orquestador según la dimensión.

#### Organización

| Dimensión | 🟢 Pi (Gentleman) | 🟠 Hermes (quantum) |
|-----------|-------------------|---------------------|
| **Metodología** | **SDD**: fases estrictas (proposal→spec→design→tasks→apply→verify→archive). Cada fase produce artifacts auditables. | **Kanban**: tablero SQLite multi-perfil. Tareas con dependencias, claims atómicos, workers. Más flexible. |
| **Flujo de trabajo** | Lineal con gates de aprobación. El orquestador pausa entre fases. | Asíncrono y event-driven. Tareas se despachan, perfiles las reclaman cuando están listos. |
| **Delegación** | Jerárquica: parent → scout → worker → reviewer. Un solo hilo de escritura. | Colaborativa: múltiples perfiles reclaman tareas del mismo tablero. Escritura paralela. |
| **Ideal para** | Desarrollo de software con calidad controlada, PRs revisables, TDD estricto. | Automatización general, multi-canal (Telegram/Discord), tareas asíncronas, cron jobs. |

**🏆 Organización:** Pi gana en rigor metodológico para software. Hermes gana en flexibilidad y automatización general.

#### Poder (Capacidades)

| Dimensión | 🟢 Pi (Gentleman) | 🟠 Hermes (quantum) |
|-----------|-------------------|---------------------|
| **Code Intelligence** | LSP nativo (definiciones, referencias, call hierarchy), AST-grep semántico. Profundo. | Depende de skills instaladas. Sin LSP nativo. |
| **Subagentes** | 15+ agentes especializados (scout, worker, reviewer, oracle, planner, SDD phases). Contexto fresh/fork. | `delegate_task` para paralelo. Perfiles como workers vía Kanban. Menos especialización. |
| **SDD** | Ciclo completo: init→explore→proposal→spec→design→tasks→apply→verify→archive. TDD estricto. | No tiene equivalente nativo. Depende de skills externas. |
| **Integraciones** | MCP client, intercom (sesiones Pi), Git, GitHub. Enfocado en desarrollo. | **Masivo**: WhatsApp, Slack, Telegram, Discord, cron, webhooks, MCP server/client, ACP, plugins, skills hub, gateway. |
| **Automatización** | Subagentes bajo demanda. | Cron jobs nativos, gateway always-on, webhooks, daemon dispatcher. |

**🏆 Poder:** Hermes tiene mayor alcance horizontal (múltiples plataformas, automatización). Pi tiene mayor profundidad vertical en desarrollo de software.

#### Control

| Dimensión | 🟢 Pi (Gentleman) | 🟠 Hermes (quantum) |
|-----------|-------------------|---------------------|
| **Safety** | **Muy alto**. Review workload guard (máx ~400 líneas), mandatory delegation triggers, incident rules, fresh-context review obligatorio. | Medio. YOLO mode, hooks. El usuario decide cuánto confiar. |
| **Rollback** | Vía git (commits, branches). No hay checkpoint automático del filesystem. | **Checkpoints nativos** (`/rollback N`, `/snapshot`). Restauración granular del filesystem. |
| **Aprobación** | El orquestador pide confirmación entre fases SDD. No ejecuta sin aprobación en modo interactive. | `/yolo` togglea aprobación de comandos peligrosos. Hooks auto-approve. |
| **Transparencia** | Trazabilidad completa: cada fase produce artifacts, cada subagente reporta. | Logs, event stream (`kanban tail`), session save/export. |
| **Workload** | Una sola escritura a la vez (single-threaded writes). Protege al reviewer humano. | Escritura paralela vía Kanban con perfiles aislados. Mayor riesgo de conflictos. |

**🏆 Control:** Pi gana en seguridad y protección del reviewer. Hermes gana en flexibilidad operativa (checkpoints, rollback, YOLO).

#### Memoria y Aprendizaje

| Dimensión | 🟢 Pi (Gentleman) | 🟠 Hermes (quantum) |
|-----------|-------------------|---------------------|
| **Persistencia** | **Engram**: memoria persistente git-backed. Searchable (tags, full-text). Project + personal scopes. Sesión a sesión. | Checkpoints (snapshots del filesystem). Session save/export. Sin memoria semántica nativa. |
| **Aprendizaje** | Guarda decisiones, bugs, patrones, preferencias del usuario. Evoluciona con el proyecto. | No tiene aprendizaje entre sesiones. Cada perfil es aislado. Depende de `memory` provider externo configurable. |
| **Contexto** | Subagentes reciben `## Project Standards` inyectado por el orquestador. Skill registry. | SOUL.md por perfil, skills cargables, `.env` por perfil. |
| **Sync** | `memory_sync` (pull/push) — colaborativo vía git. | Backup/import de perfiles. No sync colaborativo nativo. |

**🏆 Memoria:** Pi gana por mucho. Engram es memoria semántica real. Hermes solo tiene checkpoints (estado, no conocimiento).

#### Escalabilidad

| Dimensión | 🟢 Pi (Gentleman) | 🟠 Hermes (quantum) |
|-----------|-------------------|---------------------|
| **Horizontal** | Subagentes en paralelo con worktrees aislados. Chained PRs para cambios >400 líneas. Limitado a una máquina. | **Kanban multi-perfil** + gateway always-on + cron jobs autónomos. Los perfiles pueden correr en paralelo real. |
| **Vertical** | SDD chain de 9 fases. Profundidad por especialización de subagentes. | Skills hub comunitario. Plugins. Toolsets. Ecosistema extensible. |
| **Disponibilidad** | Sesión interactiva. Se cierra cuando el usuario sale. | **Gateway always-on** (Telegram/Discord/Slack). Responde 24/7. Cron jobs autónomos. |
| **Aislamiento** | Worktrees git por tarea paralela. Contexto fresh/fork. | Perfiles con directorios y configs completamente aislados. |
| **Límites** | ~15 subagentes. Single-machine. | Perfiles ilimitados. Gateway multi-plataforma. Pero sin SDD ni code intelligence profunda. |

**🏆 Escalabilidad:** Hermes gana en despliegue continuo y automatización. Pi gana en profundidad técnica por tarea.

#### Resumen Visual

```
                    Pi (Gentleman)        Hermes (quantum)
                    ─────────────         ────────────────
Organización        ⭐⭐⭐⭐⭐ SDD rígido    ⭐⭐⭐⭐ Kanban flexible
Poder (dev)         ⭐⭐⭐⭐⭐ LSP+TDD+SDD   ⭐⭐⭐ Vía skills
Poder (gral)        ⭐⭐ Solo dev          ⭐⭐⭐⭐⭐ Multi-plataforma
Control/seguridad   ⭐⭐⭐⭐⭐ Muy alto       ⭐⭐⭐ Medio (YOLO)
Memoria             ⭐⭐⭐⭐⭐ Engram         ⭐⭐ Checkpoints nomás
Escalabilidad       ⭐⭐⭐ Worktrees        ⭐⭐⭐⭐⭐ Gateway+cron+kanban
```

---

### 8.7 Arquitectura Simbiótica: ¿Cuándo Quién Orquesta?

**No es Pi vs Hermes. Es Pi + Hermes en capas complementarias.** Cada uno orquesta en su dominio de excelencia y delega al otro cuando la tarea cruza la frontera.

#### Principio Rector

```
┌─────────────────────────────────────────────────────────────┐
│                  ¿QUÉ TIPO DE TAREA ES?                      │
│                                                              │
│  Desarrollo de software          Tareas generales            │
│  con calidad crítica             y automatización            │
│  ┌──────────────────┐            ┌──────────────────┐        │
│  │  Pi ORQUESTA     │            │  Hermes ORQUESTA │        │
│  │  Hermes es MCP   │            │  Pi es skill/    │        │
│  │  server pasivo   │            │  herramienta     │        │
│  └────────┬─────────┘            └────────┬─────────┘        │
│           │                                │                 │
│           ▼                                ▼                 │
│  ┌────────────────────────────────────────────────────┐      │
│  │              AMBOS COEXISTEN                        │      │
│  │  Hermes → always-on, notificaciones, cron           │      │
│  │  Pi     → code quality, SDD, PR reviews             │      │
│  └────────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

#### Escenarios Concretos

| Escenario | Orquestador | ¿Qué hace Pi? | ¿Qué hace Hermes? |
|-----------|-------------|---------------|-------------------|
| **Feature nueva de software** | **Pi** | SDD completo: proposal→spec→design→tasks→apply→verify. Delega tareas específicas a Hermes vía MCP (ej. crear Dockerfile, revisar seguridad). | Recibe tareas concretas de Pi vía MCP y las ejecuta con sus perfiles especializados. |
| **Code review de un PR** | **Pi** | Scout analiza el diff, reviewer audita, comment-writer redacta feedback. | Puede notificar por Telegram/Discord que el review está listo. |
| **Monitoreo 24/7 + alertas** | **Hermes** | No participa directamente. | Cron jobs revisan logs, gateway notifica por Telegram si hay errores. |
| **Automatización de deploy** | **Hermes** | No participa directamente. | Perfil `devopsia` ejecuta CI/CD vía cron o webhook. |
| **Auditoría de seguridad** | **Pi** orquesta la fase de análisis | SDD spec + design para los hallazgos. Subagente reviewer especializado. | Perfil `secopsh4ck` ejecuta scanners y pentesting como herramienta MCP de Pi. |
| **Documentación de proyecto** | **Pi** | Genera docs técnicas con cognitive-doc-design. | Perfil `mentor_q` formatea, traduce y publica. Notifica por gateway. |
| **Respuestas automáticas en Telegram** | **Hermes** | No participa directamente. | Gateway always-on responde consultas técnicas en el canal. |
| **Investigación técnica** | **Pi** | Researcher + librarian buscan y analizan código fuente. | Puede aportar web_search y resúmenes vía MCP. |

#### Regla de Decisión Simplificada

```
¿La tarea involucra escribir/refactorizar/revisar código?
  ├─ SÍ → Pi ORQUESTA, Hermes como herramienta
  └─ NO  → Hermes ORQUESTA, Pi como herramienta (si necesita código)

¿La tarea necesita correr 24/7 o en horarios específicos?
  ├─ SÍ → Hermes (cron + gateway)
  └─ NO  → Pi (sesiones interactivas)

¿La tarea requiere memoria y aprendizaje entre sesiones?
  ├─ SÍ → Pi (Engram)
  └─ NO  → Hermes (más simple, sin overhead)
```

#### Stack Tecnológico Recomendado

```yaml
Capa 1 - Always-On:
  herramienta: Hermes (quantum)
  rol: Gateway multi-plataforma, cron jobs, notificaciones
  perfiles: devopsia, secopsh4ck, mentor_q
  integración: MCP serve exponiendo herramientas a Pi

Capa 2 - Calidad de Software:
  herramienta: Pi (Gentleman)
  rol: SDD, code review, TDD, documentación técnica
  subagentes: scout, worker, reviewer, oracle, sdd-*
  integración: MCP client consumiendo herramientas de Hermes

Capa 3 - Memoria:
  herramienta: Engram (vía Pi)
  rol: Persistencia de decisiones, bugs, patrones, preferencias
  sync: Git-based, colaborativo entre sesiones
```

---

### 8.8 Perfiles de Hermes como Agentes/Skills en Pi (y viceversa)

#### ¿Pueden `devopsia`, `secopsh4ck`, `mentor_q` ser agentes en Pi?

**Sí, de dos formas:**

##### A. Como Subagentes Personalizados en Pi

Crear agentes en Pi que emulen la especialización de los perfiles de Hermes:

```bash
# En Pi: crear agente devopsia
subagent create \
  --name devopsia \
  --package custom \
  --description "Especialista en DevOps: Docker, CI/CD, infraestructura como código" \
  --systemPrompt "Sos un ingeniero DevOps experto. Tu rol es crear Dockerfiles,
docker-compose, pipelines CI/CD, configuraciones de infraestructura,
y scripts de deploy. Siempre seguís buenas prácticas de seguridad
y generás configuraciones listas para producción."

# En Pi: crear agente secopsh4ck
subagent create \
  --name secopsh4ck \
  --package custom \
  --description "Especialista en ciberseguridad ofensiva y defensiva" \
  --systemPrompt "Sos un especialista en ciberseguridad. Tu rol es auditar
código y configuraciones en busca de vulnerabilidades, hacer hardening
de sistemas, revisar secretos expuestos, y sugerir mejoras de seguridad."

# En Pi: crear agente mentor_q
subagent create \
  --name mentor-q \
  --package custom \
  --description "Mentor técnico: code review, documentación, mejores prácticas" \
  --systemPrompt "Sos un mentor técnico experimentado. Tu rol es revisar código,
escribir documentación clara, sugerir mejoras de arquitectura,
y enseñar buenas prácticas. Sos constructivo y didáctico."
```

##### B. Como Skills en Pi

Cada especialidad también puede ser una skill:

```
.pi/skills/devopsia/SKILL.md
.pi/skills/secopsh4ck/SKILL.md
.pi/skills/mentor-q/SKILL.md
```

Las skills en Pi son archivos markdown con instrucciones, scripts y referencias. Se cargan bajo demanda con `/skill`.

#### Tabla de Equivalencias Pi ↔ Hermes

| Concepto Hermes | Equivalente en Pi | Notas |
|-----------------|-------------------|-------|
| **Perfil** (`hermes profile`) | **Subagente** (`subagent create`) | En Pi, cada agente tiene systemPrompt, herramientas y modelo independiente. |
| **SOUL.md** | **systemPrompt + context files** | En Pi no hay un archivo único "SOUL.md". La personalidad se define en el systemPrompt del agente y en `prompt templates` o `context files`. |
| **Skills** (`hermes skills install`) | **Skills** (`.pi/skills/` o `SKILL.md`) | Ambos usan skills. Hermes tiene un hub comunitario; Pi las carga del filesystem local o repos. |
| **Kanban** | **SDD tasks + todo** | Kanban es más flexible y multi-perfil. SDD tasks son específicas para software con fases. |
| **Gateway** | No tiene equivalente directo | Pi es interactivo, no always-on. Para mensajería, se usa Hermes. |
| **Cron jobs** | No tiene equivalente directo | Se puede emular con scripts externos que invoquen Pi. |
| **Checkpoints** | **Git + tape anchors** | Git para código, `tape` para checkpoints de sesión. |
| **`.env`** | **`.env` + `openspec/config.yaml`** | Configuración de entorno y del proyecto. |

#### ¿Hay algo similar a SOUL.md en Pi?

**No hay un archivo único "SOUL.md", pero hay 3 mecanismos equivalentes:**

| Mecanismo | Descripción | Archivo |
|-----------|-------------|--------|
| **System Prompt del agente** | Define personalidad, rol y comportamiento base. | Se pasa en `subagent create --systemPrompt`. Para la sesión principal, se configura en Pi. |
| **Prompt Templates** | Plantillas reutilizables que definen cómo Pi responde en ciertos contextos. | `.pi/prompts/` o configuración de templates. |
| **Context Files** | Archivos de contexto inyectados automáticamente en cada sesión (reglas, estándares, preferencias). | `.pi/context/` o configuración del proyecto. |

**Ejemplo de "SOUL" para un agente Pi:**

```markdown
# SOUL (systemPrompt) para agente secopsh4ck en Pi

Sos secopsh4ck, un especialista en ciberseguridad con 15 años de experiencia.

## Personalidad
- Directo y sin rodeos cuando hay vulnerabilidades críticas.
- Didáctico: explicás el porqué de cada hallazgo.
- Paranoico saludable: siempre asumís que hay un vector de ataque.

## Principios
1. No confiés en input del usuario sin validar.
2. Siempre chequiá secretos expuestos (API keys, tokens, passwords).
3. Preferí denegar por defecto (default-deny en firewalls y permisos).
4. Documentá cada vulnerabilidad con severidad, impacto y remediación.
5. Verificá con evidencia, no asumas.

## Estilo
- Reportes en formato: [CRÍTICO/ALTO/MEDIO/BAJO] Título → Descripción → Impacto → Fix.
- Código de ejemplo para cada fix.
- Checklists de hardening al final de cada auditoría.
```

Este mismo enfoque aplica para `devopsia` y `mentor_q`, cada uno con su personalidad, principios y estilo propios.

---

### 8.9 Workflow Híbrido Completo (Ejemplo Real)

```
08:00  Hermes:quantum (cron) → Revisa logs de producción, notifica por Telegram.
09:00  Usuario abre Pi → "Quiero agregar autenticación 2FA al API"
09:05  Pi (Gentleman) → SDD:proposal (define alcance: TOTP + recovery codes)
09:15  Pi → SDD:spec (requisitos funcionales y no funcionales)
09:30  Pi → SDD:design (arquitectura: middleware FastAPI + Redis para rate limiting)
09:45  Pi → SDD:tasks (5 tareas, ~350 líneas estimadas)

10:00  Pi → SDD:apply (implementación con TDD)
         │
         ├─ Pi:worker → Implementa modelos y lógica TOTP
         ├─ MCP → Hermes:devopsia → Actualiza Dockerfile para Redis
         ├─ MCP → Hermes:secopsh4ck → Audita el código de auth
         └─ Pi:sdd-apply → Corre tests (RED → GREEN → REFACTOR)

11:00  Pi → SDD:verify
         │
         ├─ Pi:reviewer → Revisa el diff completo (~320 líneas)
         └─ MCP → Hermes:mentor_q → Revisa documentación de la API

11:30  Pi → Reporta al usuario: "2FA implementado, tested, revisado. ¿Mergeo?"
11:35  Usuario aprueba → Pi hace commit + push
11:36  Hermes:quantum (gateway) → Notifica por Telegram: "2FA deployed ✓"

14:00  Hermes:quantum (cron) → Corre tests de integración, reporta OK.
```

---

### 8.10 Gateway de Mensajería: ¿Qué Plataforma Elegir?

Hermes soporta **17+ plataformas** de mensajería vía gateway. Acá las 5 mejores ordenadas por **facilidad + seguridad**:

#### Comparativa Rápida

| # | Plataforma | Facilidad | Seguridad | Requisito principal | Ideal para |
|---|-----------|-----------|-----------|-------------------|------------|
| 1 | **Telegram** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Token de @BotFather | Uso personal, notificaciones, comandos |
| 2 | **Discord** | ⭐⭐⭐⭐ | ⭐⭐⭐ | Bot token + server | Comunidades, equipos de desarrollo |
| 3 | **Matrix** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Homeserver propio (Opcional E2EE) | Privacidad máxima, self-hosting |
| 4 | **Signal** | ⭐⭐ | ⭐⭐⭐⭐⭐ | signal-cli daemon | Comunicaciones ultra-seguras |
| 5 | **WhatsApp** | ⭐⭐ | ⭐⭐⭐ | QR pairing + número de teléfono | Alcance masivo, clientes |

---

#### 1. Telegram 🥇 (Recomendado para empezar)

**La más fácil de todas. 5 minutos para tenerla andando.**

```bash
# 1. Crear el bot con @BotFather en Telegram
# 2. Configurar en Hermes
hermes gateway setup
# Elegir Telegram, pegar el token

# 3. Iniciar el gateway
hermes gateway start
```

| Aspecto | Detalle |
|---------|--------|
| **Setup** | Solo necesitás un token de BotFather. Sin infraestructura extra. |
| **Seguridad** | Bots NO tienen E2E encryption. Los mensajes pasan por servidores de Telegram. Usar allowlist (`TELEGRAM_ALLOWED_USERS`). |
| **Features** | Mensajes, imágenes, documentos, voice notes, typing indicators, comandos inline. |
| **Contras** | Sin E2E. Dependencia de servidores de Telegram. |
| **Costo** | Gratis. |

**Variables de entorno:**
```bash
TELEGRAM_BOT_TOKEN=123456:ABC-DEF
TELEGRAM_ALLOWED_USERS=123456789
TELEGRAM_HOME_CHANNEL=123456789
```

---

#### 2. Discord 🥈

**Excelente para equipos de desarrollo. Comunidades, canales, roles.**

| Aspecto | Detalle |
|---------|--------|
| **Setup** | Bot token + habilitar Privileged Gateway Intents + invitar bot al server. ~10 min. |
| **Seguridad** | Sin E2E. Allowlist por user ID. |
| **Features** | Slash commands nativos, canales, hilos, rich embeds, attachments. |
| **Contras** | Requiere server configurado. No es para uso personal simple. |
| **Costo** | Gratis. |

---

#### 3. Matrix 🥉 (Mejor balance seguridad/facilidad)

**Protocolo federado open-source. Con E2E encryption opcional.**

| Aspecto | Detalle |
|---------|--------|
| **Setup** | Necesitás un homeserver (propio o matrix.org). Access token o user/password. |
| **Seguridad** | E2E encryption con `MATRIX_ENCRYPTION=true`. Self-hosted = control total. |
| **Features** | Mensajes, imágenes, archivos, bridging a otras plataformas. |
| **Contras** | Setup más complejo que Telegram. Homeserver requiere mantenimiento. |
| **Costo** | Gratis (matrix.org) o costo de VPS si self-hosted. |

---

#### 4. Signal 🔐 (Máxima seguridad, setup complejo)

**E2E encryption por defecto. Requiere infraestructura adicional.**

| Aspecto | Detalle |
|---------|--------|
| **Setup** | Requiere `signal-cli` como daemon HTTP. Instalación + linkeo de cuenta + daemon corriendo. |
| **Seguridad** | ⭐⭐⭐⭐⭐ E2E por defecto. Señal más segura del mercado para mensajería. |
| **Features** | Mensajes, typing indicators, attachments. |
| **Contras** | Setup complejo. Daemon debe correr 24/7. Límites de rate en grupos. |
| **Costo** | Gratis (señal) + costo de mantener el daemon corriendo. |

**Requisitos:**
```bash
# Instalar signal-cli
# Linux: descargar de https://github.com/AsamK/signal-cli/releases
# macOS: brew install signal-cli
# Docker: bbernhard/signal-cli-rest-api

# Linkear cuenta
signal-cli link -n "HermesAgent"

# Iniciar daemon
signal-cli --account +TUNUMERO daemon --http 127.0.0.1:8080
```

**Variables de entorno:**
```bash
SIGNAL_HTTP_URL=http://127.0.0.1:8080
SIGNAL_ACCOUNT=+1234567890
SIGNAL_ALLOWED_USERS=+1234567890
```

---

#### 5. WhatsApp 📲 (Alcance masivo, restricciones de Meta)

**La usan todos, pero Meta impone restricciones fuertes.**

| Aspecto | Detalle |
|---------|--------|
| **Setup** | QR pairing desde la app de Hermes. Necesitás un número de teléfono. |
| **Seguridad** | E2E en teoría, pero el bot actúa como cliente no oficial (riesgo de ban). |
| **Features** | Mensajes, imágenes, documentos. Sesiones de 24h. |
| **Contras** | **Riesgo de ban** por usar cliente no oficial. Ventana de 24h para responder. Setup frágil. |
| **Costo** | Gratis, pero con riesgo. |

---

#### Recomendación por Caso de Uso

| Caso de uso | Mejor opción | ¿Por qué? |
|-------------|-------------|-----------|
| **Empezar ya, probar el sistema** | Telegram | 5 minutos, sin infraestructura |
| **Equipo de desarrollo** | Discord | Canales, roles, comandos nativos |
| **Máxima privacidad** | Signal | E2E, código abierto |
| **Self-hosting + privacidad** | Matrix | Federado, E2E opcional, control total |
| **Hablar con clientes/familia** | WhatsApp (con cuidado) | Todos lo tienen, pero riesgoso |
| **Notificaciones 24/7** | Telegram + cron | Lo más simple para alertas automáticas |

#### Configurar Múltiples Plataformas

Hermes soporta todas simultáneamente:

```bash
# Configurar varias plataformas
hermes gateway setup   # Menú interactivo, elegir todas las que quieras

# Ver estado
hermes gateway status

# Iniciar todo
hermes gateway start
```

El gateway enruta automáticamente cada mensaje según la plataforma de origen, manteniendo sesiones separadas por chat.

#### Arquitectura del Gateway

```
                   ┌──────────────────┐
                   │  Hermes Gateway  │
                   │   (always-on)    │
                   └────────┬─────────┘
                            │
        ┌────────┬──────────┼──────────┬────────┐
        ▼        ▼          ▼          ▼        ▼
    Telegram  Discord    Matrix    Signal   WhatsApp
        │        │          │          │        │
        └────────┴──────────┴──────────┴────────┘
                            │
                    ┌───────▼────────┐
                    │  Hermes Core   │
                    │  (quantum)     │
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  Pi (Gentleman)│
                    │  vía MCP       │
                    └────────────────┘
```
