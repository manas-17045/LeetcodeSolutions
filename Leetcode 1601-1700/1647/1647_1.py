# Leetcode 1647: Minimum Deletions to Make Character Frequencies Unique
# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Solved on 21st of August, 2025
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Calculates the minimum number of deletions needed to make character frequencies unique.
        :param s: The input string.
        :return: The minimum number of deletions.
        """
        charCounts = collections.Counter(s)
        deletionsCount = 0
        uniqueFrequencies = set()

        for char in charCounts:
            frequency = charCounts[char]
            while frequency > 0 and frequency in uniqueFrequencies:
                frequency -= 1
                deletionsCount += 1

            if frequency > 0:
                uniqueFrequencies.add(frequency)

        return deletionsCount