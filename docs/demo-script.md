# First Runnable Demo

## Setup

```bash
pip install -e .
```

## Record a proposal

```bash
crucible propose "Split milestone 1 into setup and runtime"
```

Expected behavior:

- stores proposal metadata
- records timestamp
- persists proposal locally

## Run sandbox simulation

```bash
crucible simulate
```

Expected behavior:

- copies workspace into isolated sandbox
- modifies sandboxed file only
- records execution trace

## Show diff

```bash
crucible diff
```

Expected behavior:

- displays unified diff
- compares source-of-truth vs sandbox

## Verify policy

```bash
crucible verify
```

Expected behavior:

- loads YAML policy
- runs verification checks
- prints approval-ready result

## Core insight

The important idea is not the complexity.

The important idea is the runtime boundary.

Agent actions are treated as:

- sandboxed
- reviewable
- reversible
- traceable

instead of directly mutating state.
