from functools import reduce

def parse_input(file):
    lines = open(file).readlines()
    return [eval(l.strip()) for l in lines]

class SnailNumber:
    """
    Represents a tree-like data structure where each node can be either an integer
    or another `SnailNumber` instance. It provides methods to traverse and update
    the left and right most nodes of the tree.

    Attributes:
        left (SnailNumber|int): Initialized in the `__init__` method. If the first
            element of the input list is an integer, it is assigned directly to
            `self.left`. Otherwise, a new `SnailNumber` instance is created with
            the first element as its input list and the current depth incremented
            by 1.
        right (SnailNumber|int): Initialized in the `__init__` method as either
            an integer from the input list or another `SnailNumber` instance created
            recursively with increased depth.
        depth (int): Used to track the nesting depth of the number within the
            nested list. It is incremented each time a nested list is encountered
            during the initialization of the `SnailNumber` object.

    """
    def __init__(self, list, depth = 0):
        self.left = list[0] if isinstance(list[0], int) else SnailNumber(list[0], depth = depth + 1)
        self.right = list[1] if isinstance(list[1], int) else SnailNumber(list[1], depth = depth + 1)
        self.depth = depth

    def __repr__(self):
        return f"[{self.left.__repr__()},{self.right.__repr__()}]"

    def left_most(self):
        if isinstance(self.left, int): return self
        else: return self.left.left_most()

    def update_left_most(self, value):
        """
        Updates the leftmost digit of the snail number by setting it to the given
        value, or recursively updates the leftmost digit of the left child if the
        left child is another SnailNumber instance.

        Args:
            value (Union[int, str]): Represented as an integer or an object that
                supports the `update_left_most` method.

        """
        if isinstance(self.left, int):
            self.left = value
        else:
            self.left.update_left_most(value)

    def right_most(self):
        if isinstance(self.right, int): return self.right
        else: return self.right.right_most()

    def update_right_most(self, value):
        """
        Updates the rightmost value in a snail number data structure, recursively
        traversing the tree-like structure until it reaches the leaf node, which
        stores the value.

        Args:
            value (int | str): Represented as a variable that holds the new value
                to be assigned to the right child of the current node.

        """
        if isinstance(self.right, int):
            self.right = value
        else:
            self.right.update_right_most(value)
    
test1 = SnailNumber(eval("[[[[[9,8],1],2],3],4]"))
test2 = SnailNumber(eval("[7,[6,[5,[4,[3,2]]]]]"))
test3 = SnailNumber(eval("[[6,[5,[4,[3,2]]]],1]"))
test4 = SnailNumber(eval("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
test5 = SnailNumber(eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"))


if __name__ == "__main__":
    input = parse_input('18/input')