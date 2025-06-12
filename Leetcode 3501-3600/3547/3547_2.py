# Leetcode 3547: Maximum Sum of Edge Values in a Graph
# https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/
# Solved on 12th of June, 2025
from collections import defaultdict


class Solution:
    def maxScore(self, n: int, edges: list[list[int]]) -> int:
        """
        Calculates the maximum possible score for assigning values to nodes in a tree or cycle graph.

        The score is calculated as the sum of the products of the assigned values for each edge.
        The values assigned are a permutation of 1 to n, assigned in a zig-zag pattern along
        the path (for a tree) or cycle (for a cycle graph).

        Args:
            n: The number of nodes in the graph.
            edges: A list of edges, where each edge is represented as a list [u, v].

        Returns:
            The maximum possible score.
        """
        if n <= 1:
            return 0

        # Build adjacency
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        m = len(edges)
        is_cycle = (m == n)

        # Extract a 0...(n - 1) sequence of nodes
        seq = []
        if is_cycle:
            # Start anywhere (say 0) and walk the cycle)
            curr = 0
            prev = -1
            for _ in range(n):
                seq.append(curr)
                # Pick the neighbor that's not 'prev'
                nxt = adj[curr][0] if adj[curr][0] != prev else adj[curr][1]
                prev, curr = curr, nxt
        else:
            # Find an endpoint (deg == 1) and walk to the other end
            start = next(u for u in range(n) if len(adj[u]) == 1)
            curr, prev = start, -1
            while True:
                seq.append(curr)
                # Move on, if there's another neighbor
                nxt = None
                for w in adj[curr]:
                    if w != prev:
                        nxt = w
                        break
                if nxt is None:
                    break
                prev, curr = curr, nxt

        # Build the zig-zag assignment vals[0...(n - 1)]
        vals = [0] * n
        mid = n // 2
        left, right = (mid - 1), (mid + 1)
        cur = n
        vals[mid] = cur
        cur -= 1
        toLeft = True
        while cur >= 1:
            if toLeft:
                vals[left] = cur
                left -= 1
            else:
                vals[right] = cur
                right += 1
            toLeft = not toLeft
            cur -= 1

        # Map back to the original node IDs
        assigned = [0] * n
        for pos, node in enumerate(seq):
            assigned[node] = vals[pos]

        # Sum up each edge, including the wrap-around if it's a cycle
        total = 0
        for u, v in edges:
            total += assigned[u] * assigned[v]
        return total