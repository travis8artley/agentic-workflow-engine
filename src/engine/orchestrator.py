from planner.plan import create_plan
from executor.run import run_task
from state.store import StateStore
from engine.summarize import summarize


def run(goal: str) -> dict:
    plan = create_plan(goal)
    store = StateStore()
    for task in plan:
        result = run_task(task.id)
        store.record(result)
    return {
        "results": store.all(),
        "summary": summarize(store.all()),
    }
