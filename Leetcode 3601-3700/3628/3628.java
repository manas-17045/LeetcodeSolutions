// Leetcode 3628: Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/
// Solved on 29th of December, 2025
class Solution {
    /**
     * Calculates the maximum number of "LCT" subsequences that can be formed after inserting one character ('L', 'C', or 'T') into the string `s`.
     *
     * @param s The input string consisting of characters 'L', 'C', and 'T'.
     * @return The maximum number of "LCT" subsequences achievable after one insertion.
     */
    public long numOfSubsequences(String s) {
        char[] chars = s.toCharArray();
        int n = chars.length;
        long[] suffixT = new long[n + 1];
        long countCT = 0;

        for (int i = n - 1; i >= 0; i--) {
            suffixT[i] = suffixT[i + 1];
            if (chars[i] == 'T') {
                suffixT[i]++;
            } else if (chars[i] == 'C') {
                countCT += suffixT[i + 1];
            }
        }

        long countL = 0;
        long countLC = 0;
        long countLCT = 0;
        long maxGainC = 0;

        for (int i = 0; i < n; i++) {
            maxGainC = Math.max(maxGainC, countL * suffixT[i]);

            if (chars[i] == 'L') {
                countL++;
            } else if (chars[i] == 'C') {
                countLC += countL;
            } else if (chars[i] == 'T') {
                countLCT += countLC;
            }
        }
        maxGainC = Math.max(maxGainC, countL * suffixT[n]);

        return countLCT + Math.max(countCT, Math.max(countLC, maxGainC));
    }
}