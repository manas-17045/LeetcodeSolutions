# Leetcode 976: Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/
# Solved on 28th of September, 2025
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the largest perimeter of a triangle with non-zero area,
        formed from three of these lengths. If it is impossible to form any triangle of non-zero area, return 0.
        :param nums: A list of integers representing potential side lengths.
        :return: The largest perimeter of a valid triangle, or 0 if no such triangle can be formed.
        """
        # Need at least 3 sides
        if len(nums) < 3:
            return 0

        # Sort descending so we can test largest triples first
        nums.sort(reverse=True)

        # Check consecutive triples: if largest < sum of next two -> valid triangle
        for i in range(len(nums) - 2):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if a < b + c:
                return a + b + c

        return 0