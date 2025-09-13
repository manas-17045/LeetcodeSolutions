# Leetcode 1074: Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# Solved on 13th of September, 2025
import collections


class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        """
        Given a matrix and a target, return the number of non-empty submatrices that sum to target.

        Args:
            matrix (list[list[int]]): The input matrix of integers.
            target (int): The target sum.
        Returns:
            int: The number of non-empty submatrices that sum to target.
        """

        numRows = len(matrix)
        numCols = len(matrix[0])
        count = 0

        for leftCol in range(numCols):
            rowSums = [0] * numRows
            for rightCol in range(leftCol, numCols):
                for r in range(numRows):
                    rowSums[r] += matrix[r][rightCol]

                prefixSumCounts = collections.defaultdict(int)
                prefixSumCounts[0] = 1
                currentSum = 0
                for rSum in rowSums:
                    currentSum += rSum
                    diff = currentSum - target
                    count += prefixSumCounts[diff]
                    prefixSumCounts[currentSum] += 1

        return count