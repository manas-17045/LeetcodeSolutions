# Leetcode 3197: Find the Minimum Area to Cover All Ones II
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/
# Solved on 23rd of August, 2025
class Solution:
    def minimumSum(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum possible sum of areas of three non-overlapping rectangles
        that collectively cover all '1's in the given binary grid.

        Args:
            grid: A list of lists of integers representing the binary grid (0s and 1s).

        Returns:
            The minimum sum of areas of the three rectangles.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def get_area(ra: int, rb: int, ca: int, cb: int) -> int:
            if ra > rb or ca > cb:
                return 0

            min_r, max_r, min_c, max_c = float('inf'), -1, float('inf'), -1
            for i in range(ra, rb + 1):
                for j in range(ca, cb + 1):
                    if grid[i][j] == 1:
                        min_r = min(min_r, i)
                        max_r = max(max_r, i)
                        min_c = min(min_c, j)
                        max_c = max(max_c, j)

            if min_r == float('inf'):
                return 0

            return (max_r - min_r + 1) * (max_c - min_c + 1)

        ans = float('inf')

        # Three horizontal strips
        for h1 in range(1, m - 1):
            for h2 in range(h1 + 1, m):
                a1 = get_area(0, h1 - 1, 0, n - 1)
                a2 = get_area(h1, h2 - 1, 0, n - 1)
                a3 = get_area(h2, m - 1, 0, n - 1)
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Three vertical strips
        for v1 in range(1, n - 1):
            for v2 in range(v1 + 1, n):
                a1 = get_area(0, m - 1, 0, v1 - 1)
                a2 = get_area(0, m - 1, v1, v2 - 1)
                a3 = get_area(0, m - 1, v2, n - 1)
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Horizontal split, then vertical on top
        for h in range(1, m):
            for v in range(1, n):
                a1 = get_area(0, h - 1, 0, v - 1)
                a2 = get_area(0, h - 1, v, n - 1)
                a3 = get_area(h, m - 1, 0, n - 1)
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Horizontal split, then vertical on bottom
        for h in range(1, m):
            for v in range(1, n):
                a1 = get_area(0, h - 1, 0, n - 1)
                a2 = get_area(h, m - 1, 0, v - 1)
                a3 = get_area(h, m - 1, v, n - 1)
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Vertical split, then horizontal on left
        for v in range(1, n):
            for h in range(1, m):
                a1 = get_area(0, h - 1, 0, v - 1)
                a2 = get_area(h, m - 1, 0, v - 1)
                a3 = get_area(0, m - 1, v, n - 1)
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        # Vertical split, then horizontal on right
        for v in range(1, n):
            for h in range(1, m):
                a1 = get_area(0, m - 1, 0, v - 1)
                a2 = get_area(0, h - 1, v, n - 1)
                a3 = get_area(h, m - 1, v, n - 1)
                if a1 > 0 and a2 > 0 and a3 > 0:
                    ans = min(ans, a1 + a2 + a3)

        return ans