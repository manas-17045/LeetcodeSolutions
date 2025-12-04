// Leetcode 3351: Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/
// Solved on 4th of November, 2025
class Solution {
    /**
     * Calculates the sum of all "good" subsequences. A subsequence is considered "good"
     * if the absolute difference between any two adjacent elements in the subsequence is at most 1.
     * @param nums The input array of integers.
     * @return The total sum of all good subsequences, modulo 10^9 + 7.
     */
    public int sumOfGoodSubsequences(int[] nums) {
        long[] count = new long[100005];
        long[] sum = new long[100005];
        long mod = 1000000007;
        long res = 0;

        for (int num : nums) {
            long c = 1;
            long s = num;

            if (num > 0) {
                c = (c + count[num - 1]) % mod;
                s = (s + sum[num - 1] + count[num - 1] * num) % mod;
            }

            if (num + 1 < 100005) {
                c = (c + count[num + 1]) % mod;
                s = (s + sum[num + 1] + count[num + 1] * num) % mod;
            }

            count[num] = (count[num] + c) % mod;
            sum[num] = (sum[num] + s) % mod;
            res = (res + s) % mod;
        }

        return (int) res;
    }
}