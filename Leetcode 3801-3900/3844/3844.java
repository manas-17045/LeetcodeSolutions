// Leetcode 3844: Longest Almost-Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/
// Solved on 18th of February, 2026
class Solution {
    /**
     * Finds the length of the longest almost-palindromic substring.
     * An almost-palindromic substring is a substring that can become a palindrome by changing at most one character.
     * @param s The input string to analyze.
     * @return The length of the longest almost-palindromic substring found.
     */
    public int almostPalindromic(String s) {
        int n = s.length();
        char[] str = s.toCharArray();
        int maxLen = 0;

        for (int i = 0; i < n; i++) {
            maxLen = Math.max(maxLen, solve(i - 1, i + 1, str, n));
            maxLen = Math.max(maxLen, solve(i, i + 1, str, n));
        }

        return maxLen;
    }

    private int solve(int left, int right, char[] str, int n) {
        while (left >= 0 && right < n && str[left] == str[right]) {
            left--;
            right++;
        }

        int baseLen = right - left - 1;

        if (left < 0 && right >= n) {
            return baseLen;
        }

        if (left < 0 || right >= n) {
            return baseLen + 1;
        }

        int len1 = baseLen + 1 + expandStrict(left - 1, right, str, n);
        int len2 = baseLen + 1 + expandStrict(left, right + 1, str, n);

        return Math.max(len1, len2);
    }

    private int expandStrict(int left, int right, char[] str, int n) {
        int count = 0;
        while (left >= 0 && right < n && str[left] == str[right]) {
            count += 2;
            left--;
            right++;
        }
        return count;
    }
}