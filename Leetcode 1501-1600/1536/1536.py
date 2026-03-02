# Leetcode 1536: Minimum Swaps to Arrange a Binary Grid
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
# Solved on 2nd of March, 2026
class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum number of adjacent row swaps needed to make the grid valid.
        A grid is valid if all cells above the main diagonal are zeros.

        :param grid: A square n x n binary grid.
        :return: The minimum swaps required, or -1 if it's impossible.
        """
        gridSize = len(grid)
        trailingZeros = []
        for row in grid:
            zeroCount = 0
            for i in range(gridSize - 1, -1, -1):
                if row[i] == 0:
                    zeroCount += 1
                else:
                    break
            trailingZeros.append(zeroCount)

        totalSwaps = 0
        for i in range(gridSize):
            targetZeros = gridSize - 1 - i
            foundIndex = -1
            for j in range(i, gridSize):
                if trailingZeros[j] >= targetZeros:
                    foundIndex = j
                    break

            if foundIndex == -1:
                return -1

            totalSwaps += foundIndex - i
            poppedValue = trailingZeros.pop(foundIndex)
            trailingZeros.insert(i, poppedValue)

        return totalSwaps