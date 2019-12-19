import pytest

from dataclasses import dataclass
from typing import List

from solution import solve


@dataclass
class Case:
    arg: List[int]
    want: int


def test_solve():
    cases: List[Case] = [
        Case([3, 4, -1, 1], 2),
        Case([1, 2, 0], 3),
        Case([2, 0, -10, 0, 1, 1, 1, 2], 3),
        Case([0], 1),
        Case([-1], 1),
    ]

    for c in cases:
        assert solve(c.arg) == c.want
