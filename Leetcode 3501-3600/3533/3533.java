// Leetcode 3533: Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/
// Solved on 25th of November, 2025
import java.util.Arrays;

class Solution {
    /**
     * Finds a permutation of the input array `nums` such that the concatenated number formed by this permutation is divisible by `k`.
     *
     * @param nums An array of integers.
     * @param k The divisor.
     * @return An array representing the permutation if found, otherwise an empty array.
     */
    public int[] concatenatedDivisibility(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int[] power = new int[n];
        int[] modVal = new int[n];

        for (int i = 0; i < n; i++) {
            int temp = nums[i];
            int len = 0;
            while (temp > 0) {
                len++;
                temp /= 10;
            }
            int p = 1;
            for (int j = 0; j < len; j++) {
                p = (p * 10) % k;
            }
            power[i] = p;
            modVal[i] = nums[i] % k;
        }

        byte[][] memo = new byte[1 << n][k];
        int[] result = new int[n];

        if (dfs(0, 0, 0, nums, k, power, modVal, memo, result)) {
            return result;
        }

        return new int[0];
    }

    private boolean dfs(int mask, int rem, int idx, int[] nums, int k, int[] power, int[] modVal, byte[][] memo, int[] result) {
        if (idx == nums.length) {
            return rem == 0;
        }
        if (memo[mask][rem] != 0) {
            return memo[mask][rem] == 1;
        }

        for (int i = 0; i < nums.length; i++) {
            if ((mask & (1 << i)) == 0) {
                if (i > 0 && nums[i] == nums[i - 1] && (mask & (1 << (i - 1))) == 0) {
                    continue;
                }

                int nextRem = (rem * power[i] + modVal[i]) % k;
                result[idx] = nums[i];

                if (dfs(mask | (1 << i), nextRem, idx + 1, nums, k, power, modVal, memo, result)) {
                    memo[mask][rem] = 1;
                    return true;
                }
            }
        }

        memo[mask][rem] = 2;
        return false;
    }
}