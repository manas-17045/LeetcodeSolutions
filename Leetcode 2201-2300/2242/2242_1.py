# Leetcode 2242: Maximum Score of a Node Sequence
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/
# Solved on 27th of July, 2025
class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the maximum score of a sequence of four distinct nodes (a, u, v, b)
        such that (u, v) is an edge, and (a, u) and (v, b) are also edges.
        The score is the sum of scores of these four nodes.

        Args:
            scores (list[int]): A list where scores[i] is the score of node i.
            edges (list[list[int]]): A list of undirected edges, where each edge is [u, v].
        Returns:
            int: The maximum score found, or -1 if no such sequence exists.
        """
        n = len(scores)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append((scores[v], v))
            adj[v].append((scores[u], u))

        for i in range(n):
            adj[i].sort(reverse=True)
            adj[i] = adj[i][:3]

        maxScore = -1

        for u, v in edges:
            for scoreA, nodeA in adj[u]:
                for scoreB, nodeB in adj[v]:
                    if nodeA != v and nodeB != u and nodeA != nodeB:
                        currentScore = scores[u] + scores[v] + scoreA + scoreB
                        if currentScore > maxScore:
                            maxScore = currentScore

        return maxScore