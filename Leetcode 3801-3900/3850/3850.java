// Leetcode 3850: Count Sequences to K
// https://leetcode.com/problems/count-sequences-to-k/
// Solved on 24th of February, 2026
class Solution {
    int[] nums;
    int targetP2, targetP3, targetP5;
    int[] remP2, remP3, remP5;
    int maxP2, maxP3, maxP5;
    int d1, d2, d3;
    int[] memo;

    /**
     * Counts the number of ways to form sequences from the given numbers such that 
     * the product of chosen elements matches the prime factorization of k.
     * @param nums An array of integers containing factors of 2, 3, 5, or 6.
     * @param k The target product represented as a long.
     * @return The total number of valid sequences that satisfy the condition.
     */
    public int countSequences(int[] nums, long k) {
        long temp = k;
        targetP2 = 0;
        targetP3 = 0;
        targetP5 = 0;
        
        while (temp > 0 && temp % 2 == 0) {
            targetP2++;
            temp /= 2;
        }
        while (temp > 0 && temp % 3 == 0) {
            targetP3++;
            temp /= 3;
        }
        while (temp > 0 && temp % 5 == 0) {
            targetP5++;
            temp /= 5;
        }
        if (temp != 1) {
            return 0;
        }
        
        int n = nums.length;
        this.nums = nums;
        remP2 = new int[n + 1];
        remP3 = new int[n + 1];
        remP5 = new int[n + 1];
        
        for (int i = n - 1; i >= 0; i--) {
            int dv2 = 0, dv3 = 0, dv5 = 0;
            if (nums[i] == 2 || nums[i] == 6) {
                dv2 = 1;
            } else if (nums[i] == 4) {
                dv2 = 2;
            }
            if (nums[i] == 3 || nums[i] == 6) {
                dv3 = 1;
            }
            if (nums[i] == 5) {
                dv5 = 1;
            }
            remP2[i] = remP2[i + 1] + dv2;
            remP3[i] = remP3[i + 1] + dv3;
            remP5[i] = remP5[i + 1] + dv5;
        }
        
        maxP2 = remP2[0];
        maxP3 = remP3[0];
        maxP5 = remP5[0];
        
        if (targetP2 > maxP2 || targetP3 > maxP3 || targetP5 > maxP5) {
            return 0;
        }
        
        d1 = 2 * maxP2 + 1;
        d2 = 2 * maxP3 + 1;
        d3 = 2 * maxP5 + 1;
        memo = new int[n * d1 * d2 * d3];
        for (int i = 0; i < memo.length; i++) {
            memo[i] = -1;
        }
        
        return solve(0, 0, 0, 0);
    }

    int solve(int i, int p2, int p3, int p5) {
        if (Math.abs(targetP2 - p2) > remP2[i]) {
            return 0;
        }
        if (Math.abs(targetP3 - p3) > remP3[i]) {
            return 0;
        }
        if (Math.abs(targetP5 - p5) > remP5[i]) {
            return 0;
        }
        
        if (i == nums.length) {
            return 1;
        }
        
        int idx = i * (d1 * d2 * d3) + (p2 + maxP2) * (d2 * d3) + (p3 + maxP3) * d3 + (p5 + maxP5);
        if (memo[idx] != -1) {
            return memo[idx];
        }
        
        int num = nums[i];
        int dv2 = 0, dv3 = 0, dv5 = 0;
        if (num == 2 || num == 6) {
            dv2 = 1;
        } else if (num == 4) {
            dv2 = 2;
        }
        if (num == 3 || num == 6) {
            dv3 = 1;
        }
        if (num == 5) {
            dv5 = 1;
        }
        
        int ways = 0;
        ways += solve(i + 1, p2 + dv2, p3 + dv3, p5 + dv5);
        ways += solve(i + 1, p2 - dv2, p3 - dv3, p5 - dv5);
        ways += solve(i + 1, p2, p3, p5);
        
        memo[idx] = ways;
        return ways;
    }
}