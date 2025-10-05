# Leetcode 417: Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Solved on 5th of October, 2025
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Finds all cells in a 2D grid of `heights` from which water can flow to both the Pacific and Atlantic oceans.

        Args:
            heights (list[list[int]]): A 2D list of integers representing the height of each cell.

        Returns:
            list[list[int]]: A list of [row, col] pairs representing the coordinates of cells from which water can flow to both oceans.
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # Sets to track cells that can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable):
            # Mark current cell as reachable
            reachable.add((r, c))

            # Explore all 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc

                # Check if the neighbor is valid, not visited, and water can flow from neighbor to current
                if (0 <= nr < m and 0 <= nc < n and
                        (nr, nc) not in reachable and
                        heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        # Start DFS from Pacific Ocean edges (top row and left column)
        for i in range(m):
            dfs(i, 0, pacific_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)

        # Start DFS from Atlantic Ocean edges (bottom row and right column)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)

        # Find intersection - cells that can reach both oceans
        result = []
        for r, c in pacific_reachable:
            if (r, c) in atlantic_reachable:
                result.append([r, c])

        return result