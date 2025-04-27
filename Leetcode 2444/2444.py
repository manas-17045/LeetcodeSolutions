# Leetcode 2444: Count Subarrays with Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        last_bad_idx = -1
        last_minK_idx = -1
        last_maxK_idx = -1
        n = len(nums)

        for r in range(n):
            num = nums[r]
            if not (minK <= num <= maxK):
                last_bad_idx = r
            if num == minK:
                last_minK_idx = r
            if num == maxK:
                last_maxK_idx = r

            valid_l_upper_bound = min(last_minK_idx, last_maxK_idx)

            num_valid_l = valid_l_upper_bound - last_bad_idx
            count += max(0, num_valid_l)

        return count