# Leetcode 2939: Maximum Xor Product
# https://leetcode.com/problems/maximum-xor-product/
# Solved on 28th of August, 2025
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        """
        Calculates the maximum XOR product of two numbers a and b, considering only the lowest n bits.

        Args:
            a (int): The first integer.
            b (int): The second integer.
            n (int): The number of lowest bits to consider.

        Returns:
            int: The maximum XOR product modulo 10^9 + 7.
        """

        mod = 10**9 + 7

        for i in range((n - 1), -1, -1):
            bit = 1 << i
            aBitSet = (a & bit) > 0
            bBitSet = (b & bit) > 0

            if aBitSet == bBitSet:
                a |= bit
                b |= bit
            else:
                if a < b:
                    a |= bit
                    b &= ~bit
                else:
                    a &= ~bit
                    b |= bit

        return (a % mod) * (b % mod) % mod