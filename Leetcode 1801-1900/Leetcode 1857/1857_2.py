# Leetcode 1857: Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# Solved on 26th of May, 2025
from array import array
from collections import deque


class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        """
        Given a directed graph where each node has a color, return the largest
        value of a path in the graph. The value of a path is the number of nodes
        of the most frequent color in that path. If the graph contains a cycle,
        return -1.

        This problem can be solved using dynamic programming and topological sort.
        We use a DP table `dp[i][c]` to store the maximum count of color `c` on
        any path ending at node `i`. We perform a topological sort to process
        nodes in a valid order. For each node `u` popped from the queue, we
        update its DP entry for its own color and then propagate its DP values
        to its neighbors `v`. If a neighbor's in-degree becomes zero, we add it
        to the queue. If we process all nodes, the maximum value in the DP table
        is the answer. Otherwise, there is a cycle.

        """
        n = len(colors)
        # Build graph and in-degree
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        # dp[i][c] = max count of color c on any path ending at i
        # use unsigned int array of length 26
        dp = [array('I', [0]) * 26 for _ in range(n)]

        dq = deque(i for i in range(n) if indeg[i] == 0)
        processed = 0
        ans = 0

        while dq:
            u = dq.popleft()
            processed += 1

            # Include u's own color
            cu = ord(colors[u]) - ord('a')
            dp[u][cu] += 1
            # Update global max
            ans = max(ans, dp[u][cu])

            # Push dp[u] → each successor v
            for v in adj[u]:
                # Propagate all 26 counts
                # We do not add v's own color here; that happens when v is popped
                for c in range(26):
                    if dp[u][c] > dp[v][c]:
                        dp[v][c] = dp[u][c]
                indeg[v] -= 1
                if indeg[v] == 0:
                    dq.append(v)

        # If not all nodes were processed, there is a cycle
        return ans if processed == n else -1