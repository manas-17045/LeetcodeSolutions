# Leetcode 3725: Count Ways to Choose Coprime Integers from Rows
# https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/
# Solved on 6th of December, 2025
import math


class Solution:
    def countCoprime(self, mat: list[list[int]]) -> int:
        """
        Counts the number of ways to choose one integer from each row such that their greatest common divisor is 1.

        Args:
            mat: A list of lists of integers, where each inner list represents a row.
        Returns:
            The number of ways to choose coprime integers, modulo 10^9 + 7.
        """

        mod = 10**9 + 7
        limit = 151
        dp = [0] * limit

        for num in mat[0]:
            dp[num] += 1

        for i in range(1, len(mat)):
            newDp = [0] * limit
            rowCounts = [0] * limit
            for num in mat[i]:
                rowCounts[num] += 1
            existingGcds = []
            for val in range(1, limit):
                if dp[val] > 0:
                    existingGcds.append(val)

            rowValues = []
            for val in range(1, limit):
                if rowCounts[val] > 0:
                    rowValues.append(val)

            for g in existingGcds:
                count = dp[g]
                for v in rowValues:
                    freq = rowCounts[v]
                    newGcd = math.gcd(g, v)
                    newDp[newGcd] = (newDp[newGcd] + count * freq) % mod

            dp = newDp

        return dp[1]