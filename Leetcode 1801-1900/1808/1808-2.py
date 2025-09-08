# Leetcode 1808: Maximize Number of Nice Divisors
# https://leetcpde.com/problems/maximize-number-of-nice-divisors/
# Solved on 8th of September, 2025
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """
        Calculates the maximum number of nice divisors for a given number of prime factors.
        :param primeFactors: The total number of prime factors.
        :return: The maximum number of nice divisors, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        # Small cases: best is to keep the number as-is
        if primeFactors <= 4:
            return primeFactors % MOD

        q, r = divmod(primeFactors, 3)

        # If remainder is 1, it's better one 3 into two 2's.
        if r == 1:
            q -= 1
            r = 4

        # Now, result = 3^q * (r)
        ans = pow(3, q, MOD)
        if r:
            ans = (ans * r) % MOD
        return ans