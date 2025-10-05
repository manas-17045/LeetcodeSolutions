# Leetcode 417: Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Solved on 5th of October, 2025
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        """
        Finds all cells in a 2D grid of `heights` from which water can flow to both the Pacific and Atlantic oceans.

        Water can flow from a cell to an adjacent cell (up, down, left, or right) if the adjacent cell's height
        is less than or equal to the current cell's height. The Pacific Ocean borders the top and left edges of the grid,
        and the Atlantic Ocean borders the bottom and right edges.

        Args:
            heights: A list of lists of integers representing the height of each cell in the grid.

        Returns:
            A list of lists of integers, where each inner list `[r, c]` represents the row and column
            of a cell from which water can flow to both oceans.
        """
        if not heights or not heights[0]:
            return []

        numRows = len(heights)
        numCols = len(heights[0])

        pacificReachable = set()
        atlanticReachable = set()

        def dfs(row, col, reachableSet):
            if (row, col) in reachableSet:
                return

            reachableSet.add((row, col))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dRow, dCol in directions:
                newRow = row + dRow
                newCol = col + dCol

                if 0 <= newRow < numRows and 0 <= newCol < numCols and heights[newRow][newCol] >= heights[row][col]:
                    dfs(newRow, newCol, reachableSet)

        for r in range(numRows):
            dfs(r, 0, pacificReachable)
            dfs(r, numCols - 1, atlanticReachable)

        for c in range(numCols):
            dfs(0, c, pacificReachable)
            dfs(numRows - 1, c, atlanticReachable)

        return list(map(list, pacificReachable & atlanticReachable))