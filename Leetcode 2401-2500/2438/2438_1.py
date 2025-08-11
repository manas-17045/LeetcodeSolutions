# Leetcode 2438: Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers/
# Solved on 11th of August, 2025
class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        Calculates the product of powers of 2 for given ranges.

        Args:
            n (int): The input integer to decompose into powers of 2.
            queries (list[list[int]]): A list of queries, where each query [l, r] represents a range.
        Returns:
            list[int]: A list of results for each query, where each result is the product of powers of 2 in the given range, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        exponents = []
        bit = 0
        temp_n = n
        while temp_n > 0:
            if temp_n & 1:
                exponents.append(bit)
            temp_n >>= 1
            bit += 1
        m = len(exponents)
        prefix = [0] * (m + 1)
        for i in range(m):
            prefix[i + 1] = prefix[i] + exponents[i]
        ans = []
        for l, r in queries:
            total_exp = prefix[r + 1] - prefix[l]
            res = pow(2, total_exp, MOD)
            ans.append(res)
        return ans