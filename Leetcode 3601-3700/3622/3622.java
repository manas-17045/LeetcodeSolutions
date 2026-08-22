// Leetcode 3622: Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
// Solved on 22nd of August, 2026
class Solution {
    /**
     * Checks if a given integer n is divisible by the sum of its digits plus the
     * product of its digits.
     *
     * @param n The integer to check for divisibility.
     * @return true if n is divisible by the sum of its digits plus the product of
     *         its digits, false otherwise.
     */
    public boolean checkDivisibility(int n) {
        int temp = n;
        int digitSum = 0;
        int digitProduct = 1;

        while (temp > 0) {
            int digit = temp % 10;
            digitSum += digit;
            digitProduct *= digit;
            temp /= 10;
        }

        int totalDivisor = digitSum + digitProduct;
        return n % totalDivisor == 0;
    }
}