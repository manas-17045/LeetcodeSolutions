// Leetcode 3746: Minimum String Length After Balanced removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/
// Solved on 26th of December, 2025
class Solution {
    /**
     * Calculates the minimum possible length of a string after performing balanced removals.
     * @param s The input string consisting of 'a's and 'b's.
     * @return The minimum length of the string after balanced removals.
     */
    public int minLengthAfterRemovals(String s) {
        int countA = 0;
        int countB = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'a') {
                countA++;
            } else {
                countB++;
            }
        }
        return Math.abs(countA - countB);
    }
}