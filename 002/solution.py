from typing import List


def solve(N: List[int]) -> List[int]:
    """Returns a list of products, excluding the element at position i.

    Args:
        N: a list of integers

    Returns:
        A list where each element at index i is the product of all the numbers
        in the original list, except the one at i.
    """

    return two_loops(N)


def brute_force(N: List[int]) -> List[int]:
    """Brute force approach using O(n(n-1)):

    - Loop through all numbers n of N
    - Generate a new array without n and multiply all the items in that array
    - Append the product to the solution set
    - If we passed a zero, it means the rest would have a product of 0
    """

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


def two_loops(N: List[int]) -> List[int]:
    """Semi-dynamic programming approach using O(2n):

    - Calculate the product of all items before item i
    - Calculate the product of all items after item i
    - For each item i, multiply the products for before and after i

    L[i] = N[i-1] * L[i-1] if i != 0 else 1
    R[j] = N[j+1] * R[j+1] if j != (len(N) - 1) else 1
    A[i] = L[i] * R[i]

    N[0] = 3
    N[1] = 7
    N[2] = 1
    N[3] = 4
    N[4] = 8
    N[5] = 9

    L[0] = 1 = 1
    L[1] = (1) * 3 = 3
    L[2] = (3) * 7 = 21
    L[3] = (21) * 1 = 21
    L[4] = (21) * 4 = 84
    L[5] = (84) * 8 = 672

    R[5] = 1 = 1
    R[4] = (1) * 9 = 9
    R[3] = (9) * 8 = 72
    R[2] = (72) * 4 = 288
    R[1] = (288) * 1 = 288
    R[0] = (288) * 7 = 2016

    A = [L[0]*R[0], L[1]*R[1], L[2]*R[2], L[3]*R[3], L[4]*R[4], L[5]*R[5]]
    A = [2016, 864, 6048, 1512, 756, 672]
    """

    items_len = len(N)
    of_left = [1 for _ in range(items_len)]
    of_right = [1 for _ in range(items_len)]
    for i in range(items_len):
        j = (items_len - 1) - i  # Invert i; start counting from len(N) to 0.
        of_left[i] = N[i-1] * of_left[i-1] if i != 0 else 1
        of_right[j] = N[j+1] * of_right[j+1] if i != 0 else 1

    return list(map(lambda p: p[0] * p[1], zip(of_left, of_right)))
