// Leetcode 3903: Smallest Stable Index I
// https://leetcode.com/problems/smallest-stable-index-i/
// Solved on 28th of April, 2026
class Solution {
    /**
     * Finds the smallest index i such that the difference between the maximum element 
     * in the prefix nums[0...i] and the minimum element in the suffix nums[i...n-1] is at most k.
     * @param nums The input array of integers.
     * @param k The maximum allowed difference threshold.
     * @return The smallest stable index i, or -1 if no such index exists.
     */
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        int[] suffixMin = new int[n];
        suffixMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.min(nums[i], suffixMin[i + 1]);
        }
        int prefixMax = nums[0];
        for (int i = 0; i < n; i++) {
            prefixMax = Math.max(prefixMax, nums[i]);
            if (prefixMax - suffixMin[i] <= k) {
                return i;
            }
        }
        return -1;
    }
}