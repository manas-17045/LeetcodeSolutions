// Leetcode 1827: Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/
// Solved on 5th of December, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to make the array strictly increasing.
     * An operation consists of incrementing an element by 1.
     * @param nums The input array of integers.
     * @return The minimum number of operations.
     */
    public int minOperations(int[] nums) {
        int totalOperations = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] <= nums[i - 1]) {
                int increment = nums[i - 1] - nums[i] + 1;
                totalOperations += increment;
                nums[i] += increment;
            }
        }
        return totalOperations;
    }
}