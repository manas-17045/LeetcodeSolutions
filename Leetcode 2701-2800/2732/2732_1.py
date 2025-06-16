# Leetcode 2732: Find a Good Subset of the Matrix
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/
# Solved on 16th of June, 2025

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: list[list[int]]) -> list[int]:
        """
        Finds a good subset of rows in a binary matrix.

        A good subset is a set of rows such that their bitwise OR is a row of all zeros.
        This is equivalent to finding a subset of rows where for each column, the sum of the elements
        in that column across the subset is 0. Since the elements are 0 or 1, this means for each
        column, all elements in that column within the subset must be 0.

        Args:
            grid: A list of lists of integers representing the binary matrix.

        Returns:
            A list of integers representing the indices of the rows in a good subset, or an empty list if no such subset exists.
        """
        m = len(grid)
        n = len(grid[0])

        maskToIndex = {}
        for i in range(m):
            mask = 0
            for j in range(n):
                if grid[i][j] == 1:
                    mask |= (1 << j)
            maskToIndex[mask] = i

        if 0 in maskToIndex:
            return [maskToIndex[0]]

        masks = list(maskToIndex.keys())

        for i in range(len(masks)):
            for j in range((i + 1), len(masks)):
                mask1 = masks[i]
                mask2 = masks[j]

                if (mask1 & mask2) == 0:
                    index1 = maskToIndex[mask1]
                    index2 = maskToIndex[mask2]
                    return sorted([index1, index2])

        return []