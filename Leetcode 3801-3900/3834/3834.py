# Leetcode 3834: Merge Adjacent Equal Elements
# https://leetcode.com/problems/merge-adjacent-equal-elements/
# Solved on 9th of February, 2026
class Solution:
    def mergeAdjacent(self, nums: list[int]) -> list[int]:
        """
        Merges adjacent equal elements in a list by summing them up repeatedly.

        :param nums: A list of integers to be processed.
        :return: A list of integers after all possible adjacent equal merges are completed.
        """
        numberStack = []

        for currentNum in nums:
            numberStack.append(currentNum)
            while len(numberStack) >= 2 and numberStack[-1] == numberStack[-2]:
                topValue = numberStack.pop()
                numberStack[-1] += topValue

        return numberStack