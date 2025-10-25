# Leetcode 2761: Prime Pairs With Target Sum
# https://leetcode.com/problems/prime-pairs-with-target-sum/
# Solved on 25th of October, 2025
class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        """
        Finds all pairs of prime numbers (x, y) such that x + y = n and x <= y.

        Args:
            n: An integer representing the target sum.
        Returns:
            A list of lists, where each inner list [x, y] represents a prime pair.
        """
        isPrime = [True] * (n + 1)
        if n >= 0:
            isPrime[0] = False
        if n >= 1:
            isPrime[1] = False

        p = 2
        while p * p <= n:
            if isPrime[p]:
                for i in range(p * p, n + 1, p):
                    isPrime[i] = False
            p += 1

        resultPairs = []
        for x in range(2, n // 2 + 1):
            y = n - x
            if isPrime[x] and isPrime[y]:
                resultPairs.append([x, y])

        return resultPairs