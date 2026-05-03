// Leetcode 3909: Compare Sums of Bitonic Parts
// https://leetcode.com/problems/compare-sums-of-bitonic-parts/
// Solved on 3rd of May, 2026
class Solution {
    /**
     * Compares the sum of the increasing part and the decreasing part of a bitonic array.
     * 
     * @param nums An array of integers representing a bitonic sequence.
     * @return 0 if left sum > right sum, 1 if right sum > left sum, and -1 if they are equal.
     */
    public int compareBitonicSums(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        int peakIndex = left;
        long leftSum = 0;
        long rightSum = 0;
        for (int i = 0; i <= peakIndex; i++) {
            leftSum += nums[i];
        }
        for (int i = peakIndex; i < nums.length; i++) {
            rightSum += nums[i];
        }
        if (leftSum > rightSum) {
            return 0;
        } else if (rightSum > leftSum) {
            return 1;
        } else {
            return -1;
        }
    }
}