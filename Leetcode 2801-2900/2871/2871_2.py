# Leetcode 2871: Split Array Into Maximum Number of Subarrays
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/
# Solved on 16th of August, 2025
class Solution:
    def maxSubarrays(self, nums: list[int]) -> int:
        """
        Calculates the maximum number of subarrays such that the bitwise AND of elements in each subarray is 0.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The maximum number of such subarrays.
        """
        # Start with all bits set
        cur = ~0
        count = 0
        for num in nums:
            cur &= num
            if cur == 0:
                count += 1
                # Reset for next subarray
                cur = ~0

        # At least one subarray always
        return max(1, count)