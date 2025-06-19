# Leetcode 3219: Minimum Cost for Cutting Cake II
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/
# Solved on 19th of June, 2025

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        """
        Calculates the minimum cost to cut a cake into m x n pieces.

        The cost of a cut is the value of the cut multiplied by the number of pieces
        it cuts through. The goal is to minimize the total cost.

        The strategy is to always perform the cut with the highest cost first,
        as this cut will be multiplied by the smallest number of pieces.

        Args:
            m: The number of horizontal pieces (rows).
            n: The number of vertical pieces (columns).
            horizontalCut: A list of costs for horizontal cuts.
            verticalCut: A list of costs for vertical cuts.

        Returns:
            The minimum total cost to cut the cake.
        """
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        hIndex = 0
        vIndex = 0

        numHorizontalPieces = 1
        numVerticalPieces = 1

        totalCost = 0

        while hIndex < len(horizontalCut) and vIndex < len(verticalCut):
            costHorizontal = horizontalCut[hIndex]
            costVertical = verticalCut[vIndex]

            if costHorizontal >= costVertical:
                totalCost += costHorizontal * numVerticalPieces
                numHorizontalPieces += 1
                hIndex += 1
            else:
                # costVertical > costHorizontal
                totalCost += costVertical * numHorizontalPieces
                numVerticalPieces += 1
                vIndex += 1

        while hIndex < len(horizontalCut):
            costHorizontal = horizontalCut[hIndex]
            totalCost += costHorizontal * numVerticalPieces
            numHorizontalPieces += 1
            hIndex += 1

        while vIndex < len(verticalCut):
            costVertical = verticalCut[vIndex]
            totalCost += costVertical * numHorizontalPieces
            numVerticalPieces += 1
            vIndex += 1

        return totalCost