// Leetcode 1254: Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/
// Solved on 25th of October, 2026
class Solution {
    /**
     * Calculates the number of closed islands in a given grid.
     * An island is considered closed if it is completely surrounded
     * by water cells and does not touch any boundary of the grid.
     *
     * @param grid a 2D integer array where 0 represents land and 1 represents water
     * @return the total number of closed islands
     */
    public int closedIsland(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;

        for (int r = 0; r < rows; r++) {
            if (grid[r][0] == 0) {
                floodFill(grid, r, 0, rows, cols);
            }
            if (grid[r][cols - 1] == 0) {
                floodFill(grid, r, cols - 1, rows, cols);
            }
        }

        for (int c = 0; c < cols; c++) {
            if (grid[0][c] == 0) {
                floodFill(grid, 0, c, rows, cols);
            }
            if (grid[rows - 1][c] == 0) {
                floodFill(grid, rows - 1, c, rows, cols);
            }
        }

        int closedIslandCount = 0;

        for (int r = 1; r < rows - 1; r++) {
            for (int c = 1; c < cols - 1; c++) {
                if (grid[r][c] == 0) {
                    floodFill(grid, r, c, rows, cols);
                    closedIslandCount++;
                }
            }
        }

        return closedIslandCount;
    }

    private void floodFill(int[][] grid, int row, int col, int rows, int cols) {
        if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] == 1) {
            return;
        }

        grid[row][col] = 1;

        floodFill(grid, row + 1, col, rows, cols);
        floodFill(grid, row - 1, col, rows, cols);
        floodFill(grid, row, col + 1, rows, cols);
        floodFill(grid, row, col - 1, rows, cols);
    }
}