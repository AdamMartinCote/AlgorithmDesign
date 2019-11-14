from typing import List

from src.algorithms.abstractbasealgo import AbstractBaseAlgo
from src.roll import Roll


class Dynamic(AbstractBaseAlgo):
    """
    L'algorithme de programmation dynamique remplit un tableau des revenus
    optimaux en fonction de la longueur du rouleau. Pour cet algorithme,
    nous ajoutons une coupe de taille 0 ayant un prix de 0. Soit un tableau
    r représentant le prix le plus haut auquel on peut vendre un rouleau de
    taille j (j = 0, ..., n), et pi (i = 0, ..., n) le prix d’une coupe de
    taille i. La relation de récurrence est :

        r0 = p0 = 0
        rj = maxi=1,...,j {pi + rj-i}, pour j > 0

    La solution se trouve en rn.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, roll: Roll):

        j: int = roll.size
        r: List[int]

        raise NotImplementedError
