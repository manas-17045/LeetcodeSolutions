# Leetcode 2242: Maximum Score of a Node Sequence
# https://leetcode.com/problems/maximum-score-of-a-node-sequence/
# Solved on 27th of July, 2025
class Solution:
    def maximumScore(self, scores: list[int], edges: list[list[int]]) -> int:
        """
        Calculates the maximum score of a path of four distinct nodes a - u - v - b,
        where (u, v) is an edge in the graph.

        Args:
            scores: A list of integers where scores[i] is the score of node i.
            edges: A list of lists representing the undirected edges in the graph.
        Returns:
            The maximum score achievable, or -1 if no such path exists.
        """
        n = len(scores)
        # For each node i, top3[i] will hold up to 3 neighbors with highest scores.
        top3 = [[] for _ in range(n)]

        # Helper function to try to insert neighbor b into a's top3 list
        def consider(a: int, b: int):
            lst = top3[a]
            lst.append(b)
            # Sort descending by neighbor's score, then trim to 3
            lst.sort(key=lambda x: scores[x], reverse=True)
            if len(lst) > 3:
                lst.pop()

        # Build directed-truncated adjacency
        for u, v in edges:
            consider(u, v)
            consider(v, u)

        ans = -1

        # For each undirected edge (u,v), try every combo a in top3[u], b in top3[v]
        # ensuring a, b, u, v are all distinct
        for u, v in edges:
            suv = scores[u] + scores[v]
            for a in top3[u]:
                if a == v:  # can't reuse v
                    continue
                for b in top3[v]:
                    if b == u or b == a:
                        continue
                    # Valid 4‑node sequence a - u - v - b
                    total = suv + scores[a] + scores[b]
                    if total > ans:
                        ans = total

        return ans