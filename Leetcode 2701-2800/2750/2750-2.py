# Leetcode 2750: Ways to Split Array Into Good Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/
# Solved on 29th of August, 2025
class Solution:
    def numberOfGoodSubarraySplits(self, nums: list[int]) -> int:
        """
        Calculates the number of good subarray splits.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The number of good subarray splits.
        """
        MOD = 10**9 + 7
        last_one = -1
        result = 1
        found_one = False

        for i, v in enumerate(nums):
            if v == 1:
                if not found_one:
                    found_one = True
                else:
                    zeros_between = i - last_one - 1
                    result = (result * (zeros_between + 1)) % MOD
                last_one = i

        return result if found_one else 0