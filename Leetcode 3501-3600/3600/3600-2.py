# Leetcode 3600: Maximize Spanning Tree Stability with Upgrades
# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
# Solved on 6th of September, 2025
class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        """
        Calculates the maximum possible stability value 'x' such that all nodes can be connected
        into a single component using at most 'k' additional edges, given certain constraints.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, s, must].
                                     u, v are nodes, s is the stability value of the edge, and must is 1 if the edge must be used, 0 otherwise.
            k (int): The maximum number of additional edges that can be used to connect components.

        Returns:
            int: The maximum stability value 'x' that can be achieved. Returns -1 if it's impossible to connect all nodes.
        """
        def make_dsu():
            parent = list(range(n))
            rank = [0] * n

            def find(x):
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(x, y):
                rx, ry = find(x), find(y)
                if rx == ry:
                    return False
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[rx] > rank[ry]:
                    parent[ry] = rx
                else:
                    parent[ry] = rx
                    rank[rx] += 1
                return True

            return find, union, parent

        if n <= 1:
            return 0

        if not edges:
            return -1 if n > 1 else 0

        max_s = 0
        for u, v, s, must in edges:
            max_s = max(max_s, s)

        def is_possible(x: int) -> bool:
            find, union, parent = make_dsu()

            for u, v, s, must in edges:
                if must == 1:
                    if s < x:
                        return False
                    if not union(u, v):
                        return False

            for u, v, s, must in edges:
                if must == 0 and s >= x:
                    union(u, v)

            roots = set(find(i) for i in range(n))
            comp_count = len(roots)
            if comp_count == 1:
                return True

            used = 0
            for u, v, s, must in edges:
                if must == 0 and s < x and s * 2 >= x:
                    if union(u, v):
                        used += 1
                        comp_count -= 1
                        if used > k:
                            return False
                        if comp_count == 1:
                            return True

            return comp_count == 1 and used <= k

        if not is_possible(0):
            return -1

        lo, hi = 0, max_s * 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_possible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo