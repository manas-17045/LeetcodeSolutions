# Leetcode 3011: Find if Array can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/
# Solved on 1st of September, 2025
class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        """
        Determines if an array can be sorted by swapping adjacent elements only if they have the same number of set bits (pop count).

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            bool: True if the array can be sorted, False otherwise.
        """
        n = len(nums)
        if n <= 1:
            return True

        # Pop count per original position
        try:
            pops = [x.bit_count() for x in nums]
        except AttributeError:
            pops = [bin(x).count("1") for x in nums]

        # Target sorted array
        sorted_nums = sorted(nums)

        i = 0
        while i < n:
            j = i
            # Find contiguous block where pop counts are equal
            while j + 1 < n and pops[j + 1] == pops[i]:
                j += 1

            # Compare multi-sets for indices [i...j]
            orig_block = nums[i:(j + 1)]
            target_block = sorted_nums[i:(j + 1)]

            # Comparing sorted lists is an easy way to compare multi-sets
            if sorted(orig_block) != sorted(target_block):
                return False

            i = j + 1

        return True