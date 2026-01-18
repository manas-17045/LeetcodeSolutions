// Leetcode 1895: Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/
// Solved on 18th of January, 2026
class Solution {
    /**
     * Finds the largest magic square within the given grid.
     * A magic square is a square subgrid where the sum of each row, each column, and both main diagonals are equal.
     *
     * @param grid The input 2D integer array representing the grid.
     * @return The side length of the largest magic square found.
     */
    public int largestMagicSquare(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] rowSum = new int[m][n + 1];
        int[][] colSum = new int[m + 1][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j];
                colSum[i + 1][j] = colSum[i][j] + grid[i][j];
            }
        }

        for (int k = Math.min(m, n); k > 1; k--) {
            for (int i = 0; i <= m - k; i++) {
                for (int j = 0; j <= n - k; j++) {
                    if (isMagic(grid, rowSum, colSum, i, j, k)) {
                        return k;
                    }
                }
            }
        }

        return 1;
    }

    private boolean isMagic(int[][] grid, int[][] rowSum, int[][] colSum, int r, int c, int k) {
        int targetSum = rowSum[r][c + k] - rowSum[r][c];

        for (int i = 1; i < k; i++) {
            if (rowSum[r + i][c + k] - rowSum[r + i][c] != targetSum) {
                return false;
            }
        }

        for (int j = 0; j < k; j++) {
            if (colSum[r + k][c + j] - colSum[r][c + j] != targetSum) {
                return false;
            }
        }

        int diag1 = 0;
        int diag2 = 0;
        for (int i = 0; i < k; i++) {
            diag1 += grid[r + i][c + i];
            diag2 += grid[r + i][c + k - 1 - i];
        }

        return diag1 == targetSum && diag2 == targetSum;
    }
}