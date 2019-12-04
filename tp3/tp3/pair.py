from tp3.card import Card


class Pair:
    def __init__(self, card1, card2):
        self.cards = (card1, card2)
        self.value = None

    def __getitem__(self, item):
        return self.cards[item]

    def get_value(self):
        if self.value is None:
            self.value = self.evaluate_pair_value(*self.cards)
        return self.value

    def evaluate_pair_value(self, card1: Card, card2: Card):
        return card1.base_value + card2.base_value + card1.synergy[card2.idx]
