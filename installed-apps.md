# Installed Apps — WSL / Ubuntu (iQuantum)

Inventario completo de aplicaciones instaladas en el entorno WSL (`Ubuntu 26.04 LTS`) para la máquina `iQuantum`.

## Stack base

| Componente | Versión | Gestor |
|---|---|---|
| OS | Ubuntu 26.04 LTS (Resolute Raccoon) | WSL |
| Shell | bash 5.3 + fish (interactivo) | apt + Homebrew |
| Homebrew | 5.1.11 | — |
| Node.js | 25.9.0 | Homebrew |
| npm | 11.12.1 | Homebrew |
| pnpm | 11.1.2 | independiente |
| Go | (via Homebrew) | Homebrew |
| Rust | (via Homebrew) | Homebrew |
| Python 3 | 3.14 | Homebrew |
| Git | 2.54.0 | Homebrew |

---

## Homebrew — Fórmulas explícitas (`brew leaves`)

### Terminal & Shell

| App | Versión | Propósito |
|---|---|---|
| **fish** | última | Shell interactiva principal |
| **atuin** | última | Historial de shell con búsqueda y sync |
| **carapace** | última | Auto-completado multiplataforma |
| **starship** | 1.25.1 | Prompt minimalista para shell |
| **zoxide** | 0.9.9 | Navegación inteligente de directorios (`z`) |
| **fzf** | 0.72.0 | Fuzzy finder universal |
| **tmux** | 3.6 | Multiplexor de terminal (vía apt) |
| **htop** | última | Monitor de procesos |
| **tldr** | última | Man pages simplificados |

### Editores & LSP

| App | Versión | Propósito |
|---|---|---|
| **neovim** | 0.12.2 | Editor de texto principal (LazyVim) |
| **glow** | 2.1.2 | Visualizador de Markdown en terminal |
| **lua-language-server** | última | LSP para Lua |
| **rust-analyzer** | última | LSP para Rust |
| **stylua** | última | Formateador Lua |
| **shfmt** | 3.13.1 | Formateador shell |
| **shellcheck** | última | Linter para scripts shell |

### File Managers

| App | Versión | Propósito |
|---|---|---|
| **yazi** | 26.5.6 | File manager de terminal (Rust) — configurado con atajos vim |

### Git & GitHub

| App | Versión | Propósito |
|---|---|---|
| **git** | 2.54.0 | Control de versiones |
| **gh** | 2.92.0 | GitHub CLI |
| **lazygit** | 0.61.1 | TUI para Git |
| **git-delta** | 0.19.2 | Diff viewer con syntax highlighting |

### Lenguajes y Compiladores

| App | Versión | Propósito |
|---|---|---|
| **node** | 25.9.0 | JavaScript runtime |
| **go** | última | Go lenguaje/compilador |
| **rust** | última | Rust lenguaje/compilador |
| **gcc** | última | GNU Compiler Collection |

### Buscadores / Productividad

| App | Versión | Propósito |
|---|---|---|
| **ripgrep (rg)** | 15.1.0 | Búsqueda de texto ultrarrápida |
| **fd** | 10.4.2 | Finder de archivos |
| **bat** | 0.26.1 | `cat` con syntax highlighting |
| **coreutils** | última | GNU coreutils actualizadas (desde Homebrew) |
| **eza** | última | `ls` moderno con íconos y colores |
| **hexyl** | última | Hex viewer |
| **hyperfine** | última | Benchmarking de comandos |
| **httpie** | última | HTTP client legible (alternativa a curl) |

### Yazi — Previews y utilidades

| App | Versión | Para qué lo usa Yazi |
|---|---|---|
| **poppler** | última | Preview de PDFs (pdftotext) |
| **jq** | última | Preview de JSON formateado |
| **ffmpegthumbnailer** | última | Thumbnails de video |
| **sevenzip** | última | Preview de archivos comprimidos |
| **chafa** | última | Image preview (fallback) |
| **imagemagick** | última | Preview de HEIC, JPEG XL, fuentes |

### Pi Ecosystem

| App | Versión | Propósito |
|---|---|---|
| **zellij** | última | Multiplexor de terminal (TUI workspace) |
| **gentle-ai** | 1.28.3 | Gentle AI harness |
| **engram** | última | Motor de memoria persistente |

### Dependencias notables (autoincluidas)

| Paquete | Para |
|---|---|
| llvm + clang-22 | Toolchain C/C++ |
| luajit | Neovim |
| openssl@3 | Crypto general |
| python@3.14 | Python runtime |
| curl | Transferencias HTTP |

---

## NPM — Paquetes globales

| Paquete | Versión | Propósito |
|---|---|---|
| `@earendil-works/pi-coding-agent` | 0.74.0 | **Pi** — coding agent runtime |
| `@devkade/pi-plan` | 0.2.2 | Planificación para Pi |
| `@juanibiapina/pi-powerbar` | 0.9.1 | Powerbar para Pi |
| `@juicesharp/rpiv-ask-user-question` | 1.8.0 | Componente RPiV de preguntas |
| `@juicesharp/rpiv-todo` | 1.8.0 | Componente RPiV de tareas |
| `@modemdev/glance-pi` | 0.1.0 | Glance.sh integration |
| `@tmustier/pi-ralph-wiggum` | 0.2.1 | Long-running dev loops |
| `gentle-engram` | 0.1.5 | Engram memory UI |
| `gentle-pi` | 0.3.4 | Gentle AI harness para Pi |
| `pi-intercom` | 0.6.0 | Comunicación entre sesiones Pi |
| `pi-lens` | 3.8.44 | LSP + AST navigation tools |
| `pi-manage-todo-list` | 0.3.0 | Gestión de tareas Pi |
| `pi-mcp-adapter` | 2.6.1 | Adaptador MCP |
| `pi-memory-md` | 0.1.36 | Memoria persistente en Markdown |
| `pi-subagents` | 0.24.3 | Delegación a subagentes |
| `pi-web-access` | 0.10.7 | Web search + fetching |
| **`typescript`** | última | TypeScript compiler |
| **`typescript-language-server`** | última | LSP para TypeScript/JavaScript |

---

## PNPM — Paquetes globales

| Paquete | Versión |
|---|---|
| `@earendil-works/pi-coding-agent` | 0.74.0 |
| `@pnpm/exe` | 11.1.2 |

---

## Go — Binarios

| Binario | Propósito |
|---|---|
| `gopls` | LSP server para Go |
| `templ` | Template engine para Go |

---

## APT — Paquetes manuales

| Paquete | Propósito |
|---|---|
| **bash** | Shell por defecto |
| **build-essential** | Toolchain de compilación |
| **coreutils / coreutils-from-uutils / rust-coreutils** | Utilidades base |
| **curl** | HTTP client |
| **ffmpeg** | Procesamiento multimedia |
| **fontconfig** | Gestión de fuentes |
| **ghostty** | Terminal emulator |
| **git** | Control de versiones (sistema) |
| **python3-dev** | Desarrollo Python |
| **ubuntu-minimal / ubuntu-wsl** | Base del sistema |
| **unzip** | Descompresión ZIP |
| **util-linux** | Utilidades del sistema |

---

## Archivos de Configuración

| Archivo | App | Propósito |
|---|---|---|
| `~/.bashrc` | bash | Inicialización de shell bash |
| `~/.profile` | bash | Perfil de login |
| `~/.gitconfig` | git | Configuración global de git |
| `~/.tmux.conf` | tmux | Configuración de tmux |
| `~/.config/starship.toml` | starship | Tema de prompt |
| `~/.config/ghostty/config` | ghostty | Terminal emulator (Gentleman Dots theme) |
| `~/.config/nvim/` | neovim | Editor (LazyVim) |
| `~/.config/fish/config.fish` | fish | Shell config (incluye `y` function para Yazi) |
| `~/.config/atuin/config.toml` | atuin | Historial shell |
| `~/.config/yazi/yazi.toml` | yazi | File manager — config general |
| `~/.config/yazi/keymap.toml` | yazi | Atajos tipo vim |
| `~/.config/zellij/` | zellij | Multiplexor TUI |
| `~/.config/lazygit/config.yml` | lazygit | Git TUI |

---

## Resumen de ecosistema

```
bash (login) → fish (interactivo, via tmux)
  ├── starship (prompt)
  ├── atuin (historial)
  ├── zoxide (cd inteligente)
  ├── carapace (autocompletado)
  └── y (wrapper Yazi)

tmux (multiplexor)
  ├── fish (default shell)
  ├── neovim (LazyVim)
  └── lazygit (git TUI)

ghostty (terminal)
  └── tmux → fish → herramientas

Yazi (file manager)
  ├── bat → preview código
  ├── fd → búsqueda archivos
  ├── rg → búsqueda contenido
  ├── fzf → navegación rápida
  ├── poppler → preview PDF
  ├── jq → preview JSON
  ├── ffmpegthumbnailer → thumbnails video
  ├── sevenzip → preview archivos
  ├── chafa → image preview fallback
  ├── imagemagick → preview HEIC/JXL/fonts
  └── hexyl → hex viewer
```

---

## Notas

- **yazi** se instaló via Homebrew (`26.5.6`) y ya tiene config personalizada con `yazi.toml` y `keymap.toml`.
- **ghostty** está instalado via APT, configuración con tema Gentleman Dots.
- El shell interactivo principal es **fish** (invocado desde bash via `alias fsh` y default en tmux).
- **tmux** está instalado via APT (`3.6`), no via Homebrew.
- La función `y` en fish permite salir de Yazi y que la terminal se posicione en el directorio que estabas viendo.
