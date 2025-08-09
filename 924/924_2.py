# Leetcode 924: Minimize Malware Spread
# https://leetcode.com/problems/minimize-malware-spread/
# Solved on 9th of August, 2025
import collections


class Solution:
    def minMalwareSpread(self, graph: list[list[int]], initial: list[int]) -> int:
        """
        Finds the node to remove from the initial set of infected nodes to minimize the total malware spread.

        Args:
            graph: An adjacency matrix representing the network. graph[i][j] = 1 if node i and node j are connected, else 0.
            initial: A list of initially infected nodes.

        Returns:
            The node from 'initial' whose removal minimizes the total number of infected nodes. If there's a tie, return the node with the smallest index.
        """
        n = len(graph)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Build unions from adjacency matrix
        for i in range(n):
            row = graph[i]
            for j in range(i + 1, n):
                if row[j] == 1:
                    union(i, j)

        # Count component sizes by root (use find to compress)
        comp_size = collections.Counter()
        for i in range(n):
            comp_size[find(i)] += 1

        # Count how many initially infected nodes per component
        infected_count = collections.Counter()
        for node in initial:
            infected_count[find(node)] += 1

        # Choose best node to remove:
        # Iterate initial in sorted order so tie-breaking uses smallest index
        best_node = min(initial)
        # Number of nodes saved by removing best_node
        max_saved = -1
        for node in sorted(initial):
            root = find(node)
            if infected_count[root] == 1:
                saved = comp_size[root]
            else:
                saved = 0
            if saved > max_saved:
                max_saved = saved
                best_node = node

        return best_node