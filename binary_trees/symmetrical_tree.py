class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return id(self.val)


def check_symmetrical(root):
    def level_order(root):
        queue = [root, None]
        level, final = [], []
        while any(queue):
            ptr = queue.pop(0)
            if ptr:
                level.append(ptr)
                if ptr.left:
                    queue.append(ptr.left)
                if ptr.right:
                    queue.append(ptr.right)
            else:
                queue.append(None)
                final.append(level)
                level = []
        final.append(level)
        return final

    left = level_order(root.left)
    right = level_order(root.right)

    # if len(left) == len(right):
    #     for idx in range(len(left)):
    #         if len(left[idx]) == len(left[idx]):
    #             for inx in range(len(left)):
    #                 print(left[inx], right[inx])
    #         return False

    if len(left) == len(right):
        for idx in range(len(left)):
            if left[idx] == right[idx][::-1]:
                continue
            else:
                return False
    else:
        return False
    return True


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)

    print(check_symmetrical(root))
