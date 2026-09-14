# Leetcode 836: Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/
# Solved on 14th of September, 2026
class Solution:
    def isRectanglePverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        """
        Determines whether two axis-aligned rectangles overlap with a positive area.

        Parameters:
            rec1 (List[int]): Coordinates of the first rectangle as [x1, y1, x2, y2].
            rec2 (List[int]): Coordinates of the second rectangle as [x1, y1, x2, y2].

        Returns:
            bool: True if the two rectangles overlap with positive area, False otherwise.
        """
        leftOne, bottomOne, rightOne, topOne = rec1
        leftTwo, bottomTwo, rightTwo, topTwo = rec2

        hasHorizontalOverlap = leftOne < rightTwo and leftTwo < rightOne
        hasVerticalOverlap = bottomOne < topTwo and bottomTwo < topOne

        return hasHorizontalOverlap and hasVerticalOverlap