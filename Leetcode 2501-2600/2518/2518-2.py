# Leetcode 2518: Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions/
# Solved on 26th of August, 2025
class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of ways to partition the array `nums` into two non-empty subarrays
        such that the sum of elements in each subarray is at least `k`.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The minimum required sum for each partition.
        Returns:
            int: The number of ways to partition the array.
        """
        MOD = 10**9 + 7
        n = len(nums)
        total = sum(nums)

        # If total sum is less than 2^k, it's impossible for both groups to be >= k.
        if total < 2 * k:
            return 0

        # dp[s] = number of subsets with sum exactly s, for 0 <= s < k.
        dp = [0] * k
        dp[0] = 1   # Empty subset

        # For each number, update dp in reverse
        for num in nums:
            if num >= k:
                continue

            for s in range(k - 1, num - 1, -1):
                dp[s] = (dp[s] + dp[s - num]) % MOD

        # Number of subsets with sum < k
        count_less_k = sum(dp) % MOD

        total_partitions = pow(2, n, MOD)
        # Subtract partitions where one side has sum < k (there are two ordered sides)
        ans = (total_partitions - 2 * count_less_k) % MOD
        return ans