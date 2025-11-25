# Leetcode 3613: Minimize Maximum Component Cost
# https://leetcode.com/problems/minimize-maximum-component-cost/
# Solved on 25th of November, 2025
class Solution:
    def minCost(self, n: int, edges: list[list[int]], k: int) -> int:
        """
        Minimizes the maximum cost of a component such that there are at most k components.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, cost].
            k (int): The maximum allowed number of components.
        Returns:
            int: The minimized maximum cost of a component.
        """
        if n <= k:
            return 0

        edges.sort(key=lambda x: x[2])

        parent = list(range(n))
        rank = [0] * n
        componentCount = n

        def find(i):
            root = i
            while root != parent[root]:
                root = parent[root]
            while i != root:
                nextNode = parent[i]
                parent[i] = root
                i = nextNode
            return root

        for u, v, w in edges:
            rootU = find(u)
            rootV = find(v)

            if rootU != rootV:
                if rank[rootU] > rank[rootV]:
                    parent[rootV] = rootU
                elif rank[rootU] < rank[rootV]:
                    parent[rootU] = rootV
                else:
                    parent[rootV] = rootU
                    rank[rootU] += 1

                componentCount -= 1

            if componentCount <= k:
                return w

        return 0