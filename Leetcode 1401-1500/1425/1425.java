// Leetcode 1425: Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/
// Solved on 12th of November, 2025
import java.util.ArrayDeque;

class Solution {
    /**
     * Calculates the maximum sum of a non-empty subsequence such that for every two consecutive elements
     * in the subsequence, `nums[i]` and `nums[j]` (with `i < j`), `j - i <= k`.
     *
     * @param nums The input array of integers.
     * @param k The maximum allowed difference between indices of consecutive elements in the subsequence.
     * @return The maximum sum of a constrained subsequence.
     */
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        int res = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            while (!dq.isEmpty() && dq.peekFirst() < i - k) {
                dq.pollFirst();
            }
            int best = dq.isEmpty() ? 0 : Math.max(0, dp[dq.peekFirst()]);
            dp[i] = nums[i] + best;
            if (dp[i] > res) {
                res = dp[i];
            }
            while (!dq.isEmpty() && dp[dq.peekLast()] <= dp[i]) {
                dq.pollLast();
            }
            dq.offerLast(i);
        }
        return res;
    }
}