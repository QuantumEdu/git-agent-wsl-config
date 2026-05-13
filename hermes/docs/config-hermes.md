# 🐍 Hermes Agent — Configuración Completa

> Máquina: WSL2 (Ubuntu) en Windows
> Fecha: 2026-05-12
> Versión: Hermes Agent v0.13.0

---

## 📋 Índice

1. [Instalación](#1-instalación)
2. [Modelos configurados](#2-modelos-configurados)
3. [Personalidad del agente (SOUL.md)](#3-personalidad-del-agente-soulmd)
4. [Contexto del usuario (USER.md)](#4-contexto-del-usuario-usermd)
5. [Ollama + Gemma 4](#5-ollama--gemma-4)
6. [DeepSeek](#6-deepseek)
7. [Comandos rápidos](#7-comandos-rápidos)
8. [Archivos clave](#8-archivos-clave)

---

## 1. Instalación

```bash
# Un solo comando
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Recargar shell
source ~/.bashrc

# Wizard de configuración inicial
hermes setup
```

**Resultado:**

- Binario: `/home/ubuntu/.local/bin/hermes`
- Home: `~/.hermes/`
- Repo: `~/.hermes/hermes-agent/`
- Python: 3.11.15 (vía uv)
- Versión: v0.13.0

---

## 2. Modelos configurados

### Configuración actual (`~/.hermes/config.yaml`)

```yaml
model:
  default: gemma4:e4b # ← modelo principal (Ollama local)
  provider: custom
  base_url: http://localhost:11434/v1

  model_aliases:
    # Local (Ollama) — gratis, privado, sin internet
    gemma4:
      model: gemma4:e4b
      provider: custom
      base_url: http://localhost:11434/v1
    gemma26:
      model: gemma4:26b
      provider: custom
      base_url: http://localhost:11434/v1
    deepseek:
      model: deepseek-r1:14b
      provider: custom
      base_url: http://localhost:11434/v1
    deepseek32:
      model: deepseek-r1:32b
      provider: custom
      base_url: http://localhost:11434/v1
    deepseek-coder:
      model: deepseek-coder-v2
      provider: custom
      base_url: http://localhost:11434/v1

    # Cloud (OpenRouter) — más capaz, requiere API key + internet
    claude:
      model: anthropic/claude-opus-4.6
      provider: openrouter
      base_url: https://openrouter.ai/api/v1

  api_params:
    ollama_num_ctx: 131072
```

### Variables de entorno (`~/.hermes/.env`)

```bash
# Ollama local
OPENAI_BASE_URL=http://localhost:11434/v1
OPENAI_API_KEY=ollama

# OpenRouter (para modelos cloud)
OPENROUTER_API_KEY=
```

### Cómo cambiar de modelo

```bash
# Desde el chat:
/model gemma4         # Gemma 4 (9GB, local)
/model gemma26        # Gemma 4 26B (requiere descarga, ~16GB)
/model deepseek       # DeepSeek R1 14B (requiere descarga, ~9GB)
/model deepseek32     # DeepSeek R1 32B (requiere descarga, ~19GB)
/model claude         # Claude vía OpenRouter (necesita API key)

# Desde terminal:
hermes model          # Menú interactivo
```

---

## 3. Personalidad del agente (SOUL.md)

**Archivo:** `~/.hermes/SOUL.md`

**Personalidad:** Agente estratégico para Qu@ntum.

Rol: arquitecto de software pragmático, consultor técnico, mentor, analista de ciberseguridad, asistente DevOps, investigador aplicado.

Tono: directo, profesional, claro, en español. Prioriza estructura, pasos concretos, tablas comparativas, y recomendaciones prácticas.

Se recarga automáticamente en cada mensaje — no requiere reinicio.

---

## 4. Contexto del usuario (USER.md)

**Archivo:** `~/.hermes/memories/USER.md`

Contiene el perfil completo de Gabriel: áreas de interés, stacks tecnológicos, proyectos activos, estilo de aprendizaje, preferencias de respuesta, herramientas de terminal, flujo de trabajo WSL/Docker.

**Hermes lo carga al inicio de cada conversación** para personalizar respuestas.

---

## 5. Ollama + Gemma 4

### Instalación de Ollama

```bash
# Instalador oficial
curl -fsSL https://ollama.com/install.sh | sh

# Verificar
ollama --version
```

### Modelos descargados

```bash
ollama list
```

| Modelo                | Tamaño   | Uso                                                      |
| --------------------- | -------- | -------------------------------------------------------- |
| `gemma4:e4b`          | 9.0 GB   | Modelo principal — conversación, análisis, código simple |
| _(deepseek-r1:14b)_   | ~9 GB    | Pendiente descargar                                      |
| _(deepseek-r1:32b)_   | ~19 GB   | Pendiente descargar                                      |
| _(deepseek-coder-v2)_ | ~9-16 GB | Pendiente descargar                                      |

### Comandos Ollama útiles

```bash
ollama list              # Modelos descargados
ollama pull <modelo>     # Descargar modelo
ollama rm <modelo>       # Eliminar modelo
ollama serve             # Iniciar servidor (si no está corriendo)
ollama ps                # Modelos cargados en memoria
```

### Contexto configurado

```yaml
api_params:
  ollama_num_ctx: 131072 # 128K tokens de contexto para Gemma
```

---

## 6. DeepSeek

### Opción A: Local vía Ollama (recomendado)

```bash
# Modelo de razonamiento (R1)
ollama pull deepseek-r1:14b     # ~9 GB — balance capacidad/velocidad
ollama pull deepseek-r1:32b     # ~19 GB — máxima capacidad

# Modelo de código
ollama pull deepseek-coder-v2   # ~9-16 GB

# Usar:
/model deepseek
/model deepseek32
/model deepseek-coder
```

### Opción B: Cloud vía OpenRouter

Agregar alias en `config.yaml`:

```yaml
model_aliases:
  deepseek-cloud:
    model: deepseek/deepseek-chat
    provider: openrouter
    base_url: https://openrouter.ai/api/v1
```

Requiere `OPENROUTER_API_KEY` en `.env`.

### ¿Cuál elegir?

| Criterio       | DeepSeek local (Ollama)  | DeepSeek cloud (OpenRouter)     |
| -------------- | ------------------------ | ------------------------------- |
| Privacidad     | ✅ Total                 | ❌ Datos van a API externa      |
| Costo          | Gratis                   | ~$0.50-2.00/M tokens            |
| Velocidad      | Depende de tu GPU        | Rápido (servidores dedicados)   |
| Disponibilidad | Siempre (sin internet)   | Requiere internet               |
| Capacidad      | Limitada por tu hardware | Modelos más grandes disponibles |
| Tool calling   | Bueno en R1 32B          | Excelente                       |

---

## 7. Comandos rápidos

```bash
# Chat
hermes                          # TUI interactiva
hermes -p <perfil>              # Usar un perfil específico

# Modelos
hermes model                    # Cambiar modelo
/model <alias>                  # Cambiar desde el chat

# Configuración
hermes setup                    # Wizard completo
hermes tools                    # Habilitar/deshabilitar herramientas
hermes config set <key> <val>   # Configuración directa
hermes config get <key>         # Leer valor

# Perfiles (agentes independientes)
hermes profile create <nombre>  # Crear nuevo agente especializado
hermes profile list             # Listar perfiles
hermes profile use <nombre>     # Fijar como default
hermes profile delete <nombre>  # Eliminar perfil

# Mantenimiento
hermes update                   # Actualizar
hermes doctor                   # Diagnóstico
hermes version                  # Versión

# Gateway (mensajería)
hermes gateway setup            # Configurar Telegram/Discord/etc
hermes gateway start            # Iniciar gateway
hermes gateway install          # Instalar como servicio systemd
```

### Atajos dentro del chat

| Comando                 | Acción                  |
| ----------------------- | ----------------------- |
| `/model <alias>`        | Cambiar modelo          |
| `/new`                  | Nueva conversación      |
| `/reset`                | Reiniciar conversación  |
| `/retry`                | Reintentar último turno |
| `/undo`                 | Deshacer último turno   |
| `/compress`             | Comprimir contexto      |
| `/usage`                | Ver uso de tokens       |
| `/tools`                | Ver herramientas        |
| `/skills`               | Ver skills              |
| `/personality <nombre>` | Cambiar personalidad    |
| `Ctrl+C`                | Interrumpir             |

---

## 8. Archivos clave

```
~/.hermes/
├── config.yaml          ← Configuración principal (modelo, tools, memoria, etc.)
├── .env                 ← Credenciales y variables de entorno
├── SOUL.md              ← Personalidad del agente
├── hermes-agent/        ← Repo clonado + venv
├── memories/
│   ├── MEMORY.md        ← Lo que Hermes aprende (auto-mantenido)
│   └── USER.md          ← Contexto del usuario (manual)
├── skills/              ← Skills instaladas
├── sessions/            ← Historial de conversaciones
├── cron/                ← Tareas programadas
├── logs/                ← Logs
└── cache/               ← Caché
```
