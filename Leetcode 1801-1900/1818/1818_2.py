# Leetcode 181: Minimum Absolute Sum Difference
# https://leetcode.com/problems/minimum-absolute-sum-difference/
# Solved on 23rd of August, 2025
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum absolute sum difference after replacing at most one element in nums1.

        Args:
            nums1 (list[int]): The first list of integers.
            nums2 (list[int]): The second list of integers.
        Returns:
            int: The minimum absolute sum difference modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums1)
        sorted_nums = sorted(nums1)
        orig_sum = 0
        max_saving = 0

        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            orig_sum += diff
            min_dist = self.findClosest(sorted_nums, nums2[i])
            saving = diff - min_dist
            if saving > max_saving:
                max_saving = saving

        result = orig_sum - max_saving
        return result % MOD

    def findClosest(self, sorted_nums, target):
        pos = bisect.bisect_left(sorted_nums, target)

        if pos == 0:
            return abs(sorted_nums[0] - target)

        if pos == len(sorted_nums):
            return abs(sorted_nums[-1] - target)

        return min(abs(sorted_nums[pos - 1] - target), abs(sorted_nums[pos] - target))