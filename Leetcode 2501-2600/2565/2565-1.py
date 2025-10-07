# Leetcode 2565: Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/
# Solved on 6th of October, 2025
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        """
        Calculates the minimum score required to make `t` a subsequence of `s` by deleting characters from `t`.

        Args:
            s (str): The main string.
            t (str): The target string to be made a subsequence.

        Returns:
            int: The minimum number of characters that need to be deleted from `t`.
        """
        sLength = len(s)
        tLength = len(t)

        suffixMatches = [-1] * tLength
        sPointer = sLength - 1
        tPointer = tLength - 1
        while sPointer >= 0 and tPointer >= 0:
            if s[sPointer] == t[tPointer]:
                suffixMatches[tPointer] = sPointer
                tPointer -= 1
            sPointer -= 1

        minScore = tPointer + 1

        if minScore == 0:
            return 0

        tSuffixPointer = 0
        tPrefixPointer = 0
        sPointer = 0
        while sPointer < sLength and tPrefixPointer < tLength:
            if s[sPointer] == t[tPrefixPointer]:
                prefixEndIndex = sPointer

                if tSuffixPointer <= tPrefixPointer:
                    tSuffixPointer = tPrefixPointer + 1

                while tSuffixPointer < tLength and (
                        suffixMatches[tSuffixPointer] == -1 or suffixMatches[tSuffixPointer] <= prefixEndIndex):
                    tSuffixPointer += 1

                if tSuffixPointer < tLength:
                    currentScore = tSuffixPointer - tPrefixPointer - 1
                    minScore = min(minScore, currentScore)
                else:
                    currentScore = tLength - tPrefixPointer - 1
                    minScore = min(minScore, currentScore)

                tPrefixPointer += 1
            sPointer += 1

        minScore = min(minScore, tLength - tPrefixPointer)

        return minScore