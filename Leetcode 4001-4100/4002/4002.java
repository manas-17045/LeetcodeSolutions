// Leetcide 4002: Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/
// Solved on 24th of August, 2026
class Solution {
    private static final int MOD = 1_000_000_007;
    
    /**
     * Computes the number of valid sequences of positive integers with the given length and sum.
     *
     * @param n the target sum of the sequence
     * @param k the number of elements in the sequence
     * @return the total number of valid sequences modulo 10^9 + 7
     */
    public int countValidSequences(int n, int k) {
        if (k > n || k <= 0) {
            return 0;
        }

        long[] fact = new long[n];
        long[] invFact = new long[n];

        fact[0] = 1;
        invFact[0] = 1;

        for (int i = 1; i < n; i++) {
            fact[i] = (fact[i - 1] * i) % MOD;
        }

        invFact[n - 1] = power(fact[n - 1], MOD - 2);
        for (int i = n - 2; i >= 1; i--) {
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD;
        }

        long totalSequences = nCr(n - 1, k - 1, fact, invFact);
        long oddSequences = 0;

        if ((n - k) % 2 == 0) {
            oddSequences = nCr((n + k) / 2 - 1, k - 1, fact, invFact);
        }

        long validSequences = (totalSequences - oddSequences + MOD) % MOD;
        return (int) validSequences;
    }

    private long nCr(int n, int r, long[] fact, long[] invFact) {
        if (r < 0 || r > n) {
            return 0;
        }
        return fact[n] * invFact[r] % MOD * invFact[n - r] % MOD;
    }

    private long power(long base, long exp) {
        long result = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }
}