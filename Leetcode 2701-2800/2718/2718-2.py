# Leetcode 2718: Sum of Matrix After Queries
# https://leetcode.com/problems/sum-of-matrix-after-queries/
# Solved on 19th of September, 2025
class Solution:
    def matrixSumQueries(self, n: int, queries: list[list[int]]) -> int:
        """
        Calculates the sum of elements in a matrix after applying a series of queries.

        Args:
            n (int): The size of the square matrix (n x n).
            queries (list[list[int]]): A list of queries, where each query is [type, index, val].
                                       type 0 means set row, type 1 means set column.
        Returns:
            int: The total sum of the elements in the matrix after all queries are applied.
        """
        seen_row = [False] * n
        seen_col = [False] * n
        rem_rows = n
        rem_cols = n
        ans = 0

        # Process queries in reverse
        for t, idx, val in reversed(queries):
            if t == 0:
                # Set row
                if not seen_row[idx]:
                    ans += val * rem_cols
                    seen_row[idx] = True
                    rem_rows -= 1
            else:
                # Set column
                if not seen_col[idx]:
                    ans += val * rem_rows
                    seen_col[idx] = True
                    rem_cols -= 1

            # Early exit: if all rows and cols are set, no further effect
            if rem_rows == 0 and rem_cols == 0:
                break

        return ans