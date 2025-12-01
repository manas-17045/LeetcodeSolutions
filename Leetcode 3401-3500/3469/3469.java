// Leetcode 3469: Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/
// Solved on 1st of December, 2025
class Solution {
    /**
     * Finds the minimum cost to remove all array elements.
     *
     * @param nums The input array of integers.
     * @return The minimum cost to remove all elements.
     */
    public int minCost(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];

        if (n % 2 == 1) {
            for (int j = 0; j < n; j++) {
                dp[j] = nums[j];
            }
        } else {
            for (int j = 0; j < n; j++) {
                dp[j] = Math.max(nums[j], nums[n - 1]);
            }
        }

        int startI = (n % 2 == 1) ? n - 2 : n - 3;

        for (int i = startI; i >= 1; i -= 2) {
            int keepI = dp[i];
            int keepIPlus1 = dp[i + 1];

            for (int j = 0; j < i; j++) {
                int op1 = Math.max(nums[j], nums[i]) + keepIPlus1;
                int op2 = Math.max(nums[j], nums[i + 1]) + keepI;
                int op3 = Math.max(nums[i], nums[i + 1]) + dp[j];

                dp[j] = Math.min(op1, Math.min(op2, op3));
            }
        }

        return dp[0];
    }
}