// Leetcode 3316: Find Maximum Removals From Sources STring
// https://leetcode.com/problems/find-maximum-removals-from-source-string/
// Solved on 7th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds the maximum number of characters that can be removed from the `sources` string
     * (at indices specified by `targetIndices`) such that `pattern` remains a subsequence of `sources`.
     *
     * @param sources The source string.
     * @param pattern The pattern string to be found as a subsequence.
     * @param targetIndices An array of indices in `sources` that can be removed.
     * @return The maximum number of removable characters that can be removed.
     */
    public int maxRemovals(String sources, String pattern, int[] targetIndices) {
        int n = source.length();
        int m = pattern.length();
        
        char[] s = source.toCharArray();
        char[] p = pattern.toCharArray();
        
        boolean[] isTarget = new boolean[n];
        for (int idx : targetIndices) {
            isTarget[idx] = true;
        }
        
        int[][] dp = new int[n + 1][m + 1];
        
        for (int[] row : dp) {
            Arrays.fill(row, Integer.MIN_VALUE / 2);
        }
        
        dp[n][m] = 0;
        for (int i = n - 1; i >= 0; i--) {
            dp[i][m] = dp[i + 1][m] + (isTarget[i] ? 1 : 0);
        }
        
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                int skipGain = (isTarget[i] ? 1 : 0);
                dp[i][j] = skipGain + dp[i + 1][j];
                
                if (s[i] == p[j]) {
                    dp[i][j] = Math.max(dp[i][j], dp[i + 1][j + 1]);
                }
            }
        }
        
        return dp[0][0];
    }
}