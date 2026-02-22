# Leetcode 868: Binary Gap
# https://leetcode.com/problems/binary-gap/
# Solved on 22nd of February, 2026
class Solution:
    def binaryGap(self, n: int) -> int:
        """
        Finds the longest distance between two adjacent 1's in the binary representation of n.

        :param n: The integer to evaluate.
        :return: The maximum distance between adjacent 1's, or 0 if no such pair exists.
        """
        lastPos = -1
        currentPos = 0
        maxDistance = 0

        while n > 0:
            if n & 1 == 1:
                if lastPos != -1:
                    if currentPos - lastPos > maxDistance:
                        maxDistance = currentPos - lastPos
                lastPos = currentPos
            n >>= 1
            currentPos += 1

        return maxDistance