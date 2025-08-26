# Leetcode 2910: Minimum Number of Groups to Create a Valid Assignment
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/
# Solved on 26th of August, 2025
import collections


class Solution:
    def minGroupsForValidAssignment(self, balls: list[int]) -> int:
        """
        Calculates the minimum number of groups required to create a valid assignment.
        Args:
            balls (list[int]): A list of integers representing the types of balls.
        Returns:
            int: The minimum number of groups.
        """
        countsMap = collections.Counter(balls)
        groupCounts = list(countsMap.values())
        minGroupCount = min(groupCounts)

        for minBoxSize in range(minGroupCount, 0, -1):
            isSizePossible = True
            totalBoxes = 0

            for count in groupCounts:
                boxesForCount = (count + minBoxSize) // (minBoxSize + 1)

                if boxesForCount * minBoxSize > count:
                    isSizePossible = False
                    break

                totalBoxes += boxesForCount

            if isSizePossible:
                return totalBoxes

        return -1