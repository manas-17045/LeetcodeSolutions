# Leetocde 611: Valid Triangle Number
# https://leetcode.com/problems/valid-triangle-number/
# Solved on 26th of September, 2025
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

        :param nums: A list of integers representing potential side lengths.
        :return: The number of triplets that can form a triangle.
        """
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        # Fix the largest size at index k, then use two pointers on [0...(k - 1)].
        for k in range(n - 1, 1, -1):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1

        return count