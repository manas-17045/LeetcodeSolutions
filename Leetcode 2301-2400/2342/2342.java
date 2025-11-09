// Leetcode 2342: Max SUm of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
// Solved on 9th of November, 2025
class Solution {
    /**
     * Finds the maximum sum of a pair of numbers from `nums` such that their digit sums are equal.
     *
     * @param nums An array of integers.
     * @return The maximum sum of such a pair, or -1 if no such pair exists.
     */
    public int maximumSum(int[] nums) {
        int[] bestVal = new int[82];
        for (int i = 0; i < bestVal.length; i++) bestVal[i] = -1;
        int maxSum = -1;
        for (int num : nums) {
            int s = digitSum(num);
            if (bestVal[s] != -1) {
                int cur = bestVal[s] + num;
                if (cur > maxSum) maxSum = cur;
            }
            if (num > bestVal[s]) bestVal[s] = num;
        }
        return maxSum;
    }
    private int digitSum(int x) {
        int s = 0;
        while (x > 0) {
            s += x % 10;
            x /= 10;
        }
        return s;
    }
}