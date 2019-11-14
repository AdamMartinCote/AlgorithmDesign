from src.algorithms.greedy import Greedy
from src.roll import Roll
from test.testbase import TestBase
from test.utils import capture_output


class TestGreedyAlgo(TestBase):
    def setUp(self) -> None:
        self.path_1 = '../exemplaires/4000-3.txt'
        self.price_option = {'display_time': False,
                             'display_price': True,
                             'display_solution': False}
        self.solution_option = {'display_time': False,
                                'display_price': False,
                                'display_solution': True}
        self.roll = Roll(self.path_1)

    def test_specific(self):
        self.algo = Greedy(**self.solution_option)
        with capture_output() as (out, err):
            self.algo(self.roll)
        self.assertEqual('[1139, 1139, 1139, 252, 252, 47, 25, 2, 2, 2, 1]\n', out.getvalue())

    def test_solution_total_equals_n(self):
        """
        sanity check
        """
        self.algo = Greedy(**self.solution_option)
        solution_4000 = self.get_solution_from_examplaire_path('../exemplaires/4000-2.txt')
        self.assertEqual(4000, sum(solution_4000))

        solution_1000 = self.get_solution_from_examplaire_path('../exemplaires/1000-7.txt')
        self.assertEqual(1000, sum(solution_1000))

        solution_400 = self.get_solution_from_examplaire_path('../exemplaires/400-1.txt')
        self.assertEqual(400, sum(solution_400))
