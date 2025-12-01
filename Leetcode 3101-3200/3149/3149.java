// Leetcode 3149: Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/
// Solved on 1st of December, 2025
class Solution {
    private int[] nums;
    private int[][] memo;
    private int n;

    /**
     * Finds the permutation of `nums` that minimizes the total cost.
     * The cost is defined as the sum of absolute differences between adjacent elements in the permutation,
     * plus the absolute difference between the last and first elements.
     * @param nums The input array of integers.
     * @return An array representing the permutation with the minimum cost.
     */
    public int[] findPermutation(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        this.memo = new int[1 << n][n];
        
        for (int i = 0; i < (1 << n); i++) {
            for (int j = 0; j < n; j++) {
                memo[i][j] = -1;
            }
        }

        solve(1, 0);

        int[] res = new int[n];
        int mask = 1;
        int prev = 0;
        res[0] = 0;

        for (int i = 1; i < n; i++) {
            for (int next = 0; next < n; next++) {
                if ((mask & (1 << next)) == 0) {
                    int score = Math.abs(prev - nums[next]) + solve(mask | (1 << next), next);
                    if (score == memo[mask][prev]) {
                        res[i] = next;
                        mask |= (1 << next);
                        prev = next;
                        break;
                    }
                }
            }
        }
        return res;
    }

    private int solve(int mask, int prev) {
        if (mask == (1 << n) - 1) {
            return Math.abs(prev - nums[0]);
        }
        if (memo[mask][prev] != -1) {
            return memo[mask][prev];
        }

        int minScore = Integer.MAX_VALUE;
        for (int next = 0; next < n; next++) {
            if ((mask & (1 << next)) == 0) {
                int score = Math.abs(prev - nums[next]) + solve(mask | (1 << next), next);
                if (score < minScore) {
                    minScore = score;
                }
            }
        }
        return memo[mask][prev] = minScore;
    }
}