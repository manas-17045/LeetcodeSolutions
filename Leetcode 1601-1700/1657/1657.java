// Leetcode 1657: Determine if Two Strings Are Close
// https://leetcode.com/problems/determine-if-two-strings-are-close/
// Solved on 4th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Determines if two strings are "close". Two strings are considered close if you can obtain one from the other
     * using the following operations:
     * 1. Swap any two existing characters.
     * 2. Transform every occurrence of one existing character into another existing character, and vice versa.
     */
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        int[] frequency1 = new int[26];
        int[] frequency2 = new int[26];

        for (int i = 0; i < word1.length(); i++) {
            frequency1[word1.charAt(i) - 'a']++;
        }

        for (int i = 0; i < word2.length(); i++) {
            frequency2[word2.charAt(i) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if ((frequency1[i] == 0 && frequency2[i] != 0) || 
                (frequency1[i] != 0 && frequency2[i] == 0)) {
                return false;
            }
        }

        Arrays.sort(frequency1);
        Arrays.sort(frequency2);

        return Arrays.equals(frequency1, frequency2);
    }
}