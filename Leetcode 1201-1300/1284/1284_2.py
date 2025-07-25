# Leetcode 1284: Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
# Solved on 25th of July, 2025
from collections import deque


class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        """
        Calculates the minimum number of flips required to make all elements in a binary matrix zero.

        Args:
            mat (list[list[int]]): The input binary matrix.
        Returns:
            int: The minimum number of flips, or -1 if it's impossible to make all elements zero.
        """

        m, n = len(mat), len(mat[0])
        total = m * n

        # Encode initial matrix into an integer state
        start = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)
        # If already zero, no flips needed
        if start == 0:
            return 0

        # Precompute flip mask for each cell
        flip_masks = []
        for i in range(m):
            for j in range(n):
                mask = 0
                for di, dj in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        mask |= 1 << (ni * n + nj)
                flip_masks.append(mask)

        # BFS
        dq = deque([(start, 0)])
        seen = {start}

        while dq:
            state, steps = dq.popleft()
            # Try flipping each cell
            for mask in flip_masks:
                nxt = state ^ mask
                if nxt == 0:
                    return steps + 1
                if nxt not in seen:
                    seen.add(nxt)
                    dq.append((nxt, steps + 1))

        return -1