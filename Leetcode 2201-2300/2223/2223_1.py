# Leetcode 2223: Sum of Scores of Built Strings
# https://leetcode.com/problems/sum-of-scores-of-built-strings/
# Solved on 28th of July, 2025
class Solution:
    def sumScores(self, s: str) -> int:
        """
        Calculates the sum of scores of all suffixes of a given string.
        The score of a string is defined as the length of its longest common prefix with the original string.

        Args:
            s (str): The input string.
        Returns:
            int: The total sum of scores of all suffixes.
        """
        strLen = len(s)
        if strLen == 0:
            return 0

        zArray = [0] * strLen
        leftBound = 0
        rightBound = 0

        for i in range(1, strLen):
            if i <= rightBound:
                zArray[i] = min(rightBound - i + 1, zArray[i - leftBound])

            while i + zArray[i] < strLen and s[zArray[i]] == s[i + zArray[i]]:
                zArray[i] += 1

            if i + zArray[i] - 1 > rightBound:
                leftBound = i
                rightBound = i + zArray[i] - 1

        totalScore = strLen + sum(zArray)
        return totalScore