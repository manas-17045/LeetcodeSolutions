// Leetcode 3130: Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/
// Solved on 10th of March, 2026
class Solution {
    /**
     * Calculates the number of stable binary arrays containing a specific number of zeros and ones.
     * A binary array is stable if no more than 'limit' consecutive 0s or 1s appear.
     *
     * @param zero  The total number of zeros required in the array.
     * @param one   The total number of ones required in the array.
     * @param limit The maximum allowed number of consecutive identical elements.
     * @return The total number of stable binary arrays modulo 10^9 + 7.
     */
    public int numberOfStableArrays(int zero, int one, int limit) {
        int mod = 1000000007;
        int[][][] dp = new int[zero + 1][one + 1][limit + 1];

        for (int i = 1; i <= Math.min(zero, limit); i++) {
            dp[i][0][0] = 1;
        }
        for (int j = 1; j <= Math.min(one, limit); j++) {
            dp[0][j][1] = 1;
        }
        
        for (int i = 1; i <= zero; i++) {
            for (int j = 1; j <= one; j++) {
                long valZero = (long) dp[i - 1][j][0] + dp[i - 1][j][1];
                if (i > limit) {
                    valZero -= dp[i - limit - 1][j][1];
                } else if (i == limit + 1) {
                    valZero -= 1;
                }
                dp[i][j][0] = (int) ((valZero % mod + mod) % mod);
                
                long valOne = (long) dp[i][j - 1][0] + dp[i][j - 1][1];
                if (j > limit) {
                    valOne -= dp[i][j - limit - 1][0];
                } else if (j == limit + 1) {
                    valOne -= 1;
                }
                dp[i][j][1] = (int) ((valOne % mod + mod) % mod);
            }
        }

        return (dp[zero][one][0] + dp[zero][one][1]) % mod;
    }
}