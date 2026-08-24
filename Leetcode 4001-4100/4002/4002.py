# Leetcode 4002: Count Valid Sequences
# https://leetcode.com/problems/count-valid-sequences/ 
# Solved on 24th of August, 2026
import math


class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        """
        Calculates the number of sequences of k positive integers summing to n with an even product.

        @param n the target sum of the sequence
        @param k the number of elements in the sequence
        @return the total number of valid sequences modulo 10^9 + 7
        """
        moduloVal = 1_000_000_007
        totalCount = math.comb(n - 1, k - 1) % moduloVal

        if (n - k) % 2 != 0:
            return totalCount

        oddCount = math.comb((n + k) // 2 - 1, k - 1) % moduloVal
        return (totalCount - oddCount + moduloVal) % moduloVal