# Leetcode 3309: Maximum Possible Number by Binary Concatenation
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/
# Solved on 26th of August, 2025
import itertools


class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible decimal number that can be formed by concatenating the binary representations
        of all possible permutations of the given list of integers.

        Args:
            nums (list[int]): A list of integers.
        Returns:
            int: The maximum decimal number formed by binary concatenation.
        """
        maxNumber = 0

        for permutation in itertools.permutations(nums):
            binaryString = "".join(bin(num)[2:] for num in permutation)
            currentValue = int(binaryString, 2)

            if currentValue > maxNumber:
                maxNumber = currentValue

        return maxNumber