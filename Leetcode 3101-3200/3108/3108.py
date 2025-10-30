# Leetcode 3108: Minimum Cost Walk in Weighted Graph
# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
# Solved on 30th of October, 2025
class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        """
        Calculates the minimum cost walk between pairs of nodes in a weighted graph.

        Args:
            n (int): The number of nodes in the graph.
            edges (list[list[int]]): A list of edges, where each edge is [u, v, w] representing an undirected edge between nodes u and v with weight w.
            query (list[list[int]]): A list of queries, where each query is [s, t] representing a request to find the minimum cost walk between node s and node t.

        Returns:
            list[int]: A list of integers, where each element is the minimum cost for the corresponding query.
                       If no walk exists between s and t, -1 is returned. If s == t, 0 is returned.
        """
        parent = list(range(n))
        componentAnd = [-1] * n

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j, weight):
            rootI = find(i)
            rootJ = find(j)

            if rootI != rootJ:
                parent[rootJ] = rootI
                componentAnd[rootI] = componentAnd[rootI] & componentAnd[rootJ] & weight
            else:
                componentAnd[rootI] = componentAnd[rootI] & weight

        for u, v, w in edges:
            union(u, v, w)

        results = []
        for s, t in query:
            if s == t:
                results.append(0)
                continue

            rootS = find(s)
            rootT = find(t)

            if rootS != rootT:
                results.append(-1)
            else:
                results.append(componentAnd[rootS])

        return results