# Leetcode 3644: Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
# Solved on 18th of October, 2025
class Solution:
    def sortPermutation(self, nums: list[int]) -> int:

        """
        This function calculates the bitwise AND of all misplaced elements in a permutation.
        If the permutation is already sorted, it returns 0.

        :param nums: A list of integers representing the permutation.
        :return: The bitwise AND of all elements that are not in their sorted position,
                 or 0 if all elements are sorted or if the bitwise AND becomes 0 at any point.
        """

        ans = None
        for i, v in enumerate(nums):
            if v != i:
                if ans is None:
                    ans = v
                else:
                    ans &= v

                if ans == 0:
                    return 0

        return 0 if ans is None else ans