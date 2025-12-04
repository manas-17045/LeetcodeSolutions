// Leetcode 1347: Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
// Solved on 4th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of steps to make two strings anagrams.
     * A step consists of changing one character in string t to another character.
     * @param s The first string.
     * @param t The second string.
     * @return The minimum number of steps.
     */
    public int minSteps(String s, String t) {
        int[] counts = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counts[s.charAt(i) - 'a']++;
            counts[t.charAt(i) - 'a']--;
        }
        int steps = 0;
        for (int count : counts) {
            if (count > 0) {
                steps += count;
            }
        }
        return steps;
    }
}