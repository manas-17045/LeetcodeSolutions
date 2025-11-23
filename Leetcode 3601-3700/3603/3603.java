// Leetcode 3603: Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/
// Solved on 23rd of November, 2025
class Solution {
    /**
     * Calculates the minimum cost to reach the bottom-right cell (m-1, n-1) from the top-left cell (0, 0)
     * in a grid, considering alternating directions and waiting costs.
     * @param m The number of rows in the grid.
     * @param n The number of columns in the grid.
     * @param waitCost A 2D array where waitCost[i][j] is the cost to wait at cell (i, j).
     * @return The minimum cost to reach the bottom-right cell.
     */
    public long minCost(int m, int n, int[][] waitCost) {
        long[] dp = new long[n];
        dp[0] = 1;

        for (int j = 1; j < n; j++) {
            long prevWait = (j == 1) ? 0 : waitCost[0][j - 1];
            dp[j] = dp[j - 1] + prevWait + (long) (j + 1);
        }

        for (int i = 1; i < m; i++) {
            long colWait = (i == 1) ? 0 : waitCost[i - 1][0];
            dp[0] += colWait + (long) (i + 1);

            for (int j = 1; j < n; j++) {
                long topWait = waitCost[i - 1][j];
                long leftWait = waitCost[i][j - 1];

                long fromTop = dp[j] + topWait;
                long fromLeft = dp[j - 1] + leftWait;

                dp[j] = Math.min(fromTop, fromLeft) + (long) (i + 1) * (j + 1);
            }
        }

        return dp[n - 1];
    }
}