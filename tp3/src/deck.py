from typing import List

from tp3.src.card import Card


class Deck:
    cards: List[Card]

    def __init__(self):
        self.cards = []

    def __str__(self):
        return str(' '.join(map(str, self.cards)))
