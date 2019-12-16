import pytest

from dataclasses import dataclass
from typing import List

from solution import solve


@dataclass
class Case:
    arg: List[int]
    answer: List[int]


def test_solve():
    cases: List[Case] = [
        Case([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        Case([3, 2, 1], [2, 3, 6]),
        Case([0, 3, 5, 7], [105, 0, 0, 0]),
        Case([-1, 3, -2, 1], [-6, 2, -3, 6]),
        Case([0, 1, 2, 3, 4], [24, 0, 0, 0, 0]),
        Case([], []),
    ]

    for c in cases:
        assert solve(c.arg) == c.answer
