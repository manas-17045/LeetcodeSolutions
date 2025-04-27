# Leetcode 2799: Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/

from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        count = 0
        n = len(nums)

        for i in range(n):
            distinct_in_sub = set()
            for j in range(i, n):
                distinct_in_sub.add(nums[j])
                if len(distinct_in_sub) == distinct_count:
                    count += 1

        return count