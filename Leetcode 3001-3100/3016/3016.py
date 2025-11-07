# Leetcode 3016: Minimum Number of Pushes to Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
# Solved on 7th of October, 2025
import collections


class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculates the minimum number of pushes required to type a given word.

        Args:
            word (str): The input word.
        Returns:
            int: The minimum number of pushes.
        """
        counts = collections.Counter(word)
        frequencies = sorted(counts.values(), reverse=True)

        totalPushes = 0
        for i, freq in enumerate(frequencies):
            pushCost = (i // 8) + 1
            totalPushes += freq * pushCost

        return totalPushes