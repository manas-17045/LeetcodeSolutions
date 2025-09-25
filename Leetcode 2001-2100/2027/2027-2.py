# Leetcode 2027: Minimum Moves to Convert String
# https://leetcode.com/problems/minimum-moves-to-convert-string/
# Solved on 25th of September, 2025
class Solution:
    def minimumMoves(self, s: str) -> int:
        """
        Calculates the minimum number of moves required to convert all 'X' characters in a string to 'O's.
        A move consists of changing 'X' to 'O' at the current position and the next two positions.

        Args:
            s (str): The input string consisting of 'X' and 'O' characters.

        Returns:
            int: The minimum number of moves.
        """
        i = 0
        n = len(s)
        moves = 0

        while i < n:
            if s[i] == 'X':
                moves += 1
                i += 3
            else:
                i += 1

        return moves