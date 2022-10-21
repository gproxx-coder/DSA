parent = {key: key for key in range(8)}


def find(x):
    print(f'{x} --> {parent[x]}')
    if parent[x] == x:
        return x
    return find(parent[x])


def union(a, b):
    global parent
    x = find(a)
    y = find(b)
    print(x, y)
    if x == y:
        print("SAME", x, y)
        return
    # if x and y:
    parent[y] = x
    print(parent)


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

# kruskal_algo(arr)

print("===================")
union(0, 2)
print("===================")
union(3, 4)
print("===================")
union(2, 4)
print("===================")
union(5, 4)
print("===================")