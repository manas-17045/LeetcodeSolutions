# Leetcode 3819: Rotate Non Negative Elements
# https://leetcode.com/problems/rotate-non-negative-elements/
# Solved on 26th of January, 2026
class Solution:
    def rotateElements(self, nums: list[int], k: int) -> list[int]:
        """
        Rotates non-negative elements in the list by k positions to the left,
        while keeping negative elements in their original positions.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The number of positions to rotate.

        Returns:
            list[int]: The list with rotated non-negative elements.
        """
        nonNegativeList = [num for num in nums if num >= 0]
        count = len(nonNegativeList)

        if count == 0:
            return nums

        k %= count
        rotatedNonNegative = nonNegativeList[k:] + nonNegativeList[:k]

        resultList = []
        pointerIndex = 0

        for num in nums:
            if num < 0:
                resultList.append(num)
            else:
                resultList.append(rotatedNonNegative[pointerIndex])
                pointerIndex += 1

        return resultList