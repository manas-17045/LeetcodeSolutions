# Leetcode 2768: Number of Black Blocks
# https://leetcode.com/problems/number-of-black-blocks/
# Solved on 8th of November, 2025
from collections import Counter


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        """
        Counts the number of 2x2 blocks that contain 0, 1, 2, 3, or 4 black cells.

        Args:
            m: The number of rows in the grid.
            n: The number of columns in the grid.
            coordinates: A list of [row, col] pairs representing the black cells.
        Returns:
            A list of 5 integers, where the i-th element is the number of 2x2 blocks with i black cells.
        """
        blockCounts = Counter()

        for r, c in coordinates:
            for tr in [r - 1, r]:
                for tc in [c - 1, c]:
                    if 0 <= tr < m - 1 and 0 <= tc < n - 1:
                        blockCounts[(tr, tc)] += 1

        ans = [0] * 5

        totalPossibleBlocks = (m - 1) * (n - 1)
        affectedBlocksCount = 0

        for blackCellCount in blockCounts.values():
            ans[blackCellCount] += 1
            affectedBlocksCount += 1

        ans[0] = totalPossibleBlocks - affectedBlocksCount

        return ans