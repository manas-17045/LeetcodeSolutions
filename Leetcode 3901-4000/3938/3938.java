// Leetcode 3938: Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/
// Solved on 7th of June, 2026
class Solution {
    /**
     * Calculates the maximum path intersection sum in a grid.
     * 
     * @param grid A 2D integer array representing the grid.
     * @return The maximum score calculated based on path intersections.
     */
    public int maxScore(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int ans = Integer.MIN_VALUE;

        for (int r = 0; r < m; r++) {
            int max1 = grid[r][0];
            for (int c = 1; c < n; c++) {
                int max2 = max1 + grid[r][c];
                if (max2 > ans) {
                    ans = max2;
                }
                max1 = Math.max(grid[r][c], max1 + grid[r][c]);
            }
        }

        for (int c = 0; c < n; c++) {
            int max1 = grid[0][c];
            for (int r = 1; r < m; r++) {
                int max2 = max1 + grid[r][c];
                if (max2 > ans) {
                    ans = max2;
                }
                max1 = Math.max(grid[r][c], max1 + grid[r][c]);
            }
        }

        for (int r = 1; r < m - 1; r++) {
            for (int c = 1; c < n - 1; c++) {
                if (grid[r][c] > ans) {
                    ans = grid[r][c];
                }
            }
        }

        return ans;
    }
}