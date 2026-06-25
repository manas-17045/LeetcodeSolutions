// Leetcode 3956: Maximum Sum of M Non-Overlapping Subarrays I
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/
// Solved on 25th of June, 2026
class Solution {
    /**
     * Computes the maximum sum of m non-overlapping subarrays of length between l and r.
     * @param nums The input array.
     * @param m The number of subarrays.
     * @param l The minimum length of a subarray.
     * @param r The maximum length of a subarray.
     * @return The maximum sum of m non-overlapping subarrays.
     */
    public long maximumSum(int[] nums, int m, int l, int r) {
        int n = nums.length;
        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        long minVal = -10000000000000000L;
        long[] prevDp = new long[n + 1];
        long finalMaxSum = minVal;
        for (int c = 1; c <= m; c++) {
            long[] currDp = new long[n + 1];
            for (int i = 0; i <= n; i++) {
                currDp[i] = minVal;
            }
            int[] deque = new int[n + 1];
            int head = 0;
            int tail = 0;
            for (int i = 1; i <= n; i++) {
                int right = i - l;
                int left = i - r;
                if (right >= 0 && prevDp[right] != minVal) {
                    long val = prevDp[right] - prefixSum[right];
                    while (head < tail && prevDp[deque[tail - 1]] - prefixSum[deque[tail - 1]] <= val) {
                        tail--;
                    }
                    deque[tail++] = right;
                }
                while (head < tail && deque[head] < left) {
                    head++;
                }
                currDp[i] = currDp[i - 1];
                if (head < tail) {
                    int bestJ = deque[head];
                    long sum = prefixSum[i] + prevDp[bestJ] - prefixSum[bestJ];
                    if (sum > currDp[i]) {
                        currDp[i] = sum;
                    }
                }
            }
            if (currDp[n] > finalMaxSum) {
                finalMaxSum = currDp[n];
            }
            prevDp = currDp;
        }
        return finalMaxSum;
    }
}