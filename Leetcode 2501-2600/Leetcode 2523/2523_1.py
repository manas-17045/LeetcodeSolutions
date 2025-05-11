# Leetcode 2523: Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range

from math import isqrt


class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        """
        Finds the two prime numbers in the inclusive range [left, right]
        that are closest to each other.

        The Sieve of Eratosthenes is used to efficiently find all prime
        numbers up to `right`. Then, the algorithm iterates through the
        primes within the given range [left, right] to find the pair
        with the minimum difference. If multiple pairs have the same
        minimum difference, the pair with the smallest first number is returned.
        If no two prime numbers are found in the range, [-1, -1] is returned.

        Args:
            left: The lower bound of the range (inclusive).
            right: The upper bound of the range (inclusive).

        Returns:
            A list containing the two closest prime numbers [num1, num2]
            such that num1 < num2. If no such pair exists, returns [-1, -1].
        """
        if right < 2:
            # No primes possible
            return [-1, -1]

        # 1. Sieve of Eratosthenes to find primes up to right
        is_prime = [True] * (right + 1)
        if right >= 0:
            is_prime[0] = False
        if right >= 1:
            is_prime[1] = False

        for p in range(2, isqrt(right) + 1):
            if is_prime[p]:
                for i in range(p * p, right + 1, p):
                    is_prime[i] = False

        # 2. Find Closest Prime Pair in the Range [left, right]
        min_difference = float('inf')
        ans = [-1, -1]
        previous_prime = -1

        # Adjust left boundary if it's less than 2, as primes start from 2
        start_num = max(left, 2)

        for current_num in range(start_num, right + 1):
            if is_prime[current_num]:
                if previous_prime != -1:
                    diff = current_num - previous_prime
                    if diff < min_difference:
                        min_difference = diff
                        ans = [previous_prime, current_num]
                        # Optimization: if min_difference is 1 (e.g., 2, 3) or 2 (e.g., 3, 5 or 5, 7),
                        # it's the smallest possible non-zero difference for distinct primes.
                        # For twin primes (diff = 2), it's the smallest possible difference other than (2, 3).
                        # If problem asked for *any* closest pair, we could potentially stop early if diff is 1 or 2.

                # However, we need the one with smallest num1 if ties, so we must continue.
                previous_prime = current_num

        return ans
