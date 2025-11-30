# Leetcode 1981: Minimize the Difference Between Target and Chosen Elements
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
# Solved on 30th of November, 2025
class Solution:
    def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
        """
        Minimizes the absolute difference between a target value and the sum of chosen elements.
        You must choose exactly one element from each row of the given matrix `mat`.

        Args:
            mat (list[list[int]]): A 2D integer matrix.
            target (int): The target integer value.

        Returns:
            int: The minimum absolute difference between the target and any possible sum.
        """
        possibleSums = 1
        for row in mat:
            currentSums = 0
            for val in set(row):
                currentSums |= (possibleSums << val)
            possibleSums = currentSums

        minDiff = float('inf')

        highPart = possibleSums >> target
        if highPart:
            diff = (highPart & -highPart).bit_length() - 1
            minDiff = min(minDiff, diff)

        lowMask = (1 << target) - 1
        lowPart = possibleSums & lowMask
        if lowPart:
            diff = target - (lowPart.bit_length() - 1)
            minDiff = min(minDiff, diff)

        return int(minDiff)