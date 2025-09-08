# Leetcode 1317: Convert Integer to the Sum of Two No-Zero Integers
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Solved on 8th of September, 2025
class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        """
        Given an integer n, return a list of two integers [A, B] such that A and B are "no-zero" integers and A + B = n.
        A no-zero integer is a positive integer that does not contain any digit 0 in its decimal representation.
        Input: n (int) - The target sum.
        Output: list[int] - A list containing two no-zero integers [A, B] that sum to n.
        """
        def has_zero(x: int) -> bool:
            # Return True if x contains digit 0
            while x:
                if x % 10 == 0:
                    return True
                x //= 10
            return False

        for a in range(1, n):
            b = n - a
            if not has_zero(a) and not has_zero(b):
                return [a, b]

        # Problem guarantees a solution exists.
        return []