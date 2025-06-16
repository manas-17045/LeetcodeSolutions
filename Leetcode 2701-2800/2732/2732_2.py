# Leetcode 2732: Find a Good Subset of the Matrix
# https://leetcode.com/problems/find-a-good-subset-of-the-matrix/
# Solved on 16th of June, 2025

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: list[list[int]]) -> list[int]:
        """
        Finds a "good" subset of rows in a binary matrix. A subset is good if the bitwise AND of all rows in the subset is a row of all zeros.

        Args:
            grid: A list of lists of integers representing the binary matrix.

        Returns:
            A list of integers representing the indices of the rows in a good subset.
            If no good subset is found, returns an empty list.
            If a single row of all zeros exists, returns a list containing the index of that row.
            If two rows exist whose bitwise AND is zero, returns a sorted list containing the indices of those two rows.
            The solution prioritizes finding a single-row subset of all zeros first, then a two-row subset whose bitwise AND is zero.
        """
        # Map from bitmask -> first row index where it appears
        first_idx = {}
        for i, row in enumerate(grid):
            # Encode row as bitmask
            mask = 0
            for b in row:
                mask = (mask << 1) | b
            # Record first occurrence
            if mask not in first_idx:
                first_idx[mask] = i
            # if mask == 0, single-row subset of size 1 is valid
            if mask == 0:
                return [i]

        masks = list(first_idx.keys())
        # Try any pair of distinct masks whose AND is zero
        for i in range(len(masks)):
            for j in range((i + 1), len(masks)):
                if masks[i] & masks[j] == 0:
                    i1, i2 = first_idx[masks[i]], first_idx[masks[j]]
                    return sorted([i1, i2])

        # No good subset found
        return []