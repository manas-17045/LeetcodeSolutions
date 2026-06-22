// Leetcode 1189: Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/
// Solved on 22nd of June, 2026
class Solution {
    /**
     * Calculates the maximum number of balloons that can be formed from the given text.
     * 
     * @param text The string of characters to form balloons from.
     * @return The maximum number of balloons that can be formed.
     */
    public int maxNumberOfBalloons(String text) {
        int[] counts = new int[26];
        for (int i = 0; i < text.length(); i++) {
            counts[text.charAt(i) - 'a']++;
        }
        int minCount = counts['b' - 'a'];
        minCount = Math.min(minCount, counts['a' - 'a']);
        minCount = Math.min(minCount, counts['l' - 'a'] / 2);
        minCount = Math.min(minCount, counts['o' - 'a'] / 2);
        minCount = Math.min(minCount, counts['n' - 'a']);
        return minCount;
    }
}