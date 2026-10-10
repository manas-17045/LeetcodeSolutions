# Leetcode 4048: Count Values With Equally Spaced Occurrences I
# https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/
# Solved on 10th of October, 2026
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        """
        Counts the number of distinct special integers in the given array.
        An integer is special if it appears exactly three times and all three 
        occurrences are equally spaced.

        Args:
            nums (list[int]): The input array of integers.

        Returns:
            int: The number of distinct special integers found in the array.
        """
        occurrenceMap = {}

        for index, value in enumerate(nums):
            if value not in occurrenceMap:
                occurrenceMap[value] = []
            occurrenceMap[value].append(index)
        
        specialCount = 0

        for indices in occurrenceMap.values():
            if len(indices) == 3:
                if indices[1] - indices[0] == indices[2] - indices[1]:
                    specialCount += 1
        
        return specialCount