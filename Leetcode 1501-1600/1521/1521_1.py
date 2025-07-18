# Leetcode 1521: Find a Value of a Mysterious Function Closest to Target
# https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/
# Solved on 18th of July, 2025
class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        """
        Given an array of integers `arr` and an integer `target`, this function finds a value `val`
        such that `val` is the result of a bitwise AND operation of a non-empty subarray of `arr`,
        and `abs(val - target)` is minimized.

        Args:
            arr (list[int]): The input array of integers.
            target (int): The target integer.

        Returns:
            int: The minimum absolute difference between a subarray AND result and the target.
        """
        minDiff = float('inf')
        possibleValues = set()

        for num in arr:
            currentValues = {num & val for val in possibleValues}
            currentValues.add(num)

            for val in currentValues:
                minDiff = min(minDiff, abs(val - target))

            if minDiff == 0:
                return 0

            possibleValues = currentValues

        return int(minDiff)