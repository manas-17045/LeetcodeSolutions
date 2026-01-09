// Leetcode 3797: Count Routes to Climb a Rectangular Grid
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/
// Solved on 9th of January, 2026
class Solution {
    /**
     * Counts the number of routes to climb a rectangular grid.
     * @param grid A 2D array of characters representing the grid, where '.' denotes an open cell and other characters denote obstacles.
     * @param d The maximum allowed Manhattan distance for horizontal moves.
     * @return The total number of valid routes from the bottom row to any cell in the top row.
     */
    public int numberOfRoutes(String[] grid, int d) {
        int mod = 1000000007;
        int rows = grid.length;
        int cols = grid[0].length();
        long[] v = new long[cols];
        long[] t = new long[cols];
        long[] p = new long[cols + 1];

        int vertMax = -1;
        long dSquared = (long) d * d;
        if (d >= 1) {
            vertMax = (int) Math.sqrt(dSquared - 1);
        }

        for (int c = 0; c < cols; c++) {
            if (grid[rows - 1].charAt(c) == '.') {
                v[c] = 1;
            }
        }

        p[0] = 0;
        for (int i = 0; i < cols; i++) {
            p[i + 1] = (p[i] + v[i]) % mod;
        }

        for (int c = 0; c < cols; c++) {
            if (grid[rows - 1].charAt(c) == '.') {
                int l = Math.max(0, c - d);
                int r = Math.min(cols - 1, c + d);
                long rangeSum = (p[r + 1] - p[l] + mod) % mod;
                long h = (rangeSum - v[c] + mod) % mod;
                t[c] = (v[c] + h) % mod;
            }
        }

        for (int r = rows - 2; r >= 0; r--) {
            p[0] = 0;
            for (int i = 0; i < cols; i++) {
                p[i + 1] = (p[i] + t[i]) % mod;
            }

            for (int c = 0; c < cols; c++) {
                v[c] = 0;
                if (grid[r].charAt(c) == '.' && vertMax >= 0) {
                    int l = Math.max(0, c - vertMax);
                    int right = Math.min(cols - 1, c + vertMax);
                    v[c] = (p[right + 1] - p[l] + mod) % mod;
                }
            }

            p[0] = 0;
            for (int i = 0; i < cols; i++) {
                p[i + 1] = (p[i] + v[i]) % mod;
            }

            for (int c = 0; c < cols; c++) {
                t[c] = 0;
                if (grid[r].charAt(c) == '.') {
                    int l = Math.max(0, c - d);
                    int right = Math.min(cols - 1, c + d);
                    long rangeSum = (p[right + 1] - p[l] + mod) % mod;
                    long h = (rangeSum - v[c] + mod) % mod;
                    t[c] = (v[c] + h) % mod;
                }
            }
        }

        long ans = 0;
        for (long val : t) {
            ans = (ans + val) % mod;
        }
        return (int) ans;
    }
}