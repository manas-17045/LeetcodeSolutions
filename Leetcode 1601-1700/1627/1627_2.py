# Leetcode 1627: Graph Connectivity With Threshold
# https://leetcode.com/problems/graph-connectivity-with-threshold/
# Solved on 18th of August, 2025
class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        """
        Determines if pairs of nodes are connected based on a given threshold.
        :param n: The number of nodes in the graph (from 1 to n).
        :param threshold: The minimum greatest common divisor (GCD) required for two nodes to be considered directly connected.
        :param queries: A list of pairs of nodes [u, v] to check for connectivity.
        :return: A list of booleans, where each boolean indicates if the corresponding query pair is connected.
        """
        # If threshold == 0, gcd(u,v) >= 1 for all u, v, so whole graph is connected.
        if threshold == 0:
            return [True] * len(queries)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x: int) -> int:
            # Iterative path compression
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # Union by size
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        upper = n // 2
        start = threshold + 1
        if start <= upper:
            for d in range(start, upper + 1):
                # Unify all multiples of d with d
                multiple = 2 * d
                while multiple <= n:
                    union(d, multiple)
                    multiple += d

        # Answer queries by checking if nodes share the same root
        res = []
        for u, v in queries:
            res.append(find(u) == find(v))
        return res