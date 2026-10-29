# Leetcode 4062: Transform Array Using Pair Operations
# https://leetcode.com/problems/transform-array-using-pair-operations/
# Solved on 29th of October, 2026
class Solution:
    def canTranform(self, source: list[int], target: list[int]) -> bool:
        """
        Determines whether the source array can be transformed into the target array.

        Parameters:
            source (list[int]): The initial list of integers.
            target (list[int]): The target list of integers.

        Returns:
            bool: True if source can be transformed to target, False otherwise."""
        sourceSum = sum(source)
        targetSum = sum(target)

        return sourceSum == targetSum