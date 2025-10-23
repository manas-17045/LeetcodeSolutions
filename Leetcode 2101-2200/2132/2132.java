// Leetcode 2132: Stamping the Grid
// https://leetcode.com/problems/stamping-the-grid/
// Solved on 23rd of October, 2025
class Solution {
    /**
     * Checks if it's possible to stamp all empty cells (0s) in a grid using a given stamp.
     * @param grid The input grid, where 0 represents an empty cell and 1 represents an obstacle.
     * @param stampHeight The height of the stamp.
     * @param stampWidth The width of the stamp.
     * @return True if all empty cells can be covered by stamps, false otherwise.
     */
    public boolean possibleToStamp(int[][] grid, int stampHeight, int stampWidth) {
        int m = grid.length;
        int n = grid[0].length;

        // Build 2D prefix sum to check if area contains only zeros
        int[][] prefixSum = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSum[i][j] = grid[i - 1][j - 1] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1];
            }
        }

        // Create difference array to mark where stamps can be placed
        int[][] diff = new int[m + 2][n + 2];

        // Try placing stamp at each valid position
        for (int i = 0; i <= m - stampHeight; i++) {
            for (int j = 0; j <= n - stampWidth; j++){
                // Check if we can place stamp at (i, j)
                int r1 = i + 1;
                int c1 = j + 1;
                int r2 = i + stampHeight;
                int c2 = j + stampWidth;

                int sum = prefixSum[r2][c2] - prefixSum[r1 - 1][c2] - prefixSum[r2][c1 - 1] + prefixSum[r1 - 1][c1 - 1];
                
                // If area is all zeros, mark it in difference array
                if (sum == 0) {
                    diff[i][j]++;
                    diff[i + stampHeight][j]--;
                    diff[i][j + stampWidth]--;
                    diff[i + stampHeight][j + stampWidth]++;
                }
            }
        }

        // Convert difference array to actual coverage using 2D prefix sum
        int[][] coverage = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                coverage[i][j] = diff[i][j];
                if (i > 0) coverage[i][j] += coverage[i - 1][j];
                if (j > 0) coverage[i][j] += coverage[i][j - 1];
                if (i > 0 && j > 0) coverage[i][j] -= coverage[i - 1][j - 1];
            }
        }

        // Check if all empty cells are covered
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0 && coverage[i][j] == 0) {
                    return false;
                }
            }
        }

        return true;
    }
}