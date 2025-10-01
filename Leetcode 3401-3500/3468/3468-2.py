# Leetcode 3468: Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/
# Solved on 1st of October, 2025
class Solution:
    def countArrays(self, original: list[int], bounds: list[list[int]]) -> int:
        """
        Counts the number of possible arrays `copy` such that `copy[i] = original[i] + x` for some integer `x`,
        and `bounds[i][0] <= copy[i] <= bounds[i][1]` for all `i`.

        :param original: A list of integers representing the original array.
        :param bounds: A list of lists, where `bounds[i]` is `[lower_bound, upper_bound]` for `copy[i]`.
        :return: The number of possible integer values for `x`.
        """
        n = len(original)
        base = original[0]

        # Initialize intersection to full integer range using first index
        L = bounds[0][0] - (original[0] - base)
        R = bounds[0][1] - (original[0] - base)

        for i in range(1, n):
            shift = original[i] - base
            li = bounds[i][0] - shift
            ri = bounds[i][1] - shift
            if li > L:
                L = li
            if ri < R:
                R = ri
            # Early exit if intersection becomes empty
            if L > R:
                return 0

        # Number of integer choices for copy[0]
        return max(0, R - L + 1)