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
