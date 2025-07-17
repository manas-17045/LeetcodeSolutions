# Leetcode 3202: Find the Maximum Length of Valid Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/
# Solved on 17th of July, 2025
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum length of a valid subsequence where adjacent elements
        have the same sum of remainders when divided by k.
        :param nums: A list of integers.
        :param k: An integer.
        :return: The maximum length of a valid subsequence.
        """
        maxLength = 0
        dp = [[0] * k for _ in range(k)]

        for num in nums:
            currentRem = num % k
            for prevRem in range(k):
                dp[prevRem][currentRem] = dp[currentRem][prevRem] + 1
                maxLength = max(maxLength, dp[prevRem][currentRem])

        return maxLength