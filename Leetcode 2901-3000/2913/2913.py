# Leetcode 2913: Subarrays Distinct Element Sum of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Solved on 15th of October, 2026
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        """
        Calculate the sum of squares of distinct counts across all subarrays.
        
        Args:
            nums (list[int]): The list of integers to evaluate.
            
        Returns:
            int: The sum of squares of distinct element counts of all subarrays.
        """
        totalSum = 0
        totalLength = len(nums)

        for startIndex in range(totalLength):
            seenElements = set()
            distinctCount = 0

            for endIndex in range(startIndex, totalLength):
                currentNum = nums[endIndex]

                if currentNum not in seenElements:
                    seenElements.add(currentNum)
                    distinctCount += 1

                totalSum += distinctCount * distinctCount

        return totalSum