// Leetcode 1021: Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/
// Solved on 8th of October, 2026
class Solution {
    /**
     * Removes the outermost parentheses of every primitive string in the
     * primitive decomposition of a valid parentheses string.
     *
     * @param s the valid parentheses string to process
     * @return the string with the outermost parentheses removed from each primitive component
     */
    public String removeOuterParentheses(String s) {
        StringBuilder result = new StringBuilder();
        int openCount = 0;

        for (char currentChar : s.toCharArray()) {
            if (currentChar == '(') {
                if (openCount > 0) {
                    result.append(currentChar);
                }
                openCount++;
            } else {
                openCount--;
                if (openCount > 0) {
                    result.append(currentChar);
                }
            }
        }

        return result.toString();
    }
}