---
name: special-instruction
description: >
  Guide the user through creating a well-structured prompt, skill, agent, or tool
  using the correct template for each type.
  Trigger: When the user runs "/special-instruction" or asks to create a new prompt,
  skill, agent, or tool instruction.
license: Apache-2.0
metadata:
  author: iQuantum
  version: "1.0"
---

# special-instruction

## Goal
Guide the user through creating a well-structured prompt, skill, agent, or tool using the correct template for each type. When invoked, detect the type from context or ask, then generate the filled template ready to use or save.

## Trigger
When the user runs `/special-instruction` or asks to create a new prompt, skill, agent, or tool instruction.

---

## Steps

### 1. Detect or Ask for Type

If the user's message clearly implies a type, use it directly. If ambiguous, present the **Selection Guide** and ask:

> "¿Qué quieres crear? (1) Prompt básico, (2) Skill/workflow, (3) Agente, (4) Tool/referencia"

Use the Selection Guide below to decide:

| Type | Use when... |
|------|-------------|
| **Prompt básico** | One-off instruction, system prompt, behavioral directive, or a reusable text block with no steps |
| **Skill (workflow)** | Multi-step repeatable workflow with clear success criteria per step |
| **Agent** | Autonomous entity that needs an identity, strengths, and behavioral guidelines |
| **Tool / Reference** | A function/capability with inputs, outputs, constraints — or a doc/decision table |

**Success criteria**: Type is determined — either inferred or confirmed by user.

---

### 2. Gather Missing Information

Before filling the template, identify any missing fields. Ask ONLY what's necessary — one question at a time if multiple gaps exist. For each missing field:
- Propose a sensible default based on context
- Ask if the default is correct or if they want something different

**Success criteria**: All required fields are known (name, goal/description, key behavior, at least one example).

---

### 3. Fill and Output the Template

Generate the complete template filled with the user's information. Use the appropriate template below.

**Success criteria**: Output is a complete, copy-paste-ready instruction block.

---

### 4. Save or Iterate

Ask: "¿Lo guardamos en `~/.Codex/skills/<name>/SKILL.md` o quieres ajustar algo primero?"

If saving:
- Determine correct path based on type:
  - Skills → `~/.Codex/skills/<name>/SKILL.md`
  - Agents → `~/.Codex/skills/<name>/SKILL.md` (same format, agent identity section)
  - Tools → document in the relevant project or `~/.Codex/skills/<name>/SKILL.md`
  - Prompts → `~/.Codex/prompts/<name>.md` or inline

**Success criteria**: File is saved at the correct path, or user confirms they'll handle saving.

---

## Templates

### Tipo 1: PROMPT BÁSICO

```markdown
# [Nombre del Prompt]

## Context
[Cuándo y para qué se usa este prompt]

## Instruction
[El prompt en sí — claro, directo, sin ambigüedad]

## Variables (si aplica)
- `{{variable}}`: [descripción]

## Example
Input: [ejemplo de entrada]
Output: [ejemplo de salida esperada]
```

---

### Tipo 2: SKILL (Workflow Steps)

```markdown
# [Nombre del Skill]

## Goal
[Una frase clara describiendo el objetivo principal del skill]

## Steps

### 1. [Nombre del Paso 1]
[Descripción detallada de qué hacer en este paso]

**Success criteria**: [Cómo saber que este paso está completo]

### 2. [Nombre del Paso 2]
[Descripción detallada]

**Success criteria**: [Criterio de éxito]

### 3. [Nombre del Paso 3]
[Descripción detallada]

**Success criteria**: [Criterio de éxito]

## Rules
- [Regla importante 1]
- [Regla importante 2]
- [Regla importante 3]

## Examples
[Ejemplos concretos de uso]
```

---

### Tipo 3: AGENTE (Identity + Strengths + Guidelines)

```markdown
# [Nombre del Agente]

You are a [role/persona] for [context].

[Optional: Critical constraints — READ-ONLY mode, scope limits, etc.]

## Your strengths
- [Strength 1]
- [Strength 2]
- [Strength 3]
- [Strength 4]

## Guidelines
- [Guideline 1]
- [Guideline 2]
- [Guideline 3]
- [Guideline 4]

## When to use
[Cuándo invocar este agente vs otros disponibles]

## Examples
[Ejemplo de invocación y resultado esperado]
```

---

### Tipo 4: TOOL / REFERENCIA (Sections + Tables)

```markdown
# [Tool/Feature Name]

[Brief introduction — what this is and why it matters]

| Parameter | Description | Examples |
|-----------|-------------|----------|
| [param1]  | [desc]      | [ex 1], [ex 2] |
| [param2]  | [desc]      | [ex 1], [ex 2] |

## When to Use This Tool
1. [Condition 1] — example: [...]
2. [Condition 2] — example: [...]
3. [Condition 3] — example: [...]

## How This Tool Works
[Step-by-step explanation of the mechanism]

## Examples

### GOOD — Use [Tool]:
[Example 1]
[Example 2]

### BAD — Don't use [Tool]:
[Example 1]
[Example 2]

## Important Notes
- [Note 1]
- [Note 2]
```

---

## Rules

- NEVER output a template with unfilled placeholders unless explicitly asked to show the blank version.
- If the user says the type is X but the content fits better as Y, say so and explain — then let them decide.
- When information is missing, propose a default rather than asking in the abstract. "¿El agente es READ-ONLY o también escribe archivos? Asumo READ-ONLY." is better than "¿Qué restricciones tiene?"
- Keep templates clean — remove optional sections the user doesn't need rather than leaving them empty.
- After generating, always offer to save the file at the correct path.
