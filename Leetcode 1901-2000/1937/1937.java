// Leetcode 1937: Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/
// Solved on 30th of November, 2025
class Solution {
    /**
     * Calculates the maximum number of points that can be obtained by selecting one cell from each row,
     * with a cost penalty for selecting cells that are far apart in adjacent rows.
     * @param points A 2D array where `points[r][c]` is the number of points at cell (r, c).
     * @return The maximum number of points achievable.
     */
    public long maxPoints(int[][] points) {
        int rows = points.length;
        int cols = points[0].length;
        long[] dp = new long[cols];

        for (int c = 0; c < cols; c++) {
            dp[c] = points[0][c];
        }

        for (int r = 1; r < rows; r++) {
            long[] nextDp = new long[cols];
            long leftMax = Long.MIN_VALUE;

            for (int c = 0; c < cols; c++) {
                if (c == 0) {
                    leftMax = dp[c];
                } else {
                    leftMax = Math.max(leftMax - 1, dp[c]);
                }
                nextDp[c] = leftMax;
            }

            long rightMax = Long.MIN_VALUE;
            for (int c = cols - 1; c >= 0; c--) {
                if (c == cols - 1) {
                    rightMax = dp[c];
                } else {
                    rightMax = Math.max(rightMax - 1, dp[c]);
                }
                nextDp[c] = Math.max(nextDp[c], rightMax) + points[r][c];
            }

            dp = nextDp;
        }

        long maxPoints = 0;
        for (long val : dp) {
            maxPoints = Math.max(maxPoints, val);
        }
        return maxPoints;
    }
}