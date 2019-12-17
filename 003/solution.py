class Node:
    """Represents a node in a binary tree."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(N: Node) -> str:
    """Returns a string serialization for the given node N.

    Args:
        N: the Node to be serialized to a string

    Returns:
        A stringified representation of a Node object.
    """

    return ''


def deserialize(S: str) -> Node:
    """Returns a new Node parsed from a string S.

    Args:
        S: the stringified representation of a Node object.

    Returns:
        A Node parsed from the string S.
    """

    return Node('')
