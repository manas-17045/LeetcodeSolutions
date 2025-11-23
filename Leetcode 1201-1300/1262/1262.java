// Leetcode 1262: Greatest Sum Divisible by Three
// https://leetcode.com/problems/greatest-sum-divisible-by-three/
// Solved on 23rd of November, 2025
class Solution {
    /**
     * Given an array nums of integers, return the maximum possible sum of elements of the array such that it is divisible by three.
     * @param nums The input array of integers.
     * @return The maximum sum of elements divisible by three.
     */
    public int maxSumDivThree(int[] nums) {
        int[] dp = new int[]{0, Integer.MIN_VALUE, Integer.MIN_VALUE};
        
        for (int num : nums) {
            int[] nextDp = dp.clone();
            for (int i = 0; i < 3; i++) {
                if (dp[i] != Integer.MIN_VALUE) {
                    int currentSum = dp[i] + num;
                    int remainder = currentSum % 3;
                    nextDp[remainder] = Math.max(nextDp[remainder], currentSum);
                }
            }
            dp = nextDp;
        }
        
        return dp[0];
    }
}