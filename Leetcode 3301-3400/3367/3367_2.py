# Leetcode 3367: Maximize Sum of Weights after Edge Removals
# https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/
# Solved on 13th of June, 2025

class Solution:
    def maximizeSumOfWeights(self, edges: list[list[int]], k: int) -> int:
        """
        Maximizes the sum of weights of selected edges in a tree, with the constraint
        that each node can be incident to at most k selected edges.

        Args:
            edges: A list of lists representing the edges of the tree. Each inner list
                   is [u, v, w], where u and v are the nodes connected by the edge,
                   and w is the weight of the edge.
            k: The maximum number of selected edges incident to any node.

        Returns:
            The maximum possible sum of weights of selected edges.
        """
        n = len(edges) + 1

        # Build undirected adjacency
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Root at 0: Discover parent & build a topological (post-order) list
        parent = [-1] * n
        order =[]
        stack = [0]
        parent[0] = -2  # Mark root
        while stack:
            u = stack.pop()
            order.append(u)
            for v, _ in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)
        # Now `order` is  preorder; we'll process iit in reverse for postorder
        dp0 = [0] * n   # u can keep up to k child-edges
        dp1 = [0] * n   # u can keep up to (k - 1) child-edges (reserve one slot for parent)

        for u in reversed(order):
            # Collect base = sum of dp0 over children,
            # and a list of gains if we choose to keep the child-edge
            base = 0
            gains = []
            for v, w in adj[u]:
                if v == parent[u]:
                    continue
                # If we drop edge (u, v), we get dp0[v]
                # If we keep edge (u, v), we get dp1[v] + w
                base += dp0[v]
                gains.append((dp1[v] + w) - dp0[v])

            # Sort gains descending
            gains.sort(reverse=True)

            # dp0[u]: we have k slots for children
            take = k
            s0 = base
            for g in gains:
                if take <= 0 or g <= 0:
                    break
                s0 += g
                take -= 1
            dp0[u] = s0

            # dp1[u]: we must reserve 1 slot for the parent edge, so children <= (k - 1)
            take = (k - 1)
            s1 = base
            for g in gains:
                if take <= 0 or g <= 0:
                    break
                s1 += g
                take -= 1
            dp1[u] = s1

        # dp0[0] is the max total weight we can keep in the whole tree
        return dp0[0]