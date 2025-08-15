# Leetcode 2595: Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/
# Solved on 15th of August, 2025
class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        """
        Counts the number of set bits at even and odd indices in the binary representation of n.

        Args:
            n (int): The input integer.
        Returns:
            list[int]: A list containing two integers: [evenCount, oddCount].
        """
        evenCount = 0
        oddCount = 0
        index = 0
        while n > 0:
            if n & 1:
                if index % 2 == 0:
                    evenCount += 1
                else:
                    oddCount += 1

            n = n >> 1
            index = index + 1

        return [evenCount, oddCount]