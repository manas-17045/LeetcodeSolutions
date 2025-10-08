# Leetcode 2581: Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/
# Solved on 8th of October, 2025
import collections


class Solution:
    def rootCount(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
        """
        Counts the number of possible root nodes such that if the tree is rooted at that node,
        at least 'k' of the given 'guesses' are correct.

        Args:
            edges: A list of lists representing the edges of the tree.
            guesses: A list of lists representing the directed guesses (u, v).
            k: The minimum number of correct guesses required.

        Returns:
            The number of possible root nodes.
        """
        numNodes = len(edges) + 1
        adjList = collections.defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        guessSet = set(tuple(g) for g in guesses)

        initialCount = 0

        # Calculate the number of correct guesses for the tree rooted at 0
        def dfs1(u, p):
            nonlocal initialCount
            for v in adjList[u]:
                if v == p:
                    continue
                # If the directed edge (u, v) is a guess, it's correct for root 0.
                if (u, v) in guessSet:
                    initialCount += 1
                dfs1(v, u)

        dfs1(0, -1)

        counts = [0] * numNodes
        counts[0] = initialCount

        # Reroot the tree and update counts for all other nodes
        def dfs2(u, p):
            for v in adjList[u]:
                if v == p:
                    continue

                # Calculate the count for v based on the count for u
                currentCount = counts[u]

                # When moving the root from u to v, the edge (u, v) flips.
                if (u, v) in guessSet:
                    currentCount -= 1
                # If (v, u) was a guess, it is now correct.
                if (v, u) in guessSet:
                    currentCount += 1

                counts[v] = currentCount

                # Recurse for the subtree rooted at v
                dfs2(v, u)

        dfs2(0, -1)

        # Count all nodes that satisfy the condition
        result = 0
        for count in counts:
            if count >= k:
                result += 1

        return result