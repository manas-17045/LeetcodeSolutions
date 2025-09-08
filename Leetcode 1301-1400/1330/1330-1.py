# Leetcode 1330: Reverse Subarray To Maximize Array Value
# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/
# Solved on 8th of September, 2025
class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        """
        Calculates the maximum possible array value after reversing at most one subarray.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The maximum array value achievable.
        """
        n = len(nums)
        originalValue = 0
        for i in range(n - 1):
            originalValue += abs(nums[i] - nums[i + 1])

        maxChange = 0

        for i in range(n - 1):
            delta = abs(nums[0] - nums[i + 1]) + abs(nums[i] - nums[i + 1])
            maxChange = max(maxChange, delta)

        for i in range(1, n):
            delta = abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1])
            maxChange = max(maxChange, delta)

        maxMinVal = float('-inf')
        minMaxVal = float('inf')

        for i in range(n - 1):
            a = nums[i]
            b = nums[i + 1]
            maxMinVal = max(maxMinVal, min(a, b))
            minMaxVal = min(minMaxVal, max(a, b))

        internalChange = 2 * (maxMinVal - minMaxVal)
        maxChange = max(maxChange, internalChange)

        return originalValue + maxChange