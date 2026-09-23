// Leetcode 1658: Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
// Solved on 23rd of September, 2026
class Solution {
    /**
     * Calculates the minimum number of operations to reduce x to zero by removing
     * elements from either the leftmost or rightmost ends of the array.
     *
     * @param nums the array of positive integers
     * @param x the target value to reduce to zero
     * @return the minimum number of operations required, or -1 if it is impossible
     */
    public int minOperations(int[] nums, int x) {
        int totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }

        int targetSum = totalSum - x;
        if (targetSum < 0) {
            return -1;
        }
        if (targetSum == 0) {
            return nums.length;
        }

        int left = 0;
        int currentSum = 0;
        int maxLength = -1;

        for (int right = 0; right < nums.length; right++) {
            currentSum += nums[right];

            while (left <= right && currentSum > targetSum) {
                currentSum -= nums[left];
                left++;
            }

            if (currentSum == targetSum) {
                maxLength = Math.max(maxLength, right - left + 1);
            }
        }

        return maxLength == -1 ? -1 : nums.length - maxLength;
    }
}