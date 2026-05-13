# 🐍 Instalación y Securización de Hermes Agent en WSL

> **Hermes Agent** es un agente AI autónomo open-source de Nous Research.
> Se auto-mejora: aprende de experiencia, crea skills solo, recuerda entre sesiones.
> Corre en Linux, macOS, WSL2, Termux, y Windows (beta).

---

## 📋 Índice

1. [Arquitectura de Agentes en Hermes](#1-arquitectura-de-agentes-en-hermes)
2. [Instalación en WSL](#2-instalación-en-wsl)
3. [Uso Solo Local (Sin Gateway)](#3-uso-solo-local-sin-gateway)
4. [Securización](#4-securización)
5. [Backend Aislado (Docker)](#5-backend-aislado-docker)
6. [Crear Múltiples Agentes (Perfiles)](#6-crear-múltiples-agentes-perfiles)
7. [Mantenimiento](#7-mantenimiento)

---

## 1. Arquitectura de Agentes en Hermes

Hermes tiene **dos conceptos distintos** de "múltiples agentes". Es clave entenderlos:

### A. Subagentes (delegate_task) — efímeros, spawned bajo demanda

```
hermes (padre)
  ├── "Analizame este repo" → subagente 1 (terminal aislado, sin memoria)
  ├── "Buscame vulnerabilidades" → subagente 2 (en paralelo)
  └── "Escribime tests" → subagente 3
```

- Se crean **durante una conversación** con la herramienta `delegate_task`
- Cada uno tiene su propia terminal aislada y contexto fresco
- **No tienen memoria persistente propia** (no pueden escribir a MEMORY.md)
- El padre solo ve el resultado final (no los pasos intermedios)
- Útiles para trabajo paralelo en una misma tarea

### B. Perfiles (hermes profile) — agentes independientes y persistentes

```
~/.hermes/                  ← perfil "default" (asistente general)
~/.hermes/profiles/finanzas/ ← perfil "finanzas" (agente especializado)
  ├── config.yaml           ← su propio modelo, herramientas
  ├── SOUL.md               ← su propia personalidad
  ├── .env                  ← sus propias credenciales
  ├── memories/MEMORY.md    ← su propia memoria persistente
  ├── memories/USER.md      ← su propio modelo de usuario
  ├── skills/               ← sus propias skills
  ├── sessions/             ← sus propias conversaciones
  ├── cron/                 ← sus propias automatizaciones
  └── gateway/              ← su propio gateway (opcional)
```

**Esto es a lo que se refería el desarrollador.** Cuando un agente "ya se volvió muy robusto en finanzas", creás un **perfil** separado con:

```bash
# Crear un perfil nuevo especializado en finanzas
hermes profile create finanzas

# Clonar todo lo que ya aprendió el default al nuevo perfil
hermes profile create finanzas --clone-all

# Usar el perfil finanzas
hermes -p finanzas
```

Cada perfil es **completamente independiente**:

- ✅ Su propia memoria (lo que aprende en finanzas no contamina al default)
- ✅ Su propio modelo (podés usar GPT-4o para código y Claude para finanzas)
- ✅ Su propia personalidad (SOUL.md distinto)
- ✅ Sus propias skills (skills financieras instaladas solo en ese perfil)
- ✅ Su propio cron (reportes financieros automáticos)
- ❌ No es otra instalación — es el mismo `hermes` con distinto `HERMES_HOME`

---

## 2. Instalación en WSL

### 2.1 Requisitos previos

```bash
# Verificar que es WSL2 (no WSL1)
wsl --list --verbose    # Desde PowerShell de Windows

# Entrar a WSL
wsl

# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar solo lo mínimo (Hermes instala el resto automáticamente)
sudo apt install -y curl git build-essential
```

### 2.2 Instalación (un solo comando)

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**Qué hace este script:**

- Instala `uv` (gestor de paquetes Python ultrarrápido)
- Instala Python 3.11
- Clona el repo en `~/.hermes/repo`
- Instala dependencias Python
- Crea binario `hermes` en el PATH
- No requiere sudo

```bash
# Recargar el shell
source ~/.bashrc   # o: source ~/.zshrc
```

### 2.3 Configuración inicial

```bash
# Wizard interactivo
hermes setup
```

Te pregunta:

1. **Proveedor LLM:** Nous Portal (OAuth), OpenRouter (API key), OpenAI, custom endpoint
2. **Modelo:** Seleccionar (ej: `openai/gpt-4o`, `anthropic/claude-sonnet-4`)
3. **API Key:** Si usás OpenRouter/OpenAI
4. **Herramientas:** Cuáles habilitar

```bash
# Cambiar de modelo después
hermes model

# Ver/editar config
cat ~/.hermes/config.yaml
```

### 2.4 Primera conversación

```bash
hermes

# Comandos útiles dentro de la TUI:
#   /model          → cambiar modelo
#   /new            → conversación nueva
#   /tools          → ver herramientas disponibles
#   /skills         → ver skills instaladas
#   /compress       → comprimir contexto
#   Ctrl+C          → interrumpir
```

---

## 3. Uso Solo Local (Sin Gateway)

Para arrancar sin exponer nada a internet ni conectar mensajería:

```bash
# Solo TUI local (sin gateway, sin Telegram, sin nada externo)
hermes

# Con herramientas mínimas (solo filesystem y terminal):
hermes tools
# Desmarcar: browser, discord, email, etc.
# Dejar solo: read_file, write_file, terminal, web_search (opcional)

# Configurar herramientas desde config.yaml:
hermes config set tools.enabled '["read_file","write_file","terminal","web_search"]'
```

### Workflow típico local

```bash
# Iniciar chat
hermes

# Dentro del chat:
#   "Leeme el archivo app.py y explicame qué hace"
#   "Creame un script que procese datos.csv"
#   "Ejecutá pytest en ./tests/"
#   /new               → tema nuevo, contexto fresco
#   /usage             → ver consumo de tokens
#   /compress          → comprimir historial si es muy largo
```

---

## 4. Securización

### 4.1 Credenciales seguras

```bash
# NUNCA pongas API keys en config.yaml
# Usar archivo .env con permisos restrictivos:

cat > ~/.hermes/.env << 'EOF'
OPENROUTER_API_KEY=sk-or-v1-tu-key
OPENAI_API_KEY=sk-tu-key
EOF

chmod 600 ~/.hermes/.env
chmod 700 ~/.hermes/
```

### 4.2 Allowlists del Gateway (si activás mensajería)

```yaml
# ~/.hermes/config.yaml
gateway:
  platforms:
    telegram:
      enabled: true
      allow_from:
        - "123456789" # TU user ID de Telegram
    discord:
      enabled: false # Deshabilitado si no usás
```

⚠️ **Nunca combines `allow_from: ["*"]` con herramientas de ejecución.**

### 4.3 Deshabilitar herramientas innecesarias

```bash
# Ver y desmarcar tools
hermes tools

# O por config:
hermes config set tools.enabled '["read_file","write_file","terminal"]'
```

### 4.4 Aislamiento de ejecución (prioridad #1)

Ver sección completa abajo: [Backend Aislado (Docker)](#5-backend-aislado-docker)

### 4.5 Revisar skills antes de instalar

```bash
# Skills guard escanea al instalar (heurístico, no infalible)
# El boundary real: VOS revisando el código Python y SKILL.md

# Ver skills instaladas
ls ~/.hermes/skills/

# Instalar solo de agentskills.io con revisión previa
hermes skills install <skill-name>
```

### 4.6 No exponer a internet pública

```bash
# Si necesitás acceso remoto, usar VPN:
# - Tailscale: https://tailscale.com/download/linux
# - ZeroTier
# - WireGuard manual

# El dashboard web default es loopback-only (seguro)
# No cambiar a --host 0.0.0.0 sin VPN + auth
```

### 4.7 Checklist de seguridad

| #   | Medida               | Cómo                                        | Prioridad  |
| --- | -------------------- | ------------------------------------------- | ---------- |
| 1   | Backend aislado      | `hermes config set terminal.backend docker` | 🔴 Crítica |
| 2   | Credenciales seguras | `.env` con `chmod 600`                      | 🔴 Crítica |
| 3   | Allowlists gateway   | Editar `config.yaml` allow_from             | 🔴 Crítica |
| 4   | Deshabilitar tools   | `hermes tools`                              | 🟡 Alta    |
| 5   | Revisar skills       | Leer Python + SKILL.md antes de instalar    | 🟡 Alta    |
| 6   | No exponer sin VPN   | Tailscale o similar                         | 🟡 Alta    |
| 7   | Actualizar seguido   | `hermes update`                             | 🟢 Media   |
| 8   | Auditoría            | `hermes doctor`                             | 🟢 Media   |

---

## 5. Backend Aislado (Docker)

### ¿Es otra instalación o un paso adicional?

**Es un paso adicional.** Docker es una instalación separada del sistema (como `git` o `python`), pero Hermes **ya incluye soporte nativo** para usarlo como backend. No necesitás instalar nada de Hermes extra.

El flujo es:

1. Instalás Docker en tu sistema (una vez)
2. Le decís a Hermes que lo use: `hermes config set terminal.backend docker`
3. Listo — Hermes ejecuta comandos dentro de contenedores aislados, no en tu host

### 5.1 Instalar Docker en WSL

```bash
# Opción A: Docker Engine nativo en WSL
sudo apt install -y docker.io
sudo usermod -aG docker $USER
# Cerrar y reabrir terminal WSL
newgrp docker

# Verificar
docker run hello-world
```

```bash
# Opción B: Docker Desktop for Windows (compartido con WSL2)
# 1. Instalar Docker Desktop en Windows
# 2. Settings → Resources → WSL Integration → habilitar tu distro
# 3. En WSL: docker ps (debería funcionar)
```

### 5.2 Configurar Hermes para usar Docker

```bash
# Cambiar backend a Docker
hermes config set terminal.backend docker

# Verificar
cat ~/.hermes/config.yaml | grep -A3 terminal

# A partir de ahora, todos los comandos que Hermes ejecute
# correrán DENTRO de un contenedor aislado, no en tu host WSL.
```

### 5.3 Qué protege el backend Docker

Hermes aplica hardening automático al contenedor:

| Protección                 | Descripción                                    |
| -------------------------- | ---------------------------------------------- |
| **Read-only root**         | El filesystem del contenedor es solo lectura   |
| **Capabilities dropeadas** | Se eliminan capabilities de Linux innecesarias |
| **PID limits**             | Límite de procesos dentro del contenedor       |
| **Network isolation**      | Red aislada (configurable)                     |
| **Filesystem isolation**   | Solo monta lo necesario                        |

### 5.4 Opciones adicionales de backend

```bash
# Docker (recomendado para WSL)
hermes config set terminal.backend docker

# SSH (ejecutar en un VPS remoto)
hermes config set terminal.backend ssh
# Requiere configurar host, user, key en config.yaml

# Modal (serverless, ~$0 idle, requiere cuenta Modal)
hermes config set terminal.backend modal

# Local (default, sin aislamiento)
hermes config set terminal.backend local
```

---

## 6. Crear Múltiples Agentes (Perfiles)

> Esto responde a la pregunta: "es el momento de crear otro agente"

### 6.1 ¿Qué es un perfil?

Un perfil es **otro agente** — otra personalidad, otra memoria, otro propósito — corriendo sobre la misma instalación de Hermes. **No es otra instalación.** Es el mismo binario `hermes` apuntando a otro directorio `HERMES_HOME`.

```
~/.hermes/                        ← agente general (default)
~/.hermes/profiles/finanzas/      ← agente de finanzas
~/.hermes/profiles/ciberseguridad/ ← agente de seguridad
~/.hermes/profiles/devops/        ← agente de DevOps
```

Cada uno es **totalmente independiente**: memoria, skills, personalidad, modelo, credenciales, cron — todo separado.

### 6.2 Crear un perfil nuevo

```bash
# Perfil vacío (solo estructura + skills bundled)
hermes profile create finanzas

# Perfil clonando config, .env, SOUL.md, y MEMORY.md del default
hermes profile create finanzas --clone

# Perfil con copia COMPLETA de todo lo del default
hermes profile create finanzas --clone-all
```

### 6.3 Usar un perfil

```bash
# Opción 1: Flag -p (una vez)
hermes -p finanzas

# Opción 2: Alias automático (se crea al crear el perfil)
finanzas

# Opción 3: Fijar como default pegajoso
hermes profile use finanzas
# A partir de ahora, "hermes" solo abre el de finanzas
hermes profile use default   # volver al general
```

### 6.4 Configurar cada perfil distinto

```bash
# Cada perfil tiene su propia config
hermes -p finanzas setup          # wizard exclusivo para finanzas
hermes -p finanzas model           # elegir modelo para finanzas
hermes -p finanzas tools           # herramientas para finanzas

# Instalar skills específicas para el perfil
hermes -p finanzas skills install finance-analyzer

# Cada perfil tiene su propio SOUL.md (personalidad)
cat > ~/.hermes/profiles/finanzas/SOUL.md << 'EOF'
# Agente Financiero

Eres un analista financiero experto. Tu trabajo es:
- Analizar datos de mercado
- Evaluar riesgos de inversión
- Generar reportes financieros
- NUNCA dar consejos de inversión personal
- Siempre citar fuentes y fechas de datos
EOF
```

### 6.5 Workflow multi-agente típico

```bash
# Mañana: el general te hace el daily briefing
hermes  # "Dame un resumen de lo que tengo hoy"

# Mediodía: el de finanzas analiza datos
finanzas  # "Analizame este CSV de cotizaciones"

# Tarde: el de DevOps despliega
devops  # "Haceme deploy a staging"

# Noche: cada uno corre sus crons automáticos
# (configurados independientemente en cada perfil)
```

### 6.6 Gateway multi-perfil (opcional avanzado)

```bash
# Cada perfil PUEDE tener su propio gateway en su propio puerto
hermes -p finanzas gateway setup   # configurar Telegram para finanzas
hermes -p finanzas gateway start --port 8643  # puerto distinto

# Así, el bot de Telegram de finanzas usa el agente financiero
# y el bot de Telegram general usa el agente default
```

### 6.7 Eliminar un perfil

```bash
hermes profile delete finanzas
# Borra el perfil, su alias, y sus services
```

---

## 7. Mantenimiento

```bash
# Actualizar Hermes
hermes update

# Diagnóstico
hermes doctor

# Ver perfiles
hermes profile list

# Ver uso de tokens y costos
hermes -p finanzas   # dentro del chat: /usage, /insights --days 7

# Backup de un perfil
cp -r ~/.hermes/profiles/finanzas ~/backups/hermes-finanzas-$(date +%Y%m%d)/
```

---

## 🔄 Flujo Completo Recomendado

```
Día 1: Instalación básica
  ├── curl | bash          → instalar
  ├── hermes setup         → configurar
  └── hermes               → primer chat local

Día 2-3: Securización
  ├── Instalar Docker
  ├── hermes config set terminal.backend docker
  ├── Configurar .env + chmod 600
  └── hermes tools         → deshabilitar innecesarias

Semana 1: Maduración
  ├── Usar en local, que aprenda tus proyectos
  ├── Crear MEMORY.md con contexto de tu trabajo
  └── Dejar que cree skills automáticamente

Semana 2: Especialización
  ├── hermes profile create finanzas --clone
  ├── Configurar SOUL.md para finanzas
  ├── Instalar skills específicas
  └── Repetir para otros dominios

Mes 1+: Gateway y automatización
  ├── hermes gateway setup → Telegram/Discord
  ├── Configurar crons (reportes diarios, backups)
  └── Evaluar Modal/Docker para producción
```

---

## 8. Interactuar con Hermes — Comandos y Atajos

### 8.1 Comandos dentro del chat

| Comando                 | Acción                                                |
| ----------------------- | ----------------------------------------------------- |
| `/model <alias>`        | Cambiar modelo al vuelo (ej: `/model deepseek`)       |
| `/new`                  | Conversación nueva con contexto limpio                |
| `/reset`                | Reiniciar conversación actual                         |
| `/retry`                | Reintentar último turno                               |
| `/undo`                 | Deshacer último turno                                 |
| `/compress`             | Comprimir contexto si se va de tokens                 |
| `/usage`                | Ver consumo de tokens y costos                        |
| `/tools`                | Ver herramientas disponibles                          |
| `/skills`               | Ver skills instaladas                                 |
| `/personality <nombre>` | Cambiar personalidad (helpful, concise, pirate, etc.) |
| `/quit` o `Ctrl+D`      | Salir                                                 |
| `Ctrl+C`                | Interrumpir al agente si se cuelga                    |

### 8.2 Atajos de teclado en la TUI

| Tecla       | Acción                        |
| ----------- | ----------------------------- |
| `Ctrl+C`    | Interrumpir generación actual |
| `Ctrl+D`    | Salir del chat                |
| `Enter`     | Enviar mensaje                |
| `Alt+Enter` | Nueva línea sin enviar        |
| `↑/↓`       | Historial de mensajes         |
| `Tab`       | Autocompletar comandos        |

### 8.3 Flujo típico de prueba

```bash
# Arranque
ollama serve &          # Asegurar que Ollama corre
hermes                  # Entrar al chat

# Dentro del chat, probá en orden:
Hola, ¿quién sos?                    # Verifica que carga SOUL.md
/model gemma4                        # Confirmar modelo local
¿Qué herramientas tenés disponibles? # Verifica tool calling
Leé ~/.hermes/memories/USER.md       # Verifica que lee tu contexto
Ejecutá: echo "prueba ok"           # Verifica ejecución de comandos
```

---

## 9. Sesiones Múltiples y Modelos Simultáneos

### 9.1 Cambiar modelo en la misma sesión (recomendado)

```bash
# Dentro del chat:
/model deepseek     # Cambia al vuelo. Ollama descarga el anterior de RAM.
/model gemma4       # Volvés al local.
/model claude       # Cloud vía OpenRouter (requiere API key).
```

**Ventaja:** Simple, no consume RAM extra. El historial de conversación se comparte.

**Desventaja:** Si un modelo respondió mal, el siguiente hereda ese contexto. Usá `/new` antes de cambiar si querés contexto fresco.

### 9.2 Dos sesiones simultáneas (terminales separadas)

Abrí **otra terminal WSL** y ejecutá:

```bash
hermes
```

Cada terminal es un proceso independiente:

```
Terminal 1: hermes → /model gemma4   → "Analizame este CSV"
Terminal 2: hermes → /model deepseek → "Escribime un script"
```

⚠️ **Cuidado con la RAM.** Con Ollama, cada modelo ocupa memoria:

| Escenario                                    | RAM usada          | ¿Funciona con 16 GB?       |
| -------------------------------------------- | ------------------ | -------------------------- |
| 1 solo modelo (gemma4:e4b)                   | ~9 GB              | ✅ Bien                    |
| 2 modelos chicos (gemma4 + qwen3:4b)         | ~13 GB             | ✅ Apretado pero anda      |
| 2 modelos grandes (gemma4 + deepseek-r1:14b) | ~18 GB             | ❌ Swap a disco, lentísimo |
| 1 local + 1 cloud                            | ~9 GB + 0 GB local | ✅ Ideal                   |

### 9.3 Estrategias para no saturar RAM

| Estrategia                 | Cómo                                                                      |
| -------------------------- | ------------------------------------------------------------------------- |
| **Alternar modelos**       | Usá `/model` en vez de abrir otra sesión. Ollama libera RAM al descargar. |
| **Una local + una cloud**  | Terminal 1: `/model gemma4`, Terminal 2: `/model claude` (no usa tu RAM)  |
| **Modelos más chicos**     | Bajate `qwen3:4b` (~3 GB) para tareas livianas en sesión 2                |
| **Cerrar sesión inactiva** | `Ctrl+D` para salir y liberar RAM                                         |

---

## 10. Límites de RAM con Ollama

### 10.1 Modelos instalados y consumo

```bash
ollama list          # Ver tus modelos y tamaños
ollama ps            # Ver qué modelos están cargados en RAM
```

### 10.2 Tamaños típicos

| Modelo              | Tamaño disco | RAM aprox | Tool calling       |
| ------------------- | ------------ | --------- | ------------------ |
| `gemma4:e4b`        | 9.0 GB       | ~9 GB     | Básico             |
| `qwen3:4b`          | 2.5 GB       | ~3 GB     | Bueno              |
| `qwen3:14b`         | 8.5 GB       | ~9 GB     | Muy bueno          |
| `deepseek-r1:14b`   | 9.0 GB       | ~9 GB     | Bueno              |
| `deepseek-r1:32b`   | 19 GB        | ~19 GB    | Excelente          |
| `deepseek-coder-v2` | 9-16 GB      | 9-16 GB   | Excelente (código) |

### 10.3 ¿Cuánta RAM tenés en WSL?

```bash
free -h              # Ver RAM total y disponible
```

**Regla práctica:** necesitás al menos el tamaño del modelo + 2-4 GB para el sistema.

- 16 GB RAM total → modelos de hasta 12-14 GB
- 32 GB RAM total → modelos de hasta 28 GB
- 8 GB RAM total → modelos chicos (qwen3:4b, llama3.2:3b)

### 10.4 Ollama descarga automática

Ollama mantiene los modelos en RAM mientras se usan. Los descarga después de 5 minutos de inactividad. Si cambiás de modelo con `/model`, descarga el anterior.

```bash
# Forzar descarga manual (rara vez necesario)
ollama stop
```

---

## 11. Warning de Tirith

### 11.1 ¿Qué es?

```
⚠ tirith security scanner enabled but not available — command scanning will use pattern matching only
```

Tirith es un scanner de seguridad que analiza comandos antes de ejecutarlos. Cuando no está instalado, Hermes usa pattern matching simple en vez del scanner completo.

### 11.2 ¿Afecta en algo?

**No.** Es un aviso informativo. El pattern matching simple funciona bien para uso local. Tus comandos se ejecutan igual.

### 11.3 Opciones

```bash
# A. Ignorarlo (recomendado para uso local)
# No hagas nada. No afecta funcionalidad.

# B. Deshabilitarlo completamente
hermes config set security.tirith_enabled false

# C. Instalarlo (requiere Rust/Cargo, solo si necesitás hardening extra)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
cargo install tirith
hermes config set security.tirith_path tirith
```

Para uso local y desarrollo, **opción A o B** es suficiente.

---

## 12. Nota sobre Modelos Locales y Personalidad

### 12.1 Modelos chicos y SOUL.md

Los modelos locales pequeños (como `gemma4:e4b` de 9 GB) pueden **no encarnar completamente** la personalidad definida en `SOUL.md`. Es normal que respondan de forma genérica ("soy un modelo de lenguaje...").

**Soluciones:**

| Causa                     | Solución                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------ |
| Modelo muy chico          | Probá `deepseek-r1:14b` o `qwen3:14b`                                                                  |
| Contexto demasiado grande | `/compress` o `/new` para liberar tokens                                                               |
| System prompt ignorado    | Modelos base (no instruct) ignoran system prompts. Gemma4:e4b debería seguirlo, pero es inconsistente. |

### 12.2 Verificar que SOUL.md se cargó

```bash
# Dentro del chat:
¿Cuál es tu personalidad definida en SOUL.md?

# O verificá desde terminal:
cat ~/.hermes/SOUL.md | head -10
```

Si el modelo responde genérico a pesar de tener SOUL.md bien escrito, **cambiate a un modelo más grande** (`/model deepseek`).
