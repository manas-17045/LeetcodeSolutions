# Leetcode 4039: Sum of Decoded Numbers
# https://leetcode.com/problems/sum-of-decoded-numbers/
# Solved on 1st of October, 2026
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        """
        Computes the sum of decoded values x^y for each encoded integer in nums modulo 10^9 + 7.

        :param nums: A list of encoded integers where each element contains width, base, and exponent.
        :type nums: list[int]
        :return: The total sum of all decoded values modulo 10^9 + 7.
        """
        moduloVal = 1_000_000_007
        totalSum = 0

        for encodedNum in nums:
            widthVal = encodedNum % 10
            trimmedNum = encodedNum // 10
            numStr = str(trimmedNum)
            baseVal = int(numStr[:widthVal])
            expVal = int(numStr[widthVal:])
            totalSum = (totalSum + pow(baseVal, expVal, moduloVal)) % moduloVal

        return totalSum