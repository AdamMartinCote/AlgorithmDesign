import time
from functools import reduce

from src.roll import Roll


class AbstractBaseAlgo:
    def __init__(self, display_solution=False, display_price=False, display_time=False):
        self.display_solution = display_solution
        self.display_price = display_price
        self.display_time = display_time

    def optimize_exemplaire(self, roll: Roll):
        start_time = time.time()
        cuts = self.execute(roll)
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

    def execute(self, roll: Roll):
        raise NotImplemented("class is abstract")
