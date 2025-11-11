# Leetcode 2610: Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
# Solved on 11th of November, 2025
import collections


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        """
        Converts a 1D array of integers into a 2D array with the following conditions:
        1. Each row contains distinct integers.
        2. The number of rows should be minimal.

        Args:
            nums: A list of integers.
        Returns:
            A 2D list of integers representing the converted matrix.
        """
        numCounts = collections.defaultdict(int)
        resultMatrix = []

        for num in nums:
            rowIndex = numCounts[num]

            if rowIndex == len(resultMatrix):
                resultMatrix.append([])

            resultMatrix[rowIndex].append(num)
            numCounts[num] += 1

        return resultMatrix