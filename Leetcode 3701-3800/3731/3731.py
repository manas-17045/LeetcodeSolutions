# Leetcode 3731: Find Missing Elements
# https://leetcode.com/problems/find-missing-elements/
# Solved on 4th of August, 2026
class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        """
        Finds the missing elements in an array of integers.
        
        @param nums: The array of integers.
        @return: A list of missing integers.
        """
        numSet = set(nums)

        minVal = min(nums)
        maxVal = max(nums)

        missingNums = []
        for currentNum in range(minVal, maxVal + 1):
            if currentNum not in numSet:
                missingNums.append(currentNum)

        return missingNums