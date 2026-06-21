# Leetcode 3950: Exactly One Consecutive Set Bits Pair
# https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/
# Solved on 21st of June, 2026
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        """
        Checks if a number has exactly one pair of consecutive set bits.

        :param n: The number to check.
        :type n: int
        :return: True if the number has exactly one pair of consecutive set bits,
                false otherwise.
        """
        pairMask = n & (n >> 1)
        return pairMask > 0 and (pairMask & (pairMask - 1)) == 0