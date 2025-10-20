# Leetcode 2943: Maximize Area of Square Hole in Grid
# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/
# Solved on 20th of October, 2025
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:

        def getMaxSide(bars: list[int]) -> int:
            barSet = set(bars)
            maxLength = 0

            for bar in barSet:
                if (bar - 1) not in barSet:
                    currentLength = 1
                    currentBar = bar

                    while (currentBar + 1) in barSet:
                        currentLength += 1
                        currentBar += 1

                    maxLength = max(maxLength, currentLength)

            return maxLength + 1

        maxHSide = getMaxSide(hBars)
        maxVSide = getMaxSide(vBars)

        squareSide = min(maxHSide, maxVSide)

        return squareSide * squareSide