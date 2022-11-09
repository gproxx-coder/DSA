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


class BinaryTree:
    @staticmethod
    def preorder_traversal(root):
        """
        Steps for Preorder:
        1. Print the node
        2. Recur to the left
        3. Recur to the right
        :param root:
        :return: List[Node]
        """
        final = []

        def inner(root):
            if root:
                final.append(root.val)

                # traverse left nodes
                inner(root.left)

                # traverse right nodes
                inner(root.right)

            return final

        return inner(root)

    @staticmethod
    def inorder_traversal(root):
        """
        Steps for Inorder:
        1. Recur to the left
        2. Print the node
        3. Recur to the right
        :param root:
        :return: List[Node]
        """
        final = []

        def inner(root):
            if root:
                # traverse left nodes
                inner(root.left)

                final.append(root.val)

                # traverse right nodes
                inner(root.right)

            return final

        return inner(root)

    @staticmethod
    def postorder_traversal(root):
        """
        Steps for Postorder:
        1. Recur to the left
        2. Recur to the right
        3. Print the node
        :param root:
        :return: List[Node]
        """
        final = []

        def inner(root):
            if root:
                # traverse left nodes
                inner(root.left)

                # traverse right nodes
                inner(root.right)

                final.append(root.val)

            return final

        return inner(root)

    @staticmethod
    def dfs(root):
        """
        DFS stands for Depth First Search
        It has 3 types:
        1. Preorder
        2. Inorder
        3. Postorder
        :param root:
        :return: List[Node]
        """
        return BinaryTree.preorder_traversal(root)

    @staticmethod
    def bfs(root):
        """
        BFS stands for Breadth First Search
        It can be achieved using Level Order Traversal algorithm
        :param root:
        :return: List[Node]
        """
        return BinaryTree.level_order_traversal_oneline(root)

    @staticmethod
    def level_order_traversal_oneline(root):
        """
        Level Order Traversal algorith gives us nodes level wise
        output of this algorithm will be Nodes in sequence
        Steps:
        1. Define a Queue
        2. Add root to queue
        3. Loop until queue is empty:
            a. Dequeue node from queue
            b. print the node
            c. if left child present to dequeued node then add to queue
            d. if right child present to dequeued node then add to queue
            e. follow steps a to e until queue is empty
        :param root:
        :return: List[Node]
        """
        if root:
            final = []
            queue = [root]
            while queue:
                ptr = queue.pop(0)
                final.append(ptr)

                if ptr.left:
                    queue.append(ptr.left)

                if ptr.right:
                    queue.append(ptr.right)

            return final

    @staticmethod
    def level_order_traversal_line_by_line(root) -> list:
        """
        Level Order Traversal algorith gives us nodes level wise
        output of this algorithm will be Nodes in level by level
        Steps:
        1. Define a Queue
        2. Add root to queue
        3. Add None to queue
        4. Loop until queue is empty:
            a. Dequeue node from queue
            b. If Dequeued node is NOT None:
                i. print the node
                ii. if left child present to dequeued node then add to queue
                iii. if right child present to dequeued node then add to queue
            c. If Dequeued node is None then print a new line and Enqueue None to queue
            d. follow steps a to d until queue is empty
        :param root:
        :return: List[Node]
        """
        if root:
            queue = [root, None]
            final = []
            level = []

            while any(queue):
                ptr = queue.pop(0)

                if ptr:
                    level.append(ptr)

                    if ptr.left:
                        queue.append(ptr.left)

                    if ptr.right:
                        queue.append(ptr.right)

                if ptr is None:
                    queue.append(None)
                    final.append(level)
                    level = []

            final.append(level)
            return final

    @staticmethod
    def get_height(root: Node) -> int:
        """
        Level Order Traversal algorith is used for getting the height of tree
        Steps:
        1. Define a Queue
        2. Add root to queue
        3. Add None to queue
        4. Loop until queue is empty:
            a. Dequeue node from queue
            b. If Dequeued node is NOT None:
                i. if left child present to dequeued node then add to queue
                ii. if right child present to dequeued node then add to queue
            c. If Dequeued node is None then Enqueue None to queue and increase height by 1
            d. follow steps a to d until queue is empty
        :param root: Node
        :return: height: int
        """
        if root:
            queue = [root, None]
            height = 1
            level = []

            while any(queue):
                ptr = queue.pop(0)

                if ptr:
                    level.append(ptr)

                    if ptr.left:
                        queue.append(ptr.left)

                    if ptr.right:
                        queue.append(ptr.right)

                if ptr is None:
                    queue.append(None)
                    height += 1
                    level = []

            return height
        return 0

    @staticmethod
    def get_left_side_nodes(root):
        """
        TO get left side nodes we use Level order traversal algorithm.
        Once we get array of nodes that are in one line, and we will have multiple such arrays inside a final array
        Then we need to pick 0th element from each inner array from final array
        :param root:
        :return: List[Node]
        """
        order = BinaryTree.level_order_traversal_line_by_line(root)
        if order:
            return [node[0] for node in order]
        return []

    @staticmethod
    def get_right_side_nodes(root):
        """
        TO get left side nodes we use Level order traversal algorithm.
        Once we get array of nodes that are in one line, and we will have multiple such arrays inside a final array
        Then we need to pick last element from each inner array from final array
        :param root:
        :return: List[Node]
        """
        order = BinaryTree.level_order_traversal_line_by_line(root)
        if order:
            return [node[-1] for node in order]
        return []

    @staticmethod
    def get_diameter(root):
        """
        For this we need to calculate diameter of
        1. Root
            height of left child + height of right child + 1 (1 is for root)
        2. Left subtree
            height of left child of left subtree + height of right child of left subtree + 1 (1 is for root of left subtree root)
        3. Right subtree
            height of left child of right subtree + height of right child of right subtree + 1 (1 is for root of right subtree root)

        Then we need to choose the maximum amongst these 3 values

        :param root:
        :return: diameter: int
        """
        if root:
            left_root = root.left
            right_root = root.right
            root_diam = BinaryTree.get_height(left_root) + BinaryTree.get_height(right_root) + 1
            left_diam = BinaryTree.get_height(left_root.left) + BinaryTree.get_height(left_root.right) + 1
            right_diam = BinaryTree.get_height(right_root.left) + BinaryTree.get_height(right_root.right) + 1
            return max(root_diam, left_diam, right_diam)

    @staticmethod
    def get_bottom_view(root):
        if root:
            bottom = []
            queue = [root]
            while queue:
                ptr = queue.pop(0)

                if not ptr.left and not ptr.right:
                    bottom.append(ptr)

                if ptr.left:
                    queue.append(ptr.left)

                if ptr.right:
                    queue.append(ptr.right)

            return bottom

    @staticmethod
    def get_top_view(root):
        if root:
            left_tops = []
            right_tops = []

            def recur_left(root):
                if root.left:
                    recur_left(root.left)
                    left_tops.append(root.left)

            def recur_right(root):
                if root.right:
                    right_tops.append(root.right)
                    recur_right(root.right)

            recur_left(root)
            recur_right(root)

            return left_tops + [root] + right_tops

    @staticmethod
    # We assign hd (horizontal distance) to every node
    def vertical_order_traversal(root):
        if root:
            from collections import defaultdict
            queue = [root]
            hash_table = defaultdict(list)

            # Hz Distance of root will be zero always
            root.hd = 0
            hash_table[0] = [root]

            while queue:
                ptr = queue.pop(0)

                if ptr.left:
                    ptr.left.hd = ptr.hd - 1
                    hash_table[ptr.hd - 1] += [ptr.left]
                    queue.append(ptr.left)

                if ptr.right:
                    ptr.right.hd = ptr.hd + 1
                    hash_table[ptr.hd + 1] += [ptr.right]
                    queue.append(ptr.right)

            return {key: hash_table[key] for key in sorted(hash_table)}

    @staticmethod
    def bottom_view(root):
        if root:
            hash_table = BinaryTree.vertical_order_traversal(root)
            return [nodes[-1] for nodes in hash_table.values()]

    @staticmethod
    def top_view(root):
        if root:
            hash_table = BinaryTree.vertical_order_traversal(root)
            return [nodes[0] for nodes in hash_table.values()]

    @staticmethod
    def lowest_common_ancestor(root, node1, node2):
        if root is None:
            return None

        if root in {node1, node2}:
            return root

        left = BinaryTree.lowest_common_ancestor(root.left, node1, node2)
        right = BinaryTree.lowest_common_ancestor(root.right, node1, node2)

        if left and right:
            return root
        else:
            return left if left else right

    # @staticmethod
    # def zig_zag_traversal(root):
    #     if root:
    #         queue = [root, None]
    #         final, level = [], []
    #         level_no = 1
    #         while any(queue):
    #             ptr = queue.pop(0)
    #
    #             if ptr:
    #                 level.append(ptr)
    #
    #                 if level_no % 2 == 0:
    #                     if ptr.left:
    #                         queue.append(ptr.left)
    #
    #                     if ptr.right:
    #                         queue.append(ptr.right)
    #                 else:
    #                     if ptr.right:
    #                         queue.append(ptr.right)
    #
    #                     if ptr.left:
    #                         queue.append(ptr.left)
    #             else:
    #                 queue.append(None)
    #                 final.append(level)
    #                 level = []
    #         else:
    #             final.append(level)
    #
    #         return final
    #     return []

    @staticmethod
    def zig_zag_traversal(root):
        if root:
            final, level = [], []
            stack_1, stack_2 = [], []
            stack_1.append(root)

            while stack_1 or stack_2:
                while stack_1:
                    # pop from s1 and print
                    popped_s1 = stack_1.pop()
                    level.append(popped_s1)

                    # push to s2 in left to right manner
                    if popped_s1.left:
                        stack_2.append(popped_s1.left)
                    if popped_s1.right:
                        stack_2.append(popped_s1.right)

                final.append(level)
                level = []

                while stack_2:
                    # pop from s2 and print
                    popped_s2 = stack_2.pop()
                    level.append(popped_s2)

                    # push to s2 in right to left manner
                    if popped_s2.right:
                        stack_1.append(popped_s2.right)
                    if popped_s2.left:
                        stack_1.append(popped_s2.left)

                final.append(level)
                level = []

            return final
        return []


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    j = Node('j')
    k = Node('k')
    l = Node('l')

    root = a

    a.left, a.right = b, c
    b.left, b.right = d, e
    # c.left, c.right = f, g
    # d.left, d.right = h, i
    # f.left, f.right = j, k
    # g.right = l

    tree_ops = BinaryTree()

    # print(tree_ops.preorder_traversal(root))

    # print(tree_ops.preorder_traversal(root))

    # print(tree_ops.inorder_traversal(root))

    # print(tree_ops.postorder_traversal(root))

    # print(tree_ops.level_order_traversal_oneline(root))

    # print("**************LEVEL ORDER LINE BY LINE**************")
    # for level in tree_ops.level_order_traversal_line_by_line(root):
    #     print(level)
    # print("****************************************************")

    print("Height of the tree:", tree_ops.get_height(root))

    # print("Left nodes of the tree:", tree_ops.get_left_side_nodes(root))
    # print("Right nodes of the tree:", tree_ops.get_right_side_nodes(root))

    print("Diameter of the tree:", tree_ops.get_diameter(root))

    # print("Vertical Order Traversal:", tree_ops.vertical_order_traversal(root))
    # print("Top nodes of the tree:", tree_ops.top_view(root))
    # print("Bottom nodes of the tree:", tree_ops.bottom_view(root))

    # n1, n2 = Node('j'), Node('e')
    # print(f"Lowest common ancestor of {n1} and {n2}: {tree_ops.lowest_common_ancestor(root, n1, n2)}")

    print("Zig Zag:", tree_ops.zig_zag_traversal(root))
