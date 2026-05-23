# Crucible Thesis

## Premise

AI agents currently operate with an unsafe execution model.

The dominant architecture today is:

1. give model context
2. give model tools
3. allow direct execution

This collapses intention, simulation, verification, and commitment into a single step.

Humans do not build reliable systems this way.

## Hypothesis

Agent systems need execution runtimes, not just better models.

A useful runtime should support:

- isolated execution
- replayability
- provenance
- policy enforcement
- reversible state transitions
- human approval checkpoints

## Core abstraction

An agent action should behave more like a pull request than a shell command.

Desired lifecycle:

1. propose
2. simulate
3. verify
4. diff
5. approve
6. commit

## Initial scope

Crucible intentionally starts with files.

Why?

Because files already contain:

- state
- history
- collaboration
- review workflows
- semantic meaning

This lets us explore runtime primitives without hiding behind infrastructure complexity.

## Long-term direction

Potential future areas:

- WASM isolation
- capability-based permissions
- semantic diffs
- multi-agent collaboration
- branchable memory systems
- provenance graphs
- deterministic replay
- execution attestations
