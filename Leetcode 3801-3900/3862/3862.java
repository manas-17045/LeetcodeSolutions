// Leetcode 3862: Find the Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/
// Solved on 10th of March, 2026
class Solution {
    /**
     * Finds the smallest index i such that the sum of elements to the left of i 
     * is equal to the product of elements to the right of i.
     *
     * @param nums An array of integers.
     * @return The smallest balanced index, or -1 if no such index exists.
     */
    public int smallestBalancedIndex(int[] nums) {
        int n = nums.length;
        long[] rightProd = new long[n];
        rightProd[n - 1] = 1;
        long limit = 1000000000000000000L;
        for (int i = n - 2; i >= 0; i--) {
            long prev = rightPrev[i + 1];
            long val = nums[i + 1];
            if (prev > limit / val) {
                rightProd[i] = limit + 1;
            } else {
                rightProd[i] = prev * val;
            }
        }
        long leftSum = 0;
        for (int i = 0; i < n; i++) {
            if (leftSum == rightprod[i]) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}