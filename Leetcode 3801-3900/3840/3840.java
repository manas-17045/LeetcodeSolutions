// Leetcode 3840: House Robber V
// https://leetcode.com/problems/house-robber-v/
// Solved on 16th of February, 2026
class Solution {
    /**
     * Calculates the maximum amount of money that can be robbed from houses
     * grouped by color, where adjacent houses of the same color cannot be robbed.
     *
     * @param nums An array of integers representing the money in each house.
     * @param colors An array of integers representing the color of each house.
     * @return The total maximum amount of money that can be robbed.
     */
    public long rob(int[] nums, int[] colors) {
        long totalRobbed = 0;
        long currentMax = 0;
        long previousMax = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            long temp = Math.max(currentMax, previousMax + nums[i]);
            previousMax = currentMax;
            currentMax = temp;

            if (i == n - 1 || colors[i] != colors[i + 1]) {
                totalRobbed += currentMax;
                currentMax = 0;
                previousMax = 0;
            }
        }

        return totalRobbed;
    }
}