// Leetcode 2654: Minimum Number of Operations to make All Array Elements Equal to 1
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/
// Solved on 21st of October, 2025
class Solution {
    
    /**
     * Calculates the minimum number of operations to make all array elements equal to 1.
     * An operation consists of replacing two adjacent elements x and y with their greatest common divisor (gcd(x, y)).
     *
     * @param nums The input array of integers.
     * @return The minimum number of operations, or -1 if it's impossible to make all elements 1.
     */
    public int minOperations(int[] nums) {
        int n = nums.length;
        int ones = 0;
        for (int x : nums) {
            if (x == 1)
                ones++;
        }
        if (ones > 0) {
            return n - ones;
        }

        int bestLen = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int g = 0;
            for (int j = i; j < n; ++j) {
                g = gcd(g, nums[j]);
                if (g == 1) {
                    bestLen = Math.min(bestLen, j - i + 1);
                    break;
                }
            }
        }

        if (bestLen == Integer.MAX_VALUE) {
            return -1;
        }

        return n + bestLen - 2;

    }

    private int gcd(int a, int b) {
        if (a == 0) {
            return b;
        }
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}