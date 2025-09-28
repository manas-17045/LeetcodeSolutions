# Leetcode 976: Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/
# Solved on 28th of September, 2025
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the largest perimeter of a triangle with non-zero area,
        formed from three of these lengths. If it is impossible to form any triangle of non-zero area, return 0.

        :param nums: A list of integers representing the lengths of line segments.
        :return: The largest perimeter of a triangle that can be formed, or 0 if no such triangle can be formed.
        """
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]

        return 0