# Leetcode 3473: Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/
# Solved on 9th of October, 2025
class Solution:
    def maxSum(self, nums: list[int], k: int, m: int) -> int:
        """
        Calculates the maximum sum of k non-overlapping subarrays, each of length at least m.

        Args:
            nums: A list of integers representing the input array.
            k: The number of non-overlapping subarrays to select.
            m: The minimum length of each subarray.

        Returns:
            The maximum possible sum.
        """
        n = len(nums)

        # Build prefix sum array for range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        NEG_INF = float('-inf')
        dp = [[NEG_INF] * (k + 1) for _ in range(n + 1)]

        # Base case
        for i in range(n + 1):
            dp[i][0] = 0

        # For each number of subarrays
        for j in range(1, k + 1):
            # Track the maximum value
            max_val = NEG_INF

            for i in range(j * m, n + 1):
                dp[i][j] = dp[i - 1][j]

                # Update max_val wth the new candidate start position
                start = i - m
                if start >= (j - i) % m:
                    max_val = max(max_val, dp[start][j - 1] - prefix[start])

                if max_val != NEG_INF:
                    dp[i][j] = max(dp[i][j], prefix[i] + max_val)

        return int(dp[n][k])