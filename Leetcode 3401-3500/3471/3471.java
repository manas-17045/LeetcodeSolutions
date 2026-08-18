// Leetcode 3471: Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/
// Solved on 18th of August, 2026
class Solution {
    /**
     * Finds the largest integer that appears in exactly one subarray of size k.
     * 
     * @param nums The input array of integers.
     * @param k The target subarray size.
     * @return The maximum value appearing in exactly one contiguous subarray
     *         of size k, or -1 if no such integer exists.
     */
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;
        int[] frequency = new int[51];
        for (int num : nums) {
            frequency[num]++;
        }

        if (k == n) {
            int maxVal = -1;
            for (int num : nums) {
                maxVal = Math.max(maxVal, num);
            }
            return maxVal;
        }

        if (k == 1) {
            int maxVal = -1;
            for (int num : nums) {
                if (frequency[num] == 1) {
                    maxVal = Math.max(maxVal, num);
                }
            }
            return maxVal;
        }

        int maxVal = -1;
        if (frequency[nums[0]] == 1) {
            maxVal = Math.max(maxVal, nums[0]);
        }
        if (frequency[nums[n - 1]] == 1) {
            maxVal = Math.max(maxVal, nums[n - 1]);
        }
        return maxVal;
    }
}