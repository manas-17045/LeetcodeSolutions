# Leetcode 1262: Greatest Sum Divisible by Three
# https://leetcode.com/problems/greatest-sum-divisible-by-three/
# Solved on 23rd of November, 2025
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        """
        Given an array of integers nums, return the maximum possible sum of elements of the array such that it is divisible by three.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The maximum possible sum of elements of the array such that it is divisible by three.
        """
        dp = [0, -100000000, -100000000]
        for num in nums:
            for currentSum in dp[:]:
                newSum = currentSum + num
                dp[newSum % 3] = max(dp[newSum % 3], newSum)

        return dp[0]