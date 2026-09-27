# Leetcode 4035: Maximum Valid Split Positions I
# https://leetcode.com/problems/maximum-valid-split-positions-i/
# Solved on 27th of September, 2026
import math


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        """
        Finds the maximum possible score by removing at most one element.

        Parameters:
            nums (list[int]): The initial sequence of integers.

        Returns:
            int: The maximum number of valid split positions achievable.
        """
        totalLength = len(nums)
        maxScore = self.computeScore(nums)

        if maxScore >= totalLength - 2:
            return maxScore

        for removalIndex in range(totalLength):
            candidateArray = nums[:removalIndex] + nums[removalIndex + 1:]
            currentScore = self.computeScore(candidateArray)
            if currentScore > maxScore:
                maxScore = currentScore
                if maxScore >= totalLength - 2:
                    return maxScore

        return maxScore

    def computeScore(self, currentList: list[int]) -> int:

        listLength = len(currentList)
        if listLength < 2:
            return 0

        suffixGcd = [0] * listLength
        suffixGcd[listLength - 1] = currentList[listLength - 1]
        for scanIndex in range(listLength - 2, -1, -1):
            suffixGcd[scanIndex] = math.gcd(suffixGcd[scanIndex + 1], currentList[scanIndex])

        validCount = 0
        prefixGcd = 0
        for splitIndex in range(listLength - 1):
            prefixGcd = math.gcd(prefixGcd, currentList[splitIndex])
            if prefixGcd == suffixGcd[splitIndex + 1]:
                validCount += 1

        return validCount