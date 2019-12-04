from typing import List


class Card:
    idx: int
    base_value: int
    synergy: List[int]

    def __init__(self, idx, base_value, synergy: List[int]):
        self.idx = idx
        self.base_value = base_value
        self.synergy = synergy

    def __str__(self):
        return str(self.idx)
