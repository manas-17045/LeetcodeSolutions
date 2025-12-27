# Leetcode 3727: Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/
# Solved on 27th of December, 2025
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum alternating sum of squares for a given list of numbers.
        :param nums: A list of integers.
        :return: The maximum alternating sum of squares.
        """
        listLength = len(nums)
        for i in range(listLength):
            nums[i] = nums[i] * nums[i]

        nums.sort()
        midIndex = listLength // 2

        return sum(nums[midIndex:]) - sum(nums[:midIndex])