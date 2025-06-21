# Leetcode 1835: Find XOR Sum of All pairs Bitwise AND
# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/
# Solved on 21st of June, 2025
class Solution:
    def getXORSum(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Calculates the bitwise AND of the XOR sum of elements in arr1 and the XOR sum of elements in arr2.

        The problem statement implies that the XOR sum of all possible (a AND b) pairs, where a is from arr1 and b is from arr2,
        is equivalent to (XOR sum of arr1) AND (XOR sum of arr2).

        :param arr1: A list of integers.
        :param arr2: A list of integers.
        :return: The bitwise AND of the XOR sum of arr1 and the XOR sum of arr2.
        """
        # Compute the XOR of all elements in arr1
        xor1 = 0
        for a in arr1:
            xor1 ^= a

        # Compute the XOR of all elements in arr2
        xor2 = 0
        for b in arr2:
            xor2 ^= b

        # Return the bitwise AND of xor1 and xor2
        return xor1 & xor2