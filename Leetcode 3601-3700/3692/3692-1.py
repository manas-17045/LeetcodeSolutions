# Leetcode 3692: Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/
# Solved on 17th of October, 2025
import collections


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        """
        Finds the group of characters that appear with the majority frequency.
        If multiple frequencies have the same maximum group size, the largest frequency is chosen.

        Args:
            s: The input string.

        Returns:
            A string containing all characters that belong to the majority frequency group, sorted alphabetically.
        """
        if not s:
            return ""

        charCounts = collections.Counter(s)

        freqToChars = collections.defaultdict(list)
        for char, freq in charCounts.items():
            freqToChars[freq].append(char)

        maxGroupSize = -1
        resultFreq = -1

        for freq, chars in freqToChars.items():
            currentGroupSize = len(chars)

            if currentGroupSize > maxGroupSize:
                maxGroupSize = currentGroupSize
                resultFreq = freq
            elif currentGroupSize == maxGroupSize:
                if freq > resultFreq:
                    resultFreq = freq

        winningChars = freqToChars[resultFreq]

        return "".join(winningChars)