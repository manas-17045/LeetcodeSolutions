# Leetcode 2038: Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Solved on 4th of November, 2025
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        Determines if Alice wins the game of removing colored pieces.

        Args:
            colors (str): A string representing the colors of the pieces.

        Returns:
            bool: True if Alice wins, False otherwise.
        """
        aliceMoves = 0
        bobMoves = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    aliceMoves += 1
                else:
                    bobMoves += 1

        return aliceMoves > bobMoves