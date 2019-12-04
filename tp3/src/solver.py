from tp3.src.card import Card
from tp3.src.deck import Deck
from tp3.src.exemplaire import Exemplaire
from tp3.src.solution import Solution
from copy import deepcopy


def make_solution(exemplaire: Exemplaire) -> Solution:
    solution = Solution()
    for i in range(0, exemplaire.nDecks):
        deck = Deck()
        for j in range(0, exemplaire.nCards):
            flat_idx = (i * 10) + j
            deck.cards.append(Card(idx=flat_idx,
                                   base_value=exemplaire.baseQuality[flat_idx]))
        solution.decks.append(deepcopy(deck))
    return solution