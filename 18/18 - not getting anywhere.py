from functools import reduce

def parse_input(file):
    lines = open(file).readlines()
    return [eval(l.strip()) for l in lines]

class SnailNumber:
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
        if isinstance(self.left, int):
            self.left = value
        else:
            self.left.update_left_most(value)

    def right_most(self):
        if isinstance(self.right, int): return self.right
        else: return self.right.right_most()

    def update_right_most(self, value):
        if isinstance(self.right, int):
            self.right = value
        else:
            self.right.update_left_most(value)
    
test1 = SnailNumber(eval("[[[[[9,8],1],2],3],4]"))
test2 = SnailNumber(eval("[7,[6,[5,[4,[3,2]]]]]"))
test3 = SnailNumber(eval("[[6,[5,[4,[3,2]]]],1]"))
test4 = SnailNumber(eval("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
test5 = SnailNumber(eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"))


if __name__ == "__main__":
    input = parse_input('18/input')