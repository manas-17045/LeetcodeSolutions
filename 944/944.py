# Leetcode 944: Delete Columns to Make Sorted
# https://leetcode.com/problems/delete-columns-to-make-sorted/
# Solved on 20th of December, 2025
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Deletes columns from a list of strings to make them sorted lexicographically.

        Args:
            strs: A list of strings.
        Returns:
            The number of columns that need to be deleted.
        """
        deletionCount = 0
        rowCount = len(strs)
        colCount = len(strs[0])

        for colIndex in range(colCount):
            for rowIndex in range(1, rowCount):
                if strs[rowIndex][colIndex] < strs[rowIndex - 1][colIndex]:
                    deletionCount += 1
                    break

        return deletionCount