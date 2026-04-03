# Architecture

```mermaid
flowchart LR
  A["Goal"] --> B["Planner.create_plan"]
  B --> C["Executor.run_task"]
  C --> D["StateStore.record"]
  D --> E["Summarize"]
  E --> F["Result envelope"]
```

## Component Responsibilities

- `planner`: task decomposition from goal to executable units.
- `executor`: unit execution contract.
- `state`: event/result persistence during a run.
- `engine`: orchestration and summary shaping.

## Extension Points

- Replace in-memory store with durable store.
- Swap executor backend for remote workers.
- Add retry and timeout policies per task type.
