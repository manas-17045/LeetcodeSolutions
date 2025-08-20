# Leetcode 1878: Get Biggest Three Rhombus Sums in a Grid
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
# Solved on 20th of August, 2025
class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        """
        Calculates the three largest unique rhombus sums in a given grid.

        Args:
            grid (list[list[int]]): The input grid of integers.
        Returns:
            list[int]: A list containing the three largest unique rhombus sums, sorted in descending order.
        """
        numRows = len(grid)
        numCols = len(grid[0])
        rhombusSums = set()


        for r in range(numRows):
            for c in range(numCols):
                # Rhombus of size 0 is just the cell itself.
                rhombusSums.add(grid[r][c])

                # Determine the maximum possible k for the current center (r, c).
                # k is the distance from the center to corners along axes.
                maxPossibleK = min(r, c, numRows - 1 - r, numCols - 1 - c)

                # Iterate through possible sizes k > 0.
                for k in range(1, maxPossibleK + 1):
                    currentSum = 0
                    for i in range(k):
                        currentSum += grid[r - k + i][c + i]
                        currentSum += grid[r + i][c + k - i]
                        currentSum += grid[r + k - i][c - i]
                        currentSum += grid[r - i][c - k + i]

                    rhombusSums.add(currentSum)

        sortedSums = sorted(list(rhombusSums), reverse=True)

        return sortedSums[:3]