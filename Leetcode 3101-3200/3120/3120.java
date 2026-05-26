// Leetcode 3120: Count the Number of Special Characters I
// https://leetcode.com/problems/count-the-number-of-special-characters-i/
// Solved on 26th of May, 2026
class Solution {
    /**
     * Counts the number of special characters in a string.
     * A character is special if both its lowercase and uppercase forms appear in the string.
     * @param word The input string consisting of English letters.
     * @return The number of unique characters that appear in both cases.
     */
    public int numberOfSpecialChars(String word) {
        int lowerMask = 0;
        int upperMask = 0;
        int length = word.length();
        for (int i = 0; i < length; i++) {
            char ch = word.charAt(i);
            if (ch >= 'a' && ch <= 'z') {
                lowerMask |= (1 << (ch - 'a'));
            } else {
                upperMask |= (1 << (ch - 'A'));
            }
        }
        return Integer.bitCount(lowerMask & upperMask);
    }
}