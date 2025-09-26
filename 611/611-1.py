# Leetocde 611: Valid Triangle Number
# https://leetcode.com/problems/valid-triangle-number/
# Solved on 26th of September, 2025
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

        :param nums: A list of integers representing potential side lengths.
        :type nums: list[int]
        :return: The number of valid triangle triplets.
        :rtype: int
        """
        numElements = len(nums)
        if numElements < 3:
            return 0

        nums.sort()

        triangleCount = 0

        for k in range(numElements - 1, 1, -1):
            left = 0
            right = k - 1

            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    triangleCount += (right - left)
                    right -= 1
                else:
                    left += 1

        return triangleCount