# Leetcode 3392: Count Subarrays of Length Three With a Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        if n < 3:
            return 0

        for i in range(n - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]

            if first + third == middle / 2:
                count += 1

        return count