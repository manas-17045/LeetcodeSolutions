// Leetcode 3599: Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Partitions the array `nums` into `k` non-empty subarrays to minimize the maximum XOR sum of any subarray.
     * @param nums The input integer array.
     * @param k The number of partitions.
     * @return The minimum possible maximum XOR sum among the `k` subarrays.
     */
    public int minXor(int[] nums, int k) {
        int n = nums.length;
        int[] prefixXor = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixXor[i + 1] = prefixXor[i] ^ nums[i];
        }

        int[][] dp = new int[k + 1][n + 1];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }

        dp[0][0] = 0;

        for (int i = 1; i <= k; i++) {
            for (int j = i; j <= n; j++) {
                for (int p = i - 1; p < j; p++) {
                    int currentXor = prefixXor[j] ^ prefixXor[p];
                    int maxVal = Math.max(dp[i - 1][p], currentXor);
                    dp[i][j] = Math.min(dp[i][j], maxVal);
                }
            }
        }

        return dp[k][n];
    }
}