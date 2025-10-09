# Leetcode 3208: Alternating Groups II
# https://leetcode.com/problems/alternating-groups-ii/
# Solved on 9th of October, 2025
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        """
        Calculates the number of alternating groups of length k in a circular array of colors.

        Args:
            colors: A list of integers representing the colors.
            k: The required length of the alternating group.
        Returns:
            The number of alternating groups of length k.
        """
        n = len(colors)
        result = 0
        currentStreak = 1

        for i in range(1, (n + k - 1)):
            if colors[i % n] != colors[(i - 1) % n]:
                currentStreak += 1
            else:
                currentStreak = 1

            if currentStreak >= k:
                result += 1

        return result