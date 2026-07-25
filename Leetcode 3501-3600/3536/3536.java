// Leetcode 3536: Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/
// Solved on 25th of July, 2026
class Solution {
    /**
     * Finds the maximum product of two distinct digits of a given integer.
     * @param n The integer to find the maximum product of two digits.
     * @return The maximum product of two distinct digits.
     */
    public int maxProduct(int n) {
        int firstMax = 0;
        int secondMax = 0;
        while (n > 0) {
            int digit = n % 10;
            if (digit > firstMax) {
                secondMax = firstMax;
                firstMax = digit;
            } else if (digit > secondMax) {
                secondMax = digit;
            }
            n /= 10;
        }
        return firstMax * secondMax;
    }
}