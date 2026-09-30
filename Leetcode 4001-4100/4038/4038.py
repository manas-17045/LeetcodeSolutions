# Leetcode 4038: Count Integers Appearing in a Single Block
# https://leetcode.com/problems/count-integers-appearing-in-a-single-block/
# Solved on 30th of September, 2026
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        """
        Counts the number of distinct integers appearing in a single contiguous block.

        Parameters:
            nums (list[int]): An array of integers.

        Returns:
            int: The total count of distinct special integers.
        """
        seenValues = set()
        invalidValues = set()
        previousValue = None

        for currentValue in nums:
            if currentValue != previousValue:
                if currentValue in seenValues:
                    invalidValues.add(currentValue)
                else:
                    seenValues.add(currentValue)
            previousValue = currentValue

        return len(seenValues - invalidValues)