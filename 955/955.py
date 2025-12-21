# Leetcode 955: Delete Columns to Make Sorted II
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# Solved on 21st of December, 2025
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Deletes the minimum number of columns such that the remaining columns,
        when read row by row, form lexicographically sorted strings.

        Args:
            strs: A list of strings, all of the same length.
        Returns:
            The minimum number of columns that need to be deleted.
        """
        deletionCount = 0
        rowCount = len(strs)
        colCount = len(strs[0])
        isSorted = [False] * (rowCount - 1)

        for col in range(colCount):
            mustDelete = False
            for row in range(rowCount - 1):
                if not isSorted[row] and strs[row][col] > strs[row + 1][col]:
                    mustDelete = True
                    break

            if mustDelete:
                deletionCount += 1
            else:
                for row in range(rowCount - 1):
                    if strs[row][col] < strs[row + 1][col]:
                        isSorted[row] = True

        return deletionCount