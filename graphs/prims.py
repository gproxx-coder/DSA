"""
Why Prims algo?
to find minimum cost spanning tree

Spanning Tree?
if V=n then E=n-1 && Graph must be connected (No cycle)

Steps:
1. current = start,   start from any vertex
2. Check connected vertex of current and choose edge-vertex with minimum cost && ALSO check
    all nodes of previous vertexes.
3. current = chosen
3. Again run point 2
"""