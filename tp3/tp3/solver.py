from copy import deepcopy
from itertools import combinations
from typing import List, Tuple

from tp3.card import Card
from tp3.deck import Deck
from tp3.exemplaire import Exemplaire
from tp3.pair import Pair
from tp3.solution import Solution


class Solver:
    def __init__(self, exemplaire: Exemplaire):
        self.exemplaire = exemplaire

    def __call__(self) -> Solution:
        # return self.build_deck_in_order()
        return self.build_decks_by_layer()

    def generate_pairs(self, cards: List[Card]) -> List[Pair]:
        return [Pair(*pair) for pair in combinations(cards, 2)]

    def evaluate_deck_synergy(self, deck: Deck, exemplaire: Exemplaire) -> int:
        pairs = self.generate_pairs(deck.cards)
        synergy = 0
        for pair in pairs:
            synergy += exemplaire.get_synergy_by_idx(pair[0].idx, pair[1].idx)
        return synergy

    def evaluate_pair_value(self, id1: int, id2: int):
        return self.exemplaire.baseQuality[id1] + \
               self.exemplaire.baseQuality[id2] + \
               self.exemplaire.get_synergy_by_idx(id1, id2)

    def build_decks_by_layer(self) -> Solution:
        cards = [Card(idx=i,
                      base_value=self.exemplaire.baseQuality[i],
                      synergy=self.exemplaire.synergyMatrix[i])
                 for i in range(self.exemplaire.nCards * self.exemplaire.nDecks)]
        pairs = [Pair(cards[i], cards[i + 1]) for i in range(0, len(cards) - 1, 2)]
        sorted_pairs = sorted(pairs, key=lambda x: x.get_value())

        decks = [Deck() for _ in range(self.exemplaire.nDecks)]
        skip = 0
        for i, pair in enumerate(sorted_pairs):
            insert_index = i + skip
            deck = decks[insert_index % self.exemplaire.nDecks]
            deck.cards.append(pair[0])
            if len(deck.cards) < self.exemplaire.nCards:
                deck.cards.append(pair[1])
            else:
                decks[(insert_index % self.exemplaire.nDecks) + 1].cards.append(pair[1])
                skip += 1

        solution = Solution()
        solution.decks = decks
        return solution

    def build_deck_in_order(self) -> Solution:
        solution = Solution()
        for i in range(0, self.exemplaire.nDecks):
            deck = Deck()
            for j in range(0, self.exemplaire.nCards):
                flat_idx = (i * self.exemplaire.nCards) + j
                deck.cards.append(Card(idx=flat_idx,
                                       base_value=self.exemplaire.baseQuality[flat_idx],
                                       synergy=self.exemplaire.synergyMatrix[flat_idx]))
            # print(f'deck synergy: {self.evaluate_deck_synergy(deck, self.exemplaire)}')
            solution.decks.append(deepcopy(deck))
        return solution
