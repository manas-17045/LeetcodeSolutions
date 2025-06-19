# Leetcode 3218: Minimum Cost for Cutting Cake I
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/
# Solved on 19th of June, 2025

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        """
        Calculates the minimum cost to cut a chocolate bar of size m x n into 1x1 squares.

        The cost of a horizontal cut is applied across all current vertical segments,
        and the cost of a vertical cut is applied across all current horizontal segments.
        To minimize the total cost, we should always perform the cut with the largest
        remaining cost first, as it will be multiplied by the current number of segments
        in the other direction.

        Args:
            m: The number of rows in the chocolate bar.
            n: The number of columns in the chocolate bar.
            horizontalCuts: A list of costs for horizontal cuts.
            verticalCuts: A list of costs for vertical cuts.

        Returns:
            The minimum total cost to cut the chocolate bar.
        """
        # Sort both cuts in descending, s we always pick the largest remaining cut
        horizontalCuts.sort(reverse=True)
        verticalCuts.sort(reverse=True)

        # Pointers to horizontalCut, verticalCut
        i = j = 0
        # Current number of horizontal pieces
        h_segments = 1
        # Current number of vertical pieces
        v_segments = 1
        # Total cost
        total_cost = 0

        # While both types of cuts remain, pick the larger cost
        while i < len(horizontalCuts) and j < len(verticalCuts):
            if horizontalCuts[i] > verticalCuts[j]:
                # Do a horizontal cut across all current vertical segments
                total_cost += horizontalCuts[i] * v_segments
                h_segments += 1
                i += 1
            else:
                # Do a vertical cut across all current horizontal segments
                total_cost += verticalCuts[j] * h_segments
                v_segments += 1
                j += 1

        # Finish any remaining horizontal cuts
        while i < len(horizontalCuts):
            total_cost += horizontalCuts[i] * v_segments
            i += 1

        # Finish any remaining vertical cuts
        while j < len(verticalCuts):
            total_cost += verticalCuts[j] * h_segments
            j += 1

        return total_cost