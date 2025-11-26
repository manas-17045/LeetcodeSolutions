// Leetcode 3724: Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/
// Solved on 26th of November, 2025
class Solution {
    /**
     * Calculates the minimum operations to transform array nums1 into nums2.
     *
     * @param nums1 The first input array.
     * @param nums2 The second input array, which is the target array.
     * @return The minimum number of operations required.
     */
    public long minOperations(int[] nums1, int[] nums2) {
        long totalOps = 0;
        long minDiff = Long.MAX_VALUE;
        int n = nums1.length;
        int lastVal = nums2[n];

        for (int i = 0; i < n; i++) {
            int curr = nums1[i];
            int target = nums2[i];
            totalOps += Math.abs(curr - target);

            int low = Math.min(curr, target);
            int high = Math.max(curr, target);

            long currentDiff = 0;
            if (lastVal < low) {
                currentDiff = low - lastVal;
            } else if (lastVal > high) {
                currentDiff = lastVal - high;
            } else {
                currentDiff = 0;
            }

            if (currentDiff < minDiff) {
                minDiff = currentDiff;
            }
        }

        return totalOps + minDiff + 1;
    }
}