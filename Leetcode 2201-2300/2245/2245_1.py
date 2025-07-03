# Leetcode 2245: Maximum Trailing Zeros in a Cornered Path
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/
# Solved on 3rd of July, 2025
class Solution:
    def maxTrailingZeros(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum number of trailing zeros in a cornered path within a given grid.

        A cornered path is defined as a path that starts at some cell, moves horizontally or vertically
        to another cell, and then turns 90 degrees to move in the perpendicular direction to a third cell.
        The path must include exactly three cells: the start, the corner, and the end.
        The number of trailing zeros is determined by the minimum count of factors of 2 and 5
        in the product of all numbers along the path.

        Args:
            grid: A list of lists of integers representing the grid.

        Returns:
            The maximum number of trailing zeros found among all possible cornered paths.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        def countFactors(num):
            count2 = 0
            tempNum = num
            while tempNum > 0 and tempNum % 2 == 0:
                count2 += 1
                tempNum //= 2

            count5 = 0
            tempNum = num
            while tempNum > 0 and tempNum % 5 == 0:
                count5 += 1
                tempNum //= 5

            return min(count2, count5)

        factorsTwo = [[0] * numCols for _ in range(numRows)]
        factorsFive = [[0] * numCols for _ in range(numRows)]

        for r in range(numRows):
            for c in range(numCols):
                factorsTwo[r][c], factorsFive[r][c] = countFactors(grid[r][c])

        prefixTwosH = [[0] * (numCols + 1) for _ in range(numRows)]
        prefixFivesH = [[0] * (numCols + 1) for _ in range(numRows)]
        prefixTwosV = [[0] * numCols for _ in range(numRows + 1)]
        prefixFivesV = [[0] * numCols for _ in range(numRows + 1)]

        for r in range(numRows):
            for c in range(numCols):
                prefixTwosH[r][c + 1] = prefixTwosH[r][c] + factorsTwo[r][c]
                prefixFivesH[r][c + 1] = prefixFivesH[r][c] + factorsFive[r][c]
                prefixTwosV[r + 1][c] = prefixTwosV[r][c] + factorsTwo[r][c]
                prefixFivesV[r + 1][c] = prefixFivesV[r][c] + factorsFive[r][c]

        maxZeros = 0

        for r in range(numRows):
            for c in range(numCols):
                twoCount, fiveCount = factorsTwo[r][c], factorsFive[r][c]

                upTwos = prefixTwosV[r][c]
                upFives = prefixFivesV[r][c]

                downTwos = prefixTwosV[numRows][c] - prefixTwosV[r + 1][c]
                downFives = prefixFivesV[numRows][c] - prefixFivesV[r + 1][c]

                leftTwos = prefixTwosH[r][c]
                leftFives = prefixFivesH[r][c]

                rightTwos = prefixTwosH[r][numCols] - prefixTwosH[r][c + 1]
                rightFives = prefixFivesH[r][numCols] - prefixFivesH[r][c + 1]

                maxZeros = max(maxZeros, min(upTwos + leftTwos + twoCount, upFives + leftFives + fiveCount))
                maxZeros = max(maxZeros, min(upTwos + rightTwos + twoCount, upFives + rightFives + fiveCount))
                maxZeros = max(maxZeros, min(downTwos + leftTwos + twoCount, downFives + leftFives + fiveCount))
                maxZeros = max(maxZeros, min(downTwos + rightTwos + twoCount, downFives + rightFives + fiveCount))

        return maxZeros