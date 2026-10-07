// Leetcode 301: Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/
// Solved on 7th of October, 2026
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    /**
     * Removes the minimum number of invalid parentheses to make the input string valid
     * and returns all unique valid strings.
     *
     * @param s the input string containing parentheses and lowercase English letters
     * @return a list of unique valid strings formed with the minimum number of removals
     */
    public List<String> removeInvalidParentheses(String s) {
        int remLeft = 0;
        int remRight = 0;

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            if (currentChar == '(') {
                remLeft++;
            } else if (currentChar == ')') {
                if (remLeft > 0) {
                    remLeft--;
                } else {
                    remRight++;
                }
            }
        }

        Set<String> resultSet = new HashSet<>();
        backtrack(s, 0, remLeft, remRight, 0, new StringBuilder(), resultSet);
        return new ArrayList<>(resultSet);
    }

    private void backtrack(String s, int index, int remLeft, int remRight, int openCount, StringBuilder current, Set<String> resultSet) {
        int remainingLength = s.length() - index;

        if (remLeft < 0 || remRight < 0 || openCount < 0) {
            return;
        }

        if (remLeft + remRight > remainingLength) {
            return;
        }

        if (openCount > remainingLength - (remLeft + remRight)) {
            return;
        }

        if (index == s.length()) {
            if (remLeft == 0 && remRight == 0 && openCount == 0) {
                resultSet.add(current.toString());
            }
            return;
        }

        char currentChar = s.charAt(index);

        if (currentChar == '(') {
            if (remLeft > 0) {
                backtrack(s, index + 1, remLeft - 1, remRight, openCount, current, resultSet);
            }
            current.append('(');
            backtrack(s, index + 1, remLeft, remRight, openCount + 1, current, resultSet);
            current.deleteCharAt(current.length() - 1);
        } else if (currentChar == ')') {
            if (remRight > 0) {
                backtrack(s, index + 1, remLeft, remRight - 1, openCount, current, resultSet);
            }
            if (openCount > 0) {
                current.append(')');
                backtrack(s, index + 1, remLeft, remRight, openCount - 1, current, resultSet);
                current.deleteCharAt(current.length() - 1);
            }
        } else {
            current.append(currentChar);
            backtrack(s, index + 1, remLeft, remRight, openCount, current, resultSet);
            current.deleteCharAt(current.length() - 1);
        }
    }
}