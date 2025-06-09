# Leetcode 3462: Maximum Sum With at Most K Elements
# https://leetcode.com/problems/maximum-sum-with-at-most-k-elemts/
# Solved on 9th of June, 2025

class Solution:
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        """
        Calculates the maximum sum by selecting at most k elements from the grid,
        with a limit on the number of elements that can be selected from each row.

        Args:
            grid: A 2D list of integers representing the grid.
            limits: A list of integers where limits[i] is the maximum number of elements
                    that can be selected from row i.
            k: The maximum total number of elements that can be selected.

        Returns:
            The maximum possible sum.
        """
        allCandidates = []
        numRows = len(grid)

        for i in range(numRows):
            row = grid[i]
            row.sort(reverse=True)
            rowLimit = limits[i]
            allCandidates.extend(row[:rowLimit])

        allCandidates.sort(reverse=True)

        maxSum = sum(allCandidates[:k])

        return maxSum