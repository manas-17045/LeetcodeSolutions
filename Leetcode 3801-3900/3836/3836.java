// Leetcode 3836: Maximum Score Using Exactly K Pairs
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/
// Solved on 10th of February, 2026
class Solution {
    /**
     * Calculates the maximum score possible by selecting exactly k pairs of elements from two arrays.
     * @param nums1 The first integer array.
     * @param nums2 The second integer array.
     * @param k The exact number of pairs to be formed.
     * @return The maximum total score obtained from the products of the k pairs.
     */
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int m = nums2.length;
        
        long[][] dp = new long[n + 1][m + 1];
        
        long minLimit = -1_000_000_000_000_000L;

        for (int p = 1; p <= k; p++) {
            long[][] nextDp = new long[n + 1][m + 1];
            
            for (int i = 0; i <= n; i++) {
                for (int j = 0; j <= m; j++) {
                    nextDp[i][j] = minLimit;
                }
            }

            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= m; j++) {
                    long match = minLimit;
                    if (dp[i - 1][j - 1] > minLimit) {
                        match = dp[i - 1][j - 1] + (long) nums1[i - 1] * nums2[j - 1];
                    }
                    
                    long skip = Math.max(nextDp[i - 1][j], nextDp[i][j - 1]);
                    
                    nextDp[i][j] = Math.max(match, skip);
                }
            }
            dp = nextDp;
        }

        return dp[n][m];
    }
}