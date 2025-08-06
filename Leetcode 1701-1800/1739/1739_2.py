# Leetcode 1739: Building Boxes
# https://leetcode.com/problems/building-boxes/
# Solved on 6th of August, 2025
import math


class Solution:
    def minimumBoxes(self, n: int) -> int:
        """
        Calculates the minimum number of boxes on the floor required to store at least n boxes.

        The method uses a binary search to find the largest integer 'k' such that a pyramid of
        height 'k' (a tetrahedron of boxes) contains less than or equal to 'n' boxes.
        The total number of boxes in a pyramid of height 'k' is given by the k-th tetrahedral
        number: k * (k + 1) * (k + 2) / 6. The number of boxes on the floor for this
        pyramid is the k-th triangular number: k * (k + 1) / 2.

        After finding the largest full pyramid that can be built, it calculates the
        number of remaining boxes. It then determines the minimum number of additional
        boxes ('m') needed for the next layer on the floor to accommodate these
        remaining boxes. This is equivalent to finding the smallest 'm' such that the
        m-th triangular number is greater than or equal to the remaining boxes.

        The final result is the sum of the base of the full pyramid and the additional
        boxes 'm'.

        Args:
            n: The total number of boxes to be placed.

        Returns:
            The minimum number of boxes that must be placed on the floor.
        """

        lo, hi = 0, int((6*n)**(1/3)) + 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * (mid + 1) * (mid + 2) // 6 <= n:
                lo = mid
            else:
                hi = mid - 1
        k = lo

        # Number of boxes used in that full tetrahedron
        used = k * (k + 1) * (k + 2) // 6

        # Triangular base area of the full stack = k * (k + 1)/2
        base = k * (k + 1) // 2

        # Remaining boxes to place
        rem = n - used
        if rem == 0:
            return base
        
        # We now need the smallest m such that m * (m + 1) / 2 >= rem.
        m = int((math.sqrt(1 + 8*rem) - 1) // 2)
        if m * (m + 1) // 2 < rem:
            m += 1

        return base + m