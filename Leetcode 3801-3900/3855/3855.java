// Leetcode 3855: Sum of K-Digit Numbers in a Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/
// Solved on 1st of March, 2026
class Solution {
    /**
     * Calculates the sum of all k-digit numbers formed within a given range [l, r].
     *
     * @param l The lower bound of the range.
     * @param r The upper bound of the range.
     * @param k The number of digits for the numbers to be summed.
     * @return The total sum modulo 10^9 + 7.
     */
    public int sumOfNumbers(int l, int r, int k) {
        long mod = 1000000007;
        long numDigits = r - l + 1;
        long sumOfDigits = (long) (l + r) * numDigits / 2;
        long termOne = sumOfDigits % mod;
        long termTwo = power(numDigits, k - 1, mod);
        long termThree = (power(10, k, mod) - 1 + mod) % mod;
        long inverseNine = power(9, mod - 2, mod);
        long result = (termOne * termTwo) % mod;
        result = (result * termThree) % mod;
        result = (result * inverseNine) % mod;
        return (int) result;
    }

    private long power(long base, long exp, long mod) {
        long res = 1;
        base = base % mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
}