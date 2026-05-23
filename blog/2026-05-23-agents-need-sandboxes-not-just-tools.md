# Agents Need Sandboxes, Not Just Tools

Most AI agent systems today have an unsafe execution model.

The dominant architecture looks like this:

1. give model context
2. give model tools
3. allow direct execution

This collapses intention, simulation, verification, and commitment into a single step.

Humans do not build reliable systems this way.

Software engineering evolved safeguards for a reason:

- pull requests
- staging environments
- CI pipelines
- code review
- audit logs
- rollback systems

Modern agents bypass most of these primitives.

That works for toy demos.

It becomes dangerous once agents operate on:

- project plans
- shared knowledge
- APIs
- production infrastructure
- long-lived memory

## The missing layer

The problem is not just model intelligence.

The problem is execution architecture.

Agents need runtimes.

A runtime should separate:

- intention
- simulation
- verification
- commitment

An agent action should behave more like a pull request than a shell command.

## The Crucible model

Crucible explores a small execution loop:

```text
propose -> simulate -> verify -> diff -> approve -> commit
```

Instead of directly mutating state, an agent:

1. proposes a change
2. executes inside a sandbox
3. generates a trace
4. passes policy checks
5. waits for approval

The first implementation intentionally focuses only on files.

Files already contain:

- state
- history
- semantic meaning
- collaboration workflows

That makes them an ideal substrate for exploring agent runtime primitives.

## Why provenance matters

One of the hardest problems in agent systems is hidden mutable context.

Agents often:

- retrieve unknown context
- transform state invisibly
- overwrite prior assumptions
- lose decision history

Humans reviewing outputs cannot reconstruct:

- why a decision happened
- what information influenced it
- what changed over time

This is fundamentally a provenance problem.

Crucible treats provenance as a first-class primitive.

Every action should produce:

- intent
- rationale
- diff
- validation result
- execution trace
- approval history

## Research direction

I suspect the bottleneck for capable agents is no longer raw intelligence.

The bottleneck is governable execution.

The future probably needs:

- sandboxed execution
- capability-based permissions
- replayable state transitions
- semantic diffs
- provenance graphs
- collaborative memory systems

Crucible is an attempt to explore these ideas from the smallest useful starting point.
