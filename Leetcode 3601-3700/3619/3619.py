# Leetcode 3619: Count Islands With Total Value Divisible by K
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
# Solved on 27th of November, 2025
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        """
        Counts the number of islands in a grid where the total value of the island is divisible by k.

        Args:
            grid: A 2D list of integers representing the grid. Positive integers represent land cells with a value.
            k: An integer. The divisor for checking island total value.

        Returns:
            The number of islands whose total value is divisible by k.
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islandCount = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    islandValue = 0
                    stack = [(r, c)]
                    islandValue += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        currR, currC = stack.pop()

                        for dr, dc in directions:
                            nr, nc = currR + dr, currC + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                                islandValue += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if islandValue % k == 0:
                        islandCount += 1

        return islandCount