// Leetcode 3345: Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/
// Solved on 6th of August, 2026
class Solution {
    /**
     * Finds the smallest number greater than or equal to n whose digit product is divisible by t.
     * 
     * @param n The lower bound of the range.
     * @param t The divisor.
     * @return The smallest number in the range [n, infinity) whose digit product is divisible by t.
     */
    public int smallestNumber(int n, int t) {
        while (true) {
            if (getDigitProduct(n) % t == 0) {
                return n;
            }
            n++;
        }
    }

    private int getDigitProduct(int number) {
        int product = 1;
        while (number > 0) {
            product *= number % 10;
            number /= 10;
        }
        return product;
    }
}