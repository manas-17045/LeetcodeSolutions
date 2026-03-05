// Leetcode 2390: Removing Stars Froma String
// https://leetcode.com/problems/removing-stars-from-a-string/
// Solved on 5th of March, 2026
class Solution {
    /**
     * Removes stars from a string by deleting the star and the closest non-star character to its left.
     * 
     * @param s The input string containing lowercase English letters and stars '*'.
     * @return The string after all stars have been removed.
     */
    public String removeStars(String s) {
        char[] chars = s.toCharArray();
        int writeIndex = 0;

        for (int readIndex = 0; readIndex < chars.length; readIndex++) {
            if (chars[readIndex] == '*') {
                writeIndex--;
            } else {
                chars[writeIndex] = chars[readIndex];
                writeIndex++;
            }
        }

        return new String(chars, 0, writeIndex);
    }
}