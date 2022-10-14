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


def get_max_sum_bst(root):

    ans = float('-inf')

    # we are using POST ORDER Traversal
    # Go to left --> Go to Right --> Do Operation
    def dfs(root):
        nonlocal ans
        if root is None:
            return True, float('inf'), float('-inf'), 0

        # Recur to Left
        # Parameters are
        # 1. tree/node is BST or not
        # 2. minimum value from left/right subtree
        # 3. maximum value from left/right subtree
        # 4. total sum of left/right subtree
        left, left_min, left_max, left_sum = dfs(root.left)
        # Recur to Right
        right, right_min, right_max, right_sum = dfs(root.right)

        # current_sum = sum of left BST + sum of right BST + current node value
        current_sum = left_sum + right_sum + root.val

        # new min = minimum of(current node value, minimum of left subtree, minimum of right subtree)
        new_min = min(root.val, left_min, right_min)
        # new max = maximum of(current node value, maximum of left subtree, maximum of right subtree)
        new_max = max(root.val, left_max, right_max)

        # If current node value is between maximum of left subtree AND minimum of right subtree
        # then that is BST, and we return True as first parameter
        if left_max < root.val < right_min and left and right:
            ans = max(ans, current_sum)
            return True, new_min, new_max, current_sum
        # If current node value is not between maximum of left subtree AND minimum of right subtree
        # then that is not BST, and we return False as first parameter
        return False, new_min, new_max, current_sum

    dfs(root)
    return ans if ans > 0 else 0


if __name__ == '__main__':
    nodes = [5, 7, 3, 2, 9, 1, 8]

    root = Node(4)  # 4
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    # root = Node(0)  # 4
    # root.left = Node(1)
    # root.right = Node(2)
    #
    # root.left.left = Node(3)
    # root.left.right = Node(4)
    #
    # root.left.left.right = Node(6)
    # root.left.left.right.right = Node(8)
    #
    # root.right.left = Node(5)
    # root.right.left.right = Node(7)

    print(get_max_sum_bst(root))
