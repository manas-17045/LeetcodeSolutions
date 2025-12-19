// Leetcode 3579: Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/
// Solved on 19th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to convert word1 into word2.
     * An operation can be either a direct conversion of a substring or a reversed conversion of a substring.
     *
     * @param word1 The source string.
     * @param word2 The target string.
     * @return The minimum number of operations.
     */
    public int minOperations(String word1, String word2) {
        int n = word1.length();
        int[] dp = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        dp[0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int cost = calculateCost(word1, word2, j, i);
                if (dp[j] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[j] + cost);
                }
            }
        }
        return dp[n];
    }

    private int calculateCost(String s1, String s2, int start, int end) {
        int mismatchesDirect = 0;
        int[][] countsDirect = new int[26][26];

        for (int k = start; k < end; k++) {
            char c1 = s1.charAt(k);
            char c2 = s2.charAt(k);
            if (c1 != c2) {
                mismatchesDirect++;
                countsDirect[c1 - 'a'][c2 - 'a']++;
            }
        }

        int swapsDirect = 0;
        for (int r = 0; r < 26; r++) {
            for (int c = r + 1; c < 26; c++) {
                swapsDirect += Math.min(countsDirect[r][c], countsDirect[c][r]);
            }
        }
        int costDirect = mismatchesDirect - swapsDirect;

        int mismatchesRev = 0;
        int[][] countsRev = new int[26][26];

        for (int k = start; k < end; k++) {
            char c1 = s1.charAt(k);
            char c2 = s2.charAt(end - 1 - (k - start));
            if (c1 != c2) {
                mismatchesRev++;
                countsRev[c1 - 'a'][c2 - 'a']++;
            }
        }

        int swapsRev = 0;
        for (int r = 0; r < 26; r++) {
            for (int c = r + 1; c < 26; c++) {
                swapsRev += Math.min(countsRev[r][c], countsRev[c][r]);
            }
        }
        int costRev = 1 + mismatchesRev - swapsRev;

        return Math.min(costDirect, costRev);
    }
}