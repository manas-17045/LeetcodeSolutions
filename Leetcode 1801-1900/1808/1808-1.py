# Leetcode 1808: Maximize Number of Nice Divisors
# https://leetcpde.com/problems/maximize-number-of-nice-divisors/
# Solved on 8th of September, 2025
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """
        Calculates the maximum number of nice divisors for a given number of prime factors.

        A "nice divisor" is defined such that if a number has `n` prime factors,
        and we want to maximize the number of its divisors, we should distribute
        these prime factors as evenly as possible among a base of 2s and 3s.
        This problem is equivalent to maximizing the product of integers that sum up to `primeFactors`.

        Args:
            primeFactors (int): The total number of prime factors available.

        Returns:
            int: The maximum number of nice divisors, modulo 1,000,000,007.
        """
        mod = 1_000_000_007
        if primeFactors <= 4:
            return primeFactors

        remainder = primeFactors % 3

        if remainder == 0:
            power = primeFactors // 3
            return pow(3, power, mod)
        elif remainder == 1:
            power = (primeFactors - 4) // 3
            result = pow(3, power, mod)
            return (result * 4) % mod
        else:
            power = primeFactors // 3
            result = pow(3, power, mod)
            return (result * 2) % mod