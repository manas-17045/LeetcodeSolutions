# Leetcode 3212: Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# Solved on 21st of August, 2025
class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        """
        Calculates the number of submatrices in a given grid where the count of 'X's equals the count of 'Y's,
        and both counts are greater than zero.
        :param grid: A list of lists of strings representing the grid. Each string is either 'X', 'Y', or '.'.
        :return: The total number of valid submatrices.
        """
        m, n = len(grid), len(grid[0])

        # Prefix sums
        cntX = [[0] * (n + 1) for _ in range(m + 1)]
        cntY = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                isX = 1 if grid[i - 1][j - 1] == 'X' else 0
                isY = 1 if grid[i - 1][j - 1] == 'Y' else 0
                cntX[i][j] = cntX[i - 1][j] + cntX[i][j - 1] - cntX[i - 1][j - 1] + isX
                cntY[i][j] = cntY[i - 1][j] + cntY[i][j - 1] - cntY[i - 1][j - 1] + isY

        ans = 0
        for i in range(m):
            for j in range(n):
                # Submatrix from (0,0) to (i,j)
                x_count = cntX[i + 1][j + 1]
                y_count = cntY[i + 1][j + 1]
                if x_count > 0 and x_count == y_count:
                    ans += 1

        return ans