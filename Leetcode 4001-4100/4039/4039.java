// Leetcode 4039: Sum of Decoded Numbers
// https://leetcode.com/problems/sum-of-decoded-numbers/
// Solved on 1st of October, 2026
class Solution {
    /**
     * Decodes each integer in the given array into a base and exponent, computes
     * the exponential value modulo 1,000,000,007, and returns their total sum.
     *
     * @param nums an array of encoded numbers
     * @return the sum of decoded values modulo 1,000,000,007
     */
    public int sumDecoded(long[] nums) {
        long modulo = 1_000_000_007L;
        long totalSum = 0;
        long[] powersOfTen = new long[16];
        powersOfTen[0] = 1L;
        for (int i = 1; i < 16; i++) {
            powersOfTen[i] = powersOfTen[i - 1] * 10L;
        }

        for (long num : nums) {
            int width = (int) (num % 10);
            long quotient = num / 10;

            long temp = quotient;
            int length = 0;
            while (temp > 0) {
                length++;
                temp /= 10;
            }

            int remainingDigits = length - width;
            long divisor = powersOfTen[remainingDigits];

            long baseValue = quotient / divisor;
            long exponentValue = quotient % divisor;

            long termResult = modularExponentiation(baseValue, exponentValue, modulo);
            totalSum = (totalSum + termResult) % modulo;
        }

        return (int) totalSum;
    }

    private long modularExponentiation(long base, long exponent, long modulo) {
        long result = 1;
        base %= modulo;

        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * base) % modulo;
            }
            base = (base * base) % modulo;
            exponent >>= 1;
        }

        return result;
    }
}