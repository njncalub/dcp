NODE_EMPTY_VALUE = '#'
NODE_VALUE_SEPARATOR = ','


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

    if not node:
        return NODE_EMPTY_VALUE

    return NODE_VALUE_SEPARATOR.join((node.val, serialize(node.left), serialize(node.right)))


def deserialize(S: str) -> Node:
    """Returns a new Node parsed from a string S.

    Args:
        S: the stringified representation of a Node object.

    Returns:
        A Node parsed from the string S.
    """

    it = iter(s.split(NODE_VALUE_SEPARATOR))

    def parse():
        val = next(it)
        if val is NODE_EMPTY_VALUE:
            return None

        node = Node(val)
        node.left = parse()
        node.right = parse()

        return node

    return parse()
