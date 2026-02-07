// Leetcode 3826: Minimum Partition Score
// https://leetcode.com/problems/minimum-partition-score/
// Solved on 7th of February, 2026
class Solution {
    /**
     * Calculates the minimum partition score of an array divided into k subarrays.
     * 
     * @param nums The input integer array to be partitioned.
     * @param k The number of subarrays to partition the array into.
     * @return The minimum possible total score after partitioning.
     */
    public long minPartitionScore(int[] nums, int k) {
        int n = nums.length;
        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }

        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = getScore(prefixSum[i]);
        }

        for (int i = 2; i <= k; i++) {
            long[] nextDp = new long[n + 1];
            compute(dp, nextDp, prefixSum, i, n, i - 1, n - 1);
            dp = nextDp;
        }

        return dp[n];
    }

    private void compute(long[] prevDp, long[] nextDp, long[] prefixSum, int left, int right, int optL, int optR) {
        if (left > right) {
            return;
        }

        int mid = left + (right - left) / 2;
        long minScore = Long.MAX_VALUE;
        int bestSplit = -1;

        int limit = Math.min(mid - 1, optR);

        for (int i = optL; i <= limit; i++) {
            long score = prevDp[i] + getScore(prefixSum[mid] - prefixSum[i]);
            if (score < minScore) {
                minScore = score;
                bestSplit = i;
            }
        }

        nextDp[mid] = minScore;

        compute(prevDp, nextDp, prefixSum, left, mid - 1, optL, bestSplit);
        compute(prevDp, nextDp, prefixSum, mid + 1, right, bestSplit, optR);
    }

    private long getScore(long sum) {
        return sum * (sum + 1) / 2;
    }
}