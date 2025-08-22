# Leetcode 3195: Find the Minimum Area to Cover All Ones I
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/
# Solved on 22nd of August, 2025
class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        """
        Calculates the minimum area of a rectangle that encloses all '1's in a binary grid.
        :param grid: A list of lists of integers representing the binary grid.
        :return: The minimum area of the bounding rectangle.
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        min_r, max_r = m, -1
        min_c, max_c = n, -1

        for i in range(m):
            row = grid[i]
            for j, val in enumerate(row):
                if val == 1:
                    if i < min_r:
                        min_r = i
                    if i > max_r:
                        max_r = i
                    if j < min_c:
                        min_c = j
                    if j > max_c:
                        max_c = j

        # If no 1's found (defensive), return 0
        if max_r == -1:
            return 0

        height = max_r - min_r + 1
        width = max_c - min_c + 1

        return height * width