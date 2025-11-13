# Leetcode 1861: Rotating the Box
# https://leetcode.com/problems/rotating-the-box/
# Solved on 13th of November, 2025
class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        """
        Rotates the given box grid 90 degrees clockwise and applies gravity.

        Args:
            boxGrid: A list of lists of strings representing the box.
        Returns:
            A list of lists of strings representing the rotated and gravitated box.
        """
        m = len(boxGrid)
        n = len(boxGrid[0])
        result = [['.'] * m for _ in range(n)]

        for i in range(m):
            targetCol = m - 1 - i
            writeRow = n - 1
            for j in range(n - 1, -1, -1):
                cell = boxGrid[i][j]
                if cell == '*':
                    result[j][targetCol] = '*'
                    writeRow = j - 1
                elif cell == '#':
                    result[writeRow][targetCol] = '#'
                    writeRow -= 1

        return result