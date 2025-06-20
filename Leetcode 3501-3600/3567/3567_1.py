# Leetcode 3567: Minimum Absolute Difference in Sliding Submatrix
# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/
# Solved on 20th of June, 2025
import math


class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        """
        Calculates the minimum absolute difference between any two distinct elements
        within each k x k submatrix of the given grid.

        Args:
            grid: A 2D list of integers representing the input grid.
            k: An integer representing the size of the square submatrix.

        Returns:
            A 2D list of integers where each element is the minimum absolute difference
            for the corresponding k x k submatrix.
        """
        gridRows = len(grid)
        gridCols = len(grid[0])

        ansRows = gridRows - k + 1
        ansCols = gridCols - k + 1
        ans = [[0 for _ in range(ansCols)] for _ in range(ansRows)]

        for rTopLeft in range(ansRows):
            for cTopLeft in range(ansCols):
                currentSubmatrixValues = []
                for submatrixRow in range(rTopLeft, (rTopLeft + k)):
                    for submatrixCol in range(cTopLeft, (cTopLeft + k)):
                        currentSubmatrixValues.append(grid[submatrixRow][submatrixCol])

                sortedDistinctValues = sorted(list(set(currentSubmatrixValues)))

                if len(sortedDistinctValues) < 2:
                    ans[rTopLeft][cTopLeft] = 0
                else:
                    currentMinAbsDiff = math.inf
                    for i in range(len(sortedDistinctValues) - 1):
                        diff = sortedDistinctValues[i + 1] - sortedDistinctValues[i]
                        if diff < currentMinAbsDiff:
                            currentMinAbsDiff = diff
                    ans[rTopLeft][cTopLeft] = int(currentMinAbsDiff)

        return ans