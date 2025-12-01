# Leetcode 2735: Collecting Chocolates
# https://leetcode.com/problems/collecting-chocolates/
# Solved on 1st of December, 2025
class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        """
        Calculates the minimum cost to collect all chocolates.

        Args:
            nums: A list of integers representing the cost of each chocolate type.
            x: An integer representing the cost to perform a rotation operation.
        Returns:
            The minimum total cost to collect all chocolates.
        """
        n = len(nums)
        minCosts = list(nums)
        result = sum(minCosts)

        for k in range(1, n):
            currentSum = 0
            for i in range(n):
                minCosts[i] = min(minCosts[i], nums[i - k])
                currentSum += minCosts[i]

            result = min(result, currentSum + k * x)

        return result