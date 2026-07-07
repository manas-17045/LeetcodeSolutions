// Leetcode 3754: Concatenate Non-Zero Digits and Multiply by Sum I
// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
// Solved on 7th of July, 2026
class Solution {
    /**
     * Concatenates the non-zero digits of a number and multiplies the result by
     * the sum of the non-zero digits.
     * 
     * @param n The number to process.
     * @return The result of concatenating the non-zero digits and multiplying by the sum of the non-zero digits.
     */
    public long sumAndMultiply(int n) {
        long x = 0;
        long sum = 0;
        long multiplier = 1;
        while (n > 0) {
            int digit = n % 10;
            if (digit != 0) {
                x = digit * multiplier + x;
                sum += digit;
                multiplier *= 10;
            }
            n /= 10;
        }
        return x * sum;
    }
}