// Leetcode 20: Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Solved on 1st of October, 2026
class Solution {
    /**
     * Determines whether the given string of brackets is valid.
     * An input string is valid if open brackets are closed by the same type of
     * brackets in the correct order, and every close bracket has a corresponding
     * opening bracket.
     *
     * @param s the string containing bracket characters
     * @return true if the string is valid, false otherwise
     */
    public boolean isValid(Strig s) {
        if (s == null || (s.length() & 1) != 0) {
            return false;
        }

        char[] stack = new char[s.length()];
        int head = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack[head++] = ')';
            } else if (c == '{') {
                stack[head++] = '}';
            } else if (c == '[') {
                stack[head++] = ']';
            } else if (head == 0 || stack[--head] != c) {
                return false;
            }
        }

        return head == 0;
    }
}