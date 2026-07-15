# Leetcode 3658: GCD of Odd and Even Sums
# https://leetcode.com/problems/gcd-of-odd-and-even-sums/
# Solved on 15th of July, 2026
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        """
        Counts the number of pairs (i, j) such that 1 <= i < j <= n and gcd(sum_odd(i..j), sum_even(i..j)) is odd.
        @param n the upper bound for i and j
        @return the number of pairs (i, j) satisfying the condition
        """
        return n