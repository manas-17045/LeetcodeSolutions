# Leetcode 2871: Split Array Into Maximum Number of Subarrays
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/
# Solved on 16th of August, 2025
class Solution:
    def maxSubarrays(self, nums: list[int]) -> int:
        """
        Splits the given array `nums` into the maximum number of subarrays such that the bitwise AND of all elements
        in each subarray is non-negative.

        Args:
            nums: A list of integers.
        Returns:
            The maximum number of subarrays.
        """
        count = 0
        currentAnd = -1

        for num in nums:
            currentAnd &= num
            if currentAnd == 0:
                count += 1
                currentAnd = -1

        return max(1, count)