# Leetcode 3219: Minimum Cost for Cutting Cake II
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/
# Solved on 19th of June, 2025

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        """
        Calculates the minimum cost to cut a chocolate bar of size m x n into 1x1 squares.

        The cost of a horizontal cut is given by horizontalCuts[i] and the cost of a
        vertical cut is given by verticalCuts[j]. The cost of a cut is multiplied by
        the number of pieces it cuts through.

        Args:
            m: The number of rows in the chocolate bar.
            n: The number of columns in the chocolate bar.
            horizontalCuts: A list of costs for horizontal cuts.
            verticalCuts: A list of costs for vertical cuts.

        Returns:
            The minimum cost to cut the chocolate bar into 1x1 squares.
        """
        # Sort both cost arrays descending
        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)

        # Number of current segments in each direction
        h_pieces = 1    # Horizontal stripes
        v_pieces = 1    # Vertical stripes

        i = j = 0   # Pointers into horizontalCut and verticalCut
        total = 0

        # Greedily take the next largest cost cut
        while i < len(horizontalCuts) and j < len(verticalCuts):
            # If next horizontal cut is >= next vertical cut, do horizontal
            if horizontalCuts[i] >= verticalCuts[j]:
                total += horizontalCuts[i] * v_pieces
                h_pieces += 1
                i += 1
            else:
                total += verticalCuts[j] * h_pieces
                v_pieces += 1
                j += 1

        # If any cuts remain in horizontalCut
        while i < len(horizontalCuts):
            total += horizontalCuts[i] * v_pieces
            i += 1

        # If any cuts remain in verticalCut
        while j < len(verticalCuts):
            total += verticalCuts[j] * h_pieces
            j += 1

        return total