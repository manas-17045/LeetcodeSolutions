// Leetcode 2980: Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/
// Solved on 7th of December, 2025
class Solution {
    /**
     * Checks if the bitwise OR of any two numbers in the given array has a trailing zero.
     * A trailing zero in binary representation means the number is even.
     *
     * @param nums An array of integers.
     * @return True if there are at least two even numbers in the array, false otherwise.
     */
    public boolean hasTrailingZeros(int[] nums) {
        int evenCount = 0;
        for (int number : nums) {
            if (number % 2 == 0) {
                evenCount++;
            }
            if (evenCount >= 2) {
                return true;
            }
        }
        return false;
    }
}