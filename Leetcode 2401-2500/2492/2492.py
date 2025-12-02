# Leetcode 2942: Minimum Score of a Path Between Two Coties
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Solved on 2nd of December, 2025
class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        """
        Calculates the minimum score of a path between two cities.

        Args:
            n (int): The number of cities.
            roads (list[list[int]]): A list of roads, where each road is represented as [city1, city2, distance].

        Returns:
            int: The minimum score of a path between two cities.
        """
        parent = list(range(n + 1))
        scores = [float('inf')] * (n + 1)

        def find(i):
            root = i
            while root != parent[root]:
                root = parent[root]
            while i != root:
                nextNode = parent[i]
                parent[i] = root
                i = nextNode
            return root

        for u, v, dist in roads:
            rootU = find(u)
            rootV = find(v)

            parent[rootU] = rootV
            scores[rootV] = min(scores[rootV], scores[rootU], dist)

        return int(scores[find(1)])