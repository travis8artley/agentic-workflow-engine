from dataclasses import dataclass, field


@dataclass
class StateStore:
    events: list[dict] = field(default_factory=list)

    def record(self, event: dict) -> None:
        self.events.append(event)

    def all(self) -> list[dict]:
        return list(self.events)
