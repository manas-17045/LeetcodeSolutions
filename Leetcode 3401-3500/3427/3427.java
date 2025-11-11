// Leetcode 3427: Sum of Variable Length Subarrays
// https://leetcode.com/problems/sum-of-variable-length-subarrays/
// Solved on 11th of November, 2025
class Solution {
    /**
     * Calculates the sum of variable-length subarrays.
     * For each element `nums[i]`, it sums the subarray from `max(0, i - nums[i])` to `i`.
     * @param nums The input array of integers.
     * @return The total sum of these variable-length subarrays.
     */
    public int subarraySum(int[] nums) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        long total = 0;
        for (int i = 0; i < n; i++) {
            int start = i - nums[i];
            if (start < 0) {
                start = 0;
            }
            total += prefix[i + 1] - prefix[start];
        }
        return (int) total;
    }
}