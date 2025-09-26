# Leetcode 2971: Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
# Solved on 26th of September, 2025
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Given an array of positive integers nums, return the largest perimeter of a polygon that can be formed from nums,
        where the polygon must have at least 3 sides. If it is impossible to form any polygon, return -1.

        Args:
            nums (list[int]): An array of positive integers.
        Returns:
            int: The largest perimeter of a polygon, or -1 if impossible.
        """
        nums.sort()
        total = sum(nums)
        n = len(nums)

        # Try using as many sides as possible, removing the largest until inequality holds.
        while n >= 3:
            largest = nums[n - 1]
            if largest < total - largest:
                return total

            # Remove the largest side and continue
            total -= largest
            n -= 1

        return -1