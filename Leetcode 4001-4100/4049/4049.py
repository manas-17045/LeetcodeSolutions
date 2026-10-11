# Leetcode 4049: Count Values With Equally Spaced Occurrences II
# https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-ii/
# Solved on 11th of October, 2026
import collections


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        """
        Counts the number of distinct integers in the array that appear at least
        three times with equally spaced occurrences throughout the array.

        Parameters:
            nums (list[int]): The list of integers to evaluate.

        Returns:
            int: The count of distinct special integers.
        """
        indexMap = collections.defaultdict(list)
        for currentIndex, numValue in enumerate(nums):
            indexMap[numValue].append(currentIndex)
        
        specialCount = 0
        for indexList in indexMap.values():
            totalOccurrences = len(indexList)
            if totalOccurrences < 3:
                continue

            stepSize = indexList[1] - indexList[0]
            isEquallySpaced = True

            for loopIndex in range(2, totalOccurrences):
                if indexList[loopIndex] - indexList[loopIndex - 1] != stepSize:
                    isEquallySpaced = False
                    break

            if isEquallySpaced:
                specialCount += 1

        return specialCount