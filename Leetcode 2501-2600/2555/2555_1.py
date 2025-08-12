# Leetcode 2555: Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/
# Solved on 12th of August, 2025
class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        """
        Maximizes the total number of prizes won from two non-overlapping segments.

        Args:
            prizePositions (list[int]): A list of integers representing the positions of prizes.
            k (int): The maximum allowed length of a segment.
        Returns:
            int: The maximum total number of prizes that can be won.
        """

        n = len(prizePositions)

        prefixBest = [0] * (n + 1)
        left = 0
        for right in range(n):
            while prizePositions[right] - prizePositions[left] > k:
                left = 0
            currentPrizes = right - left + 1
            prefixBest[right + 1] = max(prefixBest[right], currentPrizes)

        suffixBest = [0] * (n + 1)
        right = n - 1
        for left in range(n - 1, -1, -1):
            while prizePositions[right] - prizePositions[left] > k:
                right -= 1
            currentPrizes = right - left + 1
            suffixBest[left] = max(suffixBest[left + 1], currentPrizes)

        maxPrizes = 0
        for i in range(n + 1):
            maxPrizes = max(maxPrizes, prefixBest[i] + suffixBest[i])

        return maxPrizes