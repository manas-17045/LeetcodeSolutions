// Leetcode 3756: Concatenate Non-Zero Digits and Multiply by Sum II
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
// Solved on 26th of December, 2025
class Solution {
    /**
     * Concatenates non-zero digits within a given range and multiplies the resulting number by the sum of digits in that range.
     *
     * @param s The input string of digits.
     * @param queries A 2D array where each inner array `[l, r]` represents a query range (inclusive).
     * @return An array of integers, where each element `result[i]` is the calculated value for `queries[i]`.
     */
    public int[] sumAndMultiply(String s, int[][] queries) {
        int n = s.length();
        long mod = 1000000007L;

        long[] vals = new long[n + 1];
        int[] counts = new int[n + 1];
        int[] sums = new int[n + 1];
        long[] pows = new long[n + 1];

        pows[0] = 1;

        for (int i = 0; i < n; i++) {
            int digit = s.charAt(i) - '0';

            sums[i + 1] = sums[i] + digit;
            pows[i + 1] = (pows[i] * 10) % mod;

            if (digit != 0) {
                counts[i + 1] = counts[i] + 1;
                vals[i + 1] = (vals[i] * 10 + digit) % mod;
            } else {
                counts[i + 1] = counts[i];
                vals[i + 1] = vals[i];
            }
        }

        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            long currentSum = sums[r + 1] - sums[l];
            int nonZeroCount = counts[r + 1] - counts[l];

            long valFull = vals[r + 1];
            long valPrev = vals[l];

            long rangeVal = (valFull - (valPrev * pows[nonZeroCount]) % mod + mod) % mod;

            result[i] = (int) ((rangeVal * currentSum) % mod);
        }

        return result;
    }
}