# CONTEXT.md - Hermes

## TL;DR [~80 tokens — SIEMPRE leer esto]
Estado: Desarrollo activo (Sincronizado).
Proyecto: Hermes
Siguiente: Consultar DECISIONS.md para el log completo de avances.
Bloqueador: Ninguno.

---

## Detalle Completo [~800 tokens — leer solo si preguntan]

### Avances Recientes Sincronizados:
- **[SESSION_SUMMARY] Session summary: hermes**: ## Goal
Fix Ghostty SSH hook crashing fish shell on VPS, fix tmux config, fix OpenCode Ctrl+C, and document all fixes.

## Instructions
- User prefers...
- **[BUGFIX] VPS SSH hook fix confirmed working**: **What**: Confirmed fix for Ghostty SSH hook crashing fish shell on VPS.

**Why**: The root cause was that fish (as login shell) cannot parse Ghostty'...
- **[BUGFIX] VPS login shell changed to bash with fish auto-start**: **What**: Changed login shell from fish to bash on VPS (quantum-vps = 100.126.251.2), with bash auto-starting fish for interactive sessions.

**Why**:...
