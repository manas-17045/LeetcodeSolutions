# Leetcode 2749: Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
# Solved on 5th of September, 2025
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        Finds the minimum non-negative integer k such that num1 - k * num2 can be represented as a sum of k powers of 2.

        Args:
            num1 (int): The initial integer.
            num2 (int): The integer to subtract k times.
        Returns:
            int: The minimum non-negative integer k, or -1 if no such k exists.
        """
        # If already zero, zero operations needed
        if num1 == 0:
            return 0

        # Try k from 1 to 60 (inclusive). 60 is enough due to the problem's 2^i bound
        for k in range(1, 61):
            s = num1 - k * num2
            if s < 0:
                continue

            if s >= k and s.bit_count() <= k:
                return k

        return -1