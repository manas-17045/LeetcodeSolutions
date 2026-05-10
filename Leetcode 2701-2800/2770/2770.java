// Leetcode 2770: Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
// Solved on 10th of May, 2026
class Solution {
    /**
     * Calculates the maximum number of jumps to reach the last index of the array.
     * 
     * @param nums An array of integers representing the values at each index.
     * @param target An integer representing the maximum absolute difference allowed for a jump.
     * @return The maximum number of jumps to reach index n - 1, or -1 if unreachable.
     */
    public int maximumJumps(int[] nums, int target) {
        int n = nums.length;
        int[] dp = new int[n];
        
        for (int i = 0; i < n; i++) {
            dp[i] = -1;
        }
        
        dp[0] = 0;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] != -1) {
                    int diff = nums[i] - nums[j];
                    if (diff >= -target && diff <= target) {
                        dp[i] = Math.max(dp[i], dp[j] + 1);
                    }
                }
            }
        }
        
        return dp[n - 1];
    }
}