// Leetcode 856: Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/
// Solved on 5th of October, 2026
class Solution {
    /**
     * Calculates the total score of a balanced parentheses string based on defined evaluation rules.
     *
     * @param s the balanced parentheses string to be evaluated
     * @return the computed integer score of the string
     */
    public int scoreOfParentheses(String s) {
        int score = 0;
        int depth = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                depth++;
            } else {
                depth--;
                if (s.charAt(i - 1) == '(') {
                    score += 1 << depth;
                }
            }
        }

        return score;
    }
}