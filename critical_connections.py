# https://leetcode.com/problems/critical-connections-in-a-network/
from collections import defaultdict


def critical_connections(n: int, connections):
    parents_pool = set()
    for edge in connections:
        parents_pool.add(edge[0])

    final = []
    for edge in connections:
        if edge[-1] not in parents_pool:
            final.append(edge)

    return final

    # return route_dict


n = 6
connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
# Output: [[1,3]]

print(critical_connections(n, connections))
