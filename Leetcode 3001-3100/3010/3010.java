// Leetcode 3010: Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
// Solved on 1st of February, 2026
class Solution {
    /**
     * Calculates the minimum possible sum of the first elements of three subarrays.
     * The first subarray must start at index 0.
     * @param nums An array of integers.
     * @return The minimum cost to divide the array into three subarrays.
     */
    public int minimumCost(int[] nums) {
        int firstMin = Integer.MAX_VALUE;
        int secondMin = Integer.MAX_VALUE;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < firstMin) {
                secondMin = firstMin;
                firstMin = nums[i];
            } else if (nums[i] < secondMin) {
                secondMin = nums[i];
            }
        }

        return nums[0] + firstMin + secondMin;
    }
}