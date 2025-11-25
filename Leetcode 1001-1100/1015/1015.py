# Leetcode 1015: Smallest Integer Divisible by K
# https://leetcode.com/problems/smallest-integer-divisible-by-k/
# Solved on 25th of November, 2025
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Finds the length of the smallest positive integer `N` consisting only of digit 1's that is divisible by `k`.

        Args:
            k: An integer.
        Returns:
            The length of the smallest repunit divisible by `k`, or -1 if no such repunit exists.
        """
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1