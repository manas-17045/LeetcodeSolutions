# Leetcode 2598: Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/
# Solved on 16th of October, 2025
class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        """
        Finds the smallest non-negative integer that is not present in the array after applying operations.

        Args:
            nums: A list of integers.
            value: An integer representing the modulo value for operations.

        Returns:
            The smallest non-negative integer not present after operations.
        """

        remCounts = [0] * value
        for num in nums:
            remCounts[num % value] += 1

        mex = 0
        while True:
            reqRem = mex % value
            if remCounts[reqRem] > 0:
                remCounts[reqRem] -= 1
                mex += 1
            else:
                break

        return mex