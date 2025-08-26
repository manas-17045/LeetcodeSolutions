# Leetcode 3309: Maximum Possible Number by Binary Concatenation
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/
# Solved on 26th of August, 2025
from itertools import permutations


class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        """
        Calculates the maximum "good number" by concatenating three given numbers in all possible permutations.
        A "good number" is formed by concatenating the binary representations of three numbers.
        :param nums: A list of three integers [n1, n2, n3], where n1, n2, n3 >= 1.
        :return: The maximum good number that can be formed.
        """
        # Precompute bit-lengths for each element (no leading zeros since nums[i] >= 1)
        blens = [x.bit_length() for x in nums]

        best = 0
        # Enumerate all permutations of indices (0,1,2)
        for i, j, k in permutations(range(3), 3):
            # Binary concatenation
            val = (nums[i] << (blens[j] + blens[k])) | (nums[j] << blens[k]) | nums[k]
            if val > best:
                best = val

        return best