# Leetcode 2659: Make Array Empty
# https://leetcode.com/problems/make-array-empty/
# Solved on 7th of June, 2025

class Solution:
    def countOperationsToEmptyArray(self, nums: list[int]) -> int:
        """
        Counts the minimum number of operations to empty the array.

        An operation consists of finding the smallest element, removing it,
        and rotating the remaining elements to the left.

        Args:
            nums: The input list of integers.

        Returns:
            The minimum number of operations to empty the array.
        """
        pos = {val: i for i, val in enumerate(nums)}
        n = len(nums)
        ans = n
        sNums = sorted(nums)
        for i in range(1, n):
            currPos = pos[sNums[i]]
            prevPos = pos[sNums[i - 1]]
            if currPos < prevPos:
                ans += n - i
        return ans