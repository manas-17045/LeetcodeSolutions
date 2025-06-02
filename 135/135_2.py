# Leetcode 135: Candy
# https://leetcode.com/problems/candy/
# Solved on 2nd of June, 2025

class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Calculates the minimum number of candies needed to distribute to children
        based on their ratings, such that:
        1. Each child gets at least one candy.
        2. Children with a higher rating than their neighbors get more candies
           than their neighbors.

        This solution uses a single pass approach by tracking upward and downward
        slopes in the ratings.

        Args:
            ratings: A list of integers representing the ratings of children.
        Returns:
            The minimum number of candies required.
        """
        n = len(ratings)
        if n <= 1:
            return n

        r = 0
        up = 0
        down = 0
        p = 0

        for i in range(1, n):
            # Determine the "slope" between ratings[i - 1] and ratings[i]
            if ratings[i] > ratings[i - 1]:
                curr_slope = 1
            elif ratings[i] < ratings[i - 1]:
                curr_slope = -1
            else:
                curr_slope = 0

            if (p < 0 <= curr_slope) or (p > 0 and curr_slope == 0):
                r += (up * (up + 1)) // 2
                r += (down * (down + 1)) // 2
                r += max(up, down)
                up = 0
                down = 0

            # Extend the current slope counters
            if curr_slope > 0:
                up += 1
            elif curr_slope < 0:
                down += 1
            else:
                r += 1

            prevSlope = curr_slope

        r += (up * (up + 1)) // 2
        r += (down * (down + 1)) // 2
        r += max(up, down)
        r += 1

        return r