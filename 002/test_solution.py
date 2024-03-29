import pytest

from dataclasses import dataclass
from typing import List

from solution import solve


@dataclass
class Case:
    arg: List[int]
    want: List[int]


def test_solve():
    cases: List[Case] = [
        Case([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        Case([3, 2, 1], [2, 3, 6]),
        Case([0, 3, 5, 7], [105, 0, 0, 0]),
        Case([-1, 3, -2, 1], [-6, 2, -3, 6]),
        Case([0, 1, 2, 3, 4], [24, 0, 0, 0, 0]),
        Case([3, 7, 1, 4, 8, 9], [2016, 864, 6048, 1512, 756, 672]),
        Case([], []),
    ]

    for c in cases:
        assert solve(c.arg) == c.want
