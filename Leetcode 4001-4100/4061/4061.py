# Leetcode 4061: Minimum Queen Moves to Reach Target
# https://leetcode.com/problems/minimum-queen-moves-to-reach-target/
# Solved on 28th of October, 2026
class Solution:
    def minQueenMoves(seld, source: list[int], target: list[int]) -> int:
        """
        Calculates the minimum number of queen moves required to reach the target square.

        Parameters:
            source (list[int]): Starting coordinates [row, column].
            target (list[int]): Target coordinates [row, column].

        Returns:
            int: The minimum moves needed (0, 1, or 2).
        """
        sourceRow, sourceCol = source
        targetRow, targetCol = target

        if sourceRow == targetRow and sourceCol == targetCol:
            return 0

        if (
            sourceRow == targetRow
            or sourceCol == targetCol
            or abs(sourceRow - targetRow) == abs(sourceCol - targetCol)
        ):
            return 1

        return 2