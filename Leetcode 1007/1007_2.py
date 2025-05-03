# Leetcode 1007: Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
from typing import Any


class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        """
        Determine the minimum number of rotations needed so that all values in either
        the top row or the bottom row of dominoes are the same. If it is impossible to
        achieve such uniformity, return -1.

        The function iteratively evaluates rotations required to make all dominoes' top
        or bottom values the same as a specific candidate value. The candidate values
        are derived from the first top and bottom domino values. It calculates the
        rotations needed and returns the smallest count, ensuring we evaluate both
        scenarios independently.

        :param tops: List of integers representing the top row of domino values.
        :param bottoms: List of integers representing the bottom row of domino values.
        :return: The minimum number of rotations required to achieve a uniform row,
            or -1 if it is not possible.
        """
        n = len(tops)
        
        # Check if we can make all values equal to tops[0]
        def check_value(target: int) -> float | int | Any:
            """
            This class provides a solution to the problem of determining
            the minimum number of rotations needed to make all the elements
            of either the top or bottom row of dominos equal, if possible.

            The core approach involves evaluating each potential target number
            (1 to 6, for standard domino values) and calculating the rotations
            required to achieve uniformity for the given target.
            """
            # Count rotations needed to make tops all equal to target
            tops_rotation = 0
            bottoms_rotation = 0
            
            for i in range(n):
                # If neither top nor bottom matches target, it's impossible
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')

                # Count rotations needed for tops
                if tops[i] != target:
                    tops_rotation += 1

                # Count rotations needed for bottoms
                if bottoms[i] != target:
                    bottoms_rotation += 1

            # Return the minimum of the two rotation counts
            return min(tops_rotation, bottoms_rotation)

        # Check for the two possible values(from the first domino)
        # We only need to check tops[0] and bottoms[0] as candidates
        result = min(check_value(tops[0]), check_value(bottoms[0]))

        return result if result != float('inf') else -1