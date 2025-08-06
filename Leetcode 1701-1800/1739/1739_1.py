# Leetcode 1739: Building Boxes
# https://leetcode.com/problems/building-boxes/
# Solved on 6th of August, 2025
class Solution:
    def minimumBoxes(self, n: int) -> int:
        """
        Calculates the minimum number of boxes on the floor to build a structure
        with at least n boxes in total.

        Args:
            n: The total number of boxes to be placed in the structure.

        Returns:
            The minimum number of boxes that must be placed on the floor.
        """

        totalBoxes = 0
        floorBoxes = 0
        height = 0

        while totalBoxes + floorBoxes + height + 1 < n:
            height += 1
            floorBoxes += height
            totalBoxes += floorBoxes

        remainingBoxes = n - totalBoxes

        moreFloorBoxes = 0
        while remainingBoxes > 0:
            moreFloorBoxes += 1
            remainingBoxes -= moreFloorBoxes

        return floorBoxes + moreFloorBoxes