# Provenance

## Observation

Most agent systems lose decision context extremely quickly.

A user sees:

- final output
- maybe a tool call
- maybe partial chain-of-thought summaries

But not:

- which information influenced a decision
- which assumptions changed over time
- which retrieved context mattered
- what the agent believed at each stage

## Hypothesis

Provenance should be treated as a runtime primitive.

Not logging.

Not observability.

A first-class execution structure.

## Possible primitives

### Decision nodes

Every material agent decision becomes a node.

Node fields:

- intent
- rationale
- evidence
- upstream dependencies
- resulting mutations

### Semantic diffs

Not only file diffs.

Need:

- assumption diffs
- plan diffs
- memory diffs
- policy diffs

### Replayability

A human should be able to replay:

- context retrieval
- transformations
- policy checks
- state transitions

## Open question

Can provenance become the equivalent of git history for agent cognition?
