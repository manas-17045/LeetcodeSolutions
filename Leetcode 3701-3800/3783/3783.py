# Leetcode 3783: Mirror Distance of an Integer
# https://leetcode.com/problems/mirror-distance-of-an-integer/
# Solved on 18th of April, 2026
class Solution:
    def mirrorDistance(self, n: int) -> int:
        """
        Calculates the absolute difference between an integer and its reverse.

        :param n: The input integer.
        :return: The absolute difference between n and its mirror (reversed) value.
        """
        reversedValue = int(str(n)[::-1])
        return abs(n - reversedValue)