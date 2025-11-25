# Leetcode 3531: Count Covered Buildings
# https://leetcode.com/problems/count-covered-buildings/
# Solved on 25th of November, 2025
class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        """
        Counts the number of buildings that are "covered". A building is covered if it is not
        the minimum or maximum row in its column and not the minimum or maximum column in its row.
        :param n: The size of the grid (n x n).
        :param buildings: A list of buildings, where each building is represented as [row, col].
        :return: The number of covered buildings.
        """
        minRowIndices = [n + 1] * (n + 1)
        maxRowIndices = [0] * (n + 1)
        minColIndices = [n + 1] * (n + 1)
        maxColIndices = [0] * (n + 1)

        for building in buildings:
            row = building[0]
            col = building[1]

            if row < minRowIndices[col]:
                minRowIndices[col] = row
            if row > maxRowIndices[col]:
                maxRowIndices[col] = row

            if col < minColIndices[row]:
                minColIndices[row] = col
            if col > maxColIndices[row]:
                maxColIndices[row] = col

        count = 0
        for building in buildings:
            row = building[0]
            col = building[1]

            if (minRowIndices[col] < row and
                    maxRowIndices[col] > row and
                    minColIndices[row] < col and
                    maxColIndices[row] > col):
                count += 1

        return count