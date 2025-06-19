# Leetcode 3218: Minimum Cost for Cutting Cake I
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/
# Solved on 19th of June, 2025

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        """
        Calculates the minimum cost to cut a cake of size m x n into 1x1 pieces.

        The cost of a horizontal cut is multiplied by the number of vertical segments it crosses.
        The cost of a vertical cut is multiplied by the number of horizontal segments it crosses.

        Args:
            m: The number of rows in the cake.
            n: The number of columns in the cake.
            horizontalCut: A list of costs for horizontal cuts.
            verticalCut: A list of costs for vertical cuts.

        Returns:
            The minimum total cost to cut the cake.
        """
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        horizontalIndex = 0
        verticalIndex = 0

        horizontalSegments = 1
        verticalSegments = 1

        totalCost = 0

        numHorizontalCutsToMake = m - 1
        numVerticalCutsToMake = n - 1

        while horizontalIndex < numHorizontalCutsToMake or verticalIndex < numVerticalCutsToMake:
            shouldTakeHorizontalCut = False

            if horizontalIndex >= numHorizontalCutsToMake:
                shouldTakeHorizontalCut = False
            elif verticalIndex >= numVerticalCutsToMake:
                shouldTakeHorizontalCut = True
            else:
                if horizontalCut[horizontalIndex] >= verticalCut[verticalIndex]:
                    shouldTakeHorizontalCut = True
                else:
                    shouldTakeHorizontalCut = False

            if shouldTakeHorizontalCut:
                currentCutCost = horizontalCut[horizontalIndex]
                totalCost += currentCutCost * verticalSegments
                horizontalSegments += 1
                horizontalIndex += 1
            else:
                currentCutCost = verticalCut[verticalIndex]
                totalCost += currentCutCost * horizontalSegments
                verticalSegments += 1
                verticalIndex += 1

        return totalCost