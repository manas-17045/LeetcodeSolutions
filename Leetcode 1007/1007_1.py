# Leetcode 1007: Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        """
        Determines the minimum number of rotations required to make all dominoes in a row
        uniform (all values in the top row equal or all values in the bottom row equal).

        The function explores both possibilities of achieving uniformity by:
        1. Making all values in the top row equal to the value of the first domino's top.
        2. Making all values in the bottom row equal to the value of the first domino's bottom.

        The solution relies on a helper function to compute the number of rotations
        needed for a given target and considers both rows for minimum rotations.

        :param tops: A list of integers representing the values on the top row of dominoes.
            Each index corresponds to one domino.
        :param bottoms: A list of integers representing the values on the bottom row of dominoes.
            Each index corresponds to one domino.
        :return: The minimum number of rotations required to achieve uniformity in the rows, or -1
            if it is not possible to make all the values in one row uniform.

        """
        n = len(tops)

        # We use n + 1 as a value representing infinity, as the maximum
        # possible rotations is n. This avoids using float('inf').
        infinity = n + 1

        def check(target: int) -> int:
            """
            Provides a solution to determine the minimum number of rotations required
            to make all values uniform (equal) in a row of dominoes. The dominoes are
            represented with values on their top and bottom rows.

            Attributes:
                n (int): Number of dominoes in the rows. Automatically determined
                from the input list sizes.

                infinity (int): A constant representing an arbitrarily large value
                for cases where a valid solution cannot be achieved.

            Methods:
                minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
                    Solves the problem by calculating the minimum rotations needed
                    for uniformity in the rows.

            """
            # rotation_top: counts rotations needed if aiming for tops[i] == target for all i
            # rotation_bottom: counts rotations needed if aiming for bottoms[i] == target for all i
            rotations_top = 0
            rotations_bottom = 0

            for i in range(n):
                # If the target value isn't on either half of the current domino,
                # then it's impossible to make the row uniform with this target.
                if tops[i] != target and bottoms[i] != target:
                    return infinity

                # If tops[i] isn't the target, it means bottoms[i] must be the target.
                # To make the top row uniform with 'target', we MUST rotate this domino.
                elif tops[i] != target:
                    rotations_top += 1

                # If bottoms[i] isn't the target, it means tops[i] must be the target.
                # To make the bottom row uniform with 'target', we MUST rotate this domino.
                elif bottoms[i] != target:
                    rotations_bottom += 1

                # If tops[] == target AND bottoms[i] == target, then no rotation
                # is necessary for either goal for this [articular dommino, so
                # neither counter is incremented.

            # If we iterated through all dominoes, it's possible to achieve uniformity
            # with this target. Return the minimum rotations needed (either by
            # mathing the top row uniform or the bottom row uniform).
            return min(rotations_top, rotations_bottom)

        # The target value for a uniform row must exist on the first domino.
        # So, we only need to check tops[0] and bottoms[0] as potential targets.
        target1 = tops[0]
        target2 = bottoms[0]

        # Calculate the minimum rotations needed for the target
        rotations1 = check(target1)

        # Calculate the minimum rotations needed for the target2.
        # If target1 and target2 are the same, the result will be the same,
        # so we can potentially skip the second check.
        if target1 == target2:
            rotations2 = rotations1
        else:
            rotations2 = check(target2)

        # The overall minimum rotations is the minimum of the results for the two targets.
        result = min(rotations1, rotations2)

        # If the minimum result is still 'infinity', it means neither target worked.
        # Otherwise, return the calculated minimum rotations.
        return result if result != infinity else -1