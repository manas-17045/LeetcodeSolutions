# Leetcode 2392: Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/
# Resolved on 16th of October, 2025
import collections


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        """
        Builds a k x k matrix where each number from 1 to k appears exactly once,
        satisfying given row and column conditions.

        Args:
            k (int): The size of the square matrix.
            rowConditions (list[list[int]]): A list of conditions for rows, where [u, v] means u must appear above v.
            colConditions (list[list[int]]): A list of conditions for columns, where [u, v] means u must appear to the left of v.

        Returns:
            list[list[int]]: The constructed matrix, or an empty list if no such matrix can be built.
        """
        def findOrder(numItems, conditions):
            adjList = collections.defaultdict(list)
            inDegree = [0] * (numItems + 1)

            for u, v in conditions:
                adjList[u].append(v)
                inDegree[v] += 1

            queue = collections.deque()
            for i in range(1, numItems + 1):
                if inDegree[i] == 0:
                    queue.append(i)

            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in adjList[node]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        queue.append(neighbor)

            return order if len(order) == numItems else []

        rowOrder = findOrder(k, rowConditions)
        colOrder = findOrder(k, colConditions)

        if not rowOrder or not colOrder:
            return []

        valToRowMap = {val: i for i, val in enumerate(rowOrder)}
        valToColMap = {val: i for i, val in enumerate(colOrder)}

        matrix = [[0] * k for _ in range(k)]

        for val in range(1, k + 1):
            row = valToRowMap[val]
            col = valToColMap[val]
            matrix[row][col] = val

        return matrix