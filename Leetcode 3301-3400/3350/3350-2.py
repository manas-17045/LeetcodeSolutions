# Leetcode 3350: Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/
# Solved on 15th of October, 2025
class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible value of k such that there exist two non-overlapping increasing subarrays,
        each of length at least k.
        :param nums: A list of integers.
        :return: The maximum integer k.
        """
        n = len(nums)
        if n < 2:
            return 0

        prev_run = 0
        cur_run = 1
        maxk = 0

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cur_run += 1
            else:
                maxk = max(maxk, cur_run // 2)
                maxk = max(maxk, min(prev_run, cur_run))

                prev_run = cur_run
                cur_run = 1

        maxk = max(maxk, cur_run // 2)
        maxk = max(maxk, min(prev_run, cur_run))

        return maxk