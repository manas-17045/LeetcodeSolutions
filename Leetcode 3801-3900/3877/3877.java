// Leetcode 3877: Minimum Removals to Achieve Target XOR
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/
// Solved on 29th of March, 2026
class Solution {
    /**
     * Calculates the minimum number of elements to remove from the array to achieve a target XOR sum.
     * 
     * @param nums An array of integers.
     * @param target The desired XOR sum of the remaining elements.
     * @return The minimum number of removals required, or -1 if the target cannot be achieved.
     */
    public int minRemovals(int[] nums, int target) {
        int maxVal = 16384;
        int[] dp = new int[maxVal];
        for (int i = 0; i < maxVal; i++) {
            dp[i] = -1;
        }
        dp[0] = 0;
        
        for (int num : nums) {
            int[] nextDp = new int[maxVal];
            for (int i = 0; i < maxVal; i++) {
                nextDp[i] = dp[i];
            }
            for (int i = 0; i < maxVal; i++) {
                if (dp[i] != -1) {
                    int nextXor = i ^ num;
                    if (dp[i] + 1 > nextDp[nextXor]) {
                        nextDp[nextXor] = dp[i] + 1;
                    }
                }
            }
            dp = nextDp;
        }
        
        if (target >= maxVal || dp[target] == -1) {
            return -1;
        }
        
        return nums.length - dp[target];
    }
}