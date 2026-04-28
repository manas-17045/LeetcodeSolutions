# Leetcode 2033: Minimum Operations to Make a Uni-Value Grid
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
# Solved on 28th of April, 2026
class Solution:
    def minOperations(self, grid: list[list[int]], x: int) -> int:
        """
        Calculates the minimum number of operations to make all elements in the grid equal.
        An operation consists of adding or subtracting x from any element.

        :param grid: A 2D list of integers representing the grid.
        :param x: An integer representing the value to add or subtract.
        :return: The minimum operations required, or -1 if it's impossible.
        """
        flatGrid = []
        for row in grid:
            for val in row:
                flatGrid.append(val)

        targetMod = flatGrid[0] % x
        for val in flatGrid:
            if val % x != targetMod:
                return -1

        flatGrid.sort()
        numElements = len(flatGrid)
        midIndex = numElements // 2
        medianValue = flatGrid[midIndex]

        totalOperations = 0
        for val in flatGrid:
            totalOperations += abs(val - medianValue) // x

        return totalOperations