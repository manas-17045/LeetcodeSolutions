# Leetcode 1079: Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Counts the number of distinct sequences that can be formed using the given tiles.

        Args:
            tiles: A string representing the available tiles.

        Returns: The number of distinct sequences.
        """

        counts = Counter(tiles)
        result = 0

        def backtrack(current_sequence):
            nonlocal result
            if current_sequence:
                result += 1

            for tile, count in counts.items():
                if count > 0:
                    counts[tile] -= 1
                    backtrack(current_sequence + tile)
                    counts[tile] += 1

        backtrack("")
        return result