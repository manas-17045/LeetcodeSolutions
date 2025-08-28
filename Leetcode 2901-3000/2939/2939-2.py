# Leetcode 2939: Maximum Xor Product
# https://leetcode.com/problems/maximum-xor-product/
# Solved on 28th of August, 2025
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        """
        Calculates the maximum XOR product (a XOR x) * (b XOR x) for a given n.
        :param a: An integer.
        :param b: An integer.
        :param n: An integer representing the number of bits to consider (from 0 to n-1).
        :return: The maximum XOR product modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        # Iterate bits from (n - 1) down to 0
        for i in range((n - 1), -1, -1):
            bit = 1 << i

            # If flipping this bit in both numbers increases the product, do it.
            if (a ^ bit) * (b ^ bit) > a * b:
                a ^= bit
                b ^= bit

        return (a % MOD) * (b % MOD) % MOD