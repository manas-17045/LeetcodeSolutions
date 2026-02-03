# Leetcode 3637: Trionic Array I
# https://leetcode.com/problems/trionic-array-i/
# Solved on 3rd of February, 2026
class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        """
        Determines if the given array is a Trionic array.
        A Trionic array must strictly increase, then strictly decrease, then strictly increase.

        :param nums: A list of integers to be checked.
        :return: True if the array is Trionic, False otherwise.
        """
        arrayLength = len(nums)
        if arrayLength < 4:
            return False

        currentIndex = 1

        while currentIndex < arrayLength and nums[currentIndex] > nums[currentIndex - 1]:
            currentIndex += 1

        if currentIndex == 1 or currentIndex == arrayLength:
            return False

        currentPeak = currentIndex - 1

        while currentIndex < arrayLength and nums[currentIndex] < nums[currentIndex - 1]:
            currentIndex += 1

        currentValley = currentIndex - 1

        if currentValley == currentPeak or currentIndex == arrayLength:
            return False

        while currentIndex < arrayLength and nums[currentIndex] > nums[currentIndex - 1]:
            currentIndex += 1

        return currentIndex == arrayLength