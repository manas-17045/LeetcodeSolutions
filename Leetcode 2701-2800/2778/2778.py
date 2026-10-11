# Leetcode 2778: Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/
# Solved on 11th of October, 2026
class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        """
        Calculates the sum of the squares of all special elements in the array.

        Args:
            nums (list[int]): A list of integers representing the 1-indexed array.

        Returns:
            int: The sum of the squares of the special elements.
        """
        arrayLength = len(nums)
        totalSum = 0

        for i in range(1, arrayLength + 1):
            if arrayLength % i == 0:
                totalSum += nums[i - 1] * nums[i - 1]

        return totalSum