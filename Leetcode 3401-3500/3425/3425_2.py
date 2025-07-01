# Leetcode 3425: Longest Special Path
# https://leetcode.com/problems/longest-special-path/
# Solved on 30th of June, 2025
import sys


class Solution:
    def longestSpecialPath(self, edges: list[list[int]], nums: list[int]) -> list[int]:
        """
        Finds the longest "special" path in a tree, where a special path is defined by
        having no duplicate values in the `nums` array along the path.
        If multiple paths have the same maximum length, the one with the fewest nodes is preferred.

        Args:
            edges: A list of edges, where each edge is [u, v, w] representing an edge
                   between node u and node v with weight w.
            nums: A list of integers where nums[i] is the value associated with node i.

        Returns:
            A list [length, nodes] representing the length of the longest special path
            and the number of nodes in that path.
        """
        sys.setrecursionlimit(10**7)
        n = len(nums)

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        best_len = 0
        best_nodes = 1

        # Map from value -> its index on the current root->u path
        last_index = {}

        def dfs(u: int, parent: int, curr_sum: int, head: int, depth: int):
            nonlocal best_len, best_nodes

            val = nums[u]
            # If we've seen this value on the path, move head past its last occurrence
            if val in last_index:
                head = max(head, last_index[val] + 1)

            # Record/update this node's index
            old = last_index.get(val, None)
            last_index[val] = depth

            # Compute current window's length and node-count
            window_len = curr_sum - prefix_sum[head]
            window_nodes = depth - head + 1

            if (window_len > best_len) or (window_len == best_len and window_nodes < best_nodes):
                best_len = window_len
                best_nodes = window_nodes

            # Recurse to children
            for v, w in adj[u]:
                if v == parent:
                    continue
                # Before recursing, push the new prefix sum
                prefix_sum.append(curr_sum + w)
                dfs(v, u, curr_sum + w, head, depth + 1)
                prefix_sum.pop()

            # Restore last index
            if old is None:
                del last_index[val]
            else:
                last_index[val] = old

        # prefix_sum[i] = total weight from root to the node at depth i
        prefix_sum = [0]
        dfs(u=0, parent=-1, curr_sum=0, head=0, depth=0)

        return [best_len, best_nodes]