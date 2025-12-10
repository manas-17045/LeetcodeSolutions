// Leetcode 1531: String Compression II
// https://leetcode.com/problems/string-compression-ii/
// Solved on 10th of December, 2025
class Solution {
    /**
     * Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has the minimum possible length.
     * Find the minimum possible length.
     * @param s The input string.
     * @param k The maximum number of characters that can be deleted.
     * @return The minimum possible length of the run-length encoded string.
     */
    public int getLengthOfOptimalCompression(String s, int k) {
        int n = s.length();
        int[][] dp = new int[n + 1][k + 1];

        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i][j] = 9999;
            }
        }
        
        dp[0][0] = 0;

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                if (j > 0) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                
                int removed = 0;
                int count = 0;
                
                for (int p = i; p > 0; p--) {
                    if (s.charAt(p - 1) == s.charAt(i - 1)) {
                        count++;
                    } else {
                        removed++;
                        if (j - removed < 0) {
                            break;
                        }
                    }
                    
                    int length = 0;
                    if (count >= 100) {
                        length = 3;
                    } else if (count >= 10) {
                        length = 2;
                    } else if (count >= 2) {
                        length = 1;
                    } else {
                        length = 0;
                    }
                    
                    if (j - removed >= 0) {
                        dp[i][j] = Math.min(dp[i][j], dp[p - 1][j - removed] + 1 + length);
                    }
                }
            }
        }
        
        return dp[n][k];
    }
}