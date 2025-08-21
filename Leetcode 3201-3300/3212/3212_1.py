# Leetcode 3212: Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# Solved on 21st of August, 2025
class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        """
        Counts the number of submatrices within the given grid where the frequency of 'X' and 'Y' characters are equal and greater than zero.

        Args:
            grid (list[list[str]]): A 2D list of strings representing the grid, where each string is either 'X', 'Y', or '.'.
        Returns:
            int: The total count of such submatrices.
        """
        numRows = len(grid)
        numCols = len(grid[0])

        colPrefixSums = [[0, 0] for _ in range(numCols)]
        result = 0

        for r in range(numRows):
            rowPrefixSum = [0, 0]

            for c in range(numCols):
                if grid[r][c] == 'X':
                    rowPrefixSum[0] += 1
                elif grid[r][c] == 'Y':
                    rowPrefixSum[1] += 1

                colPrefixSums[c][0] += rowPrefixSum[0]
                colPrefixSums[c][1] += rowPrefixSum[1]

                countX = colPrefixSums[c][0]
                countY = colPrefixSums[c][1]

                if countX > 0 and countX == countY:
                    result += 1

        return result