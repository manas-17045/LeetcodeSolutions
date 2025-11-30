// Leetcode 2559: Count Vowel Strings in Ranges
// https://leetcode.com/problems/count-vowel-strings-in-ranges/
// Solved on 30th of November, 2025
class Solution {
    /**
     * Counts the number of vowel strings within specified ranges.
     * A string is considered a vowel string if it starts and ends with a vowel.
     * @param words An array of strings to check.
     * @param queries A 2D array where each inner array `[l, r]` represents a query range (inclusive).
     * @return An array of integers, where each element is the count of vowel strings for the corresponding query.
     */
    public int[] vowelStrings(String[] words, int[][] queries) {
        int n = words.length;
        int[] counts = new int[n + 1];
        for (int i = 0; i < n; i++) {
            char start = words[i].charAt(0);
            char end = words[i].charAt(words[i].length() - 1);
            if (isVowel(start) && isVowel(end)) {
                counts[i + 1] = counts[i] + 1;
            } else {
                counts[i + 1] = counts[i];
            }
        }
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];
            result[i] = counts[r + 1] - counts[l];
        }
        return result;
    }

    private boolean isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}