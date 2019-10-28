from src.algorithms.basealgo import BaseAlgo
from src.roll import Roll


class Dynamic(BaseAlgo):
    def __init__(self, **kwargs):
        super().__init__(kwargs)

    def execute(self, roll: Roll):
        raise NotImplemented
