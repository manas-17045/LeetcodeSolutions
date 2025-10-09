# Leetcode 3208: Alternating Groups II
# https://leetcode.com/problems/alternating-groups-ii/
# Solved on 9th of October, 2025
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        """
        Calculates the number of alternating groups of length k in a circular array of colors.

        :param colors: A list of integers representing the colors of tiles.
        :param k: An integer representing the required length of an alternating group.
        :return: The total number of alternating groups of length k.
        """
        n = len(colors)
        count = 0
        alternating_length = 1  # Current tile always forms a group of size 1

        # We need to check n + k - 2 consecutive pairs to cover all groups
        # in the circular array
        for i in range(n + k - 2):
            curr_idx = i % n
            next_idx = (i + 1) % n

            if colors[curr_idx] != colors[next_idx]:
                alternating_length += 1
            else:
                alternating_length = 1

            # If we have an alternating sequence of length k, count it
            if alternating_length >= k:
                count += 1

        return count