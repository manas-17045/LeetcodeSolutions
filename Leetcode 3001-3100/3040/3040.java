// Leetcode 3040: Maximum Number of Operations With the Same Score II
// https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/
// Solved on 4th of January, 2026
class Solution {
    private int[][] memo;
    private int[] nums;

    /**
     * Calculates the maximum number of operations that can be performed on the array `nums`
     * such that each operation removes two elements with the same sum.
     * @param nums The input array of integers.
     * @return The maximum number of operations.
     */
    public int maxOperations(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        int maxOps = 0;

        memo = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j] = -1;
            }
        }
        maxOps = Math.max(maxOps, 1 + helper(2, n - 1, nums[0] + nums[1]));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j] = -1;
            }
        }
        maxOps = Math.max(maxOps, 1 + helper(0, n - 3, nums[n - 2] + nums[n - 1]));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j] = -1;
            }
        }
        maxOps = Math.max(maxOps, 1 + helper(1, n - 2, nums[0] + nums[n - 1]));

        return maxOps;
    }

    private int helper(int left, int right, int target) {
        if (left >= right) {
            return 0;
        }
        if (memo[left][right] != -1) {
            return memo[left][right];
        }

        int result = 0;

        if (nums[left] + nums[left + 1] == target) {
            result = Math.max(result, 1 + helper(left + 2, right, target));
        }

        if (nums[right - 1] + nums[right] == target) {
            result = Math.max(result, 1 + helper(left, right - 2, target));
        }

        if (nums[left] + nums[right] == target) {
            result = Math.max(result, 1 + helper(left + 1, right - 1, target));
        }

        memo[left][right] = result;
        return result;
    }
}