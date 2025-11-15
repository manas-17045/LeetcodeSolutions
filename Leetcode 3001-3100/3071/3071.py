# Leetcode 3071: Minimum Operations to Write the Letter Y on a Grid
# https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/
# Solved on 14th of November, 2025
class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum operations to write the letter 'Y' on a grid.

        Args:
            grid: A list of lists of integers representing the grid.
        Returns:
            The minimum number of operations required.
        """
        n = len(grid)
        center = n // 2

        yCounts = [0, 0, 0]
        notYCounts = [0, 0, 0]

        for r in range(n):
            for c in range(n):
                val = grid[r][c]

                isYCell = False
                if r == c and r <= center:
                    isYCell = True
                elif c == n - 1 - r and r <= center:
                    isYCell = True
                elif c == center and r >= center:
                    isYCell = True

                if isYCell:
                    yCounts[val] += 1
                else:
                    notYCounts[val] += 1

        totalYCells = sum(yCounts)
        totalNotYCells = sum(notYCounts)

        minOps = float('inf')

        for yValue in range(3):
            for notYValue in range(3):
                if yValue == notYValue:
                    continue

                opsY = totalYCells - yCounts[yValue]
                opsNotY = totalNotYCells - notYCounts[notYValue]

                currentOps = opsY + opsNotY
                minOps = min(minOps, currentOps)

        return minOps