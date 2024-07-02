from dataclasses import dataclass


@dataclass
class Player:
    id: int
    name: str
    media: float


    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.id} - {self.name}"