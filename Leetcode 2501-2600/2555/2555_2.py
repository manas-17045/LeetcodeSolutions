# Leetcode 2555: Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/
# Solved on 12th of August, 2025
class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        """
        Maximizes the total number of prizes collected by selecting at most two non-overlapping windows of length k.

        Args:
            prizePositions (list[int]): A sorted list of unique prize positions.
            k (int): The maximum length of a window.

        Returns:
            int: The maximum number of prizes that can be collected.
        """
        n = len(prizePositions)
        if n == 0:
            return 0

        # Two pointers to compute count[i] = number of prizes in [pos[i], pos[i] + k]
        count = [0] * n
        r = 0
        for i in range(n):
            if r < i:
                r = i
            # Extend r while within window
            while (r + 1) < n and prizePositions[r + 1] <= prizePositions[i] + k:
                r += 1
            count[i] = r - i + 1

        # suffix_best[i] = best single-window count starting at or after i
        suffix_best = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_best[i] = max(suffix_best[i + 1], count[i])

        # Try using window starting at i and best non-overlapping window after its r
        ans = 0
        for i in range(n):
            r = i + count[i] - 1
            # Best for second window starts at r + 1 or later
            total = count[i] + (suffix_best[r + 1] if r + 1 < n else 0)
            if total > ans:
                ans = total

        return ans