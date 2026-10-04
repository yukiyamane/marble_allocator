from typing import Any
import random

class LoggedRNG:
    def __init__(self, seed: int, name: str):
        self.rng = random.Random(seed)
        self.name = name
        self.log = []

    def randint(self, a: int, b: int) -> int:
        value = self.rng.randint(a, b)
        self.log.append((self.name, "randint", (a, b), value))
        return value

    def random(self) -> float:
        value = self.rng.random()
        self.log.append((self.name, "random", None, value))
        return value

    def choice(self, seq: list[Any]) -> Any:
        value = self.rng.choice(seq)
        self.log.append((self.name, "choice", seq, value))
        return value

seed_base = 999
battle_randomizer = random.Random(seed_base + 1)
fx_randomizer = random.Random(seed_base + 2)