import pytest

from solution import Node, serialize, deserialize
from typing import List

from dataclasses import dataclass


def test_serialize():
    @dataclass
    class Case:
        arg: Node
        want: str

    cases: List[Case] = [
        Case(Node('P', Node('L', Node('L.L')), Node('R')), 'P,L,R,L.L'),
        Case(Node(''), ''),
    ]

    for c in cases:
        assert serialize(c.arg) == c.want


def test_deserialize():
    @dataclass
    class Case:
        arg: str
        want: Node

    cases: List[Case] = [
        Case('P,L,R,L.L', Node('P', Node('L', Node('L.L')), Node('R'))),
        Case('', Node('')),
    ]

    for c in cases:
        assert c.arg == serialize(deserialize(c.arg))
