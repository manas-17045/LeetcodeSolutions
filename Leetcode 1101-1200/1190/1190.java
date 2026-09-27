// Leetcode 1190: Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
// Solved on 27th of September, 2026
class Solution {
    /**
     * Reverses substrings within each pair of matching parentheses from the inside out
     * and returns the resulting string without any brackets.
     *
     * @param s the input string containing lowercase English letters and balanced parentheses
     * @return the transformed string with all parenthesized substrings reversed and brackets removed
     */
    public String reverseParentheses(String s) {
        int length = s.length();
        int[] pairIndices = new int[length];
        int[] bracketStack = new int[length];
        int stackPointer = 0;

        for (int index = 0; index < length; index++) {
            char currentChar = s.charAt(index);
            if (currentChar == '(') {
                bracketStack[stackPointer++] = index;
            } else if (currentChar == ')') {
                int openIndex = bracketStack[--stackPointer];
                pairIndices[openIndex] = index;
                pairIndices[index] = openIndex;
            }
        }

        StringBuilder result = new StringBuilder(length);
        int currentIndex = 0;
        int direction = 1;

        while (currentIndex >= 0 && currentIndex < length) {
            char currentChar = s.charAt(currentIndex);
            if (currentChar == '(' || currentChar == ')') {
                currentIndex = pairIndices[currentIndex];
                direction = -direction;
            } else {
                result.append(currentChar);
            }
            currentIndex += direction;
        }

        return result.toString();
    }
}