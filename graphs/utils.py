"""
BFS
1. Enqueue starting vertex (it can be any vertex)
    Rule: if Enqueue(V), then set R[V] = 1 (in Visited Array)
2. While Q is not empty:
    {
    1. P = Dequeue() and Print P
    2. Enqueue all adjacent vertex of P and Update Visited Array
    }

"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def bfs(graph):
    queue = []
    visited = {}

    # chose first element from dict as root
    start_vertex = list(graph.keys())[0]
    queue.append(start_vertex)

    while queue:
        ptr = queue.pop(0)

        # check if ptr is already visited
        if ptr not in visited:
            visited[ptr] = True

        for neighbour in graph[ptr]:
            # check if ptr is already visited
            if not visited.get(neighbour):
                queue.append(neighbour)
                visited[neighbour] = True

    return list(visited.keys())


def shortest_distance(graph, start, end):
    queue = []
    visited = {}
    level = {}

    # chose first element from dict as root
    start_vertex = start
    queue.append(start_vertex)
    level[start_vertex] = 0

    while queue:
        ptr = queue.pop(0)

        # check if ptr is already visited
        if ptr not in visited:
            visited[ptr] = True

        for neighbour in graph[ptr]:
            # check if ptr is already visited
            if not visited.get(neighbour):
                queue.append(neighbour)
                visited[neighbour] = True
                level[neighbour] = level[ptr] + 1

    return level.get(end)


def shortest_path(graph, start, end):
    queue = []
    visited = {}
    parent = {}

    # chose first element from dict as root
    start_vertex = start
    queue.append(start_vertex)

    while queue:
        ptr = queue.pop(0)

        # check if ptr is already visited
        if ptr not in visited:
            visited[ptr] = True

        for neighbour in graph[ptr]:
            # check if ptr is already visited
            if not visited.get(neighbour):
                queue.append(neighbour)
                visited[neighbour] = True
                parent[neighbour] = ptr

    path = []

    # Set last to current and traverse backwards.
    # Keep appending parent of current until start node is found
    # parent of start node will be always None, exit while and print path list
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent.get(curr, None)
    path.reverse()
    return path


def all_funcs(graph, start, end):
    queue = []
    visited = []
    level = {}
    parent = {}

    level[start] = 0
    queue.append(start)

    while queue:
        ptr = queue.pop(0)

        if ptr not in visited:
            visited.append(ptr)

        for neighbour in graph[ptr]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                level[neighbour] = level[ptr] + 1
                parent[neighbour] = ptr

    print("BFS:", visited)
    print(level)
    print(f"Shortest Distance between {start} & {end}:", level.get(end, -1))

    curr = end
    sp = []
    print(parent)
    while curr:
        sp.append(curr)
        curr = parent.get(curr, None)

    print(f"Shortest Path between {start} & {end}:", sp)


def edges_to_graph(edges):
    from collections import defaultdict
    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


if __name__ == '__main__':
    # graph = {
    #     "a": ["b", "d"],
    #     "b": ["a", "c"],
    #     "c": ["b"],
    #     "d": ["a", "e", "f"],
    #     "e": ["d", "f", "g"],
    #     "f": ["d", "e", "h"],
    #     "g": ["e", "h"],
    #     "h": ["g", "f"]
    # }

    graph = {
        "0": ["1", "2"],
        "1": ["0"],
        "2": ["0"],
        "3": ["4", "5"],
        "4": ["3", "5"],
        "5": ["3", "4"]
    }

    # print("BFS Traversal:", bfs(graph))
    # print("Shortest Distance:", shortest_distance(graph, start, end))
    # print("Shortest Path:", shortest_path(graph, start, end))

    edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
    graph = edges_to_graph(edges)
    start, end = 0, 5
    all_funcs(graph, start, end)
