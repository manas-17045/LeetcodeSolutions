// Leetcode 2919: Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/
// Solved on 5th of November, 2025
class Solution {
    /**
     * Calculates the minimum increment operations to make the array beautiful.
     * An array is beautiful if for every subarray of size 3, at least one element is greater than or equal to k.
     * @param nums The input array of integers.
     * @param k The minimum value an element must have to satisfy the beauty condition.
     * @return The minimum number of increment operations.
     */
    public long minIncrementOperations(int[] nums, int k) {
        int n = nums.length;
        long INF = 1L << 60;
        long[] dp = new long[3];
        boolean inGroup = false;
        long result = 0L;
        for (int i = 0; i < n; i++) {
            if (nums[i] < k) {
                long cost = (long)k - nums[i];
                if (!inGroup) {
                    inGroup = true;
                    dp[0] = 0L;
                    dp[1] = INF;
                    dp[2] = INF;
                }
                long minPrev = dp[0];
                if (dp[1] < minPrev) {
                    minPrev = dp[1];
                }
                if (dp[2] < minPrev) {
                    minPrev = dp[2];
                }
                long[] next = new long[3];
                next[0] = minPrev + cost;
                next[1] = dp[0] < INF ? dp[0] : INF;
                next[2] = dp[1] < INF ? dp[1] : INF;
                dp = next;
            } else {
                if (inGroup) {
                    long add = dp[0];
                    if (dp[1] < add) {
                        add = dp[1];
                    }
                    if (dp[2] < add) {
                        add = dp[2];
                    }
                    result += add;
                    inGroup = false;
                }
            }
        }
        if (inGroup) {
            long add = dp[0];
            if (dp[1] < add) {
                add = dp[1];
            }
            if (dp[2] < add) {
                add = dp[2];
            }
            result += add;
        }
        return result;
    }
}