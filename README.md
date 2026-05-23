# Crucible

Crucible is an experimental sandbox runtime for AI agents.

The core idea is simple:

> Agents should not directly mutate real systems. They should propose, simulate, verify, and only then commit.

Crucible treats agent actions like reviewable changes. An agent proposes an operation, the runtime executes it in an isolated workspace, records a trace, checks policy, shows a diff, and waits for human approval before touching the source of truth.

## Why this exists

Modern agents are getting better at planning and tool use, but most systems still give them production-like credentials too early. That creates a missing layer between intention and execution.

Crucible explores that missing layer:

- sandboxed execution
- reversible file diffs
- policy checks before commit
- provenance traces for every action
- human review as a first-class primitive
- replayable agent decisions

The first target is deliberately small: file-based project work.

## v0 demo flow

```bash
crucible propose "Split the MVP into three milestones"
crucible simulate
crucible diff
crucible verify
crucible approve
```

## Research question

> What runtime primitives make agent actions inspectable, reversible, governable, and safe enough for human collaboration?
