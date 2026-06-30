// Leetcode 1358: Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
// Solved on 30th of June, 2026
class Solution {
    /**
     * Computes the number of substrings that contain at least one 'a', 'b', and 'c'.
     * 
     * @param s The input string.
     * @return The number of substrings containing at least one 'a', 'b', and 'c'.
     */
    public int numberOfSubstrings(String s) {
        int lastA = -1;
        int lastB = -1;
        int lastC = -1;
        int count = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == 'a') {
                lastA = i;
            } else if (ch == 'b') {
                lastB = i;
            } else if (ch == 'c') {
                lastC = i;
            }
            count += Math.min(lastA, Math.min(lastB, lastC)) + 1;
        }
        return count;
    }
}