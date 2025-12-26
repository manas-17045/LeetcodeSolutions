# Leetcode 3746: Minimum String Length After Balanced Removals
# https://leetcode.com/problems/minimum-string-length-after-balanced-removals/
# Solved on 26th of December, 2025
class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        """
        Calculates the minimum length of a string after performing balanced removals.

        :param s: The input string consisting of 'a's and 'b's.
        :return: The minimum possible length of the string after balanced removals.
        """
        countA = s.count('a')
        countB = len(s) - countA
        return abs(countA - countB)