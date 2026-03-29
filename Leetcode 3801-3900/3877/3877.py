# Leetcode 3877: Minimum Removals to Achieve Target XOR
# https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/
# Solved on 29th of March, 2026
class Solution:
    def minRemovals(self, nums: list[int], target: int) -> int:
        """
        Calculates the minimum number of elements to remove from nums so that the XOR sum of the remaining elements equals target.

        :param nums: List of integers to process.
        :param target: The desired XOR sum.
        :return: Minimum removals required, or -1 if the target XOR sum is unreachable.
        """
        dp = [-1] * 16384
        dp[0] = 0

        for num in nums:
            nextDp = list(dp)
            for x in range(16384):
                if dp[x] != -1 and dp[x] + 1 > nextDp[x ^ num]:
                    nextDp[x ^ num] = dp[x] + 1
            dp = nextDp

        return len(nums) - dp[target] if dp[target] != -1 else -1