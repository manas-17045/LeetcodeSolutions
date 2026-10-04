// Leetcode 678: Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/
// Solved on 4th of Octiber, 2026
class Solution {
    /**
     * Determines whether the given string containing '(', ')', and '*' characters
     * forms a valid parentheses sequence.
     *
     * @param s the string to validate
     * @return true if the string is valid, false otherwise
     */
    public boolean checkValidString(String s) {
        int minOpen = 0;
        int maxOpen = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch == '(') {
                minOpen++;
                maxOpen++;
            } else if (ch == ')') {
                minOpen--;
                maxOpen--;
            } else {
                minOpen--;
                maxOpen++;
            }

            if (maxOpen < 0) {
                return false;
            }

            if (minOpen < 0) {
                minOpen = 0;
            }
        }

        return minOpen == 0;
    }
}