# Leetcode 2902: Count of Sub-Multisets With Bounded Sum
# https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/
# Solved on 8th of August, 2025
import collections


class Solution:
    def countSubMultisets(self, nums: list[int], l: int, r: int) -> int:
        """
        Counts the number of sub-multisets of `nums` whose sum is within the range [l, r].

        Args:
            nums (list[int]): A list of integers representing the multiset.
            l (int): The lower bound of the sum range (inclusive).
            r (int): The upper bound of the sum range (inclusive).

        Returns:
            int: The number of sub-multisets with a sum in the given range, modulo 1,000,000,007.
        """
        mod = 1_000_000_007
        freqMap = collections.Counter(nums)
        numZeros = freqMap.pop(0, 0)

        dp = [0] * (r + 1)
        dp[0] = 1

        for num, freq in freqMap.items():
            for currentSum in range(num, r + 1):
                dp[currentSum] = (dp[currentSum] + dp[currentSum - num]) % mod

            overdraftSum = num * (freq + 1)
            for currentSum in range(r, overdraftSum - 1, -1):
                dp[currentSum] = (dp[currentSum] - dp[currentSum - overdraftSum] + mod) % mod

        totalCount = 0
        for i in range(l, r + 1):
            totalCount = (totalCount + dp[i]) % mod

        return (totalCount * (numZeros + 1)) % mod