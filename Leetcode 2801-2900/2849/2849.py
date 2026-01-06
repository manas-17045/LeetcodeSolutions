# Leetcode 2849: Determine if a Cell Is Reachable at a Given Time
# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
# Solved on 6th of January, 2026
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """
        Determines if a cell (fx, fy) is reachable from (sx, sy) in exactly 't' seconds.
        A move can be made to any of the 8 adjacent cells (including diagonals) or stay in the current cell.

        Args:
            sx (int): The starting x-coordinate.
            sy (int): The starting y-coordinate.
            fx (int): The finishing x-coordinate.
            fy (int): The finishing y-coordinate.
            t (int): The time in seconds.
        Returns:
            bool: True if the cell is reachable in 't' seconds, False otherwise.
        """
        xDiff = abs(sx - fx)
        yDiff = abs(sy - fy)
        minSteps = max(xDiff, yDiff)

        if minSteps == 0 and t == 1:
            return False

        return t >= minSteps