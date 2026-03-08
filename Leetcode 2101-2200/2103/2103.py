# Leetcode 2103: Rings and Rods
# https://leetcode.com/problems/rings-and-rods/
# Solved on 8th of March, 2026
class Solution:
    def countPoints(self, rings: str) -> int:
        """
        Counts the number of rods that have all three colors (Red, Green, Blue) of rings.

        :param rings: A string describing the rings on each rod.
        :return: The total number of rods containing all three colors.
        """
        rodMasks = [0] * 10
        for i in range(0, len(rings), 2):
            color = rings[i]
            rodIndex = int(rings[i + 1])
            if color == 'R':
                rodMasks[rodIndex] |= 1
            elif color == 'G':
                rodMasks[rodIndex] |= 2
            elif color == 'B':
                rodMasks[rodIndex] |= 4

        validRodsCount = 0
        for mask in rodMasks:
            if mask == 7:
                validRodsCount += 1

        return validRodsCount