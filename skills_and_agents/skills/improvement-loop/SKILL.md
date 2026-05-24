---
name: improvement-loop
description: "Trigger: /improvement-loop or improvement, error pattern, recurring error, mejora continua. Capture repeated errors, identify root cause, and propose rules/checklists to prevent recurrence."
disable-model-invocation: true
user-invocable: false
license: MIT
metadata:
  author: gentleman-programming
  version: "1.0"
  delegate_only: true
---

> **ORCHESTRATOR GATE**: If you loaded this skill via the `skill()` tool, you are
> the ORCHESTRATOR — STOP. Execute the improvement analysis yourself. Delegate
> pattern search if needed (scanning history).

## Purpose

Convert repeated errors into operational learning.
When the same error appears multiple times, capture it, diagnose root cause,
and create a guard to prevent it from happening again.

## When to Invoke

| Trigger | Action |
|---------|--------|
| User says `/improvement-loop` | Start improvement analysis |
| Same error appears repeatedly | Suggest `/improvement-loop` |
| Review keeps rejecting for same reason | Capture pattern |
| After a rollback or incident | Run improvement loop |
| User says "esto ya pasó antes" | Trigger improvement loop |

## Workflow

### Phase 1: Capture the Error

Ask the user:
- What error or failure occurred?
- What was the context (change, environment, timing)?
- How many times has this happened?
- Was there a previous fix? Did it work?

### Phase 2: Classify the Pattern

| Pattern Category | Examples |
|-----------------|----------|
| 🏗 **Architecture** | Wrong layer, circular dependency, missing abstraction |
| 🏷 **Naming** | Inconsistent names, misleading terms, wrong conventions |
| ✅ **Validation** | Missing null check, wrong type, unvalidated input |
| 🔒 **Security** | Missing auth, exposed secrets, weak config |
| 🧪 **Testing** | Missing coverage, wrong assertion, flaky test |
| 📖 **Documentation** | Outdated docs, missing README, wrong example |
| ⚙️ **Config** | Wrong env var, incorrect setting, missing flag |
| 🔄 **Process** | Missing review, skipped step, wrong order |

### Phase 3: Diagnose Root Cause

Ask "why" until you reach the root (5 Whys technique):
1. Why did the error occur? → {answer}
2. Why did that happen? → {deeper answer}
3. Why? → ...
4. Why? → ...
5. Why? → {root cause}

### Phase 4: Propose Prevention

Based on root cause, propose ONE of:

| Solution | When |
|----------|------|
| **New rule** | Pattern needs explicit enforcement |
| **Checklist item** | Step that should be in review checklist |
| **Process change** | Workflow missing a phase or gate |
| **Skill update** | Existing skill needs better guidance |
| **Validation script** | Automated guard for the pattern |

### Phase 5: Generate Improvement

```markdown
## Improvement Loop

### Error Pattern
{description of the repeated error}

### Occurrences
- {date/context 1}
- {date/context 2}

### Root Cause
{5 Whys analysis}

### Proposed Fix
- **Type**: {rule | checklist | process | skill | validator}
- **Detail**: {what needs to change}
- **Location**: {where it should live}

### Implementation
{how to implement the fix — actionable steps}

### Verification
{how to confirm the fix works}
```

## Rules

- ALWAYS classify the pattern — don't treat unique errors as patterns
- Require at least 2 occurrences before creating a rule
- Use 5 Whys to find root cause, not surface symptom
- Propose ONE concrete fix, not a list of maybes
- If the fix is a new rule, include the exact rule text
- Return envelope per **Section D** from `skills/_shared/sdd-phase-common.md`

## References

- `local-retrospective` skill — for capturing broader session learnings
- `change-review` skill — where patterns often surface first
