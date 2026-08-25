# Leetcode 3718: Smallest Missing Multiple of K
# https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Solved on 25th of August, 2026
class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        """
        Finds the smallest positive multiple of k that does not appear in the given list of integers.

        Parameters:
            nums (List[int]): The list of positive integers.
            k (int): The positive integer whose multiples are checked.

        Returns:
            int: The smallest positive multiple of k missing from nums.
        """
        nSet = set(nums)
        cMultiple = k

        while cMultiple in nSet:
            cMultiple += k

        return cMultiple