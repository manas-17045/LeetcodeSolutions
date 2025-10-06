# Leetcode 3608: Minimum Time for K Connected Components
# https://leetcode.com/problems/minimum-time-for-k-connected-components/
# Solved on 6th of October, 2025
class Solution:
    def minTime(self, n: int, edges: list[list[int]], k: int) -> int:
        """
        Calculates the minimum time 't' such that if all edges with removal_time <= t are removed,
        the graph has at least 'k' connected components.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, removal_time].
            k (int): The target minimum number of connected components.

        Returns:
            int: The minimum time 't' to achieve at least 'k' connected components.
        """
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                px, py = self.find(x), self.find(y)
                if px == py:
                    return False
                if self.rank[px] < self.rank[py]:
                    px, py = py, px
                self.parent[py] = px
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1
                return True

            def count_components(self):
                return len(set(self.find(i) for i in range(n)))

        # Helper function to count connected components at time t
        def count_components_at_time(t):
            dsu = DSU(n)
            # Only union edges that are NOT removed (time > t)
            for u, v, time in edges:
                if time > t:
                    dsu.union(u, v)
            return dsu.count_components()

        # Edge case: if no edges or already k components
        if not edges:
            return 0 if n >= k else -1

        # Binary search on time
        times = sorted(set(edge[2] for edge in edges))

        # Check if it's possible without removing any edges
        if count_components_at_time(0) >= k:
            return 0

        # Check if it's possible even after removing all edges
        if count_components_at_time(times[-1]) < k:
            return times[-1]

        # Binary search for minimum time
        left, right = 0, times[-1]
        result = times[-1]

        while left <= right:
            mid = (left + right) // 2
            components = count_components_at_time(mid)

            if components >= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result