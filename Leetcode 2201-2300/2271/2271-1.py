# Leetcode 2271: Maximum White Tiles Covered by a Carpet
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
# Solved on 7th of October, 2025
class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        """
        Calculates the maximum number of white tiles that can be covered by a carpet of a given length.

        :param tiles: A list of lists, where each inner list `[start, end]` represents a segment of white tiles.
        :param carpetLen: The length of the carpet.
        :return: The maximum number of white tiles that can be covered.
        """
        tiles.sort()

        numTiles = len(tiles)

        maxCoverage = 0
        currentCovered = 0
        leftIndex = 0

        for rightIndex in range(numTiles):
            rightStart, rightEnd = tiles[rightIndex]

            # The carpet being considered ends at rightEnd.
            carpetStart = rightEnd - carpetLen + 1

            # Add the full length of the new tile to the running sum
            currentCovered += (rightEnd - rightStart + 1)

            # Shrink the window from the left by removing tiles that are completely to the left of the current carpet
            while tiles[leftIndex][1] < carpetStart:
                leftStart, leftEnd = tiles[leftIndex]
                currentCovered -= (leftEnd - leftStart + 1)
                leftIndex += 1

            leftStartOfWindow = tiles[leftIndex][0]

            missedOnLeft = 0
            if leftStartOfWindow < carpetStart:
                missedOnLeft = carpetStart - leftStartOfWindow

            potentialCoverage = currentCovered - missedOnLeft
            maxCoverage = max(maxCoverage, potentialCoverage)

        return maxCoverage