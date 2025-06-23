# Leetcode 1782: Count Pairs of Nodes
# https://leetcode.com/problems/count-pairs-of-nodes/
# Solved on 23rd of June, 2025
from collections import Counter


class Solution:
    def countPairs(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        """
        Counts the number of unordered pairs of distinct nodes (u, v) such that
        the sum of their degrees is strictly greater than a given query value.
        Edges between u and v are counted twice towards their sum of degrees.

        Args:
            n: The number of nodes in the graph.
            edges: A list of lists, where each inner list [u, v] represents an
                   edge between node u and node v. Nodes are 1-indexed.
            queries: A list of integers, where each integer q is a query value.

        Returns:
            A list of integers, where each element is the count of valid pairs
            for the corresponding query.

        The algorithm works as follows:
        1. Calculate the degree of each node and count the occurrences of each edge.
        2. Sort the degrees to efficiently find pairs whose sum of degrees is > q
           using a two-pointer approach. This initial count might overcount pairs
           that have a direct edge between them, as the edge contributes to both
           nodes' degrees.
        3. For each query, subtract the overcounted pairs. An overcounted pair (u, v)
           is one where `deg[u] + deg[v] > q` but `deg[u] + deg[v] - count_of_edge(u,v) <= q`.
        """
        # degrees of each node
        deg = [0] * n
        # Count of edges between each pair
        cnt = Counter()
        for u, v in edges:
            u -= 1
            v -= 1
            deg[u] += 1
            deg[v] += 1
            if u > v:
                u, v = v, u
            cnt[(u, v)] += 1

        # Sorted degrees
        sorted_deg = sorted(deg)
        res = []
        # For each query, count pairs
        for q in queries:
            # Two pointers on sorted_deg to count deg[i] + deg[j] > q
            total = 0
            left, right = 0, (n - 1)
            while left < right:
                if sorted_deg[left] + sorted_deg[right] > q:
                    total += (right - left)
                    right -= 1
                else:
                    left += 1

            # Subtract pairs that were overcounted due to direct edges
            for (u, v), c in cnt.items():
                if deg[u] + deg[v] > q and deg[u] + deg[v] - c <= q:
                    total -= 1
            res.append(total)
        return res