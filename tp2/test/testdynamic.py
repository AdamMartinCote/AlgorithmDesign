import unittest

from src.algorithms.dynamic import Dynamic
from src.algorithms.greedy import Greedy
from src.roll import Roll
from test.utils import capture_output


class TestDynamicAlgo(unittest.TestCase):
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

    @unittest.skip
    def test_4000_3(self):
        roll = Roll('../exemplaires/4000-3.txt')
        algo = Dynamic(**self.price_option)
        with capture_output() as (out, err):
            algo(roll)
        self.assertEqual('15982\n', out.getvalue())

    @unittest.skip
    def test_30000_1(self):
        roll = Roll('../exemplaires/30000-1.txt')
        algo = Dynamic(**self.price_option)
        with capture_output() as (out, err):
            algo(roll)
        self.assertEqual('119962\n', out.getvalue())
