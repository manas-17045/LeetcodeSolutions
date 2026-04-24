# Leetcode 2833: Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/
# Solved on 24th of April, 2026
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        """
        Calculates the maximum possible distance from the origin after replacing all '_' with 'L' or 'R'.

        :param moves: A string consisting of 'L', 'R', and '_' characters.
        :return: The maximum absolute distance from the origin (0).
        """
        currentPosition = 0
        blankSpaces = 0

        for currentMove in moves:
            if currentMove == 'L':
                currentPosition -= 1
            elif currentMove == 'R':
                currentPosition += 1
            else:
                blankSpaces += 1

        return abs(currentPosition) + blankSpaces