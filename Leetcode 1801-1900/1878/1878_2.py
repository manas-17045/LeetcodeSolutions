# Leetcode 1878: Get Biggest Three Rhombus Sums in a Grid
# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/
# Solved on 20th of August, 2025
class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        """
        Finds the three largest unique "rhombus sums" in a given grid.
        :param grid: A 2D list of integers representing the grid.
        :return: A list of up to three integers, sorted in descending order, representing the largest unique rhombus sums.
        """
        m, n = len(grid), len(grid[0])
        dr = [[0] * n for _ in range(m)]
        dl = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                dr[r][c] = grid[r][c]
                if r > 0 and c > 0:
                    dr[r][c] += dr[r - 1][c - 1]
                dl[r][c] = grid[r][c]
                if r > 0 and c + 1 < n:
                    dl[r][c] += dl[r - 1][c + 1]

        def sum_dr(r1, c1, r2, c2):
            res = dr[r2][c2]
            if r1 > 0 and c1 > 0:
                res -= dr[r1 - 1][c1 - 1]
            return res

        def sum_dl(r1, c1, r2, c2):
            res = dl[r2][c2]
            if r1 > 0 and c1 + 1 < n:
                res -= dl[r1 - 1][c1 + 1]
            return res

        values = set()
        for i in range(m):
            for j in range(n):
                values.add(grid[i][j])
                max_s = min(i, m - 1 - i, j, n - 1 - j)
                for s in range(1, max_s + 1):
                    top = (i - s, j)
                    right = (i, j + s)
                    bottom = (i + s, j)
                    left = (i, j - s)
                    side1 = sum_dr(top[0], top[1], right[0], right[1])
                    side2 = sum_dl(right[0], right[1], bottom[0], bottom[1])
                    side3 = sum_dr(left[0], left[1], bottom[0], bottom[1])
                    side4 = sum_dl(top[0], top[1], left[0], left[1])
                    corner_sum = grid[top[0]][top[1]] + grid[right[0]][right[1]] + grid[bottom[0]][bottom[1]] + grid[left[0]][left[1]]
                    border_sum = side1 + side2 + side3 + side4 - corner_sum
                    values.add(border_sum)

        ans = sorted(values, reverse=True)[:3]
        return ans
