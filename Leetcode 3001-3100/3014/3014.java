// Leetcode 3014: Minimum Number of Pushes to Type Word I
// https://leetcode.com/problems/minimum-number-of-pushed-to-word-i/
// Solved on 30th of July, 2026
class Solution {
    /**
     * Calculates the minimum number of pushes required to type a given word on a phone keypad.
     * 
     * The method assigns the first 8 letters to the 1st position (1 push each),
     * the next 8 letters to the 2nd position (2 pushes each), and so on.
     * 
     * @param word The input string to be typed.
     * @return The minimum total number of pushes required.
     */
    public int minimumPushes(String word) {
        int length = word.length();
        int totalPushes = 0;
        int multiplier = 1;

        while (length > 0) {
            if (length >= 8) {
                totalPushes += 8 * multiplier;
                length -= 8;
            } else {
                totalPushes += length * multiplier;
                length = 0;
            }
            multiplier++;
        }

        return totalPushes;
    }
}