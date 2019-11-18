from typing import List

from src.algorithms.abstractbasealgo import AbstractBaseAlgo
from src.algorithms.greedy import Greedy
from src.cut import Cut
from src.roll import Roll


class Backtracking(AbstractBaseAlgo):
    """

    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, roll: Roll) -> List[Cut]:

        best_path = self.explore_childs(roll=roll,
                                        current_path=[],
                                        best_path=[])
        return best_path

    def explore_childs(self, roll: Roll,
                       current_path: List[Cut],
                       best_path: List[Cut]) -> List[Cut]:
        length_left = roll.size - sum(map(lambda x: x.i, current_path))
        possible_cuts = list(filter(lambda x: x.i <= length_left, roll.cuts[1:]))

        # if len(list(possible_cuts)) == 0:
        if length_left == 0:
            current_val = Backtracking.get_path_value(current_path)
            best_val = Backtracking.get_path_value(best_path)

            return best_path if best_val > current_val else current_path

        for child in possible_cuts:
            best_path = self.explore_childs(roll=roll,
                                            current_path=current_path + [child],
                                            best_path=best_path)

        return best_path

    @staticmethod
    def get_path_value(path: List[Cut]):
        return sum(map(lambda x: x.p_i, path))
