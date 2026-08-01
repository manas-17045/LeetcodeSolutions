// Leetcode 3981: Count Distinct Ways to Form Target from Two Strings
// https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/
// Solved on 1st of August, 2026
class Solution {
    /**
     * Determines the number of distinct ways to form the target string by interleaving
     * characters from word1 and word2.
     * 
     * @param word1 The first word.
     * @param word2 The second word.
     * @param target The target string to form.
     * @return The number of distinct ways to form the target string.
     */
    public int interleaveCharacters(String word1, String word2, String target) {
        int n = target.length();
        int l1 = word1.length();
        int l2 = word2.length();
        int mod = 1000000007;

        int[][][] dp = new int[l1 + 1][l2 + 1][4];
        int[][][] nextDp = new int[l1 + 1][l2 + 1][4];
        int[][] s1 = new int[l1 + 1][l2 + 1];

        for (int i = 0; i <= l1; i++) {
            for (int j = 0; j <= l2; j++) {
                dp[i][j][3] = 1;
            }
        }

        for (int k = n - 1; k >= 0; k--) {
            char tc = target.charAt(k);

            for (int mask = 0; mask < 4; mask++) {
                int nextMask1 = mask | 1;
                int nextMask2 = mask | 2;

                for (int j = 0; j <= l2; j++) {
                    int s = 0;
                    s1[l1][j] = 0;
                    for (int i = l1 - 1; i >= 0; i--) {
                        if (word1.charAt(i) == tc) {
                            s = (s + dp[i + 1][j][nextMask1]) % mod;
                        }
                        s1[i][j] = s;
                    }
                }

                for (int i = 0; i <= l1; i++) {
                    int s = 0;
                    nextDp[i][l2][mask] = s1[i][l2];
                    for (int j = l2 - 1; j >= 0; j--) {
                        if (word2.charAt(j) == tc) {
                            s = (s + dp[i][j + 1][nextMask2]) % mod;
                        }
                        nextDp[i][j][mask] = (s1[i][j] + s) % mod;
                    }
                }
            }

            int[][][] temp = dp;
            dp = nextDp;
            nextDp = temp;
        }

        return dp[0][0][0];
    }
}