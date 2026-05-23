# OpenCode Configuration

Configuración personalizada de [OpenCode](https://opencode.ai) para WSL.

## Problema

Por defecto, OpenCode asigna `Ctrl+C` a dos acciones:

- **`app_exit`**: Salir de la aplicación (`ctrl+c,ctrl+d,<leader>q`)
- **`input_clear`**: Limpiar el campo de input (`ctrl+c`)

Esto entra en conflicto con el uso estándar de `Ctrl+C` en la terminal para **copiar texto seleccionado**. En WSL (y cualquier terminal), `Ctrl+C` es el atajo universal para copiar, pero OpenCode lo interceptaba y lo usaba para cancelar/limpiar.

## Solución

Se modificó `~/.config/opencode/tui.json` para liberar `Ctrl+C` y permitir que pase al terminal:

| Keybind | Valor por defecto | Valor ajustado | Efecto |
|---------|-------------------|----------------|--------|
| `app_exit` | `ctrl+c,ctrl+d,<leader>q` | `ctrl+d,<leader>q` | Ya no sale de la app con Ctrl+C |
| `input_clear` | `ctrl+c` | `none` | Ya no limpia el input con Ctrl+C |
| `messages_copy` | `<leader>y` | `<leader>y,ctrl+c` | Ctrl+C copia mensajes al portapapeles |

Además se agregó `ctrl+c` como atajo directo para `messages_copy`, permitiendo copiar mensajes completos al portapapeles con un solo `Ctrl+C`.

## Archivos

- **`opencode.json`**: Configuración principal de OpenCode (agentes, MCP, permisos).
- **`tui.json`**: Configuración de la interfaz TUI (keybindings, plugins, tema).

## Instalación

```bash
# Copiar los archivos de configuración al directorio de OpenCode
cp opencode.json ~/.config/opencode/opencode.json
cp tui.json ~/.config/opencode/tui.json
```

Los keybindings en `tui.json` se fusionan con los valores por defecto de OpenCode, por lo que solo es necesario especificar los cambios.

> **Nota**: OpenCode solo lee `tui.json` al iniciar. Si ya está corriendo, hay que reiniciarlo para que los cambios surtan efecto.
