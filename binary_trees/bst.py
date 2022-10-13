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


class BinarySearchTree:
    @staticmethod
    def construct_bst(nodes):
        if nodes:
            root = Node(nodes[0])

            for idx in range(1, len(nodes)):
                new_node = Node(nodes[idx])
                ptr = root
                while True:
                    if new_node.val > ptr.val:
                        if ptr.right is None:
                            ptr.right = new_node
                            break
                        else:
                            ptr = ptr.right
                    else:
                        if ptr.left is None:
                            ptr.left = new_node
                            break
                        else:
                            ptr = ptr.left
            return root

    @staticmethod
    def construct_bst_2(values):
        if values:
            root = Node(values[0])

            for idx in range(1, len(values)):
                new_node = Node(values[idx])
                curr = root

                while True:
                    if new_node.val <= curr.val:
                        if curr.left is None:
                            curr.left = new_node
                            break
                        else:
                            curr = curr.left
                    else:
                        if curr.right is None:
                            curr.right = new_node
                            break
                        else:
                            curr = curr.right
            return root
        return []

    @staticmethod
    def inorder_traversal(root):
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
    def validate_tree_min_max_method(root):
        def inner(node, mn, mx):
            if node is None:
                return True

            if node.val < mn or node.val > mx:
                return False

            return inner(node.left, mn, node.val) and inner(node.right, node.val, mx)

        return inner(root, float('-inf'), float('inf'))

    # @staticmethod
    # def validate_tree_inorder_method(root):
    #     prev_val = float('-inf')
    #
    #     def inorder(node):
    #         nonlocal prev_val
    #         if node:
    #             if not inorder(node.left):
    #                 return False
    #             if node.val <= prev_val:
    #                 return False
    #             return inorder(node.right)
    #         return True
    #
    #     return inorder(root)

    @staticmethod
    def convert_to_bst(root):
        inorder_array = BinarySearchTree.inorder_traversal(root)
        inorder_array.sort()
        return BinarySearchTree.construct_bst(inorder_array)

    @staticmethod
    def convert_to_bst_keep_shape(root):
        inorder_array = BinarySearchTree.inorder_traversal(root)
        inorder_array.sort()
        i = 0

        def inorder(node):
            nonlocal i, inorder_array
            if node:
                inorder(node.left)
                node.val = inorder_array[i]
                i += 1
                inorder(node.right)

        inorder(root)
        return root


if __name__ == '__main__':
    nodes = [5, 7, 3, 2, 9, 1, 8]

    # root = Node(4)  # 4
    # root.left = Node(2)
    # root.right = Node(5)
    # root.left.left = Node(1)
    # root.left.right = Node(3)

    root = Node(0)  # 4
    root.left = Node(1)
    root.right = Node(2)

    root.left.left = Node(3)
    root.left.right = Node(4)

    root.left.left.right = Node(6)
    root.left.left.right.right = Node(8)

    root.right.left = Node(5)
    root.right.left.right = Node(7)

    # root = BinarySearchTree.construct_bst_2(nodes)

    # Converting binary tree to BST
    print("Inorder Traversal Before converting tree to BST:", BinarySearchTree.inorder_traversal(root))
    bst_root = BinarySearchTree.convert_to_bst(root)
    print("Inorder Traversal after conversion to BST:", BinarySearchTree.inorder_traversal(bst_root))

    print()

    # Converting binary tree to BST KEEP SHAPE
    print("Inorder Traversal Before converting tree to BST:", BinarySearchTree.inorder_traversal(root))
    print("Is BST? (Min Max Method):", BinarySearchTree.validate_tree_min_max_method(root))
    bst_root = BinarySearchTree.convert_to_bst_keep_shape(root)
    print("Inorder Traversal after conversion to BST:", BinarySearchTree.inorder_traversal(bst_root))
    print("Is BST? (Min Max Method):", BinarySearchTree.validate_tree_min_max_method(bst_root))

    # print("Min Max Method:", BinarySearchTree.validate_tree_min_max_method(root))

    # print("Inorder Method:", BinarySearchTree.validate_tree_inorder_method(root))
