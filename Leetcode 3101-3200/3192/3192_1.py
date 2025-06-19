# Leetcode 3192: Minimum Operations to Make Binary Array Elements Equal to One II
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/
# Solved on 19th of June, 2025

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make all elements in the binary array equal to one.
        An operation consists of flipping all elements from the current index to the end of the array.

        Args:
            nums: A list of integers, where each element is either 0 or 1.

        Returns:
            The minimum number of operations required.
        """
        operationsCount = 0
        isFlipped = 0

        for i in range(len(nums)):
            effectiveValue = nums[i] ^ isFlipped

            if effectiveValue == 0:
                operationsCount += 1
                isFlipped = 1 - isFlipped

        return operationsCount