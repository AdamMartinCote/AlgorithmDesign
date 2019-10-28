from typing import List

from src.algorithms.basealgo import BaseAlgo
from src.cut import Cut
from src.roll import Roll


class Greedy(BaseAlgo):
    def optimize_exemplaire(self, roll: Roll) -> List[Cut]:
        return roll.cuts[:2]

