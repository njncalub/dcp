import pytest

from dataclasses import dataclass
from typing import List, Tuple

from solution import solve


@dataclass
class Case:
    args: Tuple[List[int], int]
    answer: bool


def test_solve():
    cases: List[Case] = [
        Case(([10, 15, 3, 7], 17), True),
        Case(([-10, -15, -3, -7], -25), True),
        Case(([3, 3, 3, 9], 9), False),
        Case(([3, 3, 0, 9], 9), True),
        Case(([], 17), False),
    ]

    for c in cases:
        assert solve(*c.args) == c.answer
