# Leetcode 2749: Minimum Operations to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
# Solved on 5th of September, 2025
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        Calculates the minimum number of operations to make num1 zero.

        Args:
            num1 (int): The initial integer.
            num2 (int): The integer to subtract or add.
        Returns:
            int: The minimum number of operations, or -1 if it's not possible.
        """
        for k in range(1, 65):
            target = num1 - k * num2

            if target >= k >= target.bit_count():
                return k

        return -1