// Leetcode 1340: Jump Game V
// https://leetcode.com/problems/jump-game-v/
// Solved on 24th of May, 2026
class Solution {
    /**
     * Calculates the maximum number of indices you can visit starting from any index.
     * 
     * @param arr The array of heights.
     * @param d The maximum jump distance.
     * @return The maximum number of indices that can be visited.
     */
    public int maxJumps(int[] arr, int d) {
        int n = arr.length;
        int[] dp = new int[n];
        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            ans = Math.max(ans, dfs(arr, d, i, dp));
        }
        
        return ans;
    }
    
    private int dfs(int[] arr, int d, int i, int[] dp) {
        if (dp[i] != 0) {
            return dp[i];
        }
        
        int max = 1;
        int n = arr.length;
        
        for (int j = i + 1; j <= Math.min(n - 1, i + d); j++) {
            if (arr[j] >= arr[i]) {
                break;
            }
            max = Math.max(max, 1 + dfs(arr, d, j, dp));
        }
        
        for (int j = i - 1; j >= Math.max(0, i - d); j--) {
            if (arr[j] >= arr[i]) {
                break;
            }
            max = Math.max(max, 1 + dfs(arr, d, j, dp));
        }
        
        dp[i] = max;
        return max;
    }
}