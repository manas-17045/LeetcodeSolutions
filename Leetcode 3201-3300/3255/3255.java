// Leetcode 3255: Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/
// Solved on 31st of October, 2025
class Solution {
    /**
     * Finds the "power" of k-size subarrays.
     * @param nums The input array of integers.
     * @param k The size of the subarrays.
     * @return An array where each element `results[i]` is the last element of the k-size subarray starting at `i`
     *         if it consists of `k` consecutive increasing numbers, otherwise -1.
     */
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;
        int[] results = new int[n - k + 1];
        int consecutiveCount = 0;

        for (int i = 0; i < n; i++) {
            if (i > 0 && nums[i - 1] + 1 == nums[i]) {
                consecutiveCount++;
            } else {
                consecutiveCount = 1;
            }

            int resultIndex = i - k + 1;
            if (resultIndex >= 0) {
                if (consecutiveCount >= k) {
                    results[resultIndex] = nums[i];
                } else {
                    results[resultIndex] = -1;
                }
            }
        }
        return results;
    }
}