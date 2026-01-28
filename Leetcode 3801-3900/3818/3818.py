# Leetcode 3818: Minimum Prefix Removal to Make Array Strictly Increasing
# https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/
# Solved on 28th of January, 2026
class Solution:
    def minimumPrefixLength(self, nums: list[int]) -> int:
        """
        Calculates the minimum length of a prefix to remove from the array
        to make the remaining array strictly increasing.

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The minimum length of the prefix to be removed.
        """
        arrayLength = len(nums)
        suffixStart = arrayLength - 1

        while suffixStart > 0 and nums[suffixStart - 1] < nums[suffixStart]:
            suffixStart -= 1

        return suffixStart