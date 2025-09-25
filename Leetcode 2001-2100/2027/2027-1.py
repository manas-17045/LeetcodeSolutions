# Leetcode 2027: Minimum Moves to Convert String
# https://leetcode.com/problems/minimum-moves-to-convert-string/
# Solved on 25th of September, 2025
class Solution:
    def minimumMoves(self, s: str) -> int:
        """
        Calculates the minimum number of moves required to convert all 'X' characters to 'O' characters.
        A move consists of changing an 'X' to 'O' and the next two characters (if they exist) to 'O'.

        Args:
            s (str): The input string consisting of 'X' and 'O' characters.
        Returns:
            int: The minimum number of moves.
        """
        numMoves = 0
        index = 0
        stringLength = len(s)

        while index < stringLength:
            if s[index] == 'X':
                numMoves += 1
                index += 3
            else:
                index += 1

        return numMoves