// Leetcode 3989: Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/
// Solved on 9th of August, 2026
class Solution {
    /**
     * Determines the maximum number of consistent columns in a grid.
     * 
     * @param grid The grid of integers.
     * @param limit The limit for the difference between elements in a column.
     * @return The maximum number of consistent columns.
     */
    public int maxConsistentColumns(int[][] grid, int limit) {
        int rows = grid.length;
        int cols = grid[0].length;
        int[] dp = new int[cols];
        int maxResult = 1;
        
        for (int i = 0; i < cols; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                boolean isValidPair = true;
                for (int r = 0; r < rows; r++) {
                    if (Math.abs(grid[r][i] - grid[r][j]) > limit) {
                        isValidPair = false;
                        break;
                    }
                }
                if (isValidPair) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxResult = Math.max(maxResult, dp[i]);
        }
        
        return maxResult;
    }
}