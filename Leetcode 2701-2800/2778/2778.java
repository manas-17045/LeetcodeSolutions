// Leetcode 2778: Sum of Squares of Special Elements
// https://leetcode.com/problems/sum-of-squares-of-special-elements/
// Solved on 11th of October, 2026
class Solution {
    /**
     * Calculates the sum of squares of all special elements in the array.
     * An element at 1-based index i is special if the total length n is divisible by i.
     *
     * @param nums the 1-indexed input array of integers
     * @return the sum of squares of all special elements
     */
    public int sumOfSquares(int[] nums) {
        int n = nums.length;
        int sumOfSquares = 0;

        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                sumOfSquares += nums[i - 1] * nums[i - 1];
                int pairedIndex = n / i;
                if (pairedIndex != i) {
                    sumOfSquares += nums[pairedIndex - 1] * nums[pairedIndex - 1];
                }
            }
        }

        return sumOfSquares;
    }
}