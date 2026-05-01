# Leetcode 396: Rotate Function
# https://leetcode.com/problems/rotate-function/
# Solved on 1st of May, 2026
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        """
        Calculates the maximum value of F(0), F(1), ..., F(n-1) for a given array.

        :param nums: A list of integers.
        :return: The maximum value among all rotation functions.
        """
        arrLen = len(nums)
        totalSum = sum(nums)
        currentVal = 0

        for i in range(arrLen):
            currentVal += i * nums[i]

        maxVal = currentVal

        for i in range(1, arrLen):
            currentVal += totalSum - arrLen * nums[arrLen - i]
            if currentVal > maxVal:
                maxVal = currentVal

        return maxVal