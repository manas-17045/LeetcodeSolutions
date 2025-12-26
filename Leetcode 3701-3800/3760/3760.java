// Leetcode 3760: Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/
// Solved on 26th of December, 2025
class Solution {
    /**
     * Calculates the number of distinct characters in a given string.
     * @param s The input string.
     * @return The count of distinct characters in the string.
     */
    public int maxDistinct(String s) {
        boolean[] seen = new boolean[26];
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            int index = s.charAt(i) - 'a';
            if (!seen[index]) {
                seen[index] = true;
                count++;
            }
        }
        return count;
    }
}