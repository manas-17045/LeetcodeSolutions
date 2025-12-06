// Leetcode 3748: Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/
// Solved on 6th of December, 2025
class Solution {
    /**
     * Counts the number of stable subarrays for each given query.
     * A subarray is stable if there is no index `i` such that `nums[i] > nums[i+1]`.
     * @param nums The input array of integers.
     * @param queries An array of queries, where each query `[l, r]` represents a range `[l, r]` (inclusive) in `nums`.
     * @return An array of long integers, where each element is the count of stable subarrays for the corresponding query.
     */
    public long[] countStableSubarrays(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] breaks = new int[n];
        int breakCount = 0;
        
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] > nums[i + 1]) {
                breaks[breakCount++] = i;
            }
        }

        long[] prefixSums = new long[breakCount + 1];
        for (int i = 0; i < breakCount - 1; i++) {
            long length = breaks[i + 1] - breaks[i];
            prefixSums[i + 1] = prefixSums[i] + (length * (length + 1) / 2);
        }

        long[] results = new long[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int l = queries[i][0];
            int r = queries[i][1];

            int u = lowerBound(breaks, breakCount, l);
            int v = lowerBound(breaks, breakCount, r) - 1;

            if (u > v) {
                long length = r - l + 1;
                results[i] = length * (length + 1) / 2;
            } else {
                long leftLength = breaks[u] - l + 1;
                long rightLength = r - breaks[v];
                long middleCost = prefixSums[v] - prefixSums[u];

                results[i] = (leftLength * (leftLength + 1) / 2) +
                             (rightLength * (rightLength + 1) / 2) +
                             middleCost;
            }
        }
        return results;
    }

    private int lowerBound(int[] arr, int size, int target) {
        int left = 0;
        int right = size;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}