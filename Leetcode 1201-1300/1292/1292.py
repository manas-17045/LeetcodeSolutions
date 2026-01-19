# Leetcode 1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# Solved on 19th of January, 2026
class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        """
        Finds the maximum side length of a square subgrid whose sum is less than or equal to the threshold.

        Args:
            mat: A 2D list of integers representing the matrix.
            threshold: An integer representing the maximum allowed sum for a square subgrid.
        Returns:
            An integer representing the maximum side length of such a square.
        """
        rows = len(mat)
        cols = len(mat[0])
        prefixSum = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                prefixSum[r][c] = prefixSum[r - 1][c] + prefixSum[r][c - 1] - prefixSum[r - 1][c - 1] + mat[r - 1][
                    c - 1]

        maxSide = 0
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                targetSide = maxSide + 1
                if r >= targetSide and c >= targetSide:
                    currentSum = prefixSum[r][c] - prefixSum[r - targetSide][c] - prefixSum[r][c - targetSide] + \
                                 prefixSum[r - targetSide][c - targetSide]
                    if currentSum <= threshold:
                        maxSide += 1

        return maxSide