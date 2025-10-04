# Leetcode 3615: Longest Palindromic Path in Graph
# https://leetcode.com/problems/longest-palindromic-path-in-graph/
# Solved on 4th of October, 2025
class Solution:
    def maxLen(self, n: int, edges: list[list[int]], label: str) -> int:
        """
        Calculates the maximum length of a palindromic path in a graph.

        Args:
            n: The number of nodes in the graph.
            edges: A list of lists representing the edges of the graph.
            label: A string where label[i] is the character label of the i-th node.
        Returns:
            The maximum length of a palindromic path.
        """
        if n == 0:
            return 0

        # Build adjacency
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ALL = 1 << n
        dp_by_mask: list[dict[tuple[int, int], int]] = [dict() for _ in range(ALL)]

        ans = 1

        # Initialize single-node centers
        for i in range(n):
            mask = 1 << i
            dp_by_mask[mask][(i, i)] = 1

        # Initialize two-node palindromes of length 2
        for u, v in edges:
            if label[u] == label[v]:
                m = (1 << u) | (1 << v)
                # Store both orders; expansions depend on endpoints' order
                dp_by_mask[m][(u, v)] = max(dp_by_mask[m].get((u, v), 0), 2)
                dp_by_mask[m][(v, u)] = max(dp_by_mask[m].get((v, u), 0), 2)
                ans = max(ans, 2)

        # Iterate masks in increasing order of bits (not strictly necessary but intuitive)
        for mask in range(ALL):
            if not dp_by_mask[mask]:
                continue

            # Freeze items to avoid mutation during iteration
            items = list(dp_by_mask[mask].items())
            for (u, v), cur_len in items:
                # Update global answer (some state might not be extended further)
                if cur_len > ans:
                    ans = cur_len

                # Try to expand by adding a new node to both ends
                for nu in adj[u]:
                    if (mask >> nu) & 1:
                        continue

                    for nv in adj[v]:
                        if (mask > nv) & 1 or nu == nv:
                            continue
                        # Labels must match to keep palindrome property
                        if label[nu] != label[nv]:
                            continue
                        newMask = mask | (1 << nu) | (1 << nv)
                        new_len = cur_len + 2
                        prev = dp_by_mask[newMask].get((nu, nv), 0)
                        if new_len > prev:
                            dp_by_mask[newMask][(nu, nv)] = new_len
                            if new_len > ans:
                                ans = new_len

        return ans