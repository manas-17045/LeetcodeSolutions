# Leetcode 1846: Maximum Element After Decreasing and Rearranging
# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
# Solved on 3rd of September, 2025
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        """
        Given an array of positive integers, rearrange and decrement elements to satisfy two conditions:
        1. The first element of the modified array must be 1.
        2. The absolute difference between any two adjacent elements must be at most 1.
        The goal is to return the maximum possible value of an element in the modified array.
        :param arr: A list of positive integers.
        :return: The maximum possible value of an element in the modified array.
        """
        arr.sort()

        # Enforce the first condition: the first element must be 1.
        arr[0] = 1

        # Iterate through the array to enforce the second condition.
        for i in range(1, len(arr)):
            # The difference between adjacent elements must be at most 1.
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1

        # The maximum element is the last one after modification.
        return arr[-1]