from typing import List

from src.algorithms.abstractbasealgo import AbstractBaseAlgo
from src.cut import Cut
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

    def execute(self, roll: Roll) -> List[Cut]:
        paths: List[List[Cut]] = [[]]
        r: List[int] = [0]

        def add_row(j: int) -> None:
            max_r: int = -1
            max_i: int = 0
            for i in range(1, j + 1):
                possible_cut = roll.cuts[i - 1]
                local_r = possible_cut.p_i + r[j - i]
                if local_r > max_r:
                    max_r = local_r
                    max_i = i
            paths.append(paths[j - max_i] + [roll.cuts[max_i - 1]])
            r.append(max_r)

        for j in range(1, roll.size + 1):
            add_row(j)

        return list(reversed(paths[-1]))
