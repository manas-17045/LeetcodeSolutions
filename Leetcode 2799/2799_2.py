# Leetcode 2799: Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/

from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_count = len(set(nums))
        n = len(nums)
        result = 0

        for left in range(n):
            counter = set()

            for right in range(left, n):
                counter.add(nums[right])

                if len(counter) == distinct_count:
                    result += n - right
                    break


        return result