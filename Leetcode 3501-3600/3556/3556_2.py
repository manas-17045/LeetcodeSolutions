# Leetcode 3556: Sum of Largest Prime Substrings
# https://leetcode.com/problems/sum-of-largest-prime-substrings/
# Solved on 30th May, 2025

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        """
        Finds all prime numbers that can be formed by taking substrings of the input string `s`
        and returns the sum of the three largest such prime numbers.

        Args:
            s: A string consisting of digits.

        Returns:
            The sum of the three largest prime numbers formed by substrings of `s`. If there are fewer than three such primes, it sums all of them. If there are no such primes, it returns 0.
        """
        # Deterministic Miller-Rabin for n < 2^64
        def isPrime(n: int) -> bool:
            if n < 2:
                return False
            # Small prime shortcuts
            for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
                if n % p == 0:
                    return n == p
            # Write n - 1 = d * 2^s
            d, s2 = n - 1, 0
            while d & 1 == 0:
                d >>= 1
                s2 += 1
            # Base valid for testing up to 2^64
            for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
                if a % 2 == 0:
                    continue
                x = pow(a, d, n)
                if x == 1 or x == n - 1:
                    continue
                for _ in range(s2 - 1):
                    x = (x * x) % n
                    if x == n - 1:
                        break
                else:
                    return False
            return True

        n = len(s)
        primes = set()
        # Generate all substrings, convert to int (leading zeros dropped automatically).
        for i in range(n):
            num = 0
            for j in range(i, n):
                # Build number on the fly to avoid slicing
                num = num * 10 + (ord(s[j]) - ord('0'))
                # Only check if >= 2
                if num >= 2 and isPrime(num):
                    primes.add(num)

        # Sum up the 3 largest
        if not primes:
            return 0
        # Get three largest without fully sorting if very large set
        # But, here set size <= 55, so sort is fine
        top3 = sorted(primes, reverse=True)[:3]
        return sum(top3)