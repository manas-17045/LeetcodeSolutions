// Leetcode 3644: Maximum K to Sort a Permutation
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
// Solved on 23rd of October, 2026
class Solution {
    /**
     * Computes the maximum non-negative integer k such that the given permutation
     * can be sorted in non-decreasing order using swaps where the bitwise AND of
     * the two elements equals k.
     *
     * @param nums the permutation array of integers from 0 to n - 1
     * @return the maximum integer k, or 0 if the array is already sorted
     */
    public int sortPermutation(int[] nums) {
        int maxK = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                if (maxK == -1) {
                    maxK = nums[i];
                } else {
                    maxK &= nums[i];
                }
            }
        }
        return maxK == -1 ? 0 : maxK;
    }
}