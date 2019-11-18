from typing import List
from unittest import TestCase

from src.algorithms.dynamic import Dynamic
from src.algorithms.greedy import Greedy
from src.algorithms.solution import Solution
from src.roll import Roll

exemplaires_paths: List[str] = [
    '../exemplaires/10-1.txt',
    '../exemplaires/10-2.txt',
    '../exemplaires/10-3.txt',
    '../exemplaires/10-4.txt',
    '../exemplaires/10-5.txt',
    '../exemplaires/10-6.txt',
    '../exemplaires/10-7.txt',
    '../exemplaires/10-8.txt',
    '../exemplaires/10-9.txt',
    '../exemplaires/10-10.txt',
    '../exemplaires/100-1.txt',
    '../exemplaires/100-2.txt',
    '../exemplaires/100-3.txt',
    '../exemplaires/100-4.txt',
    '../exemplaires/100-5.txt',
    '../exemplaires/100-6.txt',
    '../exemplaires/100-7.txt',
    '../exemplaires/100-8.txt',
    '../exemplaires/100-9.txt',
    '../exemplaires/100-10.txt',
    '../exemplaires/1000-1.txt',
    '../exemplaires/1000-4.txt',
    '../exemplaires/1000-8.txt',
    '../exemplaires/1000-1.txt',
    '../exemplaires/4000-2.txt',
    '../exemplaires/4000-3.txt',
    '../exemplaires/4000-4.txt',
    '../exemplaires/4000-5.txt',
]


class TestCoherence(TestCase):
    def setUp(self) -> None:
        self.options = {'display_time': False,
                        'display_price': False,
                        'display_solution': False}

        self.algo = None

    def test_dynamic_better_than_greedy(self):
        """ Ensure the DP algo alway yield equal or better results than the Greedy one"""

        for exemplaire_path in exemplaires_paths:
            self.roll = Roll(exemplaire_path)

            self.algo = Greedy(**self.options)
            greedy_solution: Solution = self.algo(self.roll)

            self.algo = Dynamic(**self.options)
            dp_solution: Solution = self.algo(self.roll)

            # print(f"greedy={greedy_solution.value}, dyn={dp_solution.value}")
            self.assertGreaterEqual(dp_solution.value, greedy_solution.value)
