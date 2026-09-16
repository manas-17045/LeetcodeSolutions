// Leetcode 1621: Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
// Solved on 16th of September, 2026
class Solution {
    /**
     * Computes the number of ways to draw exactly k non-overlapping line segments
     * across n points on a 1-D plane, where segments are allowed to share endpoints.
     *
     * @param n the total number of integer points on the line
     * @param k the exact number of line segments to draw
     * @return the number of valid configurations modulo 1,000,000,007
     */
    public int numberOfSets(int n, int k) {
        int totalN = n + k - 1;
        int totalR = 2 * k;

        if (totalR > totalN) {
            return 0;
        }

        long mod = 1_000_000_007L;
        long numerator = 1;
        long denominator = 1;

        for (int i = 0; i < totalR; i++) {
            numerator = (numerator * (totalN - i)) % mod;
            denominator = (denominator * (i + 1)) % mod;
        }

        return (int) ((numerator * power(denominator, mod - 2, mod)) % mod);
    }

    private long power(long base, long exponent, long mod) {
        long result = 1;
        base %= mod;
        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exponent >>= 1;
        }
        return result;
    }
}