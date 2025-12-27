// Leetcode 3713: Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/
// Solved on 27th of December, 2025
class Solution {
    /**
     * Finds the length of the longest balanced substring.
     * A substring is balanced if all characters in it appear the same number of times.
     * @param s The input string.
     * @return The length of the longest balanced substring.
     */
    public int longestBalanced(String s) {
        int n = s.length();
        int maxLength = 0;
        for (int i = 0; i < n; i++) {
            int[] freq = new int[26];
            int maxFreq = 0;
            int distinctCount = 0;
            for (int j = i; j < n; j++) {
                int index = s.charAt(j) - 'a';
                if (freq[index] == 0) {
                    distinctCount++;
                }
                freq[index]++;
                maxFreq = Math.max(maxFreq, freq[index]);
                
                if ((j - i + 1) == (maxFreq * distinctCount)) {
                    maxLength = Math.max(maxLength, j - i + 1);
                }
            }
        }
        return maxLength;
    }
}