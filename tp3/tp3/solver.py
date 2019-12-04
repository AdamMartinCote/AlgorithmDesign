from copy import deepcopy

from tp3.card import Card
from tp3.deck import Deck
from tp3.exemplaire import Exemplaire
from tp3.solution import Solution


def make_solution(exemplaire: Exemplaire) -> Solution:
    solution = Solution()
    for i in range(0, exemplaire.nDecks):
        deck = Deck()
        for j in range(0, exemplaire.nCards):
            flat_idx = (i * exemplaire.nCards) + j
            deck.cards.append(Card(idx=flat_idx,
                                   base_value=exemplaire.baseQuality[flat_idx]))
        solution.decks.append(deepcopy(deck))
    return solution
