// Leetcode 3993: Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/
// Solved on 15th of August, 2026
class Solution {
    /**
     * Calculates the maximum value of an alternating sequence.
     * The sequence starts with `s`, has length `n`, and each element is at most `m`.
     * 
     * @param n The length of the sequence.
     * @param s The starting value of the sequence.
     * @param m The maximum value for each element in the sequence.
     * @return The maximum value of an alternating sequence.
     */
    public long maximumValue(int n, int s, int m) {
        if (n == 1) {
            return s;
        }
        long stepCount = (n - 2) / 2;
        return (long) s + m + stepCount * (m - 1);
    }
}