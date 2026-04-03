from dataclasses import dataclass

@dataclass
class Task:
    id: str
    description: str


def create_plan(goal: str) -> list[Task]:
    return [Task(id="t1", description=f"analyze: {goal}"), Task(id="t2", description="execute subtasks")]
