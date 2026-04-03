# Decisions

## ADR-001: Explicit planner/executor separation

- Status: accepted
- Decision: Keep planning and execution modules independent.
- Why: Allows pluggable execution backends without planner rewrites.

## ADR-002: State-first orchestration output

- Status: accepted
- Decision: Return both raw results and aggregate summary.
- Why: Supports debugging and dashboard reporting simultaneously.

## ADR-003: Keep orchestration deterministic by default

- Status: accepted
- Decision: Execute tasks in plan order for baseline reproducibility.
- Why: Simplifies tracing and regression testing before concurrency is introduced.
