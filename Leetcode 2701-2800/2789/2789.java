// Leetcode 279: Largest Element in an Array after Merge Operations
// https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/
// Solved on 7th of January, 2026
class Solution {
    /**
     * Finds the largest possible element in an array after performing merge operations.
     * A merge operation combines two adjacent elements if the left element is less than or equal to the right element.
     * @param nums The input array of integers.
     * @return The largest possible element after all valid merge operations.
     */
    public long maxArrayValue(int[] nums) {
        long currentMax = nums[nums.length - 1];
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] <= currentMax) {
                currentMax += nums[i];
            } else {
                currentMax = nums[i];
            }
        }
        return currentMax;
    }
}