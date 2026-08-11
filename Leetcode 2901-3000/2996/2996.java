// Leetcode 2996: Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/
// Solved on 11th of August, 2026
class Solution {
    /**
     * Calculates the smallest missing integer greater than the sequential prefix sum of the array.
     * @param nums The input array of integers.
     * @return The smallest missing integer greater than the sequential prefix sum.
     */
    public int missingInteger(int[] nums) {
        int sum = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                sum += nums[i];
            } else {
                break;
            }
        }
        boolean[] present = new boolean[51];
        for (int num : nums) {
            present[num] = true;
        }
        while (sum <= 50 && present[sum]) {
            sum++;
        }
        return sum;
    }
}