# Leetcode 3884: First Matching Character From Both Ends
# https://leetcode.com/problems/first-matching-character-from-both-ends/
# Solved on 5th of April, 2026
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        """
        Finds the first index where the character matches the character at the corresponding position from the end.

        :param s: The input string to evaluate.
        :return: The first index i such that s[i] == s[len(s) - 1 - i], or -1 if no such index exists.
        """
        stringLength = len(s)

        for currentIndex in range(stringLength):
            if s[currentIndex] == s[stringLength - currentIndex - 1]:
                return currentIndex

        return -1