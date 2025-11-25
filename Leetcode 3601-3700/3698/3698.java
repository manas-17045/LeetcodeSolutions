// Leetcode 3698: Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/
// Solved on 25th of November, 2025
class Solution {
    /**
     * Splits an array into two non-empty subarrays such that the absolute difference between their sums is minimized.
     *
     * @param nums The input array of integers.
     * @return The minimum absolute difference between the sums of the two subarrays.
     */
    public long splitArray(int[] nums) {
        int n = nums.length;
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int incLimit = 0;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i + 1] > nums[i]) {
                incLimit++;
            } else {
                break;
            }
        }

        int decLimit = n - 1;
        for (int i = n - 1; i > 0; i--) {
            if (nums[i - 1] > nums[i]) {
                decLimit--;
            } else {
                break;
            }
        }

        long leftSum = 0;
        long minDiff = -1;

        for (int i = 0; i < n - 1; i++) {
            leftSum += nums[i];
            if (i <= incLimit && i >= decLimit - 1) {
                long rightSum = totalSum - leftSum;
                long diff = Math.abs(leftSum - rightSum);
                if (minDiff == -1 || diff < minDiff) {
                    minDiff = diff;
                }
            }
        }

        return minDiff;
    }
}