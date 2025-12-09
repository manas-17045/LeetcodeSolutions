// Leetcode 3225: Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/
// Solved on 6th of November, 2025
class Solution {
    public long maximumScore(int[][] grid) {
    /**
     * Calculates the maximum score from grid operations.
     *
     * @param grid The input grid of integers.
     * @return The maximum score achievable.
     */
        int n = grid.length;
        long[][] prefix = new long[n][n + 1];
        for (int j = 0; j < n; ++j) {
            for (int i = 0; i < n; ++i) {
                prefix[j][i + 1] = prefix[j][i] + grid[i][j];
            }
        }
        long[] prevPick = new long[n + 1];
        long[] prevSkip = new long[n + 1];
        for (int j = 1; j < n; ++j) {
            long[] currPick = new long[n + 1];
            long[] currSkip = new long[n + 1];
            for (int curr = 0; curr <= n; ++curr) {
                for (int prev = 0; prev <= n; ++prev) {
                    if (curr > prev) {
                        long score = prefix[j - 1][curr] - prefix[j - 1][prev];
                        long val1 = prevSkip[prev] + score;
                        if (val1 > currPick[curr]) {
                            currPick[curr] = val1;
                        }
                        if (val1 > currSkip[curr]) {
                            currSkip[curr] = val1;
                        }
                    } else {
                        long score = prefix[j][prev] - prefix[j][curr];
                        long val2 = prevPick[prev] + score;
                        if (val2 > currPick[curr]) {
                            currPick[curr] = val2;
                        }
                        if (prevPick[prev] > currSkip[curr]) {
                            currSkip[curr] = prevPick[prev];
                        }
                    }
                }
            }
            prevPick = currPick;
            prevSkip = currSkip;
        }
        long ans = 0;
        for (long v : prevPick) {
            if (v > ans) {
                ans = v;
            }
        }
        return ans;
    }
}