// Leetcode 921: Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
// Solved on 6th of October, 2026
class Solution {
    /**
     * Calculates the minimum number of parentheses that must be inserted
     * to make the input string valid.
     *
     * @param s the string containing only '(' and ')' characters
     * @return the minimum number of insertions required to make the string valid
     */
    public int minAddToMakeValid(String s) {
        int openCount = 0;
        int addedCount = 0;

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            if (currentChar == '(') {
                openCount++;
            } else {
                if (openCount > 0) {
                    openCount--;
                } else {
                    addedCount++;
                }
            }
        }

        return openCount + addedCount;
    }
}