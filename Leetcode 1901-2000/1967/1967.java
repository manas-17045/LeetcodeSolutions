// Leetcode 1967: Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
// Solved on 29th of June, 2026
class Solution {
    /**
     * Checks the number of strings in the given array of patterns that appear as substrings in the given word.
     * @param patterns The array of patterns to check.
     * @param word The word to check for substrings.
     * @return The number of patterns that appear as substrings in the word.
     */
    public int numOfStrings(String[] patterns, String word) {
        int matchCount = 0;
        for (String currentPattern : patterns) {
            if (word.contains(currentPattern)) {
                matchCount++;
            }
        }

        return matchCount;
    }
}