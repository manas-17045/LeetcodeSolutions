# Leetcode 3010: Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
# Solved on 1st of February, 2026
class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        """
        Calculates the minimum possible sum of the first elements of three subarrays.

        :param nums: A list of integers to be divided into three subarrays.
        :return: The minimum total cost of the three subarrays.
        """
        minimumOne = float('inf')
        minimumTwo = float('inf')

        for index in range(1, len(nums)):
            currentValue = nums[index]
            if currentValue < minimumOne:
                minimumTwo = minimumOne
                minimumOne = currentValue
            elif currentValue < minimumTwo:
                minimumTwo = currentValue

        return nums[0] + minimumOne + minimumTwo