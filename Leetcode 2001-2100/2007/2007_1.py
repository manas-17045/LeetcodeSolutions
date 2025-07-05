# Leetcode 2007: Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/
# Solved on 5th of July, 2025
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        """
        Given a changed array, return the original array if changed is a doubled array.
        A doubled array is formed by appending twice the value of each element in the original array.
        If changed is not a doubled array, return an empty array.

        Args:
            changed (list[int]): The array to check.

        Returns:
            list[int]: The original array if changed is a doubled array, otherwise an empty array.
        """
        numElements = len(changed)
        if numElements % 2 != 0:
            return []

        counts = Counter(changed)
        originalArray = []

        sortedKeys = sorted(counts.keys())

        for num in sortedKeys:
            if counts[num] == 0:
                continue

            if num == 0:
                if counts[num] % 2 != 0:
                    return []
                countOfNum = counts[num]
                originalArray.extend([0] * (countOfNum // 2))
                counts[num] = 0
                continue

            doubleNum = num * 2
            countOfNum = counts[num]

            if counts.get(doubleNum, 0) < countOfNum:
                return []

            originalArray.extend([num] * countOfNum)
            counts[doubleNum] -= countOfNum
            counts[num] = 0

        return originalArray