import collections
from typing import List


def sum_of_distance(n: int, edges: List[List[int]]) -> List[int]:
    tree = collections.defaultdict(set)
    res = [0] * n
    count = [1] * n

    for i, j in edges:
        tree[i].add(j)
        tree[j].add(i)

    def dfs(root, pre):
        for i in tree[root]:
            if i != pre:
                dfs(i, root)
                count[root] += count[i]
                res[root] += res[i] + count[i]

    def dfs2(root, pre):
        for i in tree[root]:
            if i != pre:
                res[i] = res[root] - count[i] + n - count[i]
                dfs2(i, root)

    dfs(0, -1)
    dfs2(0, -1)
    return res

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(sum_of_distance(n, edges))