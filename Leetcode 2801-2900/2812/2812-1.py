# Leetcode 2812: Find the Safest Path in a Grid
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/
# Solved on 6th of October, 2025
import collections


class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        """
        Finds the maximum safeness factor of any path from (0, 0) to (n-1, n-1) in a grid.
        The safeness factor of a path is the minimum safeness value of any cell in that path.
        The safeness value of a cell is its Manhattan distance to the nearest thief (cell with value 1).

        Args:
            grid: A 2D list of integers where 1 represents a thief and 0 represents an empty cell.
        Returns:
            The maximum safeness factor achievable.
        """
        n = len(grid)

        safenessGrid = [[-1] * n for _ in range(n)]
        q = collections.deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    safenessGrid[r][c] = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            currentSafeness = safenessGrid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safenessGrid[nr][nc] == -1:
                    safenessGrid[nr][nc] = currentSafeness + 1
                    q.append((nr, nc))

        low = 0
        high = n * 2
        maxSafeness = 0

        while low <= high:
            mid = (low + high) // 2

            if self.pathExists(mid, safenessGrid, n):
                maxSafeness = mid
                low = mid + 1
            else:
                high = mid - 1

        return maxSafeness

    def pathExists(self, minSafeness: int, safenessGrid: list[list[int]], n : int) -> bool:
        if safenessGrid[0][0] < minSafeness or safenessGrid[n - 1][n - 1] < minSafeness:
            return False

        q = collections.deque([(0, 0)])
        visited = {(0, 0)}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            r, c = q.popleft()

            if r == n - 1 and c == n - 1:
                return True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    if safenessGrid[nr][nc] >= minSafeness:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        return False