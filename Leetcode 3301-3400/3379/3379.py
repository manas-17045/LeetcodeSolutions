# Leetcode 3379: Transformed Array
# https://leetcode.com/problems/transformed-array/
# Solved on 12th of November, 2025
class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        """
        Constructs a transformed array based on the given input array.

        Args:
            nums: A list of integers.
        Returns:
            A list of integers representing the transformed array.
        """
        numLength = len(nums)
        result = [0] * numLength

        for i in range(numLength):
            currentValue = nums[i]
            newIndex = (i + currentValue) % numLength
            result[i] = nums[newIndex]

        return result