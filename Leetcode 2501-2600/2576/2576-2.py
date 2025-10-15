# Leetcode 2576: Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/
# Solved on 15th of October, 2025
class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        """
        Given a 0-indexed integer array nums, return the maximum number of marked indices in the array.
        An index i is marked if there exists some unmarked index j such that nums[i] * 2 <= nums[j].

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The maximum number of marked indices.
        """
        nums.sort()
        n = len(nums)
        i, j = 0, n // 2
        pairs = 0

        # Try to pair smallest half (i) with elements in the latter half (j)
        while i < n // 2 and j < n:
            if nums[i] * 2 <= nums[j]:
                pairs += 1
                i += 1
                j += 1
            else:
                j += 1

        return pairs * 2