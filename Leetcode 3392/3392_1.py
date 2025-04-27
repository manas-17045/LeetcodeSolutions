# Leetcode 3392: Count Subarrays of Length Three With a Condition
# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        """
        Count the number of subarrays of length exactly 3 that satisfy the
        condition: the sum of the first and third elements equals exactly
        half of the second element.

        Args:
            nums: The input list of integers.
                  Constraints: 3 <= len(nums) <= 100, -100 <= nums[i] <= 100.

        Returns:
            The count of subarrays [a, b, c] such that a + c == b / 2.
            This is checked using the equivalent integer condition 2 * (a + c) == b.
        """

        count = 0
        n = len(nums)

        for i in range(n - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]

            if 2 * (a + c) == b:
                count += 1

        return count