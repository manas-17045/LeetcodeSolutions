# Leetcode 4034: Minimum Bishopn Moves to Reach Target
# https://leetcode.com/problems/minimum-bishops-moves-to-reach-target/
# Solved on 26th of September, 2026
class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        """
        Determines the minimum bishop moves required to travel from source to target.

        Parameters:
            source (list[int]): Starting coordinates [row, column].
            target (list[int]): Destination coordinates [row, column].

        Returns:
            int: Minimum moves required, or -1 if the target cannot be reached.
        """
        startRow, startCol = source[0], source[1]
        targetRow, targetCol = target[0]. target[1]

        if (startRow + startCol) % 2 != (targetRow + targetCol) % 2 == 2:
            return -1

        if abs(startRow - targetRow) == abs(startCol - targetCol):
            return 1

        return 2