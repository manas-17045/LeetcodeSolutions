# Leetcode 1203: Sort Items by Groups Respecting Dependencies
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# Solved on 24th of August, 2025
from collections import defaultdict, deque


class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        """
        Sorts items based on their dependencies and group affiliations.

        Args:
            n (int): The total number of items.
            m (int): The initial number of groups.
            group (list[int]): A list where group[i] is the group ID of item i, or -1 if item i is ungrouped.
            beforeItems (list[list[int]]): A list where beforeItems[i] contains a list of items that must come before item i.
        Returns:
            list[int]: A list of item IDs representing a valid sorted order, or an empty list if no such order exists.
        """
        # Assign new groups for ungrouped items
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Build graphs
        item_graph = defaultdict(list)
        item_indegree = [0] * n

        group_graph = defaultdict(list)
        group_indegree = [0] * m

        for curr in range(n):
            for prev in beforeItems[curr]:
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                # If dependency is across groups, record it in group graph
                if group[prev] != group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]] += 1

        # Topological sort helper
        def topo_sort(graph, indegree, total_nodes):
            q = deque([i for i in range(total_nodes) if indegree[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return order if len(order) == total_nodes else []

        # Sort items and groups
        item_order = topo_sort(item_graph, item_indegree, n)
        group_order = topo_sort(group_graph, group_indegree, m)

        if not item_order or not group_order:
            return []

        # Arrange items according to group order
        grouped_items = defaultdict(list)
        for item in item_order:
            grouped_items[group[item]].append(item)

        result = []
        for g in group_order:
            result.extend(grouped_items[g])

        return result