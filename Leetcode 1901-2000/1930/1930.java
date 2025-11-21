// Leetcode 1930: Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
// Solved on 21st of November, 2025
class Solution {
    /**
     * Counts the number of unique length-3 palindromic subsequences in the given string.
     * A length-3 palindromic subsequence is of the form "aba", where 'a' and 'b' are characters.
     * @param s The input string.
     * @return The total number of unique length-3 palindromic subsequences.
     */
    public int countPalindromicSubsequences(String s) {
        int[] firstIndex = new int[26];
        int[] lastIndex = new int[26];
        for (int i = 0; i < 26; i++) {
            firstIndex[i] = -1;
        }

        int length = s.length();
        for (int i = 0; i < length; i++) {
            int charCode = s.charAt(i) - 'a';
            if (firstIndex[charCode] == -1) {
                firstIndex[charCode] = i;
            }
            lastIndex[charCode] = i;
        }

        int result = 0;
        for (int i = 0; i < 26; i++) {
            int start = firstIndex[i];
            int end = lastIndex[i];

            if (start != -1 && end > start + 1) {
                boolean[] seen = new boolean[26];
                for (int j = start + 1; j < end; j++) {
                    seen[s.charAt(j) - 'a'] = true;
                }
                
                for (int j = 0; j < 26; j++) {
                    if (seen[j]) {
                        result++;
                    }
                }
            }
        }
        return result;
    }
}