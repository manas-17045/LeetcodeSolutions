# Leetcode 3197: Find the Minimum Area to Cover All Ones II
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/
# Solved on 23rd of August, 2025
class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum total area of three non-overlapping rectangles that cover all '1's in the grid.

        Args:
            grid: A 2D list of integers (0s and 1s) representing the grid.
        Returns:
            The minimum possible sum of areas of three rectangles.
        """
        rows = len(grid)
        cols = len(grid[0])
        memo = {}

        def findArea(r1, c1, r2, c2):
            coordTuple = (r1, c1, r2, c2)
            if coordTuple in memo:
                return memo[coordTuple]

            minR, maxR = float('inf'), float('-inf')
            minC, maxC = float('inf'), float('-inf')
            hasOne = False
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        hasOne = True
                        minR = min(minR, r)
                        maxR = max(maxR, r)
                        minC = min(minC, c)
                        maxC = max(maxC, c)

            if not hasOne:
                result = float('inf')
            else:
                result = (maxR - minR + 1) * (maxC - minC + 1)

            memo[coordTuple] = result
            return result

        minSum = float('inf')

        for i in range(rows - 2):
            for j in range(i + 1, rows - 1):
                currentSum = findArea(0, 0, i, cols - 1) + \
                             findArea(i + 1, 0, j, cols - 1) + \
                             findArea(j + 1, 0, rows - 1, cols - 1)
                minSum = min(minSum, currentSum)

        for i in range(cols - 2):
            for j in range(i + 1, cols - 1):
                currentSum = findArea(0, 0, rows - 1, i) + \
                             findArea(0, i + 1, rows - 1, j) + \
                             findArea(0, j + 1, rows - 1, cols - 1)
                minSum = min(minSum, currentSum)

        for i in range(rows - 1):
            for j in range(cols - 1):
                sumOne = findArea(0, 0, i, j) + \
                         findArea(0, j + 1, i, cols - 1) + \
                         findArea(i + 1, 0, rows - 1, cols - 1)
                minSum = min(minSum, sumOne)

                sumTwo = findArea(0, 0, i, cols - 1) + \
                         findArea(i + 1, 0, rows - 1, j) + \
                         findArea(i + 1, j + 1, rows - 1, cols - 1)
                minSum = min(minSum, sumTwo)

        for i in range(cols - 1):
            for j in range(rows - 1):
                sumOne = findArea(0, 0, j, i) + \
                         findArea(j + 1, 0, rows - 1, i) + \
                         findArea(0, i + 1, rows - 1, cols - 1)
                minSum = min(minSum, sumOne)

                sumTwo = findArea(0, 0, rows - 1, i) + \
                         findArea(0, i + 1, j, cols - 1) + \
                         findArea(j + 1, i + 1, rows - 1, cols - 1)
                minSum = min(minSum, sumTwo)

        return int(minSum)
