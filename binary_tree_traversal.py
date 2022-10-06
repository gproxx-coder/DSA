class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    @staticmethod
    def in_order(root):
        if root:
            # First recur on left child
            BinaryTree.in_order(root.left)
            # then print the data of node
            print(root.val)
            # now recur on right child
            BinaryTree.in_order(root.right)

    @staticmethod
    def pre_order(root):
        if root:
            # First recur on left child
            BinaryTree.in_order(root.left)
            # then recur on right child
            BinaryTree.in_order(root.right)
            # then print the data of node
            print(root.val)

    @staticmethod
    def post_order(root):
        if root:
            # first print the data of node
            print(root.val)
            # then recur on left child
            BinaryTree.in_order(root.left)
            # then recur on right child
            BinaryTree.in_order(root.right)


# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

bt = BinaryTree()

print("Preorder traversal of binary tree is")
bt.pre_order(root)

print("\nInorder traversal of binary tree is")
bt.in_order(root)

print("\nPostorder traversal of binary tree is")
bt.post_order(root)
