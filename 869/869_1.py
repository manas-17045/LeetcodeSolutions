# Leetcode 869: Reordered Power of 2
# https://leetcode.com/problems/reordered-power-of-2/
# Solved on 10th of August, 2025
import collections


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Checks if a given integer n can be reordered to form a power of 2.

        :param n: The input integer.
        :return: True if n can be reordered to form a power of 2, False otherwise.
        """
        nCounter = collections.Counter(str(n))
        for i in range(34):
            power = 1 << i
            if nCounter == collections.Counter(str(power)):
                return True
        return False