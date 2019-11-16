import unittest
from typing import List

from src.algorithms.dynamic import Dynamic
from src.algorithms.solution import Solution
from src.cut import Cut
from src.roll import Roll
from test.testbase import TestBase
from test.utils import capture_output


class TestDynamicAlgo(TestBase):
    def setUp(self) -> None:
        self.path_1 = '../exemplaires/4000-3.txt'
        self.path_1 = '../exemplaires/100-1.txt'
        self.price_option = {'display_time': False,
                             'display_price': True,
                             'display_solution': False}
        self.solution_option = {'display_time': False,
                                'display_price': True,
                                'display_solution': False}
        self.roll = Roll(self.path_1)

    def test_solution_total_equals_n(self):
        """
        sanity check
        """
        self.algo = Dynamic(**self.solution_option)
        solution_4000 = self.get_solution_from_examplaire_path('../exemplaires/4000-2.txt')
        self.assertEqual(4000, sum(solution_4000))

        solution_1000 = self.get_solution_from_examplaire_path('../exemplaires/1000-7.txt')
        self.assertEqual(1000, sum(solution_1000))

        solution_400 = self.get_solution_from_examplaire_path('../exemplaires/400-1.txt')
        self.assertEqual(400, sum(solution_400))

    def test_4000_3(self):
        expected = [1, 2, 1139, 1363, 1495]
        roll = Roll('../exemplaires/4000-3.txt')
        algo = Dynamic(**self.price_option)
        solution: Solution
        with capture_output() as (out, err):
            solution = algo(roll)
        self.assertEqual('15982\n', out.getvalue())
        self.assertEqual(str(expected),
                         str(solution))

    def test_30000_1(self):
        expected = [4, 6590, 11362, 12044]
        roll = Roll('../exemplaires/30000-1.txt')
        algo = Dynamic(**self.price_option)
        solution: Solution
        with capture_output() as (out, err):
            solution = algo(roll)
        self.assertEqual('119962\n', out.getvalue())
        self.assertEqual(str(expected),
                         str(solution))
