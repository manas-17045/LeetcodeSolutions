# Leetcode 2826: Sorting Three Groups
# https://leetcode.com/problems/sorting-three-groups/
# Solved on 6th of January, 2026
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to sort the given array into three groups.
        An operation consists of changing a number's value. The goal is to make the array
        non-decreasing, where elements are grouped such that all 1s come first, then all 2s,
        then all 3s.

        Args:
            nums: A list of integers, where each integer is 1, 2, or 3.
        Returns:
            The minimum number of operations required.
        """
        seqEnding1 = 0
        seqEnding2 = 0
        seqEnding3 = 0

        for num in nums:
            if num == 1:
                seqEnding1 += 1
            elif num == 2:
                seqEnding2 = max(seqEnding1, seqEnding2) + 1
            else:
                seqEnding3 = max(seqEnding1, seqEnding2, seqEnding3) + 1

        longestSubsequence = max(seqEnding1, seqEnding2, seqEnding3)
        return len(nums) - longestSubsequence