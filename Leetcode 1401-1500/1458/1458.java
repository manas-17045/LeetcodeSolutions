// Leetcode 1458: Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/
// Solved on 28th of November, 2025
class Solution {
    /**
     * Calculates the maximum dot product of two non-empty subsequences from nums1 and nums2.
     *
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @return The maximum dot product.
     */
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int[] dp = new int[m];
        for (int j = 0; j < m; j++) {
            dp[j] = Integer.MIN_VALUE;
        }
        for (int i = 0; i < n; i++) {
            int prevDiagonal = 0;
            for (int j = 0; j < m; j++) {
                int currentVal = nums1[i] * nums2[j];
                int temp = dp[j];
                if (j > 0) {
                    currentVal += Math.max(0, prevDiagonal);
                }
                currentVal = Math.max(currentVal, temp);
                if (j > 0) {
                    currentVal = Math.max(currentVal, dp[j - 1]);
                }
                dp[j] = currentVal;
                prevDiagonal = temp;
            }
        }
        return dp[m - 1];
    }
}