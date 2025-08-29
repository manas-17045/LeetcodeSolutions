# Leetcode 2750: Ways to Split Array Into Good Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/
# Solved on 29th of August, 2025
class Solution:
    def numberOfGoodSubarraySplits(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to split an array into good subarrays.
        A good subarray is one that contains at least one '1'.

        :param nums: A list of integers (0s and 1s).
        :return: The number of ways to split the array into good subarrays, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        lastOneIndex = -1
        totalWays = 1

        for i in range(len(nums)):
            if nums[i] == 1:
                if lastOneIndex != -1:
                    ways = i - lastOneIndex
                    totalWays = (totalWays * ways) % MOD
                lastOneIndex = i

        if lastOneIndex == -1:
            return 0
        else:
            return totalWays