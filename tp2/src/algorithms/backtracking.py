from typing import List

from src.algorithms.abstractbasealgo import AbstractBaseAlgo
from src.algorithms.greedy import Greedy
from src.algorithms.solution import Solution
from src.cut import Cut
from src.roll import Roll


class Backtracking(AbstractBaseAlgo):
    """

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, roll: Roll) -> List[Cut]:
        greedy = Greedy()
        initial_solution: Solution = greedy(roll)
        visited: List[Cut] = initial_solution.choices[:]

        value: int = initial_solution.value
        stack: List[Cut] = initial_solution.choices

        return initial_solution.choices

    @staticmethod
    def _upper_bound(self, roll: Roll, stack: List[Cut], visited: List[Cut]) -> float:
        """
        using bound A)
        """
        current_val = sum(map(lambda x: x.p_i, stack))
        length_left = sum(map(lambda x: x.i, stack)) - roll.size

        possible_cuts: List[Cut] = list(filter(lambda c: c.i <= length_left and c not in visited,
                                               roll.cuts))
        value_density = max(map(lambda x: x.p_i / x.i, possible_cuts))

        return current_val + length_left * value_density
