// Leetcode 3366: Minimum Array Sum
// https://leetcode.com/problems/minimum-array-sum/
// Solved on 1st of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum possible sum of the array elements after applying at most `op1` operations of type 1 and at most `op2` operations of type 2.
     * An operation of type 1 divides an element `x` by 2 (integer division, rounding up).
     * An operation of type 2 subtracts `k` from an element `x` (only if `x >= k`).
     * @param nums The input array of integers.
     * @param k The value to subtract in operation type 2.
     * @param op1 The maximum number of type 1 operations allowed.
     * @param op2 The maximum number of type 2 operations allowed.
     * @return The minimum possible sum of the array.
     */
    public int minArraySum(int[] nums, int k, int op1, int op2) {
        int[][] dp = new int[op1 + 1][op2 + 1];
        for (int[] row : dp) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        dp[0][0] = 0;

        for (int num : nums) {
            for (int i = op1; i >= 0; i--) {
                for (int j = op2; j >= 0; j--) {
                    int minVal = Integer.MAX_VALUE;

                    if (dp[i][j] != Integer.MAX_VALUE) {
                        minVal = dp[i][j] + num;
                    }

                    if (i > 0 && dp[i - 1][j] != Integer.MAX_VALUE) {
                        minVal = Math.min(minVal, dp[i - 1][j] + (num + 1) / 2);
                    }

                    if (j > 0 && num >= k && dp[i][j - 1] != Integer.MAX_VALUE) {
                        minVal = Math.min(minVal, dp[i][j - 1] + num - k);
                    }

                    if (i > 0 && j > 0 && dp[i - 1][j - 1] != Integer.MAX_VALUE) {
                        int afterOp1 = (num + 1) / 2;
                        if (afterOp1 >= k) {
                            minVal = Math.min(minVal, dp[i - 1][j - 1] + afterOp1 - k);
                        }
                        if (num >= k) {
                            int afterOp2 = num - k;
                            minVal = Math.min(minVal, dp[i - 1][j - 1] + (afterOp2 + 1) / 2);
                        }
                    }

                    dp[i][j] = minVal;
                }
            }
        }

        int result = Integer.MAX_VALUE;
        for (int i = 0; i <= op1; i++) {
            for (int j = 0; j <= op2; j++) {
                result = Math.min(result, dp[i][j]);
            }
        }
        return result;
    }
}