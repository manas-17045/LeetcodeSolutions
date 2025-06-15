# Leetcode 3495: Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
# Solved on 15th of June, 2025
from functools import lru_cache


class Solution:
    def minOperations(self, queries: list[list[int]]) -> int:
        """
        Calculates the total minimum operations to make array elements zero for a given set of queries.

        For each query [l, r], the problem asks for the sum of minimum operations to make each number
        from l to r zero. The operation is defined as replacing a number x with floor(x / 4).

        Args:
            queries: A list of queries, where each query is [l, r].
        """
        @lru_cache(maxsize=None)
        def getOps(i: int) -> int:
            if i == 0:
                return 0
            return 1 + getOps(i // 4)

        @lru_cache(maxsize=None)
        def getF(n: int) -> int:
            if n <= 0:
                return 0

            q = n // 4
            rem = n % 4

            tN = 4 * getF(q - 1) + (rem + 1) * getOps(q)
            return n + tN

        totalOperations = 0
        for l, r in queries:
            if l == r:
                queryOps = getOps(l)
            else:
                s = getF(r) - getF(1 - l)
                queryOps = (s + 1) // 2
            totalOperations += queryOps

        return totalOperations