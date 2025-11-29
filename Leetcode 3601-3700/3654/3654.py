# Leetcode 3654: Minimum Sum After Divisible Sum Deletions
# https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/
# Solved on 29th of November, 2025
class Solution:
    def minArraySum(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum sum of a subarray such that the sum is divisible by k.

        Args:
            nums: A list of integers.
            k: An integer representing the divisor.
        Returns:
            The minimum sum of a subarray whose sum is divisible by k.
        """
        dp = [float('inf')] * k
        dp[0] = 0
        prefix = 0

        for num in nums:
            prevRem = prefix
            prefix = (prefix + num) % k

            if dp[prevRem] != float('inf'):
                dp[prefix] = min(dp[prefix], dp[prevRem] + num)

        return int(dp[prefix])