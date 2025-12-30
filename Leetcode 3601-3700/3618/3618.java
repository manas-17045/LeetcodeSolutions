// Leetcode 3618: Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Given an integer array nums, return the absolute difference between the sum of elements at prime indices and the sum of elements at composite indices.
     * @param nums The input integer array.
     * @return The absolute difference between the sum of elements at prime indices and the sum of elements at composite indices.
     */
    public long splitArray(int[] nums) {
        int n = nums.length;
        boolean[] isComposite = new boolean[n];

        if (n > 0) {
            isComposite[0] = true;
        }
        if (n > 1) {
            isComposite[1] = true;
        }

        for (int i = 2; i * i < n; i++) {
            if (!isComposite[i]) {
                for (int j = i * i; j < n; j += i) {
                    isComposite[j] = true;
                }
            }
        }

        long sumA = 0;
        long sumB = 0;

        for (int i = 0; i < n; i++) {
            if (!isComposite[i]) {
                sumA += nums[i];
            } else {
                sumB += nums[i];
            }
        }

        return Math.abs(sumA - sumB);
    }
}