# Leetcode 2132: Stamping the Grid
# https://leetcode.com/problems/stamping-the-grid/
# Solved on 23rd of October, 2025
class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        """
        Determines if it's possible to stamp all empty cells (0s) in a grid using a given stamp.

        Args:
            grid (list[list[int]]): The input grid where 0 represents an empty cell and 1 represents an obstacle.
            stampHeight (int): The height of the stamp.
            stampWidth (int): The width of the stamp.
        Returns:
            bool: True if all empty cells can be stamped, False otherwise.
        """
        m = len(grid)
        n = len(grid[0])

        prefixSum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                prefixSum[r + 1][c + 1] = grid[r][c] + prefixSum[r + 1][c] + prefixSum[r][c + 1] - prefixSum[r][c]

        coverageCount = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m - stampHeight + 1):
            for c in range(n - stampWidth + 1):
                r2 = r + stampHeight - 1
                c2 = c + stampWidth - 1

                rSum = prefixSum[r2 + 1][c2 + 1] - prefixSum[r][c2 + 1] - prefixSum[r2 + 1][c] + prefixSum[r][c]

                if rSum == 0:
                    rEnd = r + stampHeight
                    cEnd = c + stampWidth
                    coverageCount[r][c] += 1
                    coverageCount[rEnd][c] -= 1
                    coverageCount[r][cEnd] -= 1
                    coverageCount[rEnd][cEnd] += 1

        for r in range(m):
            for c in range(n):
                val = coverageCount[r][c]
                fromTop = coverageCount[r - 1][c] if r > 0 else 0
                fromLeft = coverageCount[r][c - 1] if c > 0 else 0
                fromDiag = coverageCount[r - 1][c - 1] if r > 0 and c > 0 else 0
                coverageCount[r][c] = val + fromTop + fromLeft - fromDiag

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and coverageCount[r][c] == 0:
                    return False

        return True