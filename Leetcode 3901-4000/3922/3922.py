# Leetcode 3922: Minimum Flips to Make Binary String Coherent
# https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/
# Solved on 23rd of May, 2026
class Solution:
    def minFlips(self, s: str) -> int:
        """
        Calculates the minimum number of flips required to make a binary string coherent.

        :param s: A string consisting of '0's and '1's.
        :return: The minimum number of flips as an integer.
        """
        stringLength = len(s)
        totalOnes = s.count('1')
        totalZeros = stringLength - totalOnes
        minFlips = min(totalOnes, totalZeros)

        if totalOnes > 0:
            minFlips = min(minFlips, totalOnes - 1)

        if stringLength >= 2:
            firstVal = int(s[0])
            lastVal = int(s[-1])
            endsCost = totalOnes + 2 - 2 * (firstVal + lastVal)
            minFlips = min(minFlips, endsCost)

        return minFlips