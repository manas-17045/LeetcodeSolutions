// Leetcode 2321: Maximum Score of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/
// Solved on 5th of November, 2025
class Solution {
    /**
     * Calculates the maximum possible score of a spliced array.
     * A spliced array is formed by taking either nums1 or nums2 as the base,
     * and then swapping a subarray from the other array into the base array.
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers.
     * @return The maximum possible score.
     */
    public int maximumsSplicedArray(int[] nums1, int[] nums2) {
        long sum1 = 0;
        long sum2 = 0;
        for (int i = 0; i < nums1.length; i++) {
            sum1 += nums1[i];
            sum2 += nums2[i];
        }
        long maxGainFor1 = 0;
        long curGainFor1 = 0;
        long maxGainFor2 = 0;
        long curGainFor2 = 0;
        for (int i = 0; i < nums1.length; i++) {
            long diff1 = nums2[i] - nums1[i];
            curGainFor1 = Math.max(0, curGainFor1 + diff1);
            if (curGainFor1 > maxGainFor1)
                maxGainFor1 = curGainFor1;
            long diff2 = nums1[i] - nums2[i];
            curGainFor2 = Math.max(0, curGainFor2 + diff2);
            if (curGainFor2 > maxGainFor2)
                maxGainFor2 = curGainFor2;
        }
        long res = Math.max(sum1 + maxGainFor1, sum2 + maxGainFor2);
        return (int)res;
    }
}