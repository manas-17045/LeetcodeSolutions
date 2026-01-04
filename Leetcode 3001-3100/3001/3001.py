# Leetcode 3001: Minimum Moves to Capture The Queen
# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/
# Solved on 4th of January, 2026
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        """
        Calculates the minimum number of moves required to capture the queen.

        Args:
            a (int): The x-coordinate of the rook.
            b (int): The y-coordinate of the rook.
            c (int): The x-coordinate of the bishop.
            d (int): The y-coordinate of the bishop.
            e (int): The x-coordinate of the queen.
            f (int): The y-coordinate of the queen.

        Returns:
            int: The minimum number of moves (1 or 2) to capture the queen.
        """
        if a == e and not (c == a and min(b, f) < d < max(b, f)):
            return 1

        if b == f and not (d == b and min(a, e) < c < max(a, e)):
            return 1

        if abs(c - e) == abs(d - f):
            if not ((c - e) * (d - b) == (d - f) * (c - a) and min(c, e) < a < max(c, e)):
                return 1

        return 2