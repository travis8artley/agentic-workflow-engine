from planner.plan import create_plan
from executor.run import run_task


def run(goal: str) -> list[dict]:
    plan = create_plan(goal)
    return [run_task(t.id) for t in plan]
