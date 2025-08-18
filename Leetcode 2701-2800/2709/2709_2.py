# Leetcode 2709: Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/
# Solved on 18th of August, 2025
class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        """
        Determines if all pairs of numbers in the input list can be traversed.
        :param nums: A list of integers.
        :return: True if all pairs can be traversed, False otherwise.
        """
        n = len(nums)
        if n <= 1:
            return True

        # If any element is 1 and n > 1, it can't connect to any other (gcd(1, x) == 1)
        if any(x == 1 for x in nums):
            return False

        maxV = max(nums)

        # Build smallest-prime-factor (SPF) sieve up to maxV
        spf = list(range(maxV + 1))
        for p in range(2, int(maxV**0.5) + 1):
            if spf[p] == p:
                for multiple in range(p * p, maxV + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # Union-Find
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            else:
                parent[rb] = ra
                if rank[ra] == rank[rb]:
                    rank[ra] += 1

        # Map prime -> first index seen that has this prime
        prime_to_index = {}

        # Factorize each number using SPF, dedupe primes per number and union indices
        for idx, val in enumerate(nums):
            x = val
            primes = []
            while x > 1:
                p = spf[x]
                primes.append(p)
                while x % p == 0:
                    x //= p
            # Dedupe (though SPF generation already yields primes in non-decreasing order)
            last = None
            for p in primes:
                if p == last:
                    continue
                last = p
                if p in prime_to_index:
                    union(idx, prime_to_index[p])
                else:
                    prime_to_index[p] = idx

        # Check if all indices are in the same connected component
        root0 = find(0)
        for i in range(1, n):
            if find(i) != root0:
                return False
        return True