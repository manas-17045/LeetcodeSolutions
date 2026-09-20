// Leetcode 3498: Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/
// Solved on 20th of Septemeber, 2026
class Solution {
    /**
     * Calculates the reverse degree of the given string by summing the products
     * of each character's position in the reversed alphabet and its 1-indexed
     * position within the string.
     *
     * @param s the input string consisting of lowercase English letters
     * @return the calculated reverse degree
     */
    public int reverseDegree(String s) {
        int totalDegree = 0;
        int length = s.length();

        for (int i = 0; i < length; i++) {
            int charWeight = 'z' - s.charAt(i) + 1;
            totalDegree += charWeight * (i + 1);
        }

        return totalDegree;
    }
}