# Leetcode 1735: Count Ways to Make Array With Product
# https://leetcode.com/problems/count-ways-to-make-array-with-product/
# Solved on 22nd of July, 2025
import collections


class Solution:
    def waysToFillArray(self, queries: list[list[int]]) -> list[int]:
        """
        Calculates the number of ways to fill an array of `n` positive integers such that their product is `k`.

        Args:
            queries (list[list[int]]): A list of queries, where each query is [n, k].
        Returns:
            list[int]: A list of integers, where each element is the answer to the corresponding query.
        """
        mod = 10**9 + 7
        maxK = 10001

        smallestPrimeFactor = list(range(maxK))
        i = 2
        while i * i < maxK:
            if smallestPrimeFactor[i] == i:
                for j in range(i * i, maxK, i):
                    if smallestPrimeFactor[j] == j:
                        smallestPrimeFactor[j] = i
            i += 1

        primeFactorizations = [collections.defaultdict(int) for _ in range(maxK)]
        for i in range(2, maxK):
            prime = smallestPrimeFactor[i]
            remainingPart = i // prime
            primeFactorizations[i] = primeFactorizations[remainingPart].copy()
            primeFactorizations[i][prime] += 1

        maxCombN = 10000 + 15
        factorials = [1] * maxCombN
        inverseFactorials = [1] * maxCombN

        for i in range(1, maxCombN):
            factorials[i] = (factorials[i - 1] * i) % mod

        inverseFactorials[maxCombN - 1] = pow(factorials[maxCombN - 1], (mod - 2), mod)
        for i in range(maxCombN - 2, -1, -1):
            inverseFactorials[i] = (inverseFactorials[i + 1] * (i + 1)) % mod

        def combinations(n, r):
            if r < 0 or r > n:
                return 0
            numerator = factorials[n]
            denominator = (inverseFactorials[r] * inverseFactorials[n - r]) % mod
            return (numerator * denominator) % mod

        answers = []
        for n, k in queries:
            totalWays = 1
            factors = primeFactorizations[k]

            for exponent in factors.values():
                waysForPrime = combinations(exponent + n - 1, n - 1)
                totalWays = (totalWays * waysForPrime) % mod

            answers.append(totalWays)

        return answers