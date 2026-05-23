# Troubleshooting: VPS Fish + Tmux + Ghostty SSH

## Problem 1: Ghostty SSH hook crashes remote fish shell

### Symptoms

When connecting via SSH from Ghostty terminal to a VPS running fish as login shell:

```
fish: Unsupported use of '='. In fish, please use 'set hook $(printf "{\"hook\": \"SSH\", \"value\": {\"socket_path\": \"~/.ssh/...\", \"remote_shell\": \"%s\", \"session_id\": ..., \"remote_session_id\": ...}}" "${SHELL##*/}" | command -p od -An -v -tx1 | command -p tr -d " \n")'.
Connection to 100.126.251.2 closed.
```

### Root Cause

Ghostty 1.3.x injects a bash-syntax hook (`hook=$(...)`) at the PTY level during SSH connections. This hook is sent to the remote shell regardless of:

- `shell-integration = none` in Ghostty config
- `shell-integration-features = no-ssh-env,no-ssh-terminfo`
- Any shell integration configuration

When the remote login shell is fish, fish cannot parse `var=$(...)` syntax and immediately exits, closing the SSH session.

### Solution

Change the remote login shell to bash, and auto-exec fish for interactive sessions. Bash processes the Ghostty hook correctly, then hands off to fish transparently.

#### Step 1: Change login shell

```bash
sudo chsh -s /usr/bin/bash hermes
```

#### Step 2: Add fish auto-start to `~/.bashrc`

Append at the end of `~/.bashrc`:

```bash
# Auto-start fish for interactive bash sessions (skipped in tmux since fish runs directly)
if [ -z "$FISH_STARTED" ] && [ -z "$TMUX" ]; then
    export FISH_STARTED=1
    exec /home/linuxbrew/.linuxbrew/bin/fish
fi
```

**Important**: This must go at the **end** of `.bashrc`, after all PATH and environment setup. The `FISH_STARTED` guard prevents re-execution, and `TMUX` guard prevents double-starting fish inside tmux sessions.

#### Step 3: Remove any auto-start fish from `~/.profile`

Do **not** duplicate the fish auto-start in `.profile`. The `.bashrc` early-return for non-interactive shells means `.profile` code after the `.bashrc` source call won't execute for interactive sessions anyway.

### Emergency Access

If fish is broken and you need a raw bash shell for maintenance:

```bash
ssh -t -i ~/.ssh/id_ed25519_vps_personal hermes@100.126.251.2 '/bin/bash --noprofile --norc'
```

The `-t` flag allocates a TTY. `--noprofile --norc` skips all shell initialization for a clean recovery environment.

### Ghostty Config (Local Machine)

For local Ghostty usage, restore shell integration since it works fine locally:

```
shell-integration = fish
shell-integration-features = cursor,no-sudo,title,no-ssh-env,no-ssh-terminfo,path
```

**Note**: SSH features are disabled because the Ghostty SSH hook is injected at PTY level and cannot be disabled via config. The login-shell-to-bash workaround handles this transparently.

---

## Problem 2: tmux "not a suitable shell: fish"

### Symptoms

```
.tmux.conf:7 not a suitable shell: fish
```

### Root Cause

tmux `default-command` and `default-shell` were set to `fish` (relative path), which tmux cannot resolve in all contexts (SSH sessions, non-interactive shells).

### Solution

Use the **full path** to fish in `~/.tmux.conf`:

```tmux
set -g default-command '/home/linuxbrew/.linuxbrew/bin/fish'
set -g default-shell '/home/linuxbrew/.linuxbrew/bin/fish'
```

After changing tmux config, kill the tmux server for changes to take effect:

```bash
tmux kill-server
```

Then start a new tmux session.

### Why full path is needed

- During SSH login, the shell environment may not have `fish` in PATH yet
- tmux resolves `default-command` before PATH is fully set up
- Homebrew fish at `/home/linuxbrew/.linuxbrew/bin/fish` is not in standard system paths
- System fish at `/usr/bin/fish` may not exist or be different version

---

## Problem 3: Bash prompt not visible / "Standard input is not a terminal"

### Symptoms

Connecting via `ssh user@host /bin/bash` shows no prompt and commands like `nano` fail with:

```
Standard input is not a terminal
```

### Root Cause

Running `ssh user@host /bin/bash` executes bash as a **remote command** (non-interactive, no TTY). This bypasses login shell initialization, leaves PATH empty, and doesn't allocate a pseudo-terminal.

### Solution

Don't use `/bin/bash` as a remote command. Since the login shell is now bash (which auto-execs fish), just SSH normally:

```bash
ssh -i ~/.ssh/id_ed25519_vps_personal hermes@100.126.251.2
# or with the SSH config alias:
ssh vps
```

---

## Problem 4: TERM environment variable not set

### Symptoms

```
TERM environment variable not set
```

### Root Cause

Happens when SSH doesn't allocate a TTY or the terminal emulator doesn't set `TERM`. Common with `ssh user@host /bin/bash` or when running commands inside non-interactive shells.

### Solution

Ensure SSH allocates a TTY:

```bash
# In ~/.ssh/config (local machine)
Host vps
    HostName 100.126.251.2
    User hermes
    IdentityFile ~/.ssh/id_ed25519_vps_personal
    RequestTTY yes
```

Or use `-t` flag:

```bash
ssh -t user@host
```

---

## Configuration Summary

### Remote VPS (~/.bashrc) — end of file

```bash
# Auto-start fish for interactive bash sessions (skipped in tmux since fish runs directly)
if [ -z "$FISH_STARTED" ] && [ -z "$TMUX" ]; then
    export FISH_STARTED=1
    exec /home/linuxbrew/.linuxbrew/bin/fish
fi
```

### Remote VPS (~/.tmux.conf) — shell config

```tmux
set -g default-command '/home/linuxbrew/.linuxbrew/bin/fish'
set -g default-shell '/home/linuxbrew/.linuxbrew/bin/fish'
```

### Remote VPS (/etc/passwd)

```
hermes:x:1000:1000:...:/usr/bin/bash
```

### Local Machine (~/.config/ghostty/config)

```
shell-integration = fish
shell-integration-features = cursor,no-sudo,title,no-ssh-env,no-ssh-terminfo,path
```

### Local Machine (~/.ssh/config)

```
Host vps
    HostName 100.126.251.2
    User hermes
    IdentityFile ~/.ssh/id_ed25519_vps_personal
    RequestTTY yes
```

---

## Debugging Commands

```bash
# Check current login shell
grep hermes /etc/passwd

# Check if fish is accessible
which fish
/home/linuxbrew/.linuxbrew/bin/fish --version

# Test SSH connection
ssh -v -i ~/.ssh/id_ed25519_vps_personal hermes@100.126.251.2

# Kill tmux and restart fresh
tmux kill-server
tmux new-session -A -s main

# Check tmux running config
tmux show-options -g | grep default

# Emergency raw bash access
ssh -t -i ~/.ssh/id_ed25519_vps_personal hermes@100.126.251.2 '/bin/bash --noprofile --norc'
```