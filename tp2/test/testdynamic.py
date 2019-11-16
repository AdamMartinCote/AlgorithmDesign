from unittest import TestCase, skip

from src.algorithms.dynamic import Dynamic
from src.algorithms.solution import Solution
from src.roll import Roll
from test.utils import capture_output


class TestDynamicAlgo(TestCase):
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

    @skip("too long")
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
