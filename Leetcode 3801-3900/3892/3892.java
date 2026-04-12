// Leetcode 3892: Minimum Operations to Achieve At Least K Peaks
// https://leeetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/
// Solved on 12th of April, 2026
class Solution {
    /**
     * Calculates the minimum operations to achieve at least k peaks in a circular array.
     *
     * @param nums The input array of integers.
     * @param k The target number of peaks to achieve.
     * @return The minimum number of operations required, or -1 if impossible.
     */
    public int minOperations(int[] nums, int k) {
        int n = nums.length;
        if (k == 0) {
            return 0;
        }
        if (k > n / 2) {
            return -1;
        }
        int[] costs = new int[n];
        for (int i = 0; i < n; i++) {
            int prev = nums[(i - 1 + n) % n];
            int next = nums[(i + 1) % n];
            int maxNeighbor = Math.max(prev, next);
            costs[i] = Math.max(0, maxNeighbor + 1 - nums[i]);
        }
        int ans1 = solveLinear(costs, 1, n - 1, k);
        int ans2 = costs[0] + solveLinear(costs, 2, n - 2, k - 1);
        return Math.min(ans1, ans2);
    }

    private int solveLinear(int[] costs, int start, int end, int targetK) {
        if (targetK == 0) {
            return 0;
        }
        if (end - start + 1 < targetK * 2 - 1) {
            return 1_000_000_000;
        }
        int[] prev2 = new int[targetK + 1];
        int[] prev1 = new int[targetK + 1];
        int[] curr = new int[targetK + 1];
        for (int j = 1; j <= targetK; j++) {
            prev2[j] = 1_000_000_000;
            prev1[j] = 1_000_000_000;
        }
        prev2[0] = 0;
        prev1[0] = 0;
        for (int i = start; i <= end; i++) {
            curr[0] = 0;
            for (int j = 1; j <= targetK; j++) {
                curr[j] = prev1[j];
                if (prev2[j - 1] != 1_000_000_000) {
                    curr[j] = Math.min(curr[j], prev2[j - 1] + costs[i]);
                }
            }
            int[] temp = prev2;
            prev2 = prev1;
            prev1 = curr;
            curr = temp;
        }
        return prev1[targetK];
    }
}