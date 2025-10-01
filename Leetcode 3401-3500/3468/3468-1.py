# Leetcode 3468: Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/
# Solved on 1st of October, 2025
class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        """
        Calculates the number of possible arrays `copy` such that `copy[i] = original[i] + x`
        for some integer `x`, and `bounds[i][0] <= copy[i] <= bounds[i][1]` for all `i`.

        :param original: A list of integers representing the original array.
        :param bounds: A list of lists, where `bounds[i]` is `[lower_bound_i, upper_bound_i]`.
        :return: The number of possible integer values for `x`.
        """
        numberOfElements = len(original)

        maxOfLowerBounds = bounds[0][0] - original[0]
        minOfUpperBounds = bounds[0][1] - original[0]

        for i in range(1, numberOfElements):
            currentLowerBound = bounds[i][0] - original[i]
            currentUpperBound = bounds[i][1] - original[i]

            maxOfLowerBounds = max(maxOfLowerBounds, currentLowerBound)
            minOfUpperBounds = min(minOfUpperBounds, currentUpperBound)

        if minOfUpperBounds < maxOfLowerBounds:
            return 0

        return minOfUpperBounds - maxOfLowerBounds + 1