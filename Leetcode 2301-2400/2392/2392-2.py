# Leetcode 2392: Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/
# Solved on 16th of October, 2025
from collections import deque


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        """
        Builds a k x k matrix where each number from 1 to k appears exactly once,
        satisfying the given row and column conditions.
        :param k: The size of the matrix (k x k).
        :param rowConditions: A list of conditions [u, v] meaning u must appear before v in the same row.
        :param colConditions: A list of conditions [u, v] meaning u must appear before v in the same column.
        :return: The k x k matrix satisfying all conditions, or an empty list if no such matrix exists.
        """
        def topo_sort(k: int, edges: list[list[int]]) -> list[int]:

            # Adjacency as sets to avoid duplicate edges, nodes are 1...k
            adj = [set() for _ in range(k + 1)]
            indeg = [0] * (k + 1)
            for u, v in edges:
                if v not in adj[u]:
                    adj[u].add(v)
                    indeg[v] += 1

            q = deque()
            for node in range(1, k + 1):
                if indeg[node] == 0:
                    q.append(node)

            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)

            # If we couldn't include all k nodes, there's a cycle
            return order if len(order) == k else []

        row_order = topo_sort(k, rowConditions)
        if not row_order:
            return []
        col_order = topo_sort(k, colConditions)
        if not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        # Build k × k matrix filled with 0s
        mat = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            mat[r][c] = num

        return mat