// Leetcode 3959: Check Good Integer
// https://leetcode.com/problems/check-good-integer/
// Solved on 29th of June, 2026
class Solution {
    /**
     * Checks if the given integer is a good integer.
     * A good integer is an integer that contains at least three consecutive occurrences of the same digit.
     * @param n The integer to check.
     * @return True if the integer is a good integer, False otherwise.
     */
    public boolean checkGoodInteger(int n) {
        int digitSum = 0;
        int squareSum = 0;
        while (n > 0) {
            int digit = n % 10;
            digitSum += digit;
            squareSum += digit * digit;
            n /= 10;
        }
        return (squareSum - digitSum) >= 50;
    }
}