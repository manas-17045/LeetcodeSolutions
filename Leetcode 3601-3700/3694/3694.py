# Leetcode 3694: Distinct Points Reachable After Substring Removal
# https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/
# Solved on 28th of December, 2025
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        """
        Calculates the number of distinct points reachable after removing a substring of length k.

        Args:
            s (str): The input string representing a sequence of moves (U, D, L, R).
            k (int): The length of the substring to be removed.
        Returns:
            int: The number of distinct points reachable.
        """
        totalX = 0
        totalY = 0
        for char in s:
            if char == 'U':
                totalY += 1
            elif char == 'D':
                totalY -= 1
            elif char == 'R':
                totalX += 1
            elif char == 'L':
                totalX -= 1

        windowX = 0
        windowY = 0
        for i in range(k):
            if s[i] == 'U':
                windowY += 1
            elif s[i] == 'D':
                windowY -= 1
            elif s[i] == 'R':
                windowX += 1
            elif s[i] == 'L':
                windowX -= 1

        distinctCoordinates = set()
        distinctCoordinates.add((totalX - windowX, totalY - windowY))

        for i in range(k, len(s)):
            leavingChar = s[i - k]
            enteringChar = s[i]

            if leavingChar == 'U':
                windowY -= 1
            elif leavingChar == 'D':
                windowY += 1
            elif leavingChar == 'R':
                windowX -= 1
            elif leavingChar == 'L':
                windowX += 1

            if enteringChar == 'U':
                windowY += 1
            elif enteringChar == 'D':
                windowY -= 1
            elif enteringChar == 'R':
                windowX += 1
            elif enteringChar == 'L':
                windowX -= 1

            distinctCoordinates.add((totalX - windowX, totalY - windowY))

        return len(distinctCoordinates)