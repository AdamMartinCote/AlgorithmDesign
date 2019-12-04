from copy import deepcopy
from typing import List, Tuple

from tp3.card import Card
from tp3.deck import Deck
from tp3.exemplaire import Exemplaire
from tp3.solution import Solution


class Solver:
    def __init__(self, exemplaire: Exemplaire):
        self.exemplaire = exemplaire

    def __call__(self) -> Solution:
        solution = Solution()
        for i in range(0, self.exemplaire.nDecks):
            deck = Deck()
            for j in range(0, self.exemplaire.nCards):
                flat_idx = (i * self.exemplaire.nCards) + j
                deck.cards.append(Card(idx=flat_idx,
                                       base_value=self.exemplaire.baseQuality[flat_idx]))
            print(f'deck synergy: {self.evaluate_deck_synergy(deck, self.exemplaire)}')
            solution.decks.append(deepcopy(deck))
        return solution

    def generate_couples(self, cards: List[Card]) -> List[Tuple[Card, Card]]:
        it = iter(cards)
        return list(zip(it, it))

    def evaluate_deck_synergy(self, deck: Deck, exemplaire: Exemplaire) -> int:
        pairs = self.generate_couples(deck.cards)
        synergy = 0
        for pair in pairs:
            synergy += exemplaire.get_synergy_by_idx(pair[0].idx, pair[1].idx)
        return synergy
