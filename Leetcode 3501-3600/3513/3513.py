# Leetcode 3513: Number of Unique XOR Triplets I
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/
# Solved on 4th of November, 2025
class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        """
        Calculates the number of unique XOR triplets.
        :param nums: A list of integers.
        :return: The number of unique XOR triplets.
        """
        n = len(nums)

        if n == 1:
            return 1

        if n == 2:
            return 2

        numBits = n.bit_length()
        return 1 << numBits