# Leetcode 3409: Longest Subsequence With Decreasing Adjacent Difference
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/
# Solved on 31st of December, 2025
class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        """
        Finds the length of the longest subsequence with decreasing adjacent difference.

        Args:
            nums: A list of integers.
        Returns:
            The length of the longest subsequence.
        """
        maxVal = max(nums)
        limit = maxVal + 2
        dp = [[0] * limit for _ in range(limit)]

        for num in nums:
            current = [1] * limit
            for prevVal in range(1, limit):
                if dp[prevVal][0] == 0:
                    continue

                diff = abs(num - prevVal)
                length = dp[prevVal][diff] + 1
                if length > current[diff]:
                    current[diff] = length

            runningMax = 0
            for diff in range(limit - 1, -1, -1):
                if current[diff] > runningMax:
                    runningMax = current[diff]
                if runningMax > dp[num][diff]:
                    dp[num][diff] = runningMax

        return max(row[0] for row in dp)