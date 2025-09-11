# Leetcode 3250: Find the Count of Monotonic Pairs I
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/
# Solved on 11th of September, 2025
class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        """
        Calculates the count of monotonic pairs based on the given constraints.

        Args:
            nums (list[int]): A list of integers representing the constraints for each position.
        Returns:
            int: The total count of monotonic pairs modulo 10^9 + 7.
        """
        n = len(nums)
        mod = 10**9 + 7
        maxVal = 51

        dp = [0] * maxVal

        for val in range(nums[0] + 1):
            dp[val] = 1

        for i in range(1, n):
            prefixSum = [0] * maxVal
            prefixSum[0] = dp[0]
            for k in range(1, maxVal):
                prefixSum[k] = (prefixSum[k - 1] + dp[k]) % mod

            newDp = [0] * maxVal
            diff = nums[i] - nums[i - 1]

            for val in range(nums[i] + 1):
                upperBound = val - max(0, diff)
                upperBound = min(upperBound, nums[i - 1])

                if upperBound >= 0:
                    newDp[val] = prefixSum[upperBound]

            dp = newDp

        totalCount = sum(dp) % mod
        return totalCount