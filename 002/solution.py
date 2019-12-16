from typing import List

def solve(N: List[int]) -> List[int]:
    """Returns a list of products, excluding the element at position i.

    Args:
        N: a list of integers

    Returns:
        A list where each element at index i is the product of all the numbers
        in the original list, except the one at i.
    """

    # Brute force approach using O(n(n-1)):
    # - Loop through all numbers n of N
    # - Generate a new array without n and multiply all the items in that array
    # - Append the product to the solution set
    # - If we passed a zero, it means the rest would have a product of 0

    answer = []
    for index in range(len(N)):
        product = 1
        for i, n in enumerate(N):
            if i != index:
                product *= n
            # If the product is already zero, we need not continue any further.
            if product == 0:
                break

        answer.append(product)

        # If there is a zero from this point onwards,
        # everything else would be zero.
        if N[index] == 0:
            answer += [0 for _ in range(index+1, len(N))]
            break

    return answer
