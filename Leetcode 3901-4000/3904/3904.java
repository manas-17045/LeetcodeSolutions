// Leetcode 3904: Smallest Stable Index II
// https://leetcode.com/problems/smallest-stable-index-ii/
// Solved on 28th of April, 2026
class Solution {
    /**
     * Finds the smallest index i such that the difference between the maximum 
     * element in the prefix nums[0...i] and the minimum element in the 
     * suffix nums[i...n-1] is at most k.
     *
     * @param nums An array of integers.
     * @param k The maximum allowed difference.
     * @return The smallest stable index i, or -1 if no such index exists.
     */
    public int firstStableIndex(int[] nums, int k) {
        int n = nums.length;
        int[] suffMin = new int[n];
        suffMin[n - 1] = nums[n - 1];
        
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.min(nums[i], suffMin[i + 1]);
        }
        
        int prefMax = nums[0];
        for (int i = 0; i < n; i++) {
            prefMax = Math.max(prefMax, nums[i]);
            if (prefMax - suffMin[i] <= k) {
                return i;
            }
        }
        
        return -1;
    }
}