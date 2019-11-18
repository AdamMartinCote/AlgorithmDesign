from unittest import TestCase

from src.algorithms.backtracking import Backtracking
from src.algorithms.greedy import Greedy
from src.roll import Roll
from test.utils import capture_output


class TestBacktracking(TestCase):
    def setUp(self) -> None:
        self.path_1 = '../exemplaires/4000-3.txt'
        self.price_option = {'display_time': False,
                             'display_price': True,
                             'display_solution': False}
        self.solution_option = {'display_time': False,
                                'display_price': False,
                                'display_solution': True}
        self.roll = Roll(self.path_1)

    def test_4000_3(self):
        self.algo = Backtracking(**self.solution_option)
        with capture_output() as (out, err):
            self.algo(self.roll)
        self.assertEqual('[1139, 1139, 1139, 252, 252, 47, 25, 2, 2, 2, 1]\n', out.getvalue())
