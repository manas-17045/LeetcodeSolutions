# Leetcode 2862: Maximum Element-Sum of a Complete Subset of Indices
# https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/
# Solved on 28th of May, 2025

class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of elements in `nums` where the indices of the elements
        in the sum have the same square-free part.

        The square-free part of an integer `i` is the product of its distinct prime factors.
        For example, the square-free part of 12 (2^2 * 3) is 2 * 3 = 6.

        The algorithm works by:\n
        1. Building a smallest-prime-factor (spf) sieve up to `n` to efficiently compute
           the square-free part of each index.
        2. Grouping the elements of `nums` based on the square-free part of their index.
        3. Calculating the sum of elements within each group.
        4. Returning the maximum sum among all groups.
        """
        n = len(nums)
        # Build smallest-prime-factor sieve up to n
        spf = list(range(n + 1))    # spf[x] = smallest prime dividing x
        for p in range(2, int(n**0.5) + 1):
            if spf[p] == p:
                for multiple in range(p*p, n + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        # Helper function to compute square-free part of i
        def squareFree(i: int) -> int:
            sf = 1
            while i > 1:
                p = spf[i]
                cnt = 0
                while i % p == 0:
                    i //= p
                    cnt^= 1 # We only care mod 2
                if cnt:
                    sf *= p
            return sf

        # Group sums by square-free signature
        group_sum = {}
        for idx, val in enumerate(nums, start = 1):
            sf = squareFree(idx)
            group_sum[sf] = group_sum.get(sf, 0) + val

        # Answer is maximum group sum
        return max(group_sum.values())