# Leetcode 795: Number of Subarrays with Bounded Maximum
# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
# Solved on 5th of August, 2025
class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        """
        Calculates the number of subarrays where the maximum element is within the range [left, right].

        Args:
            nums (list[int]): The input array of integers.
            left (int): The lower bound of the maximum element.
            right (int): The upper bound of the maximum element.
        """
        result = 0
        countRight = 0
        countLeft = 0

        for num in nums:
            if num <= right:
                countRight += 1
            else:
                countRight = 0

            if num < left:
                countLeft += 1
            else:
                countLeft = 0

            result += countRight - countLeft

        return result