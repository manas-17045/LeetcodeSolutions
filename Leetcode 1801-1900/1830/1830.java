// Leetcode 1830: Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/
// Solved on 4th of December, 2025
class Solution {
    private final int MOD = 1_000_000_007;

    /**
     * Calculates the minimum number of operations to make the given string sorted lexicographically.
     *
     * @param s The input string.
     * @return The minimum number of operations modulo 1,000,000,007.
     */
    public int makeStringSorted(String s) {
        int n = s.length();
        long[] fact = new long[n + 1];
        fact[0] = 1;
        for (int i = 1; i <= n; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        long denom = 1;
        for (int cnt : count) {
            denom = (denom * fact[cnt]) % MOD;
        }

        long denomInv = power(denom, MOD - 2);
        long ans = 0;

        for (int i = 0; i < n; i++) {
            int charIndex = s.charAt(i) - 'a';
            long smallerCount = 0;
            for (int j = 0; j < charIndex; j++) {
                smallerCount += count[j];
            }

            long ways = (fact[n - 1 - i] * denomInv) % MOD;
            ways = (ways * smallerCount) % MOD;
            ans = (ans + ways) % MOD;

            denomInv = (denomInv * count[charIndex]) % MOD;
            count[charIndex]--;
        }

        return (int) ans;
    }

    private long power(long base, int exp) {
        long res = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                res = (res * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return res;
    }
}