# Leetcode 3912: Valid Elements in an Array
# https://leetcode.com/problems/valid-elements-in-an-array/
# Solved on 10th of May, 2026
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        """
        Identifies valid elements in an array based on their relative values to neighbors.

        Args:
            nums (list[int]): A list of integers to evaluate.
        Returns:
            list[int]: A list containing the elements that satisfy the validity criteria.
        """
        listLength = len(nums)
        if listLength <= 1:
            return nums

        rightMaxValues = [0] * listLength
        currentRightMax = nums[-1]

        for index in range(listLength - 2, -1, -1):
            rightMaxValues[index] = currentRightMax
            if nums[index] > currentRightMax:
                currentRightMax = nums[index]

        validElements = []
        currentLeftMax = nums[0]

        for index in range(listLength):
            if index == 0 or index == listLength - 1 or nums[index] > currentLeftMax or nums[index] > rightMaxValues[index]:
                validElements.append(nums[index])

            if nums[index] > currentLeftMax:
                currentLeftMax = nums[index]

        return validElements