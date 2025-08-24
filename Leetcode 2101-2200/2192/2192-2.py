# Leetcode 2192: All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
# Solved on 24th of August, 2025
from collections import deque


class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        """
        Given a directed acyclic graph (DAG) with n nodes labeled from 0 to n - 1, and an array edges where
        edges[i] = [fromi, toi] indicates that there is a unidirectional edge from fromi to toi.
        Find the ancestors of each node in the graph and return them in a list of lists.
        An ancestor of a node x is any node y that can reach x by traversing a sequence of edges.
        The ancestors for each node should be returned in sorted order.
        """
        # Build graph and ancestors
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1

        # Topological order (Kahn)
        q = deque(i for i in range(n) if indeg[i] == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        anc_bits = [0] * n

        # Propagate ancestors in topological order
        for u in topo:
            mask_u_with_u = anc_bits[u] | (1 << u)
            for v in adj[u]:
                anc_bits[v] |= mask_u_with_u

        # Convert bitsets to sorted lists (ascending)
        result = [[] for _ in range(n)]
        for i in range(n):
            bits = anc_bits[i]
            # Extract lowest set bits one by one -> ascending order of indices
            lst = []
            while bits:
                lsb = bits & -bits
                idx = lsb.bit_length() - 1
                lst.append(idx)
                bits ^= lsb
            result[i] = lst

        return result