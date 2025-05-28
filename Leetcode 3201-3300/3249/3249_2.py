# Leetcode 3249: Count The Number of Good Nodes
# https://leetcode.com/problems/count-the-number-of-good-nodes/
# Solved on 28th of May, 2025

class Solution:
    def countGoodNodes(self, edges: list[list[int]]) -> int:
        """
        Counts the number of "good" nodes in a tree.

        A node is considered "good" if, when the tree is rooted at this node,
        all non-empty subtrees of its children have the same size.

        Args:
            edges: A list of lists representing the edges of the tree.

        Returns:
            The number of good nodes in the tree.
        """
        n = len(edges) + 1
        # Build adjacency list
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        self.ans = 0

        def dfs(u: int, p: int) -> int:
            child_sizes = []
            for v in g[u]:
                if v == p:
                    continue
                sz = dfs(v, u)
                child_sizes.append(sz)

            # Check if all non-empty child subtree sizes are equal
            if len(child_sizes) <= 1 or (max(child_sizes) == min(child_sizes)):
                self.ans += 1

            # Total size = 1 (u itself) + sum of child subtree sizes
            return 1 + sum(child_sizes)

        # root at 0 (arbitrary, since tree is undirected)
        dfs(0, -1)
        return self.ans