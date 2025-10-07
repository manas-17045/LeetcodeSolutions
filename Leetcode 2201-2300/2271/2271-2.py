# Leetcode 2271: Maximum White Tiles Covered by a Carpet
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
# Solved on 7th of October, 2025
import bisect


class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        """
        Calculates the maximum number of white tiles that can be covered by a carpet of a given length.
        :param tiles: A list of lists, where each inner list represents a tile [start, end].
        :param carpetLen: The length of the carpet.
        :return: The maximum number of white tiles that can be covered.
        """
        tiles.sort(key=lambda x: x[0])
        n = len(tiles)
        starts = [t[0] for t in tiles]
        ends = [t[1] for t in tiles]
        lengths = [ends[i] - starts[i] + 1 for i in range(n)]

        pref = [0] * n
        pref[0] = lengths[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + lengths[i]

        ans = 0
        for i in range(n):
            start = starts[i]
            endPos = start + carpetLen - 1

            r = bisect.bisect_right(ends, endPos) - 1

            if r >= i:
                full = pref[r] - (pref[i - 1] if i > 0 else 0)
            else:
                full = 0

            partial = 0
            next_idx = r + 1
            if next_idx < n and starts[next_idx] <= endPos:
                partial = min(endPos - starts[next_idx] + 1, lengths[next_idx])

            ans = max(ans, full + partial)

        return ans