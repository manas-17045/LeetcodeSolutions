# Leetcode 3423: Maximum Difference Between Adjacent Elements in a Circular Array
# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
# Solved on 12th of June, 2025

class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        n = len(nums)
        """
        Calculates the maximum absolute difference between adjacent elements in a circular array.

        Args:
            nums: A list of integers representing the circular array.

        Returns:
            The maximum absolute difference between any two adjacent elements, considering the wrap-around from the last to the first element.
        """
        # Initialize with the last-first wrap-around difference
        max_diff = abs(nums[-1] - nums[0])

        # Check every adjacent pair nums[i] amd nums[i + 1]
        for i in range(n - 1):
            diff = abs(nums[i] - nums[i + 1])
            if diff > max_diff:
                max_diff = diff

        return max_diff