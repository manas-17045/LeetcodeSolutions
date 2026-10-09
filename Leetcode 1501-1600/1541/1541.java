// Leetcode 1541: Minimum Insertions to Balance a Parentheses String
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
// Solved on 9th of October, 2026
class Solution {
    /**
     * Calculates the minimum number of insertions needed to balance a parentheses string.
     * A balanced string requires each left parenthesis to have exactly two corresponding 
     * consecutive right parentheses, and the left parenthesis must appear before them.
     *
     * @param s the input string containing only the characters '(' and ')'
     * @return the minimum number of insertions required to make the string balanced
     */
    public int minInsertions(String s) {
        int insertions = 0;
        int expectedRight = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                if (expectedRight % 2 != 0) {
                    insertions++;
                    expectedRight--;
                }
                expectedRight += 2;
            } else {
                expectedRight--;
                if (expectedRight < 0) {
                    insertions++;
                    expectedRight += 2;
                }
            }
        }
        
        return insertions + expectedRight;
    }
}