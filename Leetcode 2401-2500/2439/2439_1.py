# Leetcode 2439: Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/
# Solved on 3rd of August, 2025
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        """
        Minimizes the maximum value of the array after performing operations.

        :param nums: A list of integers.
        :return: The minimized maximum value of the array.
        """
        prefixSum = 0
        ans = 0
        for i, num in enumerate(nums):
            prefixSum += num

            currentMax = (prefixSum + i) // (i + 1)

            if currentMax > ans:
                ans = currentMax

        return ans