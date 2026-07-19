// Leetcode 1081: Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters
// Solved on 19th of July, 2026
class Solution {
    /**
     * Finds the smallest subsequence of distinct characters.
     * 
     * @param s The input string.
     * @return The smallest subsequence of distinct characters.
     */
    public String smallestSubsequence(String s) {
        int[] charCounts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            charCounts[s.charAt(i) - 'a']++;
        }
        boolean[] inStack = new boolean[26];
        char[] elementStack = new char[26];
        int stackTop = 0;
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            int charIndex = currentChar - 'a';
            charCounts[charIndex]--;
            if (inStack[charIndex]) {
                continue;
            }
            while (stackTop > 0 && elementStack[stackTop - 1] > currentChar && charCounts[elementStack[stackTop - 1] - 'a'] > 0) {
                inStack[elementStack[stackTop - 1] - 'a'] = false;
                stackTop--;
            }
            elementStack[stackTop] = currentChar;
            stackTop++;
            inStack[charIndex] = true;
        }
        return new String(elementStack, 0, stackTop);
    }
}