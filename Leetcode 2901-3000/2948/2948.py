# Leetcode 2948: Make Lexicographically Smallest Array by Swapping Elements
# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/
# solved on the 29th of August, 2026
from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        """
        Rearranges the array to be lexicographically smallest by swapping pairs
        of elements whose absolute difference is within the specified limit.

        Parameters:
            nums (List[int]): The input array of positive integers.
            limit (int): The maximum allowed difference between two swappable values.

        Returns:
            List[int]: The lexicographically smallest array possible after valid swaps.
        """
        sortedNums = sorted(nums)
        numToGroup = {}
        groupToList = {}
        currentGroup = 0

        numToGroup[sortedNums[0]] = currentGroup
        groupToList[currentGroup] = deque([sortedNums[0]])

        for i in range(1, len(sortedNums)):
            if sortedNums[i] - sortedNums[i - 1] > limit:
                currentGroup += 1

            numToGroup[sortedNums[i]] = currentGroup
            if currentGroup not in groupToList:
                groupToList[currentGroup] = deque()
            groupToList[currentGroup].append(sortedNums[i])

        resultList = []
        for num in nums:
            groupIndex = numToGroup[num]
            resultList.append(groupToList[groupIndex].popleft())

        return resultList