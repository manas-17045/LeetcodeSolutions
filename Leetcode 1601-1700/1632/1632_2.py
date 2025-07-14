# Leetcode 1632: Rank Transform of a Matrix
# https://leetcode.com/problems/rank-transform-of-a-matrix/
# Solved on 14th of July, 2025
from collections import defaultdict


class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Transforms a given matrix into a rank matrix.

        The rank of an element `matrix[r][c]` is the smallest possible integer `k`
        such that `k` is greater than the rank of all adjacent elements (in the same
        row or column) that are strictly smaller than `matrix[r][c]`. If multiple
        elements have the same value, they must have the same rank.

        Args:
            matrix: A list of lists of integers representing the input matrix.

        Returns:
            A list of lists of integers representing the rank-transformed matrix.
        """
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        # Collect positions by value
        val_positions = defaultdict(list)
        for i in range(m):
            for j in range(n):
                val_positions[matrix[i][j]].append((i, j))
        # Prepare result and rank trackers
        answer = [[0] * n for _ in range(m)]
        max_rank_row = [0] * m
        max_rank_col = [0] * n

        # DSU class for grouping
        class DSU:
            def __init__(self, size):
                self.parent = list(range(size))

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx != ry:
                    self.parent[ry] = rx

        # Process values in ascending order
        for val in sorted(val_positions):
            pos = val_positions[val]
            k = len(pos)
            # Init DSU for this value
            dsu = DSU(k)
            # Group indices by row and col
            rows = defaultdict(list)
            cols = defaultdict(list)
            for idx, (r, c) in enumerate(pos):
                rows[r].append(idx)
                cols[c].append(idx)
            # Union positions in same row
            for idxs in rows.values():
                first = idxs[0]
                for other in idxs[1:]:
                    dsu.union(first, other)
            # Union positions in same col
            for idxs in cols.values():
                first = idxs[0]
                for other in idxs[1:]:
                    dsu.union(first, other)
            # Collect components
            comp = defaultdict(list)
            for idx in range(k):
                root = dsu.find(idx)
                comp[root].append(idx)
            # Prepare updates for this value
            updates = []  # tuples of (r, c, rank)
            row_updates = {}
            col_updates = {}
            # Compute rank for each component
            for group in comp.values():
                # Determine base rank
                base = 0
                for idx in group:
                    r, c = pos[idx]
                    base = max(base, max_rank_row[r], max_rank_col[c])
                rank = base + 1
                # Record assignments
                for idx in group:
                    r, c = pos[idx]
                    updates.append((r, c, rank))
                    # Track local max for rows and cols
                    row_updates[r] = max(row_updates.get(r, 0), rank)
                    col_updates[c] = max(col_updates.get(c, 0), rank)
            # Apply updates to answer and global rank trackers
            for r, c, rank in updates:
                answer[r][c] = rank
            for r, rnk in row_updates.items():
                max_rank_row[r] = max(max_rank_row[r], rnk)
            for c, rnk in col_updates.items():
                max_rank_col[c] = max(max_rank_col[c], rnk)
        return answer