// Leetcode 3884: First matching Character From Both End
// https://leetcode.com/problems/first-matching-character-from-both-ends/
// Solved on 5th of April, 2026
class Solution {
    /**
     * Finds the first index where the character at that index matches the character 
     * at the corresponding position from the end of the string.
     * @param s The input string to search.
     * @return The first index where a match is found, or -1 if no match exists.
     */
    public int firstMatchingIndex(String s) {
        int length = s.length();
        for (int index = 0; index < length; index++) {
            if (s.charAt(index) == s.charAt(length - index - 1)) {
                return index;
            }
        }
        return -1;
    }
}