// Leetcode 3504: Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/
// Solved on 9th of December, 2025
class Solution {
    /**
     * Given two strings s and t, return the length of the longest palindrome that can be formed by concatenating a substring of s and a substring of t.
     * @param s The first string.
     * @param t The second string.
     * @return The length of the longest palindrome.
     */
    public int longestPalindrome(String s, String t) {
        int n = s.length();
        int m = t.length();
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        int[] maxPalPrefixS = new int[n + 1];
        for (int i = 0; i < 2 * n - 1; i++) {
            int l = i / 2;
            int r = l + i % 2;
            while (l >= 0 && r < n && sArr[l] == sArr[r]) {
                maxPalPrefixS[l] = Math.max(maxPalPrefixS[l], r - l + 1);
                l--;
                r++;
            }
        }

        int[] maxPalSuffixT = new int[m + 1];
        for (int i = 0; i < 2 * m - 1; i++) {
            int l = i / 2;
            int r = l + i % 2;
            while (l >= 0 && r < m && tArr[l] == tArr[r]) {
                maxPalSuffixT[r + 1] = Math.max(maxPalSuffixT[r + 1], r - l + 1);
                l--;
                r++;
            }
        }

        int ans = 0;
        for (int len : maxPalPrefixS) {
            ans = Math.max(ans, len);
        }
        for (int len : maxPalSuffixT) {
            ans = Math.max(ans, len);
        }

        char[] tRev = new char[m];
        for (int i = 0; i < m; i++) {
            tRev[i] = tArr[m - 1 - i];
        }

        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (sArr[i - 1] == tRev[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    int matchLen = dp[i][j];

                    ans = Math.max(ans, maxPalPrefixS[i] + 2 * matchLen);

                    int tMatchStart = m - j;
                    ans = Math.max(ans, maxPalSuffixT[tMatchStart] + 2 * matchLen);
                }
            }
        }

        return ans;
    }
}