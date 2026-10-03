// Leetcode 32: Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/
// Solved on 3rd of October, 2026
class Solution {
    /**
     * Calculates the length of the longest valid parentheses substring.
     *
     * @param s the input string containing '(' and ')' characters
     * @return the length of the longest valid parentheses substring
     */
    public int longestValidParentheses(String s) {
        int maxLength = 0;
        int openCount = 0;
        int closeCount = 0;
        int length = s.length();

        for (int i = 0; i < length; i++) {
            if (s.charAt(i) == '(') {
                openCount++;
            } else {
                closeCount++;
            }

            if (openCount == closeCount) {
                maxLength = Math.max(maxLength, 2 * closeCount);
            } else if (closeCount > openCount) {
                openCount = 0;
                closeCount = 0;
            }
        }

        openCount = 0;
        closeCount = 0;

        for (int i = length - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') {
                openCount++;
            } else {
                closeCount++;
            }

            if (openCount == closeCount) {
                maxLength = Math.max(maxLength, 2 * openCount);
            } else if (openCount > closeCount) {
                openCount = 0;
                closeCount = 0;
            }
        }

        return maxLength;
    }
}