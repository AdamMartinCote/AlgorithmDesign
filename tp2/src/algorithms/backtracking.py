from src.algorithms.basealgo import BaseAlgo
from src.roll import Roll


class Backtracking(BaseAlgo):
    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def execute(self, roll: Roll):
        raise NotImplemented
