// Leetcode 3129: Find All Possible Stable Binary Arrays I
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/
// Solved on 3rd of January, 2026
class Solution {
    /**
     * Calculates the number of stable binary arrays that can be formed with a given number of zeros and ones,
     * such that no more than `limit` consecutive identical characters appear.
     * @param zero The number of zeros available.
     * @param one The number of ones available.
     * @param limit The maximum number of consecutive identical characters allowed.
     * @return The total number of stable binary arrays, modulo 10^9 + 7.
     */
    public int numberOfStableArrays(int zero, int one, int limit) {
        int mod = 1_000_000_007;
        int[][][] dp = new int[zero + 1][one + 1][2];

        for (int i = 1; i <= Math.min(zero, limit); i++) {
            dp[i][0][0] = 1;
        }
        for (int j = 1; j <= Math.min(one, limit); j++) {
            dp[0][j][1] = 1;
        }

        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % mod;
                if (i > limit) {
                    dp[i][j][0] = (dp[i][j][0] - dp[i - limit - 1][j][1] + mod) % mod;
                }

                dp[i][j][1] = (dp[i][j - 1][1] + dp[i][j - 1][0]) % mod;
                if (j > limit) {
                    dp[i][j][1] = (dp[i][j][1] - dp[i][j - limit - 1][0] + mod) % mod;
                }
            }
        }

        return (dp[zero][one][0] + dp[zero][one][1]) % mod;
    }
}