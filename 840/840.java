// Leetcode 840: Magic Squares In Grid
// https://leetcode.com/problems/magic-squares-in-grid/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Given a grid of integers, return the number of 3 x 3 magic square subgrids.
     * A 3 x 3 magic square is a 3 x 3 grid of integers where all row sums, all column sums, and both diagonal sums are equal to 15.
     * @param grid The input grid of integers.
     * @return The number of 3 x 3 magic square subgrids.
     */
    public int numMagicSquaresInside(int[][] grid) {
        int count = 0;
        int rows = grid.length;
        int cols = grid[0].length;

        for (int i = 0; i <= rows - 3; i++) {
            for (int j = 0; j <= cols - 3; j++) {
                if (isValidMagicSquare(grid, i, j)) {
                    count++;
                }
            }
        }

        return count;
    }

    private boolean isValidMagicSquare(int[][] grid, int row, int col) {
        if (grid[row + 1][col + 1] != 5) {
            return false;
        }

        boolean[] seen = new boolean[10];
        for (int i = row; i < row + 3; i++) {
            for (int j = col; j < col + 3; j++) {
                int val = grid[i][j];
                if (val < 1 || val > 9 || seen[val]) {
                    return false;
                }
                seen[val] = true;
            }
        }

        if (grid[row][col] + grid[row][col + 1] + grid[row][col + 2] != 15) {
            return false;
        }
        if (grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2] != 15) {
            return false;
        }

        if (grid[row][col] + grid[row + 1][col] + grid[row + 2][col] != 15) {
            return false;
        }
        if (grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2] != 15) {
            return false;
        }

        if (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2] != 15) {
            return false;
        }
        if (grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col] != 15) {
            return false;
        }

        return true;
    }
}