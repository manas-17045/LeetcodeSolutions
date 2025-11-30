# Leetcode 3742: Maximum Path Score in a Grid
# https://leetcode.com/problems/maximum-path-score-in-a-grid/
# Solved on 30th of November, 2025
class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        """
        Calculates the maximum path score in a grid.
        :param grid: The input grid.
        :param k: The maximum number of positive cells allowed in the path.
        :return: The maximum path score.
        """
        m = len(grid)
        n = len(grid[0])
        limit = min(k, m + n - 1)
        rowDp = [[-1] * (limit + 1) for _ in range(n)]
        rowDp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cellVal = grid[i][j]
                costInc = 1 if cellVal > 0 else 0
                scoreInc = cellVal

                topArr = rowDp[j] if i > 0 else None
                leftArr = rowDp[j - 1] if j > 0 else None

                if topArr and leftArr:
                    merged = [t if t > l else l for t, l in zip(topArr, leftArr)]
                elif topArr:
                    merged = topArr[:]
                else:
                    merged = leftArr[:]

                if costInc == 1:
                    shifted = merged[:-1]
                    currentRes = [-1] + [v + scoreInc if v != -1 else -1 for v in shifted]
                else:
                    currentRes = merged

                rowDp[j] = currentRes

        return max(rowDp[n - 1])