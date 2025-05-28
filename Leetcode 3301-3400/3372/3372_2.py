# Leetcode 3372: Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/
# Solved on 28th of May, 2025
from collections import deque


class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]], k: int) -> list[int]:
        """
        Given two trees tree1 and tree2, and an integer k.
        We can add an edge between any node i in tree1 and any node j in tree2.
        The goal is to find, for each node i in tree1, the maximum number of nodes
        that can be reached within a distance of k from node i after adding such an edge.

        Args:
            edges1: The edges of the first tree.
            edges2: The edges of the second tree.
            k: The maximum allowed distance.
        """
        # Build adjacency
        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = [[] for _ in range(n)]
        for u, v in edges1:
            g1[u].append(v)
            g1[v].append(u)
        g2 = [[] for _ in range(m)]
        for u, v in edges2:
            g2[u].append(v)
            g2[v].append(u)

        # Precompute best reachable count in tree2 within distance (k - 1)
        radius2 = k - 1
        if radius2 < 0:
            # If k = 0, no node in tree2 can be reached via the new edge
            best2 = 0
        else:
            best2 = 0
            # For each candidate attachment point j in tree2
            for j in range(m):
                cnt = 0
                seen = [False] * m
                seen[j] = True
                dq = deque([(j, 0)])
                # BFS up to depth radius2
                while dq:
                    u, dist = dq.popleft()
                    cnt += 1
                    if dist < radius2:
                        for w in g2[u]:
                            if not seen[w]:
                                seen[w] = True
                                dq.append((w, dist + 1))
                best2 = max(best2, cnt)

        # Now, for each node i in tree1, count how many are within k, then add best2
        ans = [0] * n
        for i in range(n):
            cnt = 0
            seen = [False] * n
            seen[i] = True
            dq = deque([(i, 0)])
            while dq:
                u, dist = dq.popleft()
                cnt += 1
                if dist < k:
                    for w in g1[u]:
                        if not seen[w]:
                            seen[w] = True
                            dq.append((w, dist + 1))
            ans[i] = cnt + best2

        return ans