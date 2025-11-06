# Leetcode 3122: Minimum Number of Operations to Satisfy Conditions
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/
# Solved on 6th of November, 2025
class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of operations to satisfy the given conditions.

        Args:
            grid (list[list[int]]): The input grid of integers.
        Returns:
            int: The minimum number of operations.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        costMatrix = [[0] * 10 for _ in range(numCols)]

        for j in range(numCols):
            for k in range(10):
                colCost = 0
                for i in range(numRows):
                    if grid[i][j] != k:
                        colCost += 1
                costMatrix[j][k] = colCost

        prevDp = [0] * 10

        for k in range(10):
            prevDp[k] = costMatrix[0][k]

        for j in range(1, numCols):
            currDp = [0] * 10

            minVal = float('inf')
            secondMinVal = float('inf')
            minValIndex = -1

            for prevK in range(10):
                if prevDp[prevK] < minVal:
                    secondMinVal = minVal
                    minVal = prevDp[prevK]
                    minValIndex = prevK
                elif prevDp[prevK] < secondMinVal:
                    secondMinVal = prevDp[prevK]

            for k in range(10):
                currentCost = costMatrix[j][k]
                if k == minValIndex:
                    currDp[k] = currentCost + secondMinVal
                else:
                    currDp[k] = currentCost + minVal

            prevDp = currDp

        return min(prevDp)