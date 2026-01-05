// Leetcode 2957: Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/
// Solved on 5th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to remove adjacent almost-equal characters.
     * @param word The input string.
     * @return The minimum number of operations.
     */
    public int removeAlmostEqualCharacters(String word) {
        int operations = 0;
        int length = word.length();
        for (int i = 0; i < length - 1; i++) {
            if (Math.abs(word.charAt(i) - word.charAt(i + 1)) <= 1) {
                operations++;
                i++;
            }
        }
        return operations;
    }
}