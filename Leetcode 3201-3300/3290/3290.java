// Leetcode 3290: Maximum Multiplication Score
// https://leetcode.com/problems/maximum-multiplication-score/
// Solved on 2nd of January, 2026
class Solution {
    /**
     * Calculates the maximum multiplication score.
     *
     * @param a An array of integers representing coefficients.
     * @param b An array of integers representing values to multiply.
     * @return The maximum possible multiplication score.
     */
    public long maxScore(int[] a, int[] b) {
        long[] dp = {-1000000000000L, -1000000000000L, -1000000000000L, -1000000000000L};
        for (int val : b) {
            dp[3] = Math.max(dp[3], dp[2] + (long) a[3] * val);
            dp[2] = Math.max(dp[2], dp[1] + (long) a[2] * val);
            dp[1] = Math.max(dp[1], dp[0] + (long) a[1] * val);
            dp[0] = Math.max(dp[0], (long) a[0] * val);
        }
        return dp[3];
    }
}