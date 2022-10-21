"""
Why Kruskal's algo?
to find minimum cost spanning tree

Spanning Tree?
if V=n then E=n-1 && Graph must be connected (No cycle)

Steps:
1. sort all edges in increasing order wef weight
2.  i. pick the smallest edge
    ii. check if adding edge forms cycle
    iii. if cycle is not formed include edge ELSE exclude edge
3. Repeat step 2 until V-1 edges are included
"""


# Kruskal's algorithm in Python


parent = {}


def create_parent_dict(arr):
    global parent
    for src, dst, _ in arr:
        parent[src] = src
        parent[dst] = dst

    print(parent)


def find(x):
    if parent[x] == x:
        # print(f'{x} --> {parent[x]}')
        return x
    return find(parent[x])


def union(a, b):
    global parent
    x = find(a)
    y = find(b)
    if x == y:
        # print("SAME", x, y)
        return
    # if x and y:
    parent[y] = x
    return True
    # print(parent)


def kruskal_algo(arr):
    sorted_weights = sorted(arr, key=lambda tup: tup[2])

    final = []
    pool = set()
    for src, dst, weight in sorted_weights:
        if union(src, dst):
            final.append((src, dst, weight))
            print((src, dst, weight))


arr = [
    (6, 1, 10),
    (4, 3, 12),
    (7, 2, 14),
    (3, 2, 16),
    (4, 7, 18),
    (5, 4, 22),
    (5, 7, 24),
    (6, 5, 25),
    (1, 2, 28),
]

arr = [
    (0, 1, 4),
    (0, 2, 4),
    (1, 2, 2),
    (1, 0, 4),
    (2, 0, 4),
    (2, 1, 2),
    (2, 3, 3),
    (2, 5, 2),
    (2, 4, 4),
    (3, 2, 3),
    (3, 4, 3),
    (4, 2, 4),
    (4, 3, 3),
    (5, 2, 2),
    (5, 4, 3),
]


create_parent_dict(arr)
kruskal_algo(arr)