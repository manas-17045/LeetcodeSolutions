// Leetcode 66: Plus One
// https://leetcode.com/problems/plus-one/
// Solved on 1st of January, 2026
class Solution {
    /**
     * Given a large integer represented as an integer array `digits`, where each `digits[i]` is the `i`-th digit of the integer.
     * The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading zeros, except for the number 0 itself.
     * Increment the large integer by one and return the resulting array of digits.
     */
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        int[] result = new int[digits.length + 1];
        result[0] = 1;
        return result;
    }
}