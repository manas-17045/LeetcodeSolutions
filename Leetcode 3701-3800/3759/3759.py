# Leetcode 3759: Count Elements With at Least K Greater Values
# https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/
# Solved on 26th of December, 2025
class Solution:
    def countElements(self, nums: list[int], k: int) -> int:
        """
        Counts the number of elements in the array that have at least k greater values.

        Args:
            nums: A list of integers.
            k: An integer representing the minimum number of greater values required.

        Returns:
            An integer representing the count of elements with at least k greater values.
        """

        if k == 0:
            return len(nums)

        nums.sort(reverse=True)
        thresholdValue = nums[k - 1]
        arrayLength = len(nums)

        for index in range(k, arrayLength):
            if nums[index] < thresholdValue:
                return arrayLength - index

        return 0