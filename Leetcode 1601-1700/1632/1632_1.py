# Leetcode 1632: Rank Transform of a Matrix
# https://leetcode.com/problems/rank-transform-of-a-matrix/
# Solved on 14th of July, 2025
import collections


class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        rootI = self.find(i)
        rootJ = self.find(j)
        if rootI != rootJ:
            self.parent[rootJ] = rootI

class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Transforms a given matrix into a rank matrix.

        The rank of an element is its 1-based rank among all elements in its row and column.
        If two elements are equal, their ranks must be equal.

        Args:
            matrix: A list of lists of integers representing the input matrix.
        Returns:
            A list of lists of integers representing the transformed rank matrix.
        """
        rowCount = len(matrix)
        colCount = len(matrix[0])

        valueCoordinates = []
        for r in range(rowCount):
            for c in range(colCount):
                valueCoordinates.append((matrix[r][c], r, c))

        valueCoordinates.sort()

        answer = [[0] * colCount for _ in range(rowCount)]
        rowRanks = [0] * rowCount
        colRanks = [0] * colCount

        i = 0
        n = len(valueCoordinates)
        while i < n:
            j = i
            while j < n and valueCoordinates[j][0] == valueCoordinates[i][0]:
                j += 1

            currentValueBatch = valueCoordinates[i:j]

            dsu = DSU(rowCount + colCount)
            for _, r, c in currentValueBatch:
                dsu.union(r, rowCount + c)

            rankPerGroup = collections.defaultdict(int)
            for _, r, c in currentValueBatch:
                root = dsu.find(r)
                currentRank = max(rowRanks[r], colRanks[c]) + 1
                rankPerGroup[root] = max(rankPerGroup[root], currentRank)

            for _, r, c in currentValueBatch:
                root = dsu.find(r)
                finalRank = rankPerGroup[root]
                answer[r][c] = finalRank

            for _, r, c in currentValueBatch:
                finalRank = answer[r][c]
                rowRanks[r] = finalRank
                colRanks[c] = finalRank

            i = j

        return answer