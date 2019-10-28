from src.algorithms.abstractbasealgo import AbstractBaseAlgo
from src.roll import Roll


class Dynamic(AbstractBaseAlgo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, roll: Roll):
        raise NotImplemented
