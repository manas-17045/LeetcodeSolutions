// Leetcode 3325: Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/
// Solved on 23rd of October, 2025
class Solution {
    /**
     * Counts the number of substrings where at least one character appears at least k times.
     *
     * @param s The input string consisting of lowercase English letters.
     * @param k The minimum frequency threshold for a character to be considered "k-frequency".
     * @return The total number of substrings that satisfy the condition.
     */
    public int numberOfSubstrings(String s, int k) {
        int n = s.length();
        int totalSubstrings = n * (n + 1) / 2;

        // Count substrings where NO character appears at least k times
        int invalidSubstrings = countInvalidSubstrings(s, k);

        return totalSubstrings - invalidSubstrings;
    }

    private int countInvalidSubstrings(String s, int k) {
        int n = s.length();
        int count = 0;
        int left = 0;
        int[] freq = new int[26];

        for (int right = 0; right < n; right++) {
            // Add current character to window
            freq[s.charAt(right) - 'a']++;
            
            // Shrink window while any character has frequency >= k
            while (left <= right && hasKFrequency(freq, k)) {
                freq[s.charAt(left) - 'a']--;
                left++;
            }

            // All substrings from left to right are invalid
            count += right - left + 1;
        }

        return count;
    }

    private boolean hasKFrequency(int[] freq, int k) {
        for (int f : freq) {
            if (f >= k) {
                return true;
            }
        }
        return false;
    }
}