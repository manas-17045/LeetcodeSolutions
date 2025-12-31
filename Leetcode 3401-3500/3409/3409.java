// Leetcode 3409: Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/
// Solved on 31st of December, 2025
class Solution {
    /**
     * Finds the length of the longest subsequence where the absolute difference between adjacent elements is decreasing.
     * @param nums The input array of integers.
     * @return The length of the longest such subsequence.
     */
    public int longestSubsequence(int[] nums) {
        int[][] dp = new int[302][302];
        int maxLen = 0;

        for (int num : nums) {
            for (int prev = 1; prev <= 300; prev++) {
                int diff = Math.abs(num - prev);
                dp[num][diff] = Math.max(dp[num][diff], dp[prev][diff] + 1);
            }

            for (int d = 299; d >= 0; d--) {
                dp[num][d] = Math.max(dp[num][d], dp[num][d + 1]);
            }

            maxLen = Math.max(maxLen, dp[num][0]);
        }
        
        return maxLen;
    }
}