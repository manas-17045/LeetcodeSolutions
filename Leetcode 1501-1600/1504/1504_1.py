# Leetcode 1504: Count Submatrices With All Ones
# https://leetcode.com/problems/count-submatrices-with-all-ones/
# Solved on 21st of August, 2025
class Solution:
    def numSubmat(self, mat: list[list[int]]) -> int:
        """
        Counts the number of submatrices with all ones.

        Args:
            mat: A list of lists of integers representing the binary matrix.

        Returns:
            The total count of submatrices with all ones.
        """
        numRows = len(mat)
        numCols = len(mat[0])

        totalCount = 0
        heights = [0] * numCols

        for i in range(numRows):
            for j in range(numCols):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

        for j in range(numCols):
            minHeight = float('inf')
            for k in range(j, -1, -1):
                minHeight = min(minHeight, heights[k])
                if minHeight == 0:
                    break
                totalCount += minHeight

        return totalCount