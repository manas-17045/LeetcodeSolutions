# Leetcode 3978: Unique Middle Element
# https://leetcode.com/problems/unique-middle-element/s
# Solved on 26th of July, 2026
class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        """
        Checks if the middle element of the array is unique.
        @param nums: The array of integers.
        @return: True if the middle element is unique, False otherwise.
        """
        middleValue = nums[len(nums) // 2]
        return nums.count(middleValue) == 1