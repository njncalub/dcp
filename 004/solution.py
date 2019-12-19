from typing import List


def solve(numbers: List[int]) -> int:
    """Returns the lowest positive integer that does not exist in the array.

    Args:
        numbers: a list of positive or negative integers.
    
    Returns:
        The lowest positive integer that does not exist in the array.
    """

    numbers.sort()

    previous = 0
    for n in (n for n in numbers if n > 0):
        want = previous + 1
        if n in {previous, want}:
            previous = n
        else:
            return previous + 1

    return previous + 1
