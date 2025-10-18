# Leetcode 3644: Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
# Solved on 18th of October, 2025
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        """
        This function calculates the maximum K such that a permutation can be sorted by repeatedly swapping elements
        at indices i and i XOR K.

        Args:
            nums (list[int]): A 0-indexed permutation of numbers from 0 to n-1.
        Returns:
            int: The maximum K that allows sorting the permutation, or 0 if the permutation is already sorted.
        """
        arrayLength = len(nums)
        misplacedIndices = set()

        for index in range(arrayLength):
            if nums[index] != index:
                misplacedIndices.add(index)

        if not misplacedIndices:
            return 0

        maxK = -1
        for index in misplacedIndices:
            if maxK == -1:
                maxK = index
            else:
                maxK = maxK & index

        return maxK