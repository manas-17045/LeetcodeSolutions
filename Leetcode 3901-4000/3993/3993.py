# Leetcode 3993: Maximum Value of an Alternating Sequence
# https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/
# Solved on 15th of August, 2026
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        """
        Calculates the maximum value of an alternating sequence.
        
        :param n: The length of the sequence.
        :param s: The starting value of the sequence.
        :param m: The maximum value for each element in the sequence.
        :return: The maximum value of an alternating sequence.
        """
        if n == 1:
            return s

        abc = n // 2
        return s + m + (abc - 1) * (m - 1)