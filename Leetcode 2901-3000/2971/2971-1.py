# Leetcode 2971: Find Polygon With the Largest Perimeter
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/
# Solved on 26th of September, 2025
class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        Finds the largest perimeter of a polygon that can be formed from the given side lengths.

        :param nums: A list of integers representing the lengths of the sides.
        :return: The largest possible perimeter of a polygon, or -1 if no polygon can be formed.
        """
        nums.sort()

        currentPerimeter = sum(nums)

        numElements = len(nums)
        for i in range(numElements - 1, 1, -1):
            longestSize= nums[i]

            sumOfOtherSides = currentPerimeter - longestSize

            if sumOfOtherSides > longestSize:
                return currentPerimeter

            currentPerimeter -= longestSize

        return -1