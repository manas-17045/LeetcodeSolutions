# Leetcode 2576: Find the Maximum Number of Marked Indices
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/
# Solved on 15th of October, 2025
class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        """
        Finds the maximum number of marked indices in an array.

        Args:
            nums: A list of integers.
        Returns:
            The maximum number of marked indices.
        """
        listSize = len(nums)
        nums.sort()

        left = 0
        right = listSize // 2
        markedCount = 0

        while left < listSize // 2 and right < listSize:
            if 2 * nums[left] <= nums[right]:
                markedCount += 2
                left += 1
                right += 1
            else:
                right += 1

        return markedCount