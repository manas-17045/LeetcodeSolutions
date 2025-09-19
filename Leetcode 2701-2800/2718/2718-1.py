# Leetcode 2718: Sum of Matrix After Queries
# https://leetcode.com/problems/sum-of-matrix-after-queries/
# Solved on 19th of September, 2025
class Solution:
    def matrixSumQueries(self, n: int, queries: list[list[int]]) -> int:
        """
        Calculates the sum of all elements in an n x n matrix after applying a series of queries.
        Each query updates either a row or a column with a given value.
        The queries are processed in reverse order to efficiently determine the final value of each cell.

        Args:
            n: The dimension of the square matrix (n x n).
            queries: A list of queries, where each query is [type, index, val].
                     type 0 means update row 'index' with 'val', type 1 means update column 'index' with 'val'.

        Returns:
            The total sum of all elements in the matrix after all queries are applied.
        """
        seenRows = set()
        seenCols = set()
        totalSum = 0

        for query in reversed(queries):
            queryType, index, val = query

            if queryType == 0:
                if index not in seenRows:
                    totalSum += val * (n - len(seenCols))
                    seenRows.add(index)
            else:
                if index not in seenCols:
                    totalSum += val * (n - len(seenRows))
                    seenCols.add(index)

        return totalSum