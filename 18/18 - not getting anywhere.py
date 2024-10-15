from functools import reduce

def parse_input(file):
    """
    Reads a file, strips newline characters from each line, evaluates the resulting
    strings as Python expressions, and returns a list of the evaluated values.

    Args:
        file (str): Expected to be the path to a file containing input data in a
            format that can be evaluated by the `eval` function.

    Returns:
        List[Union[int,float,str,bool]]: A list containing the parsed values from
        the input file.

    """
    lines = open(file).readlines()
    return [eval(l.strip()) for l in lines]

class SnailNumber:
    """
    Represents a nested list of integers, where each integer is at the leaf level,
    and the rest are lists of two elements. It provides methods to navigate and
    update the leftmost and rightmost leaf nodes.

    Attributes:
        left (SnailNumber|int): Initialized in the `__init__` method. If the first
            element of the input list is an integer, it is assigned to `left`.
            Otherwise, a new `SnailNumber` instance is created with the first
            element of the list and the current depth, and assigned to `left`.
        right (SnailNumber|int): Initialized in the `__init__` method as either
            an integer from the `list` if it is of type int, or a new `SnailNumber`
            instance with incremented depth from the `list` if it is of type list.
        depth (int): Tracked throughout the tree-like structure, initialized at 0
            and incremented by 1 each time a new `SnailNumber` object is created
            from a non-integer value.

    """
    def __init__(self, list, depth = 0):
        """
        Initializes a SnailNumber object by recursively creating nested SnailNumber
        objects from a given list of integers and SnailNumber objects, tracking
        the depth of nesting.

        Args:
            list (List[int | SnailNumber]): Used to initialize a new `SnailNumber`
                instance. It is expected to be a list of two elements, where each
                element is either an integer or another `SnailNumber` instance.
            depth (int): Tracked throughout the recursion of the SnailNumber class,
                initially set to 0 and incremented by 1 each time a nested SnailNumber
                is encountered.

        """
        self.left = list[0] if isinstance(list[0], int) else SnailNumber(list[0], depth = depth + 1)
        self.right = list[1] if isinstance(list[1], int) else SnailNumber(list[1], depth = depth + 1)
        self.depth = depth

    def __repr__(self):
        return f"[{self.left.__repr__()},{self.right.__repr__()}]"

    def left_most(self):
        """
        Finds the leftmost node of a binary tree, which represents a number in a
        snail shell pattern. It recursively traverses the left subtree until it
        reaches a leaf node, which is an integer in this context.

        Returns:
            TreeNode|None: The leftmost node in a binary tree.

        """
        if isinstance(self.left, int): return self
        else: return self.left.left_most()

    def update_left_most(self, value):
        """
        Traverses the tree structure of the SnailNumber instance, updating the
        leftmost value encountered.

        Args:
            value (int | None): Used to replace the left child of the current node,
                whether it is an integer or another node.

        """
        if isinstance(self.left, int):
            self.left = value
        else:
            self.left.update_left_most(value)

    def right_most(self):
        """
        Determines the rightmost digit of a snail number, which is a number
        represented as a linked list, with the least significant digit at the
        rightmost position.

        Returns:
            int|None: The right-most node's value in a binary tree, where the root
            is an instance of the class containing this function.

        """
        if isinstance(self.right, int): return self.right
        else: return self.right.right_most()

    def update_right_most(self, value):
        """
        Updates the rightmost digit of a number represented as a binary tree, where
        each node represents a digit in a number written in a snail shell pattern.

        Args:
            value (int | str): Used to update the rightmost node of a binary tree,
                where the rightmost node is either an integer value or a node itself.

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