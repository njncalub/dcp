from typing import List


def solve(N: List[int], K: int) -> bool:
    """Returns whether any two numbers from list N adds up to K.

    Args:
        N: a list of integers
        K: a number that two numbers should add up to

    Returns:
        True if any two numbers from N adds up to K, otherwise, returns False
    """

    searched = set()
    for n in N:
        if K - n in searched:
            return True
        searched.add(n)

    return False
