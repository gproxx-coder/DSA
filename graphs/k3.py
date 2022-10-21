parent = {}
rank = {}


def create_parent_dict(arr):
    global parent, rank
    for src, dst, _ in arr:
        parent[src] = src
        parent[dst] = dst

    print(parent)
    rank = {key:0 for key in parent.keys()}


def find(x):
    if parent[x] == x:
        # print(f'{x} --> {parent[x]}')
        return x
    return find(parent[x])


def union(a, b):
    global parent, rank
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return

    if rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    elif rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] = rank[root_a] + 1
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

# arr = [
#     (0, 1, 4),
#     (0, 2, 4),
#     (1, 2, 2),
#     (1, 0, 4),
#     (2, 0, 4),
#     (2, 1, 2),
#     (2, 3, 3),
#     (2, 5, 2),
#     (2, 4, 4),
#     (3, 2, 3),
#     (3, 4, 3),
#     (4, 2, 4),
#     (4, 3, 3),
#     (5, 2, 2),
#     (5, 4, 3),
# ]


create_parent_dict(arr)
kruskal_algo(arr)

# print("===================")
# union(0, 2)
# print("===================")
# union(3, 4)
# print("===================")
# union(2, 4)
# print("===================")
# union(5, 4)
# print("===================")
