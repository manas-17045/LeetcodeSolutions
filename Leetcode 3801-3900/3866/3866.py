# Leetcode 3866: First Unique Even Element
# https://leetcode.com/problems/first-unique-even-element/
# Solved on 17th of March, 2026
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        """
        Finds the first even integer in the list that appears exactly once.

        :param nums: A list of integers to search through.
        :return: The first unique even integer found, or -1 if none exist.
        """
        frequencyMap = {}
        for num in nums:
            if num % 2 == 0:
                frequencyMap[num] = frequencyMap.get(num, 0) + 1

        for num in nums:
            if num % 2 == 0 and frequencyMap[num] == 1:
                return num

        return -1