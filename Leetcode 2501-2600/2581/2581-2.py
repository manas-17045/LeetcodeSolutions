# Leetcode 2581: Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/
# Solved on 8th of October, 2025
class Solution:
    def rootCount(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
        """
        Counts the number of possible roots such that if the tree is rooted at that node,
        at least 'k' of the given guesses are correct.

        Args:
            edges: A list of lists representing the edges of the tree.
            guesses: A list of lists representing the directed guesses (u, v).
            k: The minimum number of correct guesses required for a root to be valid.
        Returns:
            The number of valid roots.
        """
        n = len(edges) + 1

        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Store guesses in a set for O(1) lookup
        guess_set = set()
        for u, v in guesses:
            guess_set.add((u, v))

        # First DFS: Count correct guesses when 0 is root
        correct_count = [0]

        def dfs1(node, parent):
            for child in graph[node]:
                if child != parent:
                    # Check if guess (node -> child) is correct
                    if (node, child) in guess_set:
                        correct_count[0] += 1
                    dfs1(child, node)

        dfs1(0, -1)

        # Second DFS: Reroot and count valid roots
        result = [0]

        def dfs2(node, parent, current_correct):
            # Check if current node can be root
            if current_correct >= k:
                result[0] += 1

            for child in graph[node]:
                if child != parent:
                    # Calculate correct count when child becomes root
                    new_correct = current_correct

                    # If (node, child) was a correct guess, it becomes incorrect
                    if (node, child) in guess_set:
                        new_correct -= 1

                    # If (child, node) is a guess, it becomes correct
                    if (child, node) in guess_set:
                        new_correct += 1

                    dfs2(child, node, new_correct)

        dfs2(0, -1, correct_count[0])

        return result[0]