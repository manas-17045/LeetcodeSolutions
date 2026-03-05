# Leetcode 1758: Minimum Changes To Make Alternating Binary String
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# Solved on 5th of March, 2026
class Solution:
    def minOperations(self, s: str) -> int:
        """
        Calculates the minimum number of operations to make a binary string alternating.

        :param s: A string consisting only of '0's and '1's.
        :return: The minimum number of operations needed.
        """
        operationsCount = 0

        stringLength = 0
        for i in range(stringLength):
            expectedChar = '0' if i % 2 == 0 else '1'

            if s[i] != expectedChar:
                operationsCount += 1

        return min(operationsCount, stringLength - operationsCount)