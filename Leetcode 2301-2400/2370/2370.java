// Leetcode 2370: Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/
// Solved on 7th of December, 2025
class Solution {
    /**
     * Finds the length of the longest ideal subsequence.
     * An ideal subsequence is one where the absolute difference between the character values of adjacent characters is at most k.
     *
     * @param s The input string.
     * @param k The maximum allowed difference between adjacent characters in the subsequence.
     * @return The length of the longest ideal subsequence.
     */
    public int longestIdealString(String s, int k) {
        int[] dp = new int[26];
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            int curr = s.charAt(i) - 'a';
            int best = 0;
            
            int lower = Math.max(0, curr - k);
            int upper = Math.min(25, curr + k);

            for (int j = lower; j <= upper; j++) {
                best = Math.max(best, dp[j]);
            }

            dp[curr] = best + 1;
            maxLen = Math.max(maxLen, dp[curr]);
        }

        return maxLen;
    }
}