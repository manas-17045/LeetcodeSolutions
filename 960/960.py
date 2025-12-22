# Leetcode 960: Delete Columns to Make Sorted III
# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
# Solved on 22nd of December, 2025
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        """
        Calculates the minimum number of columns to delete such that the remaining columns are sorted lexicographically.

        Args:
            strs: A list of strings, all of the same length.
        Returns:
            The minimum number of columns that need to be deleted.
        """
        numRows = len(strs)
        strLen = len(strs[0])
        lengths = [1] * strLen

        for i in range(strLen):
            for j in range(i):
                isValid = True
                for k in range(numRows):
                    if strs[k][j] > strs[k][i]:
                        isValid = False
                        break

                if isValid:
                    lengths[i] = max(lengths[i], lengths[j] + 1)

        return strLen - max(lengths)