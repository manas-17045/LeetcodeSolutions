# Leetcode 2910: Minimum Number of Groups to Create a Valid Assignment
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/
# Solved on 26th of August, 2025
from collections import Counter


class Solution:
    def minGroupsForValidAssignment(self, balls: list[int]) -> int:
        """
        Calculates the minimum number of groups required to assign balls such that each group
        contains either 'm' or 'm+1' balls for some integer 'm'.

        :param balls: A list of integers representing the types of balls.
        :return: The minimum number of groups.
        """
        if not balls:
            return 0

        freq = list(Counter(balls).values())
        min_f = min(freq)
        total_balls = len(balls)
        # Upper bound: put every ball in its own box
        best = total_balls

        # Try every possible smallest box size m (boxes sizes are m or (m + 1))
        for m in range(1, min_f + 1):
            valid = True
            groups = 0
            for f in freq:
                # Minimal number of boxes needed for this value when max box size is m + 1
                t = (f + (m + 1) - 1) // (m + 1)
                # Check whether using t boxes we can ensure each box has at least m balls
                if t * m > f:
                    valid = False
                    break
                groups += t
                # Small optimization: if groups already >= best, no need to continue
                if groups >= best:
                    valid = False
                    break

            if valid:
                best = min(best, groups)

        return best