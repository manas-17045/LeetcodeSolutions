// Leetcode 4030: Check ASCII Palindromic
// https://leetcode.com/problems/check-ascii-palindromic/
// Solved on 22nd of September, 2026
class Solution {
    /**
     * Determines whether the concatenated 8-bit binary representations
     * of each character in the given string form a palindrome.
     *
     * @param s the input string consisting of lowercase English letters
     * @return true if the resulting binary sequence is palindromic, false otherwise
     */
    public boolean isPalindromic(String s) {
        int totalBits = s.length() * 8;
        int leftIndex = 0;
        int rightIndex = totalBits - 1;

        while (leftIndex < rightIndex) {
            int leftBit = (s.charAt(leftIndex / 8) >> (7 - (leftIndex % 8))) & 1;
            int rightBit = (s.charAt(rightIndex / 8) >> (7 - (rightIndex % 8))) & 1;

            if (leftBit != rightBit) {
                return false;
            }

            leftIndex++;
            rightIndex--;
        }

        return true;
    }
}