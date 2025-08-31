# Leetcode 2661: First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/
# Solved on 31st of August, 2025
class Solution:
    def firstCompleteIndex(self, arr: list[list[int]], mat: list[list[int]]) -> int:
        """
        Finds the first index in `arr` such that painting the numbers up to that index
        results in a complete row or column in `mat`.
        :param arr: A list of integers representing the order in which numbers are painted.
        :param mat: A 2D list of integers representing the matrix.
        :return: The 0-indexed first complete index in `arr`.
        """
        m = len(mat)
        n = len(mat[0])

        pos = [None] * (m * n + 1)
        for r in range(m):
            row_r = mat[r]
            for c in range(n):
                pos[row_r[c]] = (r, c)

        row_count = [0] * m
        col_count = [0] * n

        for i, val in enumerate(arr):
            r, c = pos[val]
            row_count[r] += 1
            if row_count[r] == n:
                return i
            col_count[c] += 1
            if col_count[c] == m:
                return i

        return -1