# Leetcode 1573: Number of Ways to Split a String
# https://leetcode.com/problems/number-of-ways-to-split-a-string/
# Solved on 23rd of August, 2025
class Solution:
    def numWays(self, s: str) -> int:
        """
        Calculates the number of ways to split a binary string into three non-empty parts,
        such that each part has the same number of '1's.

        Args:
            s (str): The input binary string.
        Returns:
            int: The number of ways to split the string, modulo 10^9 + 7.
        """
        stringLength = len(s)
        modulo = 10 ** 9 + 7

        oneIndices = [i for i, char in enumerate(s) if char == '1']

        totalOnes = len(oneIndices)

        if totalOnes % 3 != 0:
            return 0

        if totalOnes == 0:
            numWays = (stringLength - 1) * (stringLength - 2) // 2
            return numWays % modulo

        onesPerPart = totalOnes // 3

        idx1 = onesPerPart - 1
        idx2 = onesPerPart
        idx3 = 2 * onesPerPart - 1
        idx4 = 2 * onesPerPart

        waysForFirstCut = oneIndices[idx2] - oneIndices[idx1]
        waysForSecondCut = oneIndices[idx4] - oneIndices[idx3]

        return (waysForFirstCut * waysForSecondCut) % modulo