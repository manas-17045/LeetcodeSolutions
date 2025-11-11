// Leetcode 474: Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/
// Solved on 11th of November, 2025
class Solution {
    /**
     * Finds the maximum number of strings that can be formed from the given array `strs`
     * such that the total number of '0's in the chosen strings is at most `m`
     * and the total number of '1's is at most `n`.
     * @param strs An array of binary strings.
     * @param m The maximum allowed number of '0's.
     * @param n The maximum allowed number of '1's.
     * @return The maximum number of strings that can be formed.
     */
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (String s : strs) {
            int zeros = 0;
            int ones = 0;
            for (int k = 0; k < s.length(); k++) {
                if (s.charAt(k) == '0') {
                    zeros++;
                } else {
                    ones++;
                }
            }
            if (zeros > m || ones > n) {
                continue;
            }
            for (int i = m; i >= zeros; i--) {
                for (int j = n; j >= ones; j--) {
                    int cand = dp[i - zeros][j - ones] + 1;
                    if (cand > dp[i][j]) {
                        dp[i][j] = cand;
                    }
                }
            }
        }
        return dp[m][n];
    }
}