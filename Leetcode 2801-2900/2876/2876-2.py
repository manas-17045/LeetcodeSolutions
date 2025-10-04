# Leetcode 2876: Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/
# Solved on 4th of October, 2025
from collections import deque


class Solution:
    def countVisitedNodes(self, edges: list[int]) -> list[int]:
        """
        Calculates the number of nodes reachable from each node in a directed graph.

        :param edges: A list representing the directed graph where edges[i] is the node that node i points to.
        :return: A list where ans[i] is the number of nodes reachable from node i.
        """
        n = len(edges)
        indeg = [0] * n
        for u in range(n):
            indeg[edges[u]] += 1

        q = deque([i for i in range(n) if indeg[i] == 0])
        removed = [False] * n
        removal_order = []

        while q:
            u = q.popleft()
            removed[u] = True
            removal_order.append(u)
            v = edges[u]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        ans = [0] * n

        visited = [False] * n
        for i in range(n):
            if removed[i] or visited[i]:
                continue
            cur = i
            cycle_nodes = []
            while not visited[cur]:
                visited[cur] = True
                cycle_nodes.append(cur)
                cur = edges[cur]
            if cur in cycle_nodes:
                idx = cycle_nodes.index(cur)
                cycle = cycle_nodes[idx:]
                cycle_size = len(cycle)
                for node in cycle:
                    ans[node] = cycle_size

        for u in reversed(removal_order):
            ans[u] = ans[edges[u]] + 1

        return ans