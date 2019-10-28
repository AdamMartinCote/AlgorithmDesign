from functools import reduce
from typing import List

from src.algorithms.basealgo import BaseAlgo
from src.cut import Cut
from src.roll import Roll


class Greedy(BaseAlgo):
    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def execute(self, roll: Roll) -> List[Cut]:
        """
        returns the optimal list of cuts according to this algorithm
        """
        def get_best(acc: Cut, cut: Cut):
            return cut if cut.r_i > acc.r_i else acc

        roll_length_left = roll.size

        solution: List[Cut] = []
        while roll_length_left > 0:
            possible_cuts = roll.cuts[:roll_length_left]
            best_cut: Cut = reduce(get_best, possible_cuts, possible_cuts[0])
            solution.append(best_cut)
            roll_length_left -= best_cut.i

        return solution

