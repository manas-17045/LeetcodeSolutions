// Leetcode 1680: Concatenation of Consecutive Binary Numbers
// https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
// Solved on 28th of February, 2026
class Solution {
    /**
     * Concatenates the binary representations of numbers from 1 to n and returns the result modulo 10^9 + 7.
     *
     * @param n The integer up to which binary representations are concatenated.
     * @return The decimal value of the concatenated binary string modulo 10^9 + 7.
     */
    public int concatenatedBinary(int n) {
        long result = 0;
        int mod = 1000000007;
        int bitLength = 0;

        for (int i = 0; i <= n; i++) {
            if ((i & (i - 1)) == 0) {
                bitLength++;
            }
            result = ((result << bitLength) | i) % mod;
        }

        return (int) result;
    }
}