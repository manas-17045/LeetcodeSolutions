# Leetcode 1611: Minimum One Bit Operations to Make Integers Zero
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
# Solved on 17th of July, 2025
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        Calculates the minimum number of one-bit operations to make n zero.

        Args:
            n: A non-negative integer.

        Returns:
            The minimum number of one-bit operations to transform n to 0.
        """
        result = 0
        while n > 0:
            result ^= n
            n >>= 1
        return result