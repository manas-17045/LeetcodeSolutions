# Leetcode 3889: Mirror Frequency Distance
# https://leetcode.com/problems/mirror-frequency-distance/
# Solved on 12th of April, 2026
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        """
        Calculates the total absolute difference in frequencies between characters and their mirror counterparts.

        Args:
            s (str): The input string containing characters to analyze.
        Returns:
            int: The sum of absolute frequency differences for all unique mirror pairs.
        """
        charCount = {}
        for charValue in s:
            charCount[charValue] = charCount.get(charValue, 0) + 1

        visitedPairs = set()
        totalDifference = 0

        for charValue in charCount:
            if 'a' <= charValue <= 'z':
                mirrorChar = chr(219 - ord(charValue))
            else:
                mirrorChar = chr(105 - ord(charValue))

            pairKey = charValue if charValue < mirrorChar else mirrorChar

            if pairKey not in visitedPairs:
                visitedPairs.add(pairKey)
                mirrorCount = charCount.get(mirrorChar, 0)
                totalDifference += abs(charCount[charValue] - mirrorCount)

        return totalDifference