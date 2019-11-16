from typing import List

from src.cut import Cut


class Solution:
    choices: List[Cut]

    def __init__(self, choices: List[Cut]):
        self.choices = choices

    def __str__(self) -> str:
        return str(list(map(lambda choice: choice.i, self.choices)))

    @property
    def value(self):
        return sum(map(lambda choice: choice.p_i, self.choices))
