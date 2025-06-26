# Leetcode 1702: Maximum Binary String After Change
# https://leetcode.com/problems/maximum-binary-string-after-change/
# Solved on 26th of June, 2025
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        """
        Given a binary string binary, return the maximum possible binary string
        that can be obtained by applying the following operations any number of times:

        1. "00" -> "10"
        2. "10" -> "01"

        The goal is to transform the given binary string into the lexicographically
        largest possible binary string.

        Args: binary: The input binary string.
        Returns: The maximum possible binary string.
        """
        n = len(binary)

        numZeros = binary.count('0')

        if numZeros == 0:
            return binary

        firstZeroIndex = binary.find('0')

        zeroPositionInResult = firstZeroIndex + numZeros - 1

        resultChars = ['1'] * n
        resultChars[zeroPositionInResult] = '0'

        return "".join(resultChars)