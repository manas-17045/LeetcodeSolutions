# Leetcode 2518: Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions/
# Solved on 26th of August, 2025
class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of "great partitions" of an array `nums`.
        A partition is considered "great" if both partitions have a sum of at least `k`.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The minimum sum required for each partition to be considered "great".

        Returns: The number of great partitions.
        """
        mod = 10 ** 9 + 7
        n = len(nums)

        totalSum = sum(nums)
        if totalSum < 2 * k:
            return 0

        dp = [0] * k
        dp[0] = 1

        for num in nums:
            for j in range(k - 1, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % mod

        invalidSubsetCount = sum(dp) % mod

        totalPartitions = pow(2, n, mod)

        invalidPartitions = (2 * invalidSubsetCount) % mod

        result = (totalPartitions - invalidPartitions + mod) % mod

        return result