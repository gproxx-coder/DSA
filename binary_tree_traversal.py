class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class BinaryTree:
    @staticmethod
    def in_order(root):
        if root:
            # First recur on left child
            BinaryTree.in_order(root.left)
            # then print the data of node
            print(root.val, end=" ")
            # now recur on right child
            BinaryTree.in_order(root.right)

    @staticmethod
    def pre_order(root):
        if root:
            # first print the data of node
            print(root.val, end=" ")
            # then recur on left child
            BinaryTree.pre_order(root.left)
            # then recur on right child
            BinaryTree.pre_order(root.right)

    @staticmethod
    def post_order(root):
        if root:
            # First recur on left child
            BinaryTree.post_order(root.left)
            # then recur on right child
            BinaryTree.post_order(root.right)
            # then print the data of node
            print(root.val, end=" ")

    @staticmethod
    def level_order_one_line(root):
        """
        1. Enqueue root
        2. Dequeue node and print
        3. Enqueue left and right child of Dequeued node
        4. repeat from step 2 until Queue is empty
        :param root:
        :return:
        """
        if root:
            queue = [root]
            while queue:
                popped = queue.pop(0)
                print(popped.val, end="=")
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

    @staticmethod
    def level_order_level_by_level(root):
        """
        1. Enqueue root
        2. Enqueue null
        3. P = Dequeue() node and print. Here P is pointer pointing to Dequeued node.
            Enqueue left and right child of Dequeued node which P is pointing
            Again go and P = Dequeue()
        4. If P = Null:
            a. Change level (print \n char)
            b. Enqueue null
        7. repeat from step 2 until Queue is empty
        :param root:
        :return:
        """
        if root:
            print("\n=== TREE LEVEL ORDER ===")
            queue = [root, None]
            while any(queue):
                pointer = queue.pop(0)
                if pointer:
                    print(pointer.val, end=" ")
                    if pointer.left:
                        queue.append(pointer.left)
                    if pointer.right:
                        queue.append(pointer.right)
                else:
                    print()
                    queue.append(None)
                    # if queue[0] is None and pointer is None:
                    #     break
            print("\n=========================")

    @staticmethod
    def level_order_lefts_and_rights(root):
        """
        1. Enqueue root
        2. Enqueue null
        3. P = Dequeue() node and print. Here P is pointer pointing to Dequeued node.
            Enqueue left and right child of Dequeued node which P is pointing
            Again go and P = Dequeue()
        4. If P = Null:
            a. Change level (print \n char)
            b. Enqueue null
        7. repeat from step 2 until Queue is empty
        :param root:
        :return:
        """
        print("\n=== TREE LEVEL ORDER ===")
        if root:
            final_list = []
            temp_list = []
            queue = [root, None]
            while any(queue):
                pointer = queue.pop(0)
                if pointer:
                    print(pointer.val, end=" ")
                    temp_list.append(pointer.val)
                    if pointer.left:
                        queue.append(pointer.left)
                    if pointer.right:
                        queue.append(pointer.right)
                else:
                    print()
                    final_list.append(temp_list)
                    temp_list = []
                    queue.append(None)
            final_list.append(temp_list)
            print("\n=========================")
            lefts, rights = [], []
            for level in final_list:
                lefts.append(level[0])
                rights.append(level[-1])

            print("LEFT Nodes", lefts)
            print("RIGHT Nodes", rights)


# Driver code
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# one = Node(1)
# two = Node(2)
# three = Node(3)
# four = Node(4)
# five = Node(5)
# six = Node(6)
# seven = Node(7)
# eight = Node(8)
# nine = Node(9)

# root = one
# root.left = two
# root.right = three
#
# two.left = four
# two.right = five
#
# four.left = six
# four.right = seven
#
# five.left = eight
# five.right = nine

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
c.left, c.right = f, g
d.left, d.right = h, i
f.left, f.right = j, k
g.right = l
"""
              1
            /   \
          2       3
        /   \
      4       5
     / \    /  \
    6   7  8    9
"""

bt = BinaryTree()


print("Preorder traversal of binary tree is")
bt.pre_order(root)

print("\nInorder traversal of binary tree is")
bt.in_order(root)

print("\nPostorder traversal of binary tree is")
bt.post_order(root)

# bt.level_order_one_line(root)


# bt.level_order_level_by_level(root)


# bt.level_order_lefts_and_rights(root)
