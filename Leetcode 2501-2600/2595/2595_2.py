# Leetcode 2595: Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/
# Solved on 15th of August, 2025
class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        """
        Counts the number of set bits at even and odd positions in the binary representation of n.

        Args:
            n (int): The input integer.
        Returns:
            list[int]: A list containing two integers: [count of set bits at even positions, count of set bits at odd positions].
        """
        even = 0
        odd = 0
        idx = 0
        while n:
            if n & 1:
                if idx % 2 == 0:
                    even += 1
                else:
                    odd += 1
            n >>= 1
            idx += 1
        return [even, odd]