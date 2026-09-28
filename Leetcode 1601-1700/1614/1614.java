// Leetcode 1614: Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
// Solved on 28th of September, 2026
class Solution {
    /**
     * Calculates the maximum nesting depth of parentheses in a valid parentheses string.
     *
     * @param s the valid parentheses string to evaluate
     * @return the maximum nesting depth
     */
    public int maxDepth(String s) {
        int currentDepth = 0;
        int maxDepth = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(') {
                currentDepth++;
                if (currentDepth > maxDepth) {
                    maxDepth = currentDepth;
                }
            } else if (ch == ')') {
                currentDepth--;
            }
        }

        return maxDepth;
    }
}