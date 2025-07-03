# Leetcode 2245: Maximum Trailing Zeros in a Cornered Path
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/
# Solved on 3rd of July, 2025
class Solution:
    def maxTrailingZeros(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum number of trailing zeros in a path shaped like a plus sign (+)
        within a given grid of integers.

        A path consists of a horizontal segment and a vertical segment that intersect at a cell.
        The number of trailing zeros is determined by the minimum count of factors of 2 and 5
        in the product of all numbers along the path.

        The solution uses prefix sums to efficiently calculate the number of factors of 2 and 5
        for various path segments.
        """
        m, n = len(grid), len(grid[0])

        # helper to count p-factors in x
        def count_factor(x: int, p: int) -> int:
            c = 0
            while x % p == 0:
                x //= p
                c += 1
            return c

        # build arrays of factor-counts
        two = [[0] * n for _ in range(m)]
        five = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                two[i][j] = count_factor(val, 2)
                five[i][j] = count_factor(val, 5)

        # prefix sums along rows and columns
        row2 = [[0] * n for _ in range(m)]
        row5 = [[0] * n for _ in range(m)]
        col2 = [[0] * n for _ in range(m)]
        col5 = [[0] * n for _ in range(m)]

        for i in range(m):
            acc2 = acc5 = 0
            for j in range(n):
                acc2 += two[i][j]
                acc5 += five[i][j]
                row2[i][j] = acc2
                row5[i][j] = acc5

        for j in range(n):
            acc2 = acc5 = 0
            for i in range(m):
                acc2 += two[i][j]
                acc5 += five[i][j]
                col2[i][j] = acc2
                col5[i][j] = acc5

        ans = 0

        # for each cell as corner
        for i in range(m):
            for j in range(n):
                c2, c5 = two[i][j], five[i][j]

                # horizontal arm to the left, including (i,j)
                left2 = row2[i][j]
                left5 = row5[i][j]
                # horizontal arm to the right, including (i,j)
                right2 = row2[i][n - 1] - (row2[i][j - 1] if j > 0 else 0)
                right5 = row5[i][n - 1] - (row5[i][j - 1] if j > 0 else 0)

                # vertical arm upward, including (i,j)
                up2 = col2[i][j]
                up5 = col5[i][j]
                # vertical arm downward, including (i,j)
                down2 = col2[m - 1][j] - (col2[i - 1][j] if i > 0 else 0)
                down5 = col5[m - 1][j] - (col5[i - 1][j] if i > 0 else 0)

                # combine without double counting the corner gcf
                # 1) left + up
                total2 = left2 + up2 - c2
                total5 = left5 + up5 - c5
                ans = max(ans, min(total2, total5))

                # 2) left + down
                total2 = left2 + down2 - c2
                total5 = left5 + down5 - c5
                ans = max(ans, min(total2, total5))

                # 3) right + up
                total2 = right2 + up2 - c2
                total5 = right5 + up5 - c5
                ans = max(ans, min(total2, total5))

                # 4) right + down
                total2 = right2 + down2 - c2
                total5 = right5 + down5 - c5
                ans = max(ans, min(total2, total5))

        return ans