# Leetcode 3244: Shortest Distance After Road Addition Queries II
# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
# Solved on 3rd of December, 2025
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Calculates the shortest distance after a series of road addition queries.

        Args:
            n (int): The number of cities.
            queries (list[list[int]]): A list of queries, where each query [u, v] represents adding a road from city u to city v.
        Returns:
            list[int]: A list of integers, where each element is the shortest distance from city 0 to city n-1 after each query.
        """
        currentDist = n - 1
        nextCity = list(range(1, n)) + [0]
        output = []

        for u, v in queries:
            if 0 < nextCity[u] < v:
                k = nextCity[u]

                while k < v:
                    currentDist -= 1
                    temp = nextCity[k]
                    nextCity[k] = 0
                    k = temp
                nextCity[u] = v

            output.append(currentDist)

        return output