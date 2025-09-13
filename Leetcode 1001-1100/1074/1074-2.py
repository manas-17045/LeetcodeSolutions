# Leetcode 1074: Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# Solved on 13th of September, 2025
class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        """
        Given a matrix and a target, return the number of non-empty submatrices that sum to target.
        :param matrix: The input matrix of integers.
        :param target: The target sum.
        :return: The number of submatrices that sum to the target.
        """
        # Transpose if rows > cols to reduce number if row-pairs (small optimization)
        if len(matrix) > len(matrix[0]):
            matrix = [list(row) for row in zip(*matrix)]

        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        # Fix top row, then extend bottom row; maintain column-wise sums
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                # Accumulate column cums for the bew bottom row
                row_b = matrix[bottom]
                for c in range(cols):
                    col_sums[c] += row_b[c]

                # Count subarrays in col_sums with sum == target using prefix sums
                prefix = 0
                freq = {0: 1}
                for v in col_sums:
                    prefix += v
                    ans += freq.get(prefix - target, 0)
                    freq[prefix] = freq.get(prefix, 0) + 1

        return ans