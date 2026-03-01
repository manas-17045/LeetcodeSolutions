// Leetcode 3856: Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/
// Solved on 1st of March, 2026
class Solution {
    /**
     * Removes all trailing vowel characters ('a', 'e', 'i', 'o', 'u') from the end of the string.
     *
     * @param s The input string to be trimmed.
     * @return A substring of s with all trailing vowels removed.
     */
    public String trimTrailingVowels(String s) {
        int lastIndex = s.length() - 1;
        while (lastIndex >= 0) {
            char currentChar = s.charAt(lastIndex);
            if (currentChar == 'a' || currentChar == 'e' || currentChar == 'i' || currentChar == 'o' || currentChar == 'u') {
                lastIndex--;
            } else {
                break;
            }
        }
        return s.substring(0, lastIndex + 1);
    }
}