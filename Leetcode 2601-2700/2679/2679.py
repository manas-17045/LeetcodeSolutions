# Leetcode 2679: Sum in a Matrix
# https://leetcode.com/problems/sum-in-a-matrix/
# Solved on 8th of January, 2026
class Solution:
    def matrixSum(self, nums: list[list[int]]) -> int:
        """
        Calculates the sum of maximums of columns after sorting each row in descending order.

        Args:
            nums: A list of lists of integers representing the matrix.

        Returns:
            An integer representing the final score.
        """
        finalScore = 0
        for row in nums:
            row.sort()

        for col in zip(*nums):
            finalScore += max(col)

        return finalScore