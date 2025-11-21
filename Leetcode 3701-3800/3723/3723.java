// Leetcode 3723: Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
// Solved on 21st of November, 2025
class Solution {
    /**
     * This method aims to construct the largest possible number (as a string) with 'num' digits
     * such that the sum of its digits equals 'sum'.
     * @param num The desired number of digits in the resulting number.
     * @param sum The target sum of the digits.
     * @return A string representing the largest number with 'num' digits and digit sum 'sum', or an empty string if impossible.
     */
    public String maxSumOfSquares(int num, int sum) {
        if (sum > num * 9) {
            return "";
        }

        StringBuilder result = new StringBuilder(num);
        int nines = sum / 9;
        int remainder = sum % 9;

        for (int i = 0; i < nines; i++) {
            result.append('9');
        }

        if (remainder > 0) {
            result.append(remainder);
        }

        while (result.length() < num) {
            result.append('0');
        }

        return result.toString();
    }
}