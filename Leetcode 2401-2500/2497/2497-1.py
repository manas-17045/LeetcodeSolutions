# Leetcode 2497: Maximum Star Sum of a Graph
# https://leetcode.com/problems/maximum-star-sum-of-a-graph/
# Solved on 18th of September, 2025
class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        """
        Calculates the maximum star sum of a graph.
        :param vals: A list of integers representing the values of the nodes.
        :param edges: A list of lists of integers representing the edges of the graph.
        :param k: An integer representing the maximum number of neighbors to consider for a star.
        :return: An integer representing the maximum star sum.
        """
        numNodes = len(vals)
        adjList = [[] for _ in range(numNodes)]

        for u, v in edges:
            adjList[u].append(vals[v])
            adjList[v].append(vals[u])

        maxResult = -float('inf')

        for i in range(numNodes):
            adjList[i].sort(reverse=True)

            currentSum = vals[i]

            numNeighbors = min(k, len(adjList[i]))

            for j in range(numNeighbors):
                if adjList[i][j] > 0:
                    currentSum += adjList[i][j]
                else:
                    break

            if currentSum > maxResult:
                maxResult = currentSum

        return maxResult