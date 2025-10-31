// Leetcode 3026: Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/
// Solved on 31st of October, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the maximum good subarray sum.
     * A subarray is considered "good" if the absolute difference between its first and last element is exactly `k`.
     * @param nums The input array of integers.
     * @param k The required absolute difference between the first and last elements of a good subarray.
     * @return The maximum good subarray sum, or 0 if no good subarray is found.
     */
    public long maximumSubarraySum(int[] nums, in k) {
        int n = nums.length;
        Map<Integer, Long> minPrefixSum = new HashMap<>();
        long currentPrefixSum = 0;
        long maxSum = Long.MIN_VALUE;
        boolean found = false;

        for (int j = 0; j < n; j++) {
            int currentValue = nums[j];
            long prefixBeforeCurrent = currentPrefixSum;
            currentPrefixSum += currentValue;

            int target1 = currentValue - k;
            int target2 = currentValue + k;

            if (minPrefixSum.containsKey(target1)) {
                long prefixSum = minPrefixSum.get(target1);
                long currentSum = currentPrefixSum - prefixSum;
                maxSum = Math.max(maxSum, currentSum);
                found = true;
            }

            if (minPrefixSum.containsKey(target2)) {
                long prefixSum = minPrefixSum.get(target2);
                long currentSum = currentPrefixSum - prefixSum;
                maxSum = Math.max(maxSum, currentSum);
                found = true;
            }

            if (!minPrefixSum.containsKey(currentValue) || prefixBeforeCurrent < minPrefixSum.get(currentValue)) {
                minPrefixSum.put(currentValue, prefixBeforeCurrent);
            }
        }

        return found ? maxSum : 0;
    }
}