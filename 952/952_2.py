# Leetcode 952: Largest Component Size by Common Factor
# https://leetcode.com/problems/largest-component-size-by-common-factor/
# Solved on 13th of July, 2025
import math


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        """
        Given a list of unique integers nums, return the size of the largest connected component.
        Two integers are connected if they share a common factor greater than 1.

        The problem can be modeled as finding the largest connected component in a graph.
        Each number in `nums` is a node. An edge exists between two numbers if they share
        a common prime factor.

        We use a Union-Find data structure to group numbers that share common factors.
        For each number, we find its prime factors. If a prime factor has been seen before
        in another number, we union the current number's index with the index of the
        previously seen number that had this prime factor.

        """
        n = len(nums)
        if n <= 1:
            return n

        # Union-Find with path compression & union by size
        parent = list(range(n))
        size = [1] * n

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # Attached smaller tree to larger tree
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # Precompute all primes up to sqrt(max(nums))
        max_num = max(nums)
        lim = int(math.isqrt(max_num)) + 1
        sieve = [True] * (lim + 1)
        primes = []
        for i in range(2, (lim + 1)):
            if sieve[i]:
                primes.append(i)
                for j in range(i * i, (lim + 1), i):
                    sieve[j] = False

        # map from prime factor -> first index in nums that had it
        factor_to_index = {}

        # Factor each number and union indices sharing any factor
        for i, x in enumerate(nums):
            temp = x
            for p in primes:
                if p * p > temp:
                    break
                if temp % p == 0:
                    # p is a factor
                    if p not in factor_to_index:
                        factor_to_index[p] = i
                    else:
                        union(i, factor_to_index[p])

                    # Remove all p-factors
                    while temp % p == 0:
                        temp //= p

            if temp > 1:
                # temp is a prime factor
                if temp not in factor_to_index:
                    factor_to_index[temp] = i
                else:
                    union(i, factor_to_index[temp])

        count = {}
        ans = 1
        for i in range(n):
            r = find(i)
            count[r] = count.get(r, 0) + 1
            if count[r] > ans:
                ans = count[r]

        return ans