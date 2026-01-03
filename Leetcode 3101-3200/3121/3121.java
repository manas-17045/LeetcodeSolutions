// Leetcode 3121: Count the Number of Special Characters II
// https://leetcode.com/problems/count-the-number-of-special-characters-ii/
// Solved on 3rd of January, 2026
class Solution {
    /**
     * Counts the number of "special" characters in a given word.
     * A character is considered special if its lowercase version appears before its uppercase version in the word.
     * @param word The input string to analyze.
     * @return The total count of special characters.
     */
    public int numberOfSpecialChars(String word) {
        int[] lastLower = new int[26];
        int[] firstUpper = new int[26];

        for (int i = 0; i < 26; i++) {
            lastLower[i] = -1;
            firstUpper[i] = -1;
        }

        int n = word.length();
        for (int i = 0; i < n; i++) {
            char c = word.charAt(i);
            if (c >= 'a' && c <= 'z') {
                lastLower[c - 'a'] = i;
            } else {
                int idx = c - 'A';
                if (firstUpper[idx] == -1) {
                    firstUpper[idx] = i;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (lastLower[i] != -1 && firstUpper[i] != -1 && lastLower[i] < firstUpper[i]) {
                count++;
            }
        }

        return count;
    }
}