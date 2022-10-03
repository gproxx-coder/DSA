# https://leetcode.com/problems/reconstruct-itinerary/
from collections import defaultdict


def find_itinerary(tickets):
    route_dict = defaultdict(list)

    for departure, arrival in sorted(tickets)[::-1]:
        route_dict[departure].append(arrival)

    stack = ["JFK"]
    final_route = []

    while stack:
        while route_dict[stack[-1]]:
            stack.append(route_dict[stack[-1]].pop())
        final_route.append(stack.pop())

    return final_route[::-1]



# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

print(find_itinerary(tickets))
