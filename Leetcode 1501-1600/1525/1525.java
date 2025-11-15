// Leetcode 1525: Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
// Solved on 15th of November, 2025
class Solution {
    /**
     * Counts the number of "good" ways to split a string.
     * A split is considered "good" if the number of distinct characters in the left substring is equal to the number of distinct characters in the right substring.
     * @param s The input string.
     * @return The number of good ways to split the string.
     */
    public int numSplits(String s) {
        int n = s.length();
        if (n < 2) {
            return 0;
        }
        int[] suffixCounts = new int[26];
        for (int i = 0; i < n; i++) {
            suffixCounts[s.charAt(i) - 'a']++;
        }
        int suffixUnique = 0;
        for (int v : suffixCounts) {
            if (v > 0) {
                suffixUnique++;
            }
        }
        int[] prefixCounts = new int[26];
        int prefixUnique = 0;
        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            int idx = s.charAt(i) - 'a';
            if (prefixCounts[idx] == 0) {
                prefixUnique++;
            }
            prefixCounts[idx]++;
            suffixCounts[idx]--;
            if (suffixCounts[idx] == 0) {
                suffixUnique--;
            }
            if (prefixUnique == suffixUnique) {
                ans++;
            }
        }
        return ans;
    }
}