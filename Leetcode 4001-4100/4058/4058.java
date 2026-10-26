// Leetcode 4058: Maximum Pulse Value After One Subarray Rotation
// https://leetcode.com/problems/maximum-pulse-value-after-one-subarray-rotation/
// Solved on 26th of October, 2026
class Solution {
    /**
     * Calculates the maximum pulse value of the array after performing at most one subarray left-rotation.
     *
     * @param nums the input array of integers
     * @return the maximum achievable pulse value
     */
    public long maxValue(int[] nums) {
        long currentSum = 0;
        long maxEvenPrefix = 0;
        long maxOddPrefix = 0;
        boolean hasOddPrefix = false;
        long maxDelta = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                currentSum += nums[i];
                if (hasOddPrefix) {
                    long delta = 2 * (maxOddPrefix - currentSum);
                    if (delta > maxDelta) {
                        maxDelta = delta;
                    }
                }
                if (!hasOddPrefix || currentSum > maxOddPrefix) {
                    maxOddPrefix = currentSum;
                    hasOddPrefix = true;
                }
            } else {
                currentSum -= nums[i];
                long delta = 2 * (maxEvenPrefix - currentSum);
                if (delta > maxDelta) {
                    maxDelta = delta;
                }
                if (currentSum > maxEvenPrefix) {
                    maxEvenPrefix = currentSum;
                }
            }
        }

        return currentSum + maxDelta;
    }
}