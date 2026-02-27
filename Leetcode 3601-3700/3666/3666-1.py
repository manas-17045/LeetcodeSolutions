# Leetcode 3666: Minimum Operations to Equalize Binary String
# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/
# Solved on 27th of February, 2026
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        """
        Calculates the minimum number of operations to make all characters in a binary string equal to '1'.
        Each operation involves flipping exactly k characters.

        :param s: A string consisting of '0's and '1's.
        :param k: The number of characters to flip in a single operation.
        :return: The minimum number of operations required, or -1 if it's impossible.
        """
        numZeros = s.count('0')
        if numZeros == 0:
            return 0

        strLen = len(s)
        leftBound = numZeros
        rightBound = numZeros
        targetR = strLen - k

        for operations in range(1, strLen + 5):
            prevL = leftBound
            prevR = rightBound

            if leftBound <= k <= rightBound:
                newLeft = (k - leftBound) % 2
            elif k < leftBound:
                newLeft = leftBound - k
            else:
                newLeft = k - rightBound

            if leftBound <= targetR <= rightBound:
                minDistR = (targetR - leftBound) % 2
            elif targetR < leftBound:
                minDistR = leftBound - targetR
            else:
                minDistR = targetR - rightBound

            newRight = strLen - minDistR
            leftBound = newLeft
            rightBound = newRight

            if leftBound == 0:
                return operations

            if leftBound == prevL and rightBound == prevR:
                return -1

        return -1