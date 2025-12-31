// Leetcode 3503: Longest Palindrome After Substring Concatenation I
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/
// Solved on 31st of December, 2025
class Solution {
    /**
     * Finds the length of the longest palindrome that can be formed by concatenating a substring from `s` and a substring from `t`.
     * @param s The first input string.
     * @param t The second input string.
     * @return The length of the longest palindromic concatenation.
     */
    public int longestPalindrome(String s, String t) {
        int maxLen = 0;
        int sLen = s.length();
        int tLen = t.length();

        for (int i = 0; i < sLen; i++) {
            for (int j = i; j < sLen; j++) {
                if (isPalindrome(s, i, j)) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }

        for (int i = 0; i < tLen; i++) {
            for (int j = i; j < tLen; j++) {
                if (isPalindrome(t, i, j)) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }

        for (int i = 0; i < sLen; i++) {
            for (int j = i; j < sLen; j++) {
                for (int k = 0; k < tLen; k++) {
                    for (int l = k; l < tLen; l++) {
                        if (isCombinedPalindrome(s, i, j, t, k, l)) {
                            int currentLen = (j - i + 1) + (l - k + 1);
                            maxLen = Math.max(maxLen, currentLen);
                        }
                    }
                }
            }
        }

        return maxLen;
    }

    private boolean isPalindrome(String str, int start, int end) {
        while (start < end) {
            if (str.charAt(start) != str.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    private boolean isCombinedPalindrome(String s, int sStart, int sEnd, String t, int tStart, int tEnd) {
        int len1 = sEnd - sStart + 1;
        int len2 = tEnd - tStart + 1;
        int totalLen = len1 + len2;

        for (int p = 0; p < totalLen / 2; p++) {
            char leftChar = (p < len1) 
                ? s.charAt(sStart + p) 
                : t.charAt(tStart + (p - len1));
            
            int rightIndex = totalLen - 1 - p;
            char rightChar = (rightIndex < len1) 
                ? s.charAt(sStart + rightIndex) 
                : t.charAt(tStart + (rightIndex - len1));

            if (leftChar != rightChar) {
                return false;
            }
        }
        return true;
    }
}