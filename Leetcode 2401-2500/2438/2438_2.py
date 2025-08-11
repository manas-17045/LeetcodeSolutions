# Leetcode 2438: Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers/
# Solved on 11th of August, 2025
class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Calculates the product of powers of 2 for specified ranges of set bits in n.

        Args:
            n (int): The integer whose binary representation determines the powers of 2.
            queries (list[list[int]]): A list of queries, where each query [l, r] represents
                                       a range of indices (0-indexed) of the set bits in n.
        Returns:
            list[int]: A list of integers, where each element is the product of 2^i for the
                       set bits at indices from l to r (inclusive), modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Collect exponents i where 2^i is present in n (bit, set), in ascending order
        exps = []
        i = 0
        temp = n
        while temp:
            if temp & 1:
                exps.append(i)
            i += 1
            temp >>= 1

        # Prefix sums of exponents for range-sum queries
        pref = [0] * (len(exps) + 1)
        for idx, e in enumerate(exps, start=1):
            pref[idx] = pref[idx - 1] + e

        ans = []
        for l, r in queries:
            # Sum of exponents in range
            s = pref[r + 1] - pref[l]
            ans.append(pow(2, s, MOD))

        return ans