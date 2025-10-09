# Leetcode 3473: Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/
# Solved on 9th of October, 2025
class Solution:
    def maxSum(self, nums: list[int], k: int, m: int) -> int:
        """
        Calculates the maximum sum of k non-overlapping subarrays, where each subarray has a length of at least m.

        Args:
            nums: A list of integers representing the input array.
            k: The number of non-overlapping subarrays to select.
            m: The minimum length required for each subarray.

        Returns:
            The maximum possible sum of k subarrays satisfying the conditions.
        """
        n = len(nums)

        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        dp = [[float('-inf')] * (n + 1) for _ in range(k + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k + 1):
            maxPrev = float('-inf')
            for i in range(j * m, n + 1):
                p = i - m

                maxPrev = max(maxPrev, dp[j-1][p] - prefixSum[p])

                optionOne = dp[j][i - 1]
                optionTwo = prefixSum[i] + maxPrev

                dp[j][i] = max(optionOne, optionTwo)

        return int(dp[k][n])