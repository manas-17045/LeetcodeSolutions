// Leetcode 3428: Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/
// Solved on 31st of December, 2025
import java.util.Arrays;

class Solution {
    long[] fact;
    long[] invFact;
    long mod = 1000000007;

    /**
     * Calculates the sum of maximum and minimum sums of all subsequences of `nums` with at most size `k`.
     *
     * @param nums The input array of integers.
     * @param k The maximum size of subsequences to consider.
     * @return The total sum of maximum and minimum sums modulo 10^9 + 7.
     */
    public int minMaxSums(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        
        fact = new long[n + 1];
        invFact = new long[n + 1];
        fact[0] = 1;
        invFact[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            fact[i] = (fact[i - 1] * i) % mod;
        }
        
        invFact[n] = power(fact[n], mod - 2);
        for (int i = n - 1; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % mod;
        }

        long[] s = new long[n];
        s[0] = 1;
        for (int i = 1; i < n; i++) {
            long val = (s[i - 1] * 2) % mod;
            if (i - 1 >= k - 1) {
                val = (val - nCr(i - 1, k - 1) + mod) % mod;
            }
            s[i] = val;
        }

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long ways = (s[i] + s[n - 1 - i]) % mod;
            ans = (ans + nums[i] * ways) % mod;
        }

        return (int) ans;
    }

    private long nCr(int n, int r) {
        if (r < 0 || r > n) {
            return 0;
        }
        return fact[n] * invFact[r] % mod * invFact[n - r] % mod;
    }

    private long power(long base, long exp) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return res;
    }
}