# Leetcode 3373: Maximize the Number of Target nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-
# Solved on 29th of May, 2025
from collections import deque


class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        """
        Given two trees represented by their edge lists, `edges1` and `edges2`,
        connect them by adding an edge between any node in the first tree and
        any node in the second tree. The goal is to maximize the number of
        "target nodes" in the resulting combined graph. A target node is a node
        that is at an even distance from node 0 in the combined graph.

        For each possible connection between a node `i` in the first tree and
        any node in the second tree, determine the maximum number of target nodes.

        Args:
            edges1: The edge list of the first tree.
            edges2: The edge list of the second tree.
        """
        # Build adjacency lists
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        adj1 = [[] for _ in range(n1)]
        adj2 = [[] for _ in range(n2)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        def bfsCount(adj: list[list[int]], mark_even: list[bool] = None) -> int:
            q = deque([0])
            parent = [-1] * len(adj)
            depth = [0] * len(adj)
            seen = [False] * len(adj)
            seen[0] = True
            even_cnt = 0

            while q:
                u = q.popleft()
                if depth[u] % 2 == 0:
                    even_cnt += 1
                    if mark_even is not None:
                        mark_even[u] = True
                for w in adj[u]:
                    if not seen[w]:
                        seen[w] = True
                        parent[w] = u
                        depth[w] = depth[u] + 1
                        q.append(w)

            return even_cnt

        # How many at even vs odd levels from 0?
        even2 = bfsCount(adj2)
        odd2 = n2 - even2
        best2 = max(even2, odd2)

        # Tree-1: Mark which nodes are at even distance from 0, and count them
        included = [False] * n1
        even1 = bfsCount(adj1, mark_even=included)

        # Build answer
        ans = [0] * n1
        for i in range(n1):
            # If i is at even dist from 0 in tree1, we get even1 targets there,
            # otherwise we get (n1 - even), and in both cases add best2 from tree2
            ans[i] = (even1 if included[i] else (n1 - even1)) + best2

        return ans
