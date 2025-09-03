# Leetcode 1846: Maximum Element After Decreasing and Rearranging
# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
# Solved on 3rd of September, 2025
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        """
        Given an array of positive integers, rearrange and decrement elements to maximize the final element.
        The first element must be 1, and the absolute difference between adjacent elements must be at most 1.

        :param arr: A list of positive integers.
        :return: The maximum possible value of the last element after performing the operations.
        """
        if not arr:
            return 0
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]