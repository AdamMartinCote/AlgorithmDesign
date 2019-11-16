import time
from functools import reduce
from typing import List, Tuple

from src.algorithms.solution import Solution
from src.cut import Cut
from src.roll import Roll


class AbstractBaseAlgo:
    def __init__(self, display_solution=False, display_price=False, display_time=False):
        self.display_solution = display_solution
        self.display_price = display_price
        self.display_time = display_time

    def __call__(self, roll: Roll) -> Solution:
        start_time = time.time()
        cuts: List[Cut] = self.execute(roll)
        end_time = time.time()

        if self.display_solution:
            print(list(map(lambda x: x.i, cuts)))

        if self.display_price:
            total_price = reduce(lambda acc, x: acc + x,
                                 map(lambda x: x.p_i,
                                     cuts))
            print(total_price)

        if self.display_time:
            print(end_time - start_time)

        return Solution(choices=cuts)

    def execute(self, roll: Roll) -> List[Cut]:
        raise NotImplemented("class is abstract")
