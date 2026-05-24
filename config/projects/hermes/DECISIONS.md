# DECISIONS.md - Decisiones del Proyecto Hermes

## Registro Automático de Decisiones y Logros (Desde Engram)

### [2026-05-23 17:35:11] Session summary: hermes (SESSION_SUMMARY)
- **Detalle:** ## Goal
Fix Ghostty SSH hook crashing fish shell on VPS, fix tmux config, fix OpenCode Ctrl+C, and document all fixes.

## Instructions
- User prefers Ctrl+C for copy, not exit app
- User wants bash as emergency maintenance shell, not primary shell
- User prefers documentation in their GitHub repos

## Discoveries
- Ghostty 1.3.x injects bash-syntax hook (`hook=$(...)`) at PTY level during SSH — NOT controlled by shell-integration-features config
- This server (quantum-vps) IS the VPS at 100.126.251.2 (Tailscale)
- Login shell was `/home/linuxbrew/.linuxbrew/bin/fish` which crashes on the hook
- tmux `default-shell 'fish'` uses relative path, must be full path
- `.bashrc` early return for non-interactive shells means `.profile` auto-start fish won't work
- `ssh user@host /bin/bash` runs non-interactive (no TTY), causing "Standard input is not a terminal"

## Accomplished
- ✅ Changed login shell to /usr/bin/bash via `sudo chsh`
- ✅ Added fish auto-start in ~/.bashrc (skips inside tmux via $TMUX check)
- ✅ Fixed tmux.conf to use full path /home/linuxbrew/.linuxbrew/bin/fish
- ✅ Fixed OpenCode Ctrl+C: removed from app_exit, kept in input_clear
- ✅ Created troubleshooting_vps_fish_tmux.md and pushed to GitHub
- ✅ Revoked exposed GitHub PAT token

## Next Steps
- Verify SSH from Ghostty works correctly after all changes
- Consider reporting Ghostty bug (SSH hook incompatible with fish shell)

## Relevant Files
- /home/hermes/.bashrc — fish auto-start at end
- /home/hermes/.profile — clean, no duplicate fish start
- /home/hermes/.tmux.conf — full path to fish
- /home/hermes/.config/ghostty/config — shell-integration fish, SSH features disabled
- /home/hermes/.config/opencode/tui.json — keybinds for Ctrl+C
- /home/hermes/.ssh/config — vps alias with RequestTTY
- /home/hermes/.config/fish/config.fish — removed vps alias

---

### [2026-05-23 17:24:35] VPS SSH hook fix confirmed working (BUGFIX)
- **Detalle:** **What**: Confirmed fix for Ghostty SSH hook crashing fish shell on VPS.

**Why**: The root cause was that fish (as login shell) cannot parse Ghostty's injected bash-syntax hook. Changing login shell to bash absorbs the hook, then bash auto-execs fish for interactive use.

**Where**: 
- /etc/passwd — login shell changed to /usr/bin/bash
- ~/.bashrc — added auto-start fish for interactive sessions (skips inside tmux)
- ~/.tmux.conf — default-shell/default-command uses full path /home/linuxbrew/.linuxbrew/bin/fish

**Learned**: 
- `.bashrc` must have the fish auto-start because `.profile` sources `.bashrc` which has an early return for non-interactive shells
- Inside tmux, `$TMUX` is set so bash skips the fish exec (tmux runs fish directly via default-command)
- Must kill tmux server after config changes (`tmux kill-server`) for default-command changes to take effect

---

### [2026-05-23 17:13:36] VPS login shell changed to bash with fish auto-start (BUGFIX)
- **Detalle:** **What**: Changed login shell from fish to bash on VPS (quantum-vps = 100.126.251.2), with bash auto-starting fish for interactive sessions.

**Why**: Ghostty injects a bash-syntax hook (`hook=$(...)`) during SSH connections at the PTY level. When the remote login shell is fish, fish rejects this syntax with "Unsupported use of '='", causing the SSH session to immediately close. This happens regardless of Ghostty's shell-integration config — the hook is injected at a level below those settings. By using bash as login shell, bash processes the hook correctly, then auto-execs fish for the interactive session.

**Where**: 
- /etc/passwd (login shell needs `sudo chsh -s /usr/bin/bash hermes`)
- ~/.bashrc (added auto-start fish block)
- ~/.ssh/config (simplified)
- ~/.config/fish/config.fish (removed vps alias)

**Learned**: 
- Ghostty's SSH hook injection is at PTY level, NOT controlled by shell-integration-features or shell-integration config options
- This server (quantum-vps) IS the VPS at 100.126.251.2 (Tailscale)
- The login shell was `/home/linuxbrew/.linuxbrew/bin/fish` which crashes on the bash hook
- `/usr/bin/fish` was not in `/etc/shells` initially but now is
- The fix: bash as login shell absorbs the Ghostty hook, then execs fish for interactive use

---

### [2026-05-23 17:01:25] Ghostty SSH hook crashes remote fish shell (BUGFIX)
- **Detalle:** **What**: Ghostty 1.3.x injects a bash-syntax hook (`hook=$(...)`) at PTY level during SSH sessions. This crashes remote fish shells with "Unsupported use of '='".

**Why**: Ghostty's SSH integration sends bash syntax to the remote shell. Fish doesn't support `var=$(...)` assignment syntax. This is NOT controlled by `shell-integration-features` — it's injected below that config level.

**Where**: ~/.config/ghostty/config, ~/.config/alacritty/alacritty.toml, ~/.ssh/config, ~/.config/fish/config.fish

**Learned**: 
- Ghostty's `shell-integration-features = no-ssh-env,no-ssh-terminfo` does NOT prevent the hook injection — it's at PTY level
- `shell-integration = none` also doesn't prevent it — the hook is injected regardless of shell integration settings
- Solution: use Alacritty as terminal for SSH connections to fish-shell VPS
- Ghostty config restored to `shell-integration = fish` with `no-ssh-env,no-ssh-terminfo` for local use
- Created alias `vps` in fish to open Alacritty for SSH

---

