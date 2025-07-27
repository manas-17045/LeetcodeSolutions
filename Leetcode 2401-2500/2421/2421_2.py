# Leetcode 2421: Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/
# Solved on 27th of July, 2025
from collections import Counter, defaultdict


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        # Union by size
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True


class Solution:
    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the number of "good paths" in a tree.

        A path is "good" if:
        1. The starting node and the ending node have the same value.
        2. All intermediate nodes on the path have values less than or equal to the starting (and ending) node's value.
        :param vals: A list of integers representing the values of the nodes.
        :param edges: A list of lists representing the edges of the tree.
        :return: The total number of good paths.
        """
        n = len(vals)
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Group nodes by value
        val_to_nodes = defaultdict(list)
        for i, v in enumerate(vals):
            val_to_nodes[v].append(i)

        # Prepare DSU
        dsu = DSU(n)
        # Every single node is a trivial good path
        good_paths = n

        # Process values in ascending order
        for v in sorted(val_to_nodes):
            # Union current-value nodes with already-visited neighbors <= v
            for node in val_to_nodes[v]:
                for nei in adj[node]:
                    if vals[nei] <= v:
                        dsu.union(node, nei)

            # Count how many nodes of value v are in each component
            cnt = Counter()
            for node in val_to_nodes[v]:
                root = dsu.find(node)
                cnt[root] += 1

            # Within each component, any two nodes of the same value form a good path
            for c in cnt.values():
                good_paths += c * (c - 1) // 2

        return good_paths