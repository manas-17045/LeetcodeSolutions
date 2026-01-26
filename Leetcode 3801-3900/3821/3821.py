# Leetcode 3821: Find Nth Smallest Integer With K One Bits
# https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/
# Solved on 26th of January, 2026
import math


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        """
        Finds the nth smallest integer with exactly k one bits in its binary representation.

        Args:
            n (int): The rank of the integer to find (1-indexed).
            k (int): The number of set bits (one bits) required.

        Returns:
            int: The nth smallest integer with k set bits.
        """
        currentRank = n - 1
        result = 0
        upperBound = 50

        for i in range(k, 0, -1):
            currentPos = upperBound

            while True:
                combinations = math.comb(currentPos, i)
                if combinations <= currentRank:
                    break
                currentPos -= 1

            result |= (1<< currentPos)

            currentRank -= math.comb(currentPos, i)
            upperBound = currentPos - 1

        return result