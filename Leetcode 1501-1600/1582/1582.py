# Leetcode1582: Special Positions in a Binary Matrix
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/
# Solved on 4th of March, 2026
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        """
        Counts the number of special positions in a binary matrix.
        A position (i, j) is special if mat[i][j] == 1 and all other elements in row i and column j are 0.

        :param mat: A 2D list of integers representing the binary matrix.
        :return: The total count of special positions.
        """
        rowCount = len(mat)
        colCount = len(mat[0])
        rowSums = [sum(row) for row in mat]
        colSums = [sum(col) for col in zip(*mat)]

        specialCount = 0
        for i in range(rowCount):
            for j in range(colCount):
                if mat[i][j] == 1 and rowSums[i] == 1 and colSums[j] == 1:
                    specialCount += 1

        return specialCount