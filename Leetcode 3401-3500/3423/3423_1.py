# Leetcode 3423: Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
# Solved on 12th of June, 2025

class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        """
        Finds the maximum absolute difference between adjacent elements in a circular array.

        Args:
            nums: A list of integers representing the circular array.

        Returns:
            The maximum absolute difference between adjacent elements.
        """
        listLength = len(nums)
        maxDifference = abs(nums[0] - nums[1])
        for i in range(listLength - 1):
            currentDifference = abs(nums[i] - nums[i + 1])
            if currentDifference > maxDifference:
                maxDifference = currentDifference
        return maxDifference