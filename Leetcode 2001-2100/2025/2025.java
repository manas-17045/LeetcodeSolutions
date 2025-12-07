// Leetcode 2025: Maximum Number of Ways to Partition an Array
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/
// Solved on 7th of December, 2025
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Calculates the maximum number of ways to partition an array such that the sum of the left part equals the sum of the right part.
     * A single element can be changed to `k` to achieve this.
     *
     * @param nums The input array of integers.
     * @param k The value to which an element can be changed.
     * @return The maximum number of ways to partition the array.
     */
    public int waysToPartition(int[] nums, int k) {
        int n = nums.length;
        long[] prefixSum = new long[n];
        prefixSum[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = prefixSum[i - 1] + nums[i];
        }

        long totalSum = prefixSum[n - 1];
        Map<Long, Integer> rightMap = new HashMap<>();
        for (int i = 0; i < n - 1; i++) {
            rightMap.put(prefixSum[i], rightMap.getOrDefault(prefixSum[i], 0) + 1);
        }

        int maxWays = 0;
        if (totalSum % 2 == 0) {
            maxWays = rightMap.getOrDefault(totalSum / 2, 0);
        }

        Map<Long, Integer> leftMap = new HashMap<>();
        for (int i = 0; i < n; i++) {
            long diff = k - nums[i];
            long newSum = totalSum + diff;

            if (newSum % 2 == 0) {
                long target = newSum / 2;
                int ways = leftMap.getOrDefault(target, 0) + rightMap.getOrDefault(target - diff, 0);
                maxWays = Math.max(maxWays, ways);
            }

            if (i < n - 1) {
                long val = prefixSum[i];
                rightMap.put(val, rightMap.get(val) - 1);
                leftMap.put(val, leftMap.getOrDefault(val, 0) + 1);
            }
        }

        return maxWays;
    }
}