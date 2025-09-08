# Leetcode 1317: Convert Integer to the Sum of Two No-Zero Integers
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
# Solved on 8th of September, 2025
class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        """
        Given an integer n, return a list of two no-zero integers A and B such that A + B = n.
        A no-zero integer is an integer that does not contain any digit 0 in its decimal representation.

        :param n: The input integer.
        :return: A list containing two no-zero integers [A, B] that sum up to n.
        """
        for numA in range(1, n):
            numB = n - numA
            if '0' not in str(numA) and '0' not in str(numB):
                return [numA, numB]

        return []