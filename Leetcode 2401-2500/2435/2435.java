// Leetcode 2435: Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
// Solved on 26th of November, 2025
class Solution {
    /**
     * Calculates the number of paths from the top-left corner to the bottom-right corner of a grid
     * such that the sum of the values along the path is divisible by k.
     * @param grid The input grid of integers.
     * @param k The divisor.
     * @return The number of paths whose sum is divisible by k, modulo 10^9 + 7.
     */
    public int numberOfPaths(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int mod = 1000000007;
        int[][] dp = new int[n][k];

        dp[0][grid[0][0] % k] = 1;

        for (int j = 1; j < n; j++) {
            int val = grid[0][j] % k;
            for (int r = 0; r < k; r++) {
                dp[j][r] = dp[j - 1][(r - val + k) % k];
            }
        }

        for (int i = 1; i < m; i++) {
            int[] firstCol = new int[k];
            int val = grid[i][0] % k;
            for (int r = 0; r < k; r++) {
                firstCol[r] = dp[0][(r - val + k) % k];
            }
            dp[0] = firstCol;

            for (int j = 1; j < n; j++) {
                int[] cell = new int[k];
                val = grid[i][j] % k;
                for (int r = 0; r < k; r++) {
                    int prev = (r - val + k) % k;
                    cell[r] = (dp[j][prev] + dp[j - 1][prev]) % mod;
                }
                dp[j] = cell;
            }
        }

        return dp[n - 1][0];
    }
}