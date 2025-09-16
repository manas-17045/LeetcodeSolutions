# Leetcode 3044: Most Frequent Prime
# https://leetcode.com/problems/most-frequent-prime/
# Solved on 16th of September, 2025
from collections import Counter


class Solution:
    def mostFrequentPrime(self, mat: list[list[int]]) -> int:
        """
        Finds the most frequent prime number formed by concatenating digits in all 8 directions from each cell.

        Args:
            mat: A 2D list of integers representing the matrix.
        Returns:
            The most frequent prime number, or -1 if no prime numbers are found.
        """
        m = len(mat)
        n = len(mat[0])
        # 8 directions (no (0,0))
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # Primality test for n (deterministic, fast for n up to ~1e12; here numbers <= 10^6)
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return n in (2, 3)
            i = 5
            # Check 6k-1 and 6k+1
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        prime_cache = {}
        freq = Counter()

        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    x, y = i, j
                    num = 0
                    # Traverse in direction until out of bounds
                    while 0 <= x < m and 0 <= y < n:
                        num = num * 10 + mat[x][y]
                        if num > 10:
                            # Cache primality results to avoid repeated checks
                            p = prime_cache.get(num)
                            if p is None:
                                p = is_prime(num)
                                prime_cache[num] = p
                            if p:
                                freq[num] += 1
                        x += dx
                        y += dy

        if not freq:
            return -1

        # Find prime(s) with max frequency, tie-breaker: largest prime
        max_freq = max(freq.values())
        # Filter keys with that freq and take the maximum key
        candidates = [num for num, c in freq.items() if c == max_freq]
        return max(candidates)