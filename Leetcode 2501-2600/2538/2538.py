# Leetcode 2538: Difference Between Maximum and Minimum Price Sum
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/
# Solved on 11th of December, 2025
from collections import deque


class Solution:
    def maxOutput(self, n: int, edges: list[list[int]], price: list[int]) -> int:
        """
        Calculates the maximum possible difference between the maximum and minimum price sum
        of a path in a tree, where the path must start and end at different nodes.

        Args:
            n (int): The number of nodes in the tree.
            edges (list[list[int]]): A list of edges representing the tree.
            price (list[int]): A list of prices for each node.

        Returns:
            The maximum possible difference.
        """

        if n == 1:
            return 0

        adjacencyList = [[] for _ in range(n)]
        for u, v in edges:
            adjacencyList[u].append(v)
            adjacencyList[v].append(u)

        def bfs(startNode):
            distances = [-1] * n
            distances[startNode] = price[startNode]
            queue = deque([startNode])
            farthestNode = startNode
            maxDistance = price[startNode]

            while queue:
                currentNode = queue.popleft()
                if distances[currentNode] > maxDistance:
                    maxDistance = distances[currentNode]
                    farthestNode = currentNode

                for neighbor in adjacencyList[currentNode]:
                    if distances[neighbor] == -1:
                        distances[neighbor] = distances[currentNode] + price[neighbor]
                        queue.append(neighbor)

            return farthestNode, distances

        nodeU, _ = bfs(0)
        nodeV, distFromU = bfs(nodeU)
        _, distFromV = bfs(nodeV)

        maxCost = 0
        for i in range(n):
            maxPath = max(distFromU[i], distFromV[i])
            maxCost = max(maxCost, maxPath - price[i])

        return maxCost