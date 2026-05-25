# DECISIONS.md - Decisiones del Proyecto Para_Ace

## Registro Automático de Decisiones y Logros (Desde Engram)

### [2026-05-24 23:45:49] Session summary (SESSION_SUMMARY)
- **Detalle:** ## Goal
Copy two recently created HTML files into the QuantumEdu/tuts repository and publish them.

## Instructions
- User asked first for the recent HTML files, then requested copying those two files into the repo's hermes directory, and finally explicitly authorized commit and push.

## Discoveries
- The two recent HTML files were in `1_PARA/Resources/` under the current workspace.
- The target repo was not present locally, so it had to be cloned to `/home/hermes/tuts`.
- The `hermes/` folder in the target repo already contained several tutorial HTML files.
- Push access to `https://github.com/QuantumEdu/tuts` worked directly from the local clone.

## Accomplished
- ✅ Identified the two recent HTML files: `Guia_Prompts_Hermes.html` and `hermes-kanban-triage.html`.
- ✅ Cloned `QuantumEdu/tuts` locally and created/verified the `hermes/` directory.
- ✅ Copied both HTML files into `/home/hermes/tuts/hermes/`.
- ✅ Committed the addition with `docs: add Hermes prompt and kanban HTML guides`.
- ✅ Pushed commit `70ba6a7` to `origin/main`.

## Next Steps
- None required unless the user wants a PR, release note, or verification against GitHub UI.

## Relevant Files
- `1_PARA/Resources/Guia_Prompts_Hermes.html` — source HTML file copied into the target repo.
- `1_PARA/Resources/hermes-kanban-triage.html` — source HTML file copied into the target repo.
- `/home/hermes/tuts/hermes/Guia_Prompts_Hermes.html` — new published tutorial page in the target repo.
- `/home/hermes/tuts/hermes/hermes-kanban-triage.html` — new published tutorial page in the target repo.

---

### [2026-05-24 23:45:42] Pushed Hermes HTML guides to tuts main (DECISION)
- **Detalle:** **What**: Committed and pushed two HTML files into the QuantumEdu/tuts repository under hermes/ on branch main.
**Why**: The user explicitly requested uploading the copied Hermes HTML files to the repository.
**Where**: /home/hermes/tuts/hermes/Guia_Prompts_Hermes.html, /home/hermes/tuts/hermes/hermes-kanban-triage.html; commit 70ba6a7 on origin/main
**Learned**: The remote push to https://github.com/QuantumEdu/tuts succeeded directly from the local clone without additional auth prompts.

---

### [2026-05-24 23:44:00] Copied Hermes HTML guides into tuts (DISCOVERY)
- **Detalle:** **What**: Cloned the QuantumEdu/tuts repository locally to /home/hermes/tuts and copied Guia_Prompts_Hermes.html plus hermes-kanban-triage.html into the hermes/ directory.
**Why**: The user asked to place the two recently created HTML files into the repo's hermes folder.
**Where**: /home/hermes/tuts/hermes/Guia_Prompts_Hermes.html, /home/hermes/tuts/hermes/hermes-kanban-triage.html
**Learned**: The hermes/ directory already contained multiple HTML tutorial files; the two copied files are currently untracked and not committed/pushed.

---

