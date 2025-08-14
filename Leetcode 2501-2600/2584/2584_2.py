# Leetcode 2584: Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/
# Solved on 14th of August, 2025
import math


class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        """
        Finds the smallest index `i` such that the product of elements in `nums[0...i]`
        and the product of elements in `nums[i+1...n-1]` are coprime.

        :param nums: A list of integers.
        :return: The smallest index `i` that satisfies the condition, or -1 if no such index exists.
        """

        n = len(nums)
        if n <= 1:
            return -1

        maxA = max(nums)
        # Factorization helper: Use SPF if maxA is reasonably small, otherwise use trial division.
        if maxA <= 10**6:
            # Build Smallest-Prime-Factor (SPF) sieve up to maxA
            spf = list(range(maxA + 1))
            spf[0] = 0
            if maxA >= 1:
                spf[1] = 1
            limit = int(math.isqrt(maxA)) + 1
            for p in range(2, limit):
                if spf[p] == p:
                    step = p
                    start = p * p
                    for multiple in range(start, maxA + 1, step):
                        if spf[multiple] == multiple:
                            spf[multiple] = p

            def prime_factors(x: int):
                primes = set()
                while x > 1:
                    p = spf[x]
                    primes.add(p)
                    while x % p == 0:
                        x //= p
                return primes

        else:
            # Fallback: generate primes up to sqrt(maxA) and trial-divide each number
            lim = int(math.isqrt(maxA)) + 1
            sieve = bytearray(b'\x01') * (lim + 1)
            sieve[0:2] = b'x\00\x00'
            for i in range(2, int(math.isqrt(lim)) + 1):
                if sieve[i]:
                    step = i
                    start = i * i
                    sieve[start:(lim + 1):step] = b'\x00' * (((lim - start) // step) + 1)
            small_primes = [i for i, isPrime in enumerate(sieve) if isPrime]

            def prime_factors(x: int):
                primes = set()
                for p in small_primes:
                    if p * p > x:
                        break
                    if x % p == 0:
                        primes.add(p)
                        while x % p == 0:
                            x //= p

                if x > 1:
                    primes.add(x)
                return primes

        # Factor each number once and record first/last occurrence of each prime
        factors_per_index = [None] * n
        first_occ = {}
        last_occ = {}
        for i, val in enumerate(nums):
            primes = prime_factors(val)
            factors_per_index[i] = primes
            for p in primes:
                if p not in first_occ:
                    first_occ[p] = i
                last_occ[p] = i

        # Scan left-to-right and keep the farthest last-occurrence of primes seen so far
        farthest = -1
        for i in range(n - 1):
            primes = factors_per_index[i]
            if primes:
                for p in primes:
                    # Extend farthest to cover primes that appear later
                    farthest = max(farthest, last_occ[p])

            if farthest <= i:
                return i

        return -1