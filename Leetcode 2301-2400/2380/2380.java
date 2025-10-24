// Leetcode 2380: Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
// Solved on 24th of October, 2025
class Solution {
    /**
     * Calculates the minimum time needed to rearrange a binary string such that all '0's are to the left of all '1's.
     * In one second, any "01" pair can be transformed into "10".
     * @param s The input binary string.
     * @return The minimum number of seconds required.
     */
    public int secondsToRemoveOccurrences(String s) {
        int zeros = 0;
        int time = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                zeros++;
            } else {
                if (zeros > 0) {
                    time = Math.max(time + 1, zeros);
                }
            }
        }

        return time;
    }
}