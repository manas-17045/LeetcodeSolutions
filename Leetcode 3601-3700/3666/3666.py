# Leetcode 3666: Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/
# Solved on 28th of November, 2025
import collections


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        """
        Calculates the minimum number of operations to equalize a binary string.

        Args:
            s: The input binary string.
            k: The number of bits to flip in each operation.
        Returns:
            The minimum number of operations, or -1 if it's impossible.
        """
        n = len(s)
        initialZeros = s.count('0')
        if initialZeros == 0:
            return 0

        # Distance array to track minimum operations
        dist = [-1] * (n + 1)
        dist[initialZeros] = 0
        queue = collections.deque([initialZeros])

        # DSU parent array to efficiently find the next unvisited node.
        # size is n + 3 to handle boundary conditions safely (curr + 2).
        parent = list(range(n + 3))

        def find(i):
            root = i
            while root != parent[root]:
                root = parent[root]
            # Path compression
            curr = i
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
            return root

        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootI] = rootJ

        # Mark the starting node as visited by linking it to the next node with step 2
        union(initialZeros, initialZeros + 2)

        while queue:
            u = queue.popleft()
            d = dist[u]

            # Calculate the range of reachable zeros [minV, maxV] with step 2
            # Minimum zeros: flip as many current zeros as possible
            minV = abs(u - k)

            # Maximum zeros: flip as few current zeros as possible
            if k <= n - u:
                maxV = u + k
            else:
                maxV = 2 * n - u - k

            # Iterate over unvisited nodes in the range using DSU
            curr = find(minV)
            while curr <= maxV:
                dist[curr] = d + 1
                if curr == 0:
                    return d + 1

                queue.append(curr)
                # Mark curr as visited by unioning with curr + 2
                union(curr, curr + 2)
                curr = find(curr)

        return -1