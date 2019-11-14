from re import sub
from typing import List
from unittest import TestCase

from src.roll import Roll
from test.utils import capture_output


class TestBase(TestCase):
    def get_solution_from_examplaire_path(self, path: str) -> List[int]:
        roll = Roll(path)
        with capture_output() as (out, err):
            self.algo(roll)

        solution_list = out.getvalue().split()
        values = list(map(lambda x: int(sub(r'\D', '', x)), solution_list))
        return values
