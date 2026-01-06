# Leetcode 2865: Beautiful Towers I
# https://leetcode.com/problems/beautiful-towers-i/
# Solved on 6th of January, 2026
class Solution:
    def maximumSumOfHeights(self, heights: list[int]) -> int:
        """
        Calculates the maximum possible sum of heights of a "beautiful" tower configuration.

        Args:
            heights: A list of integers representing the maximum allowed height for each tower.
        Returns:
            An integer representing the maximum sum of heights.
        """
        n = len(heights)
        maxSum = 0

        for i in range(n):
            currentSum = heights[i]
            currentMin = heights[i]

            for j in range(i - 1, -1, -1):
                if heights[j] < currentMin:
                    currentMin = heights[j]
                currentSum += currentMin

            currentMin = heights[i]
            for j in range(i + 1, n):
                if heights[j] < currentMin:
                    currentMin = heights[j]
                currentSum += currentMin

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum