// Leetcode 22: Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/
// Solved on 2nd of October, 2026
import java.util.ArrayList;
import java,util.List;

class Solution {
    /**
     * Generates all combinations of well-formed parentheses for a given number of pairs.
     *
     * @param n the number of pairs of parentheses
     * @return a list containing all combinations of well-formed parentheses
     */
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        char[] currentString = new char[2 * n];
        backtrack(result, currentString, 0, 0, 0, n);
        return result;
    }

    private void backtrack(List<String> result, char[] currentString, int index, int openCount, int closeCount, int maxPairs) {
        if (index == 2 * maxPairs) {
            result.add(new String(currentString));
            return;
        }

        if (openCount < maxPairs) {
            currentString[index] = '(';
            backtrack(result, currentString, index + 1, openCount + 1, closeCount, maxPairs);
        }

        if (closeCount < openCount) {
            currentString[index] = ')';
            backtrack(result, currentString, index + 1, openCount, closeCount + 1, maxPairs);
        }
    }
}