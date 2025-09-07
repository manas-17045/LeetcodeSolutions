# Leetcode 2289: Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/
# Solved on 7th of September, 2025
class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        """
        Calculates the maximum number of steps required to make the array non-decreasing.
        In each step, all elements nums[i] such that nums[i-1] > nums[i] are removed.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The maximum number of steps.
        """
        n = len(nums)
        stepCount = [0] * n
        monoStack = []

        for i in range(n):
            currentStep = 0
            while monoStack and nums[monoStack[-1]] <= nums[i]:
                currentStep = max(currentStep, stepCount[monoStack.pop()])

            if monoStack:
                stepCount[i] = currentStep + 1

            monoStack.append(i)

        return max(stepCount)