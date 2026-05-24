# DECISIONS.md - Decisiones del Proyecto Personal

## Registro Automático de Decisiones y Logros (Desde Engram)

### [2026-05-23 14:39:32] Server setup audit - quantum-vps (DISCOVERY)
- **Detalle:** **What**: Full audit of quantum-vps: Gentleman.Dots install, tmux/ghostty status, system performance, Pi agent, QuantumEdu config sync
**Why**: User asked to verify installations, diagnose slowness, copy configs from QuantumEdu repo, and check Pi agent
**Where**: /home/hermes/ (quantum-vps Ubuntu 26.04 LTS, 3.7GB RAM, 2 CPU)
**Learned**: opencode uses 18% RAM (722MB) and is the main CPU consumer. tmux-kanagawa cpu_info.sh spawns top every 5s. ghostty cannot open windows on VPS (no desktop). tmux config differs from QuantumEdu (uses tmux-256color instead of xterm-ghostty). Pi agent (nonresearch) is installed at ~/.pi but binary itself is not in PATH. yazi and gitconfig are missing from server.

---

### [2026-05-22 21:31:50] Locate Gentle AI Hermes config in OpenCode (DISCOVERY)
- **Detalle:** What: Hermes/OpenCode Gentle AI integration is configured through ~/.config/opencode/opencode.json and ~/.config/opencode/prompts/sdd plus ~/.config/opencode/skills, not through Pi runtime files.
Why: The user needed to know how Hermes recognizes the Gentle orchestrator and SDD subagents.
Where: ~/.config/opencode/opencode.json; ~/.config/opencode/prompts/sdd/; ~/.config/opencode/skills/.
Learned: The current opencode.json already defines gentle-orchestrator as primary and sdd-* subagents with prompt files under ~/.config/opencode/prompts/sdd. Hermes should invoke OpenCode with agent gentle-orchestrator or select it in the UI.

---

### [2026-05-22 21:27:34] Session summary (SESSION_SUMMARY)
- **Detalle:** Goal: Explain how to configure gentle-pi so Hermes recognizes the orchestrator, skills, and related runtime pieces.
Instructions: Verify the actual local Pi installation and answer in Spanish with practical steps.
Discoveries: gentle-pi is already installed globally via ~/.pi/agent/settings.json; package list includes gentle-pi, pi-subagents, pi-intercom, gentle-engram, pi-web-access, pi-lens, todo, and ask-user-question. Global SDD assets already exist at ~/.pi/agent/agents/sdd-*.md and ~/.pi/agent/chains/sdd-*.chain.md. gentle-pi package exposes extensions, prompts, and skills via its pi manifest. The orchestrator is injected by extensions/gentle-ai.ts from assets/orchestrator.md, not as a manually selected user agent. Skill registry refreshes .atl/skill-registry.md unless Pi starts with --no-skills or --no-skill-registry.
Accomplished: Collected Pi core docs (README, skills, packages) and gentle-pi README sections relevant to package install, skill discovery, skill registry, orchestrator injection, commands, and global asset paths. Prepared an explanation tailored to the user's current setup.
Next Steps: Tell the user that their setup is already recognized, show verification commands (/gentle-ai:status, /reload, /skill-registry:refresh, pi list), explain where custom/project skills should live, and warn about common gotchas like PI_CODING_AGENT_DIR, --no-skills, and disabled resources via pi config.
Relevant Files: ~/.pi/agent/settings.json; ~/.pi/agent/agents/; ~/.pi/agent/chains/; ~/.pi/agent/npm/node_modules/gentle-pi/README.md; Pi docs README.md, docs/skills.md, docs/packages.md.

---

