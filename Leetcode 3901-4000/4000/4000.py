# Leetcode 4000: Largest Integer With Given Digit Sum
# https://leetcode.com/problems/largest-integer-with-given-digit-sum/
# Solved on 22nd of August, 2026
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        """
        Generates the largest integer with n digits that has a digit sum of s.

        @param n: The number of digits in the integer.
        @param s: The desired digit sum.
        @return: The largest integer with n digits and digit sum s, or -1 if no such integer exists.
        """
        if s > 9 * n:
            return -1

        rValue = 0
        rSum = s

        for _ in range(n):
            cDigit = min(9, rSum)
            rValue = rValue * 10 + cDigit
            rSum -= cDigit

        return rValue