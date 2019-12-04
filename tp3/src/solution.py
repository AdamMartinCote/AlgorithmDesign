from typing import List

from tp3.src.deck import Deck


class Solution:
    decks: List[Deck]

    def __init__(self):
        self.decks = []

    def __str__(self):
        return '\n'.join(map(str, self.decks))
