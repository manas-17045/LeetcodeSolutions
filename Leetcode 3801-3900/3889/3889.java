// Leetcode 3889: Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/
// Solved on 12th of April, 2026
class Solution {
    /**
     * Calculates the mirror frequency distance of a string.
     * 
     * @param s The input string containing characters to analyze.
     * @return The total absolute difference in frequencies between mirrored character pairs.
     */
    public int mirrorFrequency(String s) {
        int[] frequency = new int[128];
        int stringLength = s.length();

        for (int i = 0; i < stringLength; i++) {
            frequency[s.charAt(i)]++;
        }

        int totalSum = 0;

        for (char c = 'a'; c <= 'm'; c++) {
            char mirrorChar = (char) ('z' - (c - 'a'));
            int currentDiff = frequency[c] - frequency[mirrorChar];
            totalSum += currentDiff > 0 ? currentDiff : -currentDiff;
        }

        for (char c '0'; c <= '4'; c++) {
            char mirrorChar = (char) ('9' - (c - '0'));
            int currentDiff = frequency[c] - frequency[mirrorChar];
            totalSum += currentDiff > 0 ? currentDiff : -currentDiff;
        }

        return totalSum;
    }
}