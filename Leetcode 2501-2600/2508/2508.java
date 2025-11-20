// Leetcode 2508: Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/
// Solved on 20th of November, 2025
class Solution {
    /**
     * Finds the final value after repeatedly multiplying the original value by two if it exists in the given array.
     * @param nums An array of integers.
     * @param original The initial integer value.
     * @return The final value after multiplication.
     */
    public int findFinalValue(int[] nums, int original) {
        boolean[] isPresent = new boolean[1001];
        for (int num : nums) {
            isPresent[num] = true;
        }
        while (original <= 1000 && isPresent[original]) {
            original *= 2;
        }
        return original;
    }
}