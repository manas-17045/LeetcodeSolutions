# Leetcode 657: Robots Return to Origin
# https://leetcode.com/problems/robots-return-to-origin/
# Solved on 5th of April, 2026
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determines if the robot returns to the origin (0, 0) after a sequence of moves.

        :param moves: A string representing the sequence of moves ('R', 'L', 'U', 'D').
        :return: True if the robot ends at (0, 0), False otherwise.
        """
        xCoordinate = 0
        yCoordinate = 0

        for currentMove in moves:
            if currentMove == 'R':
                xCoordinate += 1
            elif currentMove == 'L':
                xCoordinate -= 1
            elif currentMove == 'U':
                yCoordinate += 1
            elif currentMove == 'D':
                yCoordinate -= 1

        return xCoordinate == 0 and yCoordinate == 0