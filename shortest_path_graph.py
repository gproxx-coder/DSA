"""
Find the shortest path of all cities
"""

class Graph:
    def __init__(self, edges):
        self.graph_dict = {}
        self.edges = edges
        self.create_graph_dict()

    def create_graph_dict(self):
        for start, end in self.edges:
            if start not in self.graph_dict:
                self.graph_dict[start] = [end]
            else:
                self.graph_dict[start].append(end)

    def get_all_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        all_possible_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_all_paths(start=node, end=end, path=path)
                for p in new_paths:
                    all_possible_paths.append(p)

        return all_possible_paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(start=node, end=end, path=path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

# routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris", "Dubai"),
#         ("Paris", "New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto"),
#     ]

g = Graph(routes)
print(g.graph_dict)

start = "Pune"
end = "Bangaluru"

print(g.get_all_paths(start, end))
print(g.get_shortest_path(start, end))