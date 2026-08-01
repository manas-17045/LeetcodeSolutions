// Leetcode 486: Predict the Winner
// https://leetcode.com/problems/predict-the-winner/
// Solved on 1st of August, 2026
class Solution {
    /**
     * Determines if the first player can win in the given array.
     * 
     * @param nums The array of integers.
     * @return True if the first player can win, False otherwise.
     */
    public boolean predictTheWinner(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = nums[i];
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                dp[j] = Math.max(nums[i] - dp[j], nums[j] - dp[j - 1]);
            }
        }
        return dp[n - 1] >= 0;
    }
}