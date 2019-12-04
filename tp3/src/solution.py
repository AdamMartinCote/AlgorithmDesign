from typing import List


class Solution:
    decks: List[List[int]]

    def __init__(self):
        self.decks = []

    def __str__(self):
        return str([val for deck in self.decks for val in deck])
