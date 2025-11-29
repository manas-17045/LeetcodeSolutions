// Leetcode 3326: Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/
// Solved on 29th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of division operations to make the array non-decreasing.
     * An operation consists of replacing a number `x` with its smallest prime factor `spf[x]`.
     * @param nums The input array of integers.
     * @return The minimum number of operations, or -1 if it's impossible to make the array non-decreasing.
     */
    public int minOperations(int[] nums) {
        int n = nums.length;
        int maxVal = 0;
        for (int x : nums) {
            maxVal = Math.max(maxVal, x);
        }

        int[] spf = new int[maxVal + 1];
        for (int i = 0; i <= maxVal; i++) {
            spf[i] = i;
        }

        for (int i = 2; i * i <= maxVal; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxVal; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }

        int count = 0;
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] > nums[i + 1]) {
                int div = spf[nums[i]];
                if (nums[i] == div) {
                    return -1;
                }
                nums[i] = div;
                count++;
                if (nums[i] > nums[i + 1]) {
                    return -1;
                }
            }
        }
        return count;
    }
}