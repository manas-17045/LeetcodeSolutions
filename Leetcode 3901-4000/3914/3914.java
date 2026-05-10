// Leetcode 3914: Minimum Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/
// Solved on 10th of May, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to make the array non-decreasing.
     * 
     * @param nums An array of integers.
     * @return The total number of operations required.
     */
    public long minOperations(int[] nums) {
        long operations = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] > nums[i]) {
                operations += (nums[i - 1] - nums[i]);
            }
        }
        return operations;
    }
}