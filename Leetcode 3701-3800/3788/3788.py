# Leetcode 3788: Maximum Score of a Split
# https://leetcode.com/problems/maximum-score-of-a-split/
# Solved on 8th of January, 2026
class Solution:
    def maximumScore(self, nums: list[int]) -> int:
        """
        Calculates the maximum score of a split in the given array.

        The score of a split is defined as (sum of prefix) - (minimum of suffix).

        Args:
            nums: A list of integers.
        Returns:
            The maximum score achievable.
        """
        n = len(nums)
        totalSum = sum(nums)
        suffixMin = nums[n - 1]
        suffixSum = nums[n - 1]
        maxScore = (totalSum - suffixSum) - suffixMin

        for i in range(n - 2, 0, -1):
            currentNum = nums[i]
            suffixSum += currentNum
            if currentNum < suffixMin:
                suffixMin = currentNum

            currentScore = (totalSum - suffixSum) - suffixMin
            if currentScore > maxScore:
                maxScore = currentScore

        return maxScore