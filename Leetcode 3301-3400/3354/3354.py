# Leetcode 3354: Make Array Elements Equal to Zero
# https://leetcode.com/problems/make-array-elements-equal-to-zero/
# Solved on 28th of October, 2025
class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        """
        Counts the number of valid starting selections (index and direction) that can make all array elements zero.

        Args:
            nums: A list of integers representing the array.
        Returns:
            The total count of valid starting selections.
        """
        n = len(nums)
        startIndices = []
        for i in range(n):
            if nums[i] == 0:
                startIndices.append(i)

        def isAllZero(arr):
            for val in arr:
                if val != 0:
                    return False
            return True

        def runSimulation(startIndex, startDirection):
            currentNums = list(nums)
            curr = startIndex
            dr = startDirection

            while 0 <= curr < n:
                if currentNums[curr] > 0:
                    currentNums[curr] -= 1
                    dr = -dr
                    curr += dr
                else:
                    curr += dr

            return isAllZero(currentNums)

        validSelections = 0
        for index in startIndices:
            if runSimulation(index, -1):
                validSelections += 1

            if runSimulation(index, 1):
                validSelections += 1

        return validSelections