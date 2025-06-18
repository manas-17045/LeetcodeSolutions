# Leetcode 3405: Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/
# Solved on 17th of June, 2025

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        """
        Counts the number of "good" arrays of length n.

        An array is considered "good" if it has exactly k pairs of adjacent equal elements.

        Args:
            n: The length of the array.
            m: The maximum value an element in the array can take (elements are from 1 to m).
            k: The required number of adjacent equal pairs.
        """
        MOD = 10**9 + 7
        # There are only (n - 1) adjacent slots, so impossible if k > (n - 1).
        if k < 0 or k > (n - 1):
            return 0

        # Precompute factorials and inverse factorials up to (n - 1).
        fact = [1] * (n)
        for i in range(1, n):
            fact[i] = (fact[i - 1] * i) % MOD
        invFact = [1] * n
        invFact[n - 1] = pow(fact[n - 1], MOD - 2, MOD)
        for i in range((n - 1), 0, -1):
            invFact[i - 1] = (invFact[i] * i) % MOD

        C = fact[n - 1] * invFact[k] % MOD * invFact[n - 1 - k] % MOD

        return m * C % MOD * pow((m - 1), (n - 1 - k), MOD) % MOD