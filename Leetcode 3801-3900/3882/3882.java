// Leetcode 3882: Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/
// Solved on 5th of April, 2026
class Solution {
    /**
     * Calculates the minimum XOR sum path from the top-left to the bottom-right of a grid.
     *
     * @param grid A 2D integer array representing the costs at each cell.
     * @return The minimum possible XOR sum of all values along a path from (0,0) to (m-1, n-1).
     */
    public int minCost(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] dp = new boolean[n][1024];
        
        dp[0][grid[0][0]] = true;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }
                
                boolean[] next = new boolean[1024];
                int val = grid[i][j];
                
                if (i > 0) {
                    for (int k = 0; k < 1024; k++) {
                        if (dp[j][k]) {
                            next[k ^ val] = true;
                        }
                    }
                }
                
                if (j > 0) {
                    for (int k = 0; k < 1024; k++) {
                        if (dp[j - 1][k]) {
                            next[k ^ val] = true;
                        }
                    }
                }
                
                dp[j] = next;
            }
        }
        
        for (int k = 0; k < 1024; k++) {
            if (dp[n - 1][k]) {
                return k;
            }
        }
        
        return 0;
    }
}